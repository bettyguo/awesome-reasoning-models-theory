# Chapter 4 — Search at Inference

> *Structured exploration over CoT prefixes recovers solutions a greedy decode misses.*

## TL;DR

If sampling is a flat distribution over CoTs and best-of-N picks the best one, *search* introduces structure: the model can branch from promising prefixes, abandon dead ends, and aggregate partial solutions. Tree of Thoughts (Yao et al. 2023) and Graph of Thoughts (Besta et al. 2023) formalized this. AlphaCode-style massive parallel sampling-and-rerank (Li et al. 2022) is its industrial precursor. The 2025 wave of "recursive self-aggregation" methods unifies search with iterative refinement. The empirical picture: search helps when the partial-solution value function is informative, hurts when it isn't, and is consistently outperformed in compute-per-accuracy terms by RL training that *internalizes* the search procedure into the policy (Ch 5).

## The mechanism

Three families of inference-time search, in order of structural complexity:

1. **Linear refinement (self-refine, self-improve, self-correction).** The model evaluates and edits its own output. Cheap; surprisingly often *hurts* accuracy because the model rewrites correct solutions into wrong ones (Huang et al. 2024). Useful with an external critic or verifier.

2. **Tree search (ToT, MCTS over CoT).** Branch at decision points; use a value heuristic to expand promising children; prune unpromising ones. Closer to classical game-tree search. The value heuristic is usually the model rating its own partial chains (often unreliable) or a trained PRM (Ch 3).

3. **Graph / DAG search (GoT, recursive aggregation).** Generalizes tree search with operators for combining partial solutions. Useful when the problem decomposes and sub-solutions can be merged (e.g. sorting, multi-step planning).

**The value-function bottleneck.** Search dominates flat BoN only when the partial-solution value function is informative. For math at training time, PRMs supply this; for novel problems with no PRM, the model rates its own partial work, which is unreliable in the way Lanham/Turpin showed CoTs themselves can be. Without a good value function, tree search degenerates to weighted BoN.

**Search vs amortized search.** RL-trained reasoners (Ch 5) appear to *internalize* parts of the search loop: their unconditional sampling distribution puts more mass on solution paths a tree search would discover. Hence the recurring 2024–2025 finding that explicit MCTS over an RL-trained model adds *less* than the same MCTS over a base model. The two compete for the same explanatory variable.

**Where search is still ahead.** On tasks that don't fit the RL training distribution (formal theorem proving, novel mathematical olympiad style problems, ARC-AGI-style abstract reasoning), explicit search continues to add value because the policy hasn't been trained to mimic the search.

## Key papers

- **Tree of Thoughts: Deliberate Problem Solving with Large Language Models** (2023) — *Yao, Yu, Zhao, Shafran, Griffiths, Cao, Narasimhan.* [arXiv:2305.10601](https://arxiv.org/abs/2305.10601).
  - **Contribution**: Generalizes CoT to a tree of partial-solution states with branch evaluation and pruning. Demonstrates gains on Game of 24, creative writing, mini crosswords.
  - **Why it matters**: The canonical "search over CoT" paper. The frame for the entire sub-area.
  - **Status**: 🟢 Verified.

- **Graph of Thoughts: Solving Elaborate Problems with Large Language Models** (2023) — *Besta et al.* [arXiv:2308.09687](https://arxiv.org/abs/2308.09687).
  - **Contribution**: Extends ToT to DAGs with explicit aggregation operators (sort, merge, score). Useful when sub-solutions are non-redundant and combinable.
  - **Why it matters**: Establishes the DAG generalization; some tasks (e.g. sorting) literally need it.
  - **Status**: 🟢 Verified.

- **Competition-Level Code Generation with AlphaCode** (2022) — *Li, Choi, Chung, ... DeepMind.* Science. [arXiv:2203.07814](https://arxiv.org/abs/2203.07814).
  - **Contribution**: Pre-LLM-era industrial demonstration that massive parallel sampling (up to 10^6 samples per problem) plus filtering and clustering solves competition-level coding problems.
  - **Why it matters**: The maximal-scale BoN/search benchmark; informs scaling laws for sampling-based inference.
  - **Status**: 🟢 Verified.

- **Self-Refine: Iterative Refinement with Self-Feedback** (2023) — *Madaan et al.* [arXiv:2303.17651](https://arxiv.org/abs/2303.17651).
  - **Contribution**: Show that models can iteratively critique and rewrite their own outputs to improve quality on multiple tasks.
  - **Why it matters**: The optimistic side of self-refinement. Pair with Huang et al. (next) for the pessimistic counterpart.
  - **Status**: 🟢 Verified.

- **Large Language Models Cannot Self-Correct Reasoning Yet** (2024) — *Huang, Chen, Mishra, Zheng, Yu, Song, Zhou.* ICLR 2024. [arXiv:2310.01798](https://arxiv.org/abs/2310.01798).
  - **Contribution**: Without an external signal of correctness, model-driven self-correction often *degrades* accuracy: the model second-guesses correct answers into wrong ones.
  - **Why it matters**: The corrective to over-optimism about self-refinement. Search-without-a-value-function is unreliable.
  - **Status**: 🟢 Verified.

- **Recursive Self-Aggregation Unlocks Deep Thinking in Large Language Models** (2025) — *Venkatraman et al.* [arXiv:2509.26626](https://arxiv.org/abs/2509.26626).
  - **Contribution**: Recursive loop: sample K chains, summarize them into a meta-prompt, recurse. Empirically competitive with explicit tree search at lower implementation complexity.
  - **Why it matters**: Suggests a simpler search regime that achieves much of the benefit. The 2025 trend toward "search-by-iterative-self-prompting" over explicit tree data structures.
  - **Status**: 🟡 Verify arXiv ID at addition time.

- **Reasoning with Reinforced Functional Token Tuning** (2025) — *e.g. ReFT and its successors.* [arXiv:2401.08967](https://arxiv.org/abs/2401.08967).
  - **Contribution**: Train the policy to emit special tokens that trigger tree-search-like behavior at inference. Internalize part of the search.
  - **Why it matters**: A concrete example of the search-vs-RL collapse: the search is partially baked into the policy.
  - **Status**: 🟡 Verify.

- **Stream of Search (SoS): Learning to Search in Language** (2024) — *Gandhi, Lee, Grand, Liu, Cheng, Sharma, Goodman.* [arXiv:2404.03683](https://arxiv.org/abs/2404.03683).
  - **Contribution**: Train language models to perform search inline, emitting backtracking and exploration as natural language. Outperforms in-context CoT on countdown-style puzzles.
  - **Why it matters**: Most direct demonstration that search can be *learned* rather than externally implemented. Important precedent for the o1/R1-style internalization.
  - **Status**: 🟢 Verified.

- **AlphaProof / AlphaGeometry-style theorem-proving systems** (DeepMind, 2024–2025). [project page](https://deepmind.google/research/projects/ai-mathematical-olympiad/).
  - **Contribution**: Tree search over formal proof steps with neural value functions. Achieves IMO-medal-level performance in formal-proof settings.
  - **Why it matters**: Demonstrates that on the *right* task (formal verifier exists), explicit search remains the dominant approach. Open evidence for the regime structure of search.
  - **Status**: 🟢 Verified, primary-source DeepMind.

- **OpenAI o1 / Strawberry rumored MCTS** — *unconfirmed.*
  - **Contribution**: Rumored to use MCTS over CoT during training and/or inference. *(closed-model, unconfirmed)* — no architectural details released.
  - **Why it matters**: Mostly fodder for speculation. R1's open release suggests MCTS may not be load-bearing; pure RL with verifiable rewards reproduces the phenomenon.
  - **Status**: 🔴 Unverified. Cite for context only.

## Debates

- **Explicit search vs internalized policy.** R1 is the empirical anchor: pure RL with verifiable rewards reproduces o1-class scaling without external search. If true at frontier scale, explicit inference-time search is less load-bearing than the 2023 ToT/GoT framing suggested. Critics: this is a function of the training distribution; on novel tasks, search re-emerges.

- **Self-correction with vs without external signal.** Huang et al. is the cleanest negative result. Self-refine (Madaan) and its descendants survive only when an external check (compiler, verifier, ground truth) is available.

- **Where the value function comes from.** PRMs (Ch 3) supply it for math; learned reward models supply it elsewhere; for hard tasks neither suffices. Open question: can the *policy itself* serve as a usable critic? Mostly no, but Yao et al. show partial successes.

## Where to start

- **Skim path (90 min)**: Yao et al. ToT → Madaan et al. Self-Refine → Huang et al. (self-correction limits).
- **Deep path (1 weekend)**: + Besta et al. GoT, AlphaCode (Li et al.), Gandhi et al. (SoS), Venkatraman et al. (recursive self-aggregation).
- **Research path**: full chapter + AlphaProof / AlphaGeometry references and the Chapter 5 RL papers that internalize search.

## Reproduction

- **Notebook (partial)**: [`notebooks/02-best-of-n-vs-self-consistency.ipynb`](../notebooks/02-best-of-n-vs-self-consistency.ipynb) includes a self-refine baseline.
- **What it shows**: On a small open model, naïve self-refine without an external check degrades accuracy on a MATH sample, replicating Huang et al. on a tiny scale.

A more explicit ToT-style search demo is on the WANTED list — open to PRs.

## Open problems

- **A predictor of when search beats RL-trained-policy.** Empirically depends on training-distribution coverage; no formal account.
- **Search over compiled-program intermediate states (theorem proving, code generation).** Domain-specific successes (AlphaProof, AlphaCode), but no unifying framework.
- **The role of "implicit search" in RL-trained reasoners.** Mechanistic-interp work has barely started here. See the cross-cutting essay [Search vs RL: the deep tension](../essays/search-vs-rl-the-deep-tension.md).

---

*Previous: [Chapter 3 — Sampling and Verification](03-sampling-and-verification.md). Next: [Chapter 5 — RL for Reasoning](05-rl-for-reasoning.md).*
