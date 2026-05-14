# Chapter 8 — Theoretical Frameworks

> *Candidate unifying accounts: compute-depth, program synthesis, Bayes-over-thoughts.*

## TL;DR

Three theoretical accounts compete (and partly cooperate) to explain why reasoning models work, beyond the empirical scaling observations of Chapters 1–7:

1. **Compute-depth equivalence.** A CoT of T tokens extends a constant-depth transformer to T serial computational steps. The expressivity-via-CoT view, mostly formal.
2. **Program synthesis / amortized planning.** Pretraining exposes the model to enough worked examples that it has learned to *synthesize* short programs (chains) that produce answers. RL elicits and refines this synthesis ability.
3. **Bayes-over-thoughts.** CoT is implicit posterior inference over a latent "solution" given the question, with each token sampled from a posterior that integrates over plausible continuations.

None alone is sufficient. Different chapters of the empirical literature line up with different frameworks: Ch 1 / Ch 6 with compute-depth, Ch 5 with program synthesis, Ch 1's Prystawski result with Bayes-over-thoughts. A unified theory would have to reconcile all three.

This chapter cross-cites work from the [sister list](https://github.com/bettyguo/awesome-llm-reasoning-foundations) (formal theorems live there) and adds the empirical/explanatory bridging work.

## The mechanism

### Framework 1 — Compute-depth equivalence

**The claim.** A single forward pass of a constant-depth, log-precision transformer is in TC0; many serial problems aren't. T tokens of CoT provide T additional units of serial compute. Formally (Merrill & Sabharwal 2024; Li et al. 2024): with logarithmic CoT length the model stays in TC0, with polynomial CoT length it reaches P, with exponential length it reaches EXPTIME.

**What it explains.**
- Why CoT helps on serial-bottleneck tasks (multi-digit arithmetic, dynamic programming, complex parsing).
- Why filler tokens partly substitute for content tokens on parallelizable tasks (Pfau et al. 2024) — the *compute* is what matters there.
- Why model depth + CoT length jointly determine an effective compute axis (Merrill & Sabharwal's "log-depth" follow-up).

**What it does not explain.**
- *Why* a particular training pipeline (RLVR, R1) gives access to the long-CoT regime in practice — the theory says it's possible, not how to elicit it.
- Why structural CoT content (Bayesian-locality patterns) matters more than length on the tasks where it does.
- Why reasoning models still fail on problems that should fit (Dziri et al. compositionality).

### Framework 2 — Program synthesis / amortized planning

**The claim.** Pretraining teaches the model to recognize and emit short *programs* whose execution traces (when fed back as tokens) produce answers. A CoT is the source code of one such program. RL elicits and refines this synthesis ability — the policy learns to synthesize *useful* programs more reliably.

**What it explains.**
- The "elicitation, not learning" interpretation of R1-Zero: pretraining contains the programs; RL increases probability mass on the right ones.
- Why distillation of R1 → smaller students works so well: the synthesized programs transfer.
- Why CoT helps on novel tasks composed of familiar primitives.

**What it does not explain.**
- Why programs from one domain (math) don't always transfer to another (commonsense), even when the primitives look similar.
- Why some CoTs are unfaithful: the *program* and the *answer* can come from different computational paths.

### Framework 3 — Bayes-over-thoughts

**The claim.** Each emitted token is a sample from `p(token | context)`, which implicitly integrates over a latent posterior `p(solution | question, observed_tokens)`. A long CoT is an iterated posterior update: each token adds evidence and conditions subsequent generations. This extends the ICL-as-Bayes account (Xie et al. 2022) to the multi-step / generation setting.

**What it explains.**
- Prystawski et al.'s locality result: CoT recovers conditional dependencies given training distribution structure.
- Why self-consistency works: independent samples are MC estimates of the posterior; majority vote approximates the mode.
- Why temperature affects CoT correctness in regime-dependent ways.

**What it does not explain.**
- The architectural mechanism (the compute-depth point) — Bayes is about *information*, not *operations*.
- Why filler tokens help (Pfau et al.) — pure Bayes would say content matters.

### The unification problem

Each framework explains a slice. A unified theory would need to:
- Combine *operational* expressivity (compute-depth) with *informational* content (Bayes-over-thoughts).
- Account for *training-shaped* synthesis (program-synthesis view) — what the policy learns to *emit*, not just what the architecture *can* emit.
- Cover both faithfulness wins (when chain content matters) and faithfulness failures (when it doesn't).

No such theory exists in 2026. Several candidate sketches; nothing converged.

## Key papers

(Many central formal papers — Merrill & Sabharwal CoT-expressivity, Li et al. serial problems, Feng et al. CoT mystery — live in the [sister list](https://github.com/bettyguo/awesome-llm-reasoning-foundations) by scope decision. They are cited here as bridging references.)

- **The Expressive Power of Transformers with Chain of Thought** (2024) — *Merrill, Sabharwal.* ICLR 2024. [arXiv:2310.07923](https://arxiv.org/abs/2310.07923).
  - **Contribution**: Characterizes the expressive power of decoder-only transformers with intermediate tokens, by generation length: log-many ⊆ TC0, linear-many ⊇ P, polynomial-many ⊇ EXPTIME.
  - **Why it matters**: The cleanest formal compute-depth-equivalence result. Cross-listed in foundations.
  - **Status**: 🟢 Verified, ICLR.

- **Chain of Thought Empowers Transformers to Solve Inherently Serial Problems** (2024) — *Li, Liu, Razaviyayn, Sra.* ICLR 2024. [arXiv:2402.12875](https://arxiv.org/abs/2402.12875).
  - **Contribution**: Proves that T(n) intermediate tokens let a constant-depth transformer simulate T(n)-step sequential computation. Recovers serial-complexity classes inaccessible to a single forward pass.
  - **Why it matters**: Operational form of the compute-depth-equivalence claim. Cross-listed in foundations.
  - **Status**: 🟢 Verified.

- **Towards Revealing the Mystery behind Chain of Thought: A Theoretical Perspective** (2023) — *Feng, Zhang, Lan, Liu, Yang, Li, Hu, Du, He.* NeurIPS 2023. [arXiv:2305.15408](https://arxiv.org/abs/2305.15408).
  - **Contribution**: Constructs a constant-size CoT transformer that solves arithmetic and dynamic-programming tasks unreachable by any fixed-depth no-CoT transformer.
  - **Why it matters**: Unconditional separation between with-CoT and without-CoT expressivity. Cross-listed in foundations.
  - **Status**: 🟢 Verified.

- **An Explanation of In-context Learning as Implicit Bayesian Inference** (2022) — *Xie, Raghunathan, Liang, Ma.* ICLR 2022. [arXiv:2111.02080](https://arxiv.org/abs/2111.02080).
  - **Contribution**: Models pretraining as a mixture-of-HMMs prior; ICL emerges as posterior inference over latent task variables.
  - **Why it matters**: The framework that Bayes-over-thoughts extends to multi-step. Cross-listed in foundations.
  - **Status**: 🟢 Verified.

- **Why think step by step? Reasoning emerges from the locality of experience** (2023) — *Prystawski, Li, Goodman.* [arXiv:2304.03843](https://arxiv.org/abs/2304.03843).
  - **Contribution**: Bayesian-network analysis showing CoT helps when training data has local conditional dependencies but the query crosses many of them.
  - **Why it matters**: The cleanest concrete instance of the Bayes-over-thoughts framework on a structured task. Pairs with the formal expressivity story to give a more complete account.
  - **Status**: 🟢 Verified.

- **Auto-Regressive Next-Token Predictors are Universal Learners** (2023) — *Malach.* [arXiv:2309.06979](https://arxiv.org/abs/2309.06979).
  - **Contribution**: Shows that autoregressive next-token prediction with a chain of thought is a universal learner: any efficiently computable function can be expressed by an autoregressive predictor with polynomially-bounded intermediate token complexity.
  - **Why it matters**: Strong learnability-meets-expressivity result. Cross-listed in foundations.
  - **Status**: 🟢 Verified.

- **Let's Think Dot by Dot: Hidden Computation in Transformer Language Models** (2024) — *Pfau, Merrill, Bowman.* COLM 2024. [arXiv:2404.15758](https://arxiv.org/abs/2404.15758).
  - **Contribution**: Filler tokens can boost accuracy on parallelizable tasks — empirically separates compute-extension from content.
  - **Why it matters**: The hardest empirical test for the Bayes-over-thoughts view alone. Cross-listed.
  - **Status**: 🟢 Verified.

- **Transformers Provably Solve Parity Efficiently with Chain of Thought** (2025) — *Kim, Suzuki.* ICLR 2025 (Oral). [arXiv:2410.08633](https://arxiv.org/abs/2410.08633).
  - **Contribution**: Constructs a small transformer with CoT that *learns* parity efficiently (sample complexity proven, not just expressivity). End-to-end (expressivity + trainability) result.
  - **Why it matters**: Bridges the expressivity-only papers with the learnability story. A program-synthesis-flavored reading is natural.
  - **Status**: 🟢 Verified.

- **The pitfalls of next-token prediction** (2024) — *Bachmann, Nagarajan.* ICML 2024. [arXiv:2403.06963](https://arxiv.org/abs/2403.06963).
  - **Contribution**: Identifies *Clever Hans cheat* and *snowball error* failure modes of teacher-forced next-token training — formal critique even with perfect data.
  - **Why it matters**: Tempers the program-synthesis view: the *learning* procedure has formal limits the synthesized programs inherit.
  - **Status**: 🟢 Verified.

- **Programmatic Knowledge Editing as Knowledge Compilation** (essay-style framing).
  - **Contribution**: Treats "knowledge of how to reason" as compiled programs in the model's weights — a unifying frame for the program-synthesis view that connects also to knowledge-editing literature.
  - **Why it matters**: Useful framing; mostly informal as of 2026.
  - **Status**: 🟡 Position piece. Cite for context.

## Debates

- **Which framework is *most* explanatory?** Compute-depth wins on formal completeness; program-synthesis wins on training-pipeline intuition; Bayes-over-thoughts wins on training-distribution structure. None wins on all axes.

- **Are the frameworks reducible to each other?** Probably not cleanly. Compute-depth and Bayes-over-thoughts answer different questions (operational vs informational). Program-synthesis sits between them.

- **What does "reasoning" mean, formally?** Some authors define it operationally (the model emits a chain and gets correct answers on a benchmark); others demand a stronger condition (the chain is causal for the answer, generalizes to held-out tasks, transfers across domains). The choice of definition determines which framework looks most explanatory.

- **Mechanistic-interpretability bridging.** The frameworks above are theoretical / behavioral. Connecting them to *circuits* (which heads, which residual-stream directions) is barely begun for reasoning. Promising direction.

## Where to start

- **Skim path (90 min)**: Merrill & Sabharwal 2024 (compute-depth) → Prystawski et al. 2023 (Bayes-locality) → Pfau et al. 2024 (filler-tokens test).
- **Deep path (1 weekend)**: + Li et al. 2024 (serial problems), Feng et al. 2023 (CoT mystery), Xie et al. 2022 (ICL-as-Bayes), Bachmann & Nagarajan 2024 (next-token pitfalls).
- **Research path**: full chapter + the foundations-list theory papers + the cross-cutting essay [Why do reasoning models work? A synthesis](../essays/why-do-reasoning-models-work-a-synthesis.md).

## Reproduction

- No notebook for this chapter. Theoretical content is verified formally, not reproduced numerically.
- For the *empirical* anchors (Prystawski locality, Pfau filler tokens), each has open code linked in the cited papers.

## Open problems

- **A unifying theory of CoT effectiveness.** Combining compute-depth (operational), program-synthesis (training), and Bayes-over-thoughts (informational) into one account. No serious candidate as of 2026.
- **A predictor of *which* tasks each framework explains.** Empirical taxonomy needed; partial sketches exist.
- **The role of mechanistic interpretability.** Connecting theoretical frameworks to circuit-level evidence; barely begun for reasoning models.
- **The faithfulness-framework interaction.** Bayes-over-thoughts predicts faithful CoTs (the tokens are evidence). Empirical unfaithfulness is a problem for the strict Bayesian view. Resolution unclear.

---

*Previous: [Chapter 7 — Faithfulness of Reasoning Traces](07-faithfulness-of-reasoning.md). Back to [README](../README.md).*
