# Chapter 1 — Chain of Thought and Scratchpads

> *Intermediate tokens turn a fixed-depth forward pass into an unbounded serial program.*

## TL;DR

A constant-depth transformer can only compute what TC0 circuits compute in one forward pass. Letting it emit intermediate tokens — a *chain of thought* or *scratchpad* — and feed them back as input lifts this ceiling: with T intermediate tokens, the model effectively runs T serial computational steps. Empirically, this is what makes CoT prompting (Wei et al. 2022) work on multi-step problems, and it is what reasoning models industrialize. But the mechanism is real *only when the visible chain participates in the computation*: when it doesn't (the faithfulness failures of Ch 7), CoT is just decoration over a different process.

## The mechanism

Two complementary perspectives. Take them together; either alone is misleading.

**The compute-extension view.** A single forward pass of a fixed-depth transformer is shallow. Many natural problems — multi-step arithmetic, multi-hop QA, anything requiring sequential state updates over many tokens — exceed what TC0 can decide. Emitting an intermediate token and reading it back is the model's only way to do *unbounded* serial work: each emitted token effectively reads the previous N tokens of context and writes one new symbol the next decoding step can read. T emitted tokens give T extra serial steps, the same way T iterations of an outer loop convert a shallow circuit into a deep computation. This is the formal core of why CoT works on these tasks: it is the only knob the architecture offers for serial depth. (Detailed theorems on this in [the sister list](https://github.com/bettyguo/awesome-llm-reasoning-foundations) — Merrill & Sabharwal 2024, Li et al. 2024, Feng et al. 2023.)

**The Bayesian / structure view.** Prystawski et al. (2023) show that on Bayesian-network-shaped data, CoT helps *exactly when* training data has local conditional dependencies but the target query requires conditioning across many of them. CoT chains together locally-evidenced edges to reach a globally implied conclusion that direct prediction misses. This view says CoT isn't just "more compute" — it's compute in a particular *structured* form that recovers reasoning relations the training distribution made locally salient.

**Why both views matter.** The compute-extension view explains why CoT *can* help on hard serial problems. The Bayes/structure view explains why CoT *does* help on training distributions that look like real text. Modern reasoning models inhabit both regimes simultaneously: they are trained on text whose dependencies look Bayesian-locally-evidenced *and* they exploit the architectural compute-extension move.

**What the mechanism does not say.** Nothing about the *visible chain being the actual computation*. The forward pass can use the chain as scratchpad, or it can ignore the chain and produce the answer from internal computation while *also* emitting plausible-looking chain text. Both are consistent with the compute-extension story; only the first is consistent with CoT-as-thought. Empirical faithfulness work (Ch 7) is needed to distinguish.

## Key papers

- **Chain-of-Thought Prompting Elicits Reasoning in Large Language Models** (2022) — *Wei et al.* [arXiv:2201.11903](https://arxiv.org/abs/2201.11903).
  - **Contribution**: Shows that prompting an LLM with worked examples that include intermediate reasoning produces a large accuracy jump on multi-step problems, particularly math word problems.
  - **Why it matters**: Establishes the empirical phenomenon and names it. The starting point for the modern reasoning-model literature.
  - **Status**: 🟢 Verified, near-universally cited.
  - **Reproduction**: Trivial; many open implementations.

- **Show Your Work: Scratchpads for Intermediate Computation with Language Models** (2021) — *Nye et al.* [arXiv:2112.00114](https://arxiv.org/abs/2112.00114).
  - **Contribution**: Predates CoT by a few months; demonstrates the same idea (let the model emit intermediate state) for algorithmic tasks like long-form arithmetic and Python program execution.
  - **Why it matters**: Provides the cleaner experimental setting (synthetic algorithmic tasks where ground-truth scratchpad is known) that frames CoT as compute-extension rather than emergent reasoning.
  - **Status**: 🟢 Verified.

- **Large Language Models are Zero-Shot Reasoners** (2022) — *Kojima et al.* [arXiv:2205.11916](https://arxiv.org/abs/2205.11916).
  - **Contribution**: Adding "Let's think step by step" to a prompt elicits CoT without exemplars. Surprisingly effective on math benchmarks.
  - **Why it matters**: Decouples CoT from few-shot prompting; shows the capability is latent in the base model, not learned from in-context exemplars.
  - **Status**: 🟢 Verified, but later reasoning models supersede the zero-shot framing — they emit CoT regardless of the trigger phrase.

- **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2022) — *Wang et al.* [arXiv:2203.11171](https://arxiv.org/abs/2203.11171).
  - **Contribution**: Sample K independent chains, take the majority-vote answer. Recovers most of the test-time compute scaling benefit without a verifier.
  - **Why it matters**: First and still-standard demonstration that CoT plus multi-sample aggregation acts like search. Lives more naturally in [Chapter 3](03-sampling-and-verification.md) but the conceptual root is here.
  - **Status**: 🟢 Verified.

- **Why think step by step? Reasoning emerges from the locality of experience** (2023) — *Prystawski, Li, Goodman.* [arXiv:2304.03843](https://arxiv.org/abs/2304.03843).
  - **Contribution**: Constructs a Bayesian-network model of "training data with local conditional structure" and proves CoT exactly recovers chained conditional inferences that direct prediction misses.
  - **Why it matters**: Most rigorous explanation of *why* CoT helps for the kind of data LLMs are trained on, not just *that* it helps. Predicts which kinds of CoT structures should and should not transfer.
  - **Status**: 🟢 Verified, ICML 2023 / cogsci-bridging influential paper.

- **To CoT or not to CoT? Chain-of-thought helps mainly on math and symbolic reasoning** (2024) — *Sprague et al.* ICLR 2025. [arXiv:2409.12183](https://arxiv.org/abs/2409.12183).
  - **Contribution**: Meta-analysis of 100+ CoT-vs-direct comparisons across benchmarks. CoT gains are concentrated on math/symbolic tasks; on commonsense and knowledge tasks the gain is small or zero.
  - **Why it matters**: Calibrates the literature against the claim "CoT helps generally". It mostly doesn't — except where serial computation is the bottleneck.
  - **Status**: 🟢 Verified.

- **Language Models Don't Always Say What They Think: Unfaithful Explanations in Chain-of-Thought Prompting** (2023) — *Turpin et al.* NeurIPS 2023. [arXiv:2305.04388](https://arxiv.org/abs/2305.04388).
  - **Contribution**: Biasing prompts can change a model's answer without the change being reflected in its CoT. The chain *post-hoc rationalizes* a conclusion driven by the prompt bias.
  - **Why it matters**: The first widely-cited demonstration that CoT ≠ the model's actual computation. Foundational for [Chapter 7](07-faithfulness-of-reasoning.md).
  - **Status**: 🟢 Verified.

- **Measuring Faithfulness in Chain-of-Thought Reasoning** (2023) — *Lanham et al.* (Anthropic). [arXiv:2307.13702](https://arxiv.org/abs/2307.13702).
  - **Contribution**: Operationalizes "faithfulness" via truncation, paraphrase, mistake-injection, and filler-token tests across model scales. Finds faithfulness varies non-monotonically with scale.
  - **Why it matters**: Establishes the measurement framework now used by every follow-up. See also [Chapter 7](07-faithfulness-of-reasoning.md).
  - **Status**: 🟢 Verified.

- **Let's Think Dot by Dot: Hidden Computation in Transformer Language Models** (2024) — *Pfau, Merrill, Bowman.* COLM 2024. [arXiv:2404.15758](https://arxiv.org/abs/2404.15758).
  - **Contribution**: Shows that semantically empty filler tokens (`"...."` or pause tokens) can boost transformer accuracy on certain parallelizable tasks. The benefit isn't *only* from chained reasoning content — extra compute alone helps.
  - **Why it matters**: Empirically separates CoT's compute-extension role from its interpretability role. Caveat: the filler-token gain is task-restricted; on many problems the chain content does matter.
  - **Status**: 🟢 Verified.

- **Think before you speak: Training Language Models With Pause Tokens** (2024) — *Goyal et al.* ICLR 2024. [arXiv:2310.02226](https://arxiv.org/abs/2310.02226).
  - **Contribution**: Train decoder-only models to consume learnable pause tokens before answering. Reports reasoning gains.
  - **Why it matters**: Empirical counterpart to the compute-extension theory: extra forward-pass compute, with no extra semantic content, transfers to accuracy on some tasks.
  - **Status**: 🟢 Verified.

- **Faith and Fate: Limits of Transformers on Compositionality** (2023) — *Dziri et al.* NeurIPS 2023. [arXiv:2305.18654](https://arxiv.org/abs/2305.18654).
  - **Contribution**: On compositional tasks (multi-digit multiplication, dynamic-programming puzzles, logic grids) transformers fail catastrophically as depth grows, *even with* CoT. The failure is systematic.
  - **Why it matters**: A counterweight to the compute-extension narrative. CoT isn't a free pass: there are tasks where the chain-extended model still fails. Helps locate where reasoning models actually buy you something.
  - **Status**: 🟢 Verified.

- **Premise Order Matters in Reasoning with Large Language Models** (2024) — *Chen et al.* [arXiv:2402.08939](https://arxiv.org/abs/2402.08939).
  - **Contribution**: Even for tasks that LLMs nominally solve via CoT, reordering the premises in the prompt drops accuracy by 30%+. The chain is order-fragile in ways the underlying computation should not be.
  - **Why it matters**: Evidence against a pure "CoT is execution of a stable program" view. Points to CoT being prompt-sensitive heuristic chaining, not robust algorithmic reasoning.
  - **Status**: 🟢 Verified.

- **Emergent Abilities of Large Language Models** (2022) — *Wei et al.* TMLR. [arXiv:2206.07682](https://arxiv.org/abs/2206.07682).
  - **Contribution**: Documents capability discontinuities as a function of training scale; CoT-elicited multi-step reasoning is one of the canonical "emergent" abilities in the original framing.
  - **Why it matters**: The framing has been challenged (Schaeffer et al. argue emergence is metric-dependent) but the empirical pattern — CoT works much better past a scale threshold — is real and load-bearing.
  - **Status**: 🟢 Verified.

- **Challenging BIG-Bench Tasks and Whether Chain-of-Thought Can Solve Them** (2022) — *Suzgun et al.* (BBH). [arXiv:2210.09261](https://arxiv.org/abs/2210.09261).
  - **Contribution**: Identifies 23 BIG-Bench tasks where models underperform humans; tests CoT prompting on each. CoT lifts accuracy substantially on math/symbolic subsets, less on others.
  - **Why it matters**: Predecessor to the Sprague et al. (2024) meta-analysis; provides the canonical task set for CoT-vs-direct comparisons.
  - **Status**: 🟢 Verified.

## Debates

- **Compute-extension vs structure-induction**: Pfau et al. say filler tokens help (pure compute matters); Prystawski et al. say chain content helps via Bayesian-locality recovery. Both are right on *different* tasks; the unsettled question is the relative magnitude. Defenders of the structure view: Prystawski, Wei. Defenders of the compute view: Pfau, Goyal, Merrill (theoretically). Synthesis emerging: depends on task structure (parallel-decomposable → filler suffices; serial-dependency → content matters).

- **Is CoT thought, or is it post-hoc rationalization?** Turpin and Lanham say CoT is often the latter. Reasoning-model partisans say RL-with-verifiable-rewards fixes this by aligning CoT with the actually-rewarded computation. The 2025 Anthropic paper "Reasoning Models Don't Always Say What They Think" finds even RL-trained reasoners are unfaithful in measurable ways. Live as of 2026.

- **Does CoT scale to truly hard problems, or is it a regime crutch?** Dziri et al. say compositional gaps persist; the o1/R1 partisans say new scaling laws bypass this. Resolution depends on whether you weight saturated benchmarks (where reasoners now succeed) or designed-to-be-hard benchmarks like FrontierMath (where they still struggle).

## Where to start

- **Skim path (90 min)**: Wei et al. (CoT origin) → Kojima et al. (zero-shot trigger) → Sprague et al. (where CoT actually helps).
- **Deep path (1 weekend)**: + Nye et al. (scratchpad origin), Prystawski et al. (why-locality), Pfau et al. (filler tokens), Turpin et al. (unfaithfulness), Lanham et al. (measurement), Dziri et al. (limits).
- **Research path**: full chapter + sister-list theory chapter (Merrill & Sabharwal CoT-expressivity, Li et al. serial problems, Feng et al. CoT mystery).

## Reproduction

- **Notebook**: [`notebooks/04-overthinking-demo.ipynb`](../notebooks/04-overthinking-demo.ipynb) (mostly aimed at Ch 6, but Section 1 of that notebook demonstrates the basic CoT-vs-direct comparison and its task-dependence.)
- **What it shows**: On a non-CoT-friendly task (factual lookup), CoT does not help and sometimes hurts. On a CoT-friendly task (multi-step arithmetic), CoT helps reliably. Matches the Sprague et al. meta-analysis on a tiny scale.

## Open problems

- **Mechanistic interpretability of CoT in reasoning models.** What internal computations do RL-trained reasoners run that base-model + zero-shot CoT does not? Largely unaddressed as of 2026.
- **A quantitative theory of when CoT content matters vs. when filler suffices.** Pfau et al. is qualitative; no closed-form predictor exists.
- **Faithful CoT under RL training.** Whether RLVR systematically improves or degrades faithfulness is an open empirical question; conflicting signals across labs.
- **Robustness of CoT to premise reordering, paraphrase, distractors.** Chen et al. (2024) shows fragility; whether reasoning-model RL training fixes it is unclear.

---

*Next: [Chapter 2 — Test-Time Compute Scaling](02-test-time-compute-scaling.md).*
