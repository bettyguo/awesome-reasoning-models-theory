# Why do reasoning models work? A synthesis.

*Essay. Argued position, not survey. Comments and dissents welcome via PR.*

---

We have eight chapters of empirical regularities, three theoretical frameworks, several debates that haven't closed, and a 2024–2026 cohort of models — o1, o3, R1, Claude with thinking, Gemini reasoning — that perform meaningfully better on math, code, and science than their non-reasoning siblings. What is the single best account of *why*?

The honest answer is: there isn't one. But the components of an honest answer are now visible.

## Component 1: the architecture wasn't the bottleneck

A constant-depth, log-precision transformer is in TC0. Many of the tasks reasoning models solve (multi-digit arithmetic, multi-hop QA, dynamic programming) are not in TC0 in their non-CoT forms. The architecture, in one forward pass, cannot do them.

This is well-known and, by itself, would imply non-reasoning LLMs should fail on these tasks. They don't — they succeed at a non-zero rate, but with a *much* lower per-problem hit rate and much more variance, because each pass is essentially a guess shaped by next-token statistics.

What CoT does is give the model an outer loop. Emit a token, read it back, emit another. T emitted tokens give T units of serial compute. The formal arguments (Merrill & Sabharwal 2024; Li et al. 2024) establish this rigorously. The reasoning-model era is, in part, the industrialization of an architectural affordance that was always there.

**This account is necessary but not sufficient.** It explains why the *ceiling* is higher with CoT. It does not explain why a typical chain happens to land below the ceiling on the right answer.

## Component 2: pretraining contains the programs

R1-Zero — pure RL from the base, no SFT seed — produces a strong reasoner. The most parsimonious explanation: the base model already contained the reasoning circuits. Pretraining on web-scale text exposed it to enough worked solutions, debugged code, mathematical exposition, that the policy distribution has support — possibly low-mass — on reasoning paths that lead to correct answers.

RLVR is then *elicitation*: move probability mass onto those paths. It is not, in this view, learning new computations; it is reshaping the policy over computations that exist.

This is the program-synthesis view, in informal form. A more rigorous version would say: pretraining trains a *meta-learner* over a set of compositional primitives (arithmetic ops, syntactic transformations, schema-filling); inference-time CoT is the meta-learner synthesizing a short program from the primitives; RL increases the probability that the synthesized programs are useful for the rewarded tasks.

**Why this view fits the evidence**:
- R1-Zero works without SFT. If the model had to *learn* the reasoning, this should fail.
- Distillation works. The synthesized programs are transferable.
- Base-model quality matters more than RL-budget for whether R1-style training succeeds. Programs that don't exist in the base can't be elicited.

**Why this view is incomplete**:
- It doesn't say where the *novelty* in long CoTs comes from when reasoning models tackle problems whose specific structure isn't in pretraining.
- It collapses "search" into the policy, which is part of the empirical picture but not the whole.

## Component 3: structure in the training distribution makes CoT necessary

The Prystawski et al. (2023) result: on Bayesian-network-shaped training distributions, CoT helps exactly when the data has local conditional dependencies but the query crosses many of them.

Real text is shaped this way. Documents about *X* mention what *X* is locally related to (its definition, its near-neighbors). Documents that *jointly* condition on *X*, *Y*, *Z*, *W* are rare. So a model that wants to answer "given the relation between *X* and *Z*, what follows about *W*?" has not seen that joint statement in training, but has seen each local edge. CoT chains the edges.

This explains why CoT helps a lot on tasks where the answer requires composing locally-evidenced primitives (math word problems, logical inference over named entities, multi-hop reasoning) and helps little on tasks where the answer is directly evidenced in training data (factual lookup, sentiment, summarization).

**This view fits the empirical CoT-helps-mostly-on-math-and-symbolic finding** (Sprague et al. 2024) without making strong claims about expressivity.

## Component 4: search, partially internalized

Tree of Thoughts (Yao et al. 2023), Graph of Thoughts (Besta et al. 2023), and the 2025 recursive-self-aggregation line make a different claim: at inference time, explicitly searching over CoT branches recovers solutions that greedy decoding misses.

Concurrent: R1-Zero appears to *internalize* parts of this search into the policy. Long chains in RL-trained reasoners look like search transcripts: "let me try X... no that fails, try Y... aha." The "aha moments" DeepSeek documented are exactly this.

Whether the internalized search is *the same* search a tree-search algorithm would explicitly run is empirically unsettled. The interesting prediction: explicit MCTS over an RL-trained reasoner should add *less* than the same MCTS over a base model — because the policy has already absorbed most of the gain. This appears to be what we see, but the studies are not yet decisive.

## Putting them together

A plausible synthesis:

1. **Architecture** gives the ceiling. CoT raises it from TC0-shallow to serially-deep.
2. **Pretraining** populates the policy with reasoning programs as low-mass continuations.
3. **Training-distribution structure** makes CoT *useful* — the Bayesian-locality view says exactly when chain-of-thought-style reasoning is the right tool for the task.
4. **RLVR** moves probability mass onto reasoning programs that lead to correct answers, including search-like behaviors.
5. **Inference-time test-time-compute scaling** then amortizes the resulting policy: sampling, voting, reranking, occasional explicit search, each in regime where they help.

Different chapters of this repo emphasize different components. They are not in tension; they are *layered*.

## What this synthesis does *not* claim

- That reasoning models think, in any psychologically interesting sense. The empirical-unfaithfulness literature (Ch 7) rules out a naïve identification of CoT with thought.
- That the scaling will continue forever. Saturation on individual benchmarks is visible; whether new benchmarks will be solved by more of the same recipe is genuinely uncertain. FrontierMath and ARC-AGI-3 are stress tests.
- That the closed/open gap reflects a fundamental advantage. Most of the headline gap as of mid-2026 is timing — the closed labs have one to three months of capability lead. R1 closed that gap once; reproducing the gap-closing is the open-source community's recurring task.

## What follows for research

If this synthesis is right:

- **More base-model strength** matters more than more RL compute for any given reasoner. Component 2 is rate-limiting.
- **Training-distribution shaping** has under-explored leverage. The Bayesian-locality view predicts which kinds of synthetic pretraining data should help; experiments are sparse.
- **Mechanistic interpretability of long chains** is the next bottleneck. We don't know which residual-stream directions correspond to "I'm searching now" vs "I'm rationalizing." Until we do, the faithfulness debate doesn't close.
- **Verifier scaling** (Ch 3) deserves more compute. Most pipelines underspend on the verifier.

## What's likely to be wrong about this essay

In two years (2028) the most likely revisions:

- The "elicitation, not learning" framing of RLVR is incomplete. Some new training paradigm probably *does* teach genuinely new reasoning, undermining Component 2.
- The Bayesian-locality account will be supplanted by a sharper structural theory of CoT-relevant data.
- Mechanistic-interp results will recast at least one of the components in unfamiliar terms (some specific circuit will turn out to be load-bearing in a way none of the current frameworks predict).
- The closed-source frontier will be running a different paradigm we don't yet see.

The first three are likely to be progress. The fourth is the field's perennial epistemological problem.

---

*Filed: 2026-05-14. Linked from [README](../README.md) and [Chapter 8](../chapters/08-theoretical-frameworks.md). Comments via issue / PR.*
