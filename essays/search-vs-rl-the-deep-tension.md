# Search vs RL: the deep tension.

*Essay. Updated 2026-05-14.*

---

Two stories about why reasoning models work compete for the same explanatory variable.

**Story 1 — Search.** Reasoning is search. At inference time, models explore a tree of partial CoTs, prune unpromising branches, and aggregate solutions. Tree of Thoughts, Graph of Thoughts, MCTS-over-CoT, recursive self-aggregation. The 2023 framing.

**Story 2 — Amortized RL.** Reasoning is a learned policy. RL with verifiable rewards (RLVR) trains the policy to *sample* the right reasoning paths greedily. No external search needed. The 2025 framing, anchored by R1-Zero.

The empirical finding that forces the question: explicit MCTS over an RL-trained reasoner adds *much less* than explicit MCTS over a non-RL-trained base. R1 doesn't appear to need it.

If RL fully internalizes the search, search is downstream of RL. If RL is doing something search isn't, the two are complementary. The state of the field in mid-2026: somewhere between, with the balance task-dependent.

## What each story explains

**Search explains:**
- Why ToT helps on Game of 24 and similar small-state planning puzzles.
- Why AlphaProof / AlphaGeometry win on formal-theorem tasks: explicit search over verifiable proof steps, with a learned value function.
- Why CoT-with-best-of-N works: BoN *is* shallow search.

**Search does not explain:**
- Why R1-Zero, with no explicit search at training or inference, reaches o1-class performance.
- Why long unconditional samples from R1-class models contain search-transcript-shaped text (the "aha moments").

**Amortized RL explains:**
- The R1-Zero observation.
- The "aha moments" — the policy has learned to emit recovery steps when it notices a contradiction.
- Why test-time compute scaling has the *shape* it does for RL-trained models (smooth log-linear) — a sampled-search interpretation predicts steps and discontinuities; an amortized-policy interpretation predicts smoothness.

**Amortized RL does not explain:**
- Why explicit search still dominates on tasks the RL training distribution doesn't cover (novel theorem proving, ARC-AGI-3-style puzzles).
- The compute-per-accuracy curve when the policy is held fixed and search depth is varied; if RL fully internalized search, this curve should be flat. It isn't, on hard tasks.

## The mechanistic prediction

If amortized RL is the dominant story, RL-trained reasoning models should *internally* implement a search-like procedure across forward passes. Mechanistic-interp evidence would look like:

- Specific residual-stream directions corresponding to "current best hypothesis" and "current alternatives."
- Attention patterns that pull historical "alternative" tokens forward for re-evaluation.
- Circuits that produce backtracking ("Wait, that's wrong...") under specific intermediate-state conditions.

If search is irreducible — if reasoning is *fundamentally* an external loop — then RL-trained models should *not* internally implement search; the gains should come from elsewhere (better single-step decisions, better domain knowledge, better calibration). Mech-interp evidence would look like:

- Strong single-step reasoning circuits, no explicit "exploration" pattern.
- Long chains as Markov chains of independent decisions.
- The "aha moments" turn out to be linguistic artifacts of training data, not functional backtracking.

We don't have decisive evidence either way as of 2026.

## What the synthesis suggests

A reasonable hybrid: pretraining + RL gives the policy a *base rate* of finding correct paths via greedy decoding; explicit search adds value when the policy's base rate is below what search would extract, and adds little when the base rate is already high.

On math benchmarks where RL-trained policies are strong, search adds little. On harder tasks or out-of-distribution problems where the policy is weak, search adds more. This is consistent with the empirics.

The compute-allocation implication: invest in RL until the policy saturates; add explicit search at the margin where it helps. Most current systems are not at the search-helps margin — they're in the RL-still-paying-off regime.

## The training-time question

So far we discussed inference-time search. There's a parallel question for training-time:

- **Pure RL** (R1-Zero): the policy explores via on-policy sampling. The search is in the loss landscape, not the algorithm.
- **Search-guided RL** (some 2025 systems): use MCTS or beam search at training time to generate higher-quality rollouts, then learn from them.

Empirically, pure RL is competitive with search-guided RL on math; the marginal benefit of training-time search is small. This is striking — a year ago many of us would have predicted otherwise. The implication: even at training time, sampled exploration is enough for the policy to internalize good behaviors.

## Why this debate matters

The debate has practical consequences beyond explanation:

- **Compute allocation.** If amortized RL dominates, more compute should go to RL training; if search dominates, more compute should go to inference-time search infrastructure.
- **Out-of-distribution generalization.** If the policy has internalized search, OOD should degrade gracefully (the policy can search its way out). If the policy is just amortizing in-distribution patterns, OOD should fail sharply.
- **Mechanistic interpretability.** What we look for in the model's internals depends on which story we believe.
- **Safety oversight.** A model that performs search internally has more degrees of freedom for hidden computation than a model that performs straight greedy decoding (Ch 7 connections).

## What might settle this

- Mechanistic-interp work showing whether RL-trained reasoners do or don't implement search-like patterns internally.
- A controlled study of OOD generalization on a task family where the training/test split is calibrated.
- A scaling law for explicit-search benefit as a function of RL training compute. If the benefit decays smoothly, the story is hybrid; if it falls off a cliff, the story is "RL has internalized search at scale X."

## Bottom line

The state of the field is that *both* stories have evidence and neither is sufficient alone. The deep tension is whether RL-trained policies have absorbed the search into their sampling, or whether they're just very good single-step samplers that don't need search on most current benchmarks because the benchmarks aren't hard enough.

The 2026 working hypothesis I'd defend: substantial absorption of search into the policy on training-distribution tasks; residual search-helps margin on adversarial / OOD tasks. Updates pending.

---

*Filed: 2026-05-14. Pointer to [Chapter 4](../chapters/04-search-at-inference.md) and [Chapter 5](../chapters/05-rl-for-reasoning.md). Disagreement welcome.*
