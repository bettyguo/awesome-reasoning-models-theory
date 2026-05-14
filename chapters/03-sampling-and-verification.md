# Chapter 3 — Sampling and Verification

> *Reranking / voting over samples extracts answer-quality faster than improving any single sample.*

## TL;DR

A reasoning model that gets the right answer 30% of the time on one sample may get it 80% of the time across 32 samples — *if* you can identify the right one. The two routes are *self-consistency* (majority vote, no verifier) and *best-of-N* (rerank with a verifier). Cobbe et al. (2021) and Wang et al. (2022) established the empirical phenomenon. Lightman et al. (2023) showed that *process* reward models — verifiers that score intermediate steps — train better than *outcome* reward models at the same labeling budget. The current frontier: scaling laws for the verifier (Liu et al. 2025), and dealing with imperfect verifiers without amplifying their errors (Rohatgi et al. 2025).

## The mechanism

Frame the model's output as a distribution `p(answer | question)`. If the right answer has mass `p`, drawing N samples gets you `pass@N = 1 - (1-p)^N` — coverage. The hard part is *selection*: picking the right answer when multiple appear.

Three selection regimes, in increasing strength and cost:

1. **Majority vote (self-consistency).** Pick the answer with the most votes. Works when (a) the answer space is discrete and (b) the model is right more often than any specific wrong answer. Failure mode: confidently wrong answers dominate the vote.

2. **Outcome reward model (ORM).** Train a scoring head to predict final-answer correctness from the full (question, chain, answer) trace. Use it to rerank. Strictly stronger than majority vote when the ORM beats vote on the held-out set.

3. **Process reward model (PRM).** Score each *intermediate step*. Aggregate (sum, min, product) to a trace score. Use for reranking *or* for step-level search (Ch 4). Empirically stronger per label budget than ORMs (Lightman et al. 2023), at higher labeling cost.

**Why PRMs win at fixed label budget.** Lightman et al. analyze on MATH that step-level labels carry more information per dollar than trace-level labels, because they identify *where* a chain goes wrong, not just *whether*. Math-Shepherd (Wang et al. 2023) shows you can synthesize PRM labels via Monte-Carlo rollouts ("a step is good if rollouts from it land correctly") — partially closes the label-cost gap.

**Imperfect verifiers and reward hacking.** A verifier's job is to be more accurate than the policy. When it isn't, BoN amplifies verifier error. Rohatgi et al. (2025) study how to "tame imperfect process verifiers" with calibration and ensembling. In RL training (Ch 5), reward hacking is the operationalization: the policy finds inputs the verifier scores high but a human wouldn't.

**The compute-allocation question.** At fixed total budget, do you spend more on generator samples or verifier scoring? Liu et al. (2025) show non-trivially that scaling verifier compute (longer, more careful PRM forward passes) matters comparably to scaling generator samples — implying current pipelines underspend on verifiers.

## Key papers

- **Training Verifiers to Solve Math Word Problems** (2021) — *Cobbe et al.* [arXiv:2110.14168](https://arxiv.org/abs/2110.14168).
  - **Contribution**: Introduces GSM8K and trains a verifier that reranks generated solutions. Sample-and-rerank substantially outperforms greedy decoding.
  - **Why it matters**: The original best-of-N-with-verifier paper. The pattern every modern reasoning system uses.
  - **Status**: 🟢 Verified.

- **Self-Consistency Improves Chain of Thought Reasoning in Language Models** (2022) — *Wang et al.* [arXiv:2203.11171](https://arxiv.org/abs/2203.11171).
  - **Contribution**: Sample K independent CoTs, take the majority-vote answer. No verifier needed. Recovers most of the BoN benefit on math.
  - **Why it matters**: The verifier-free baseline. Surprisingly hard to beat for many tasks.
  - **Status**: 🟢 Verified.

- **Let's Verify Step by Step** (2023) — *Lightman, Kosaraju, Burda, Edwards, Baker, Lee, Leike, Schulman, Sutskever, Cobbe.* [arXiv:2305.20050](https://arxiv.org/abs/2305.20050).
  - **Contribution**: Trains a process reward model on MATH using human step-level labels (the PRM800K dataset). PRMs substantially beat ORMs at fixed labeling budget when used to rerank.
  - **Why it matters**: The canonical PRM paper. Sets the methodological standard for the sub-field.
  - **Status**: 🟢 Verified.

- **Solving math word problems with process- and outcome-based feedback** (2022) — *Uesato, Kushman, Kumar, Song, Siegel, Wang, Creswell, Irving, Higgins.* [arXiv:2211.14275](https://arxiv.org/abs/2211.14275).
  - **Contribution**: Predates Lightman et al. on the process-vs-outcome comparison. Independent demonstration that step-level feedback helps.
  - **Why it matters**: Establishes the result is not OpenAI-specific. DeepMind angle.
  - **Status**: 🟢 Verified.

- **Math-Shepherd: Verify and Reinforce LLMs Step-by-step without Human Annotations** (2023) — *Wang et al.* [arXiv:2312.08935](https://arxiv.org/abs/2312.08935).
  - **Contribution**: Replaces human PRM labels with automatic ones: a step is labeled "good" if Monte-Carlo rollouts from it reach the correct answer with sufficient probability.
  - **Why it matters**: Closes the cost gap with human-labeled PRMs. The de facto standard for open-source PRM labeling pipelines.
  - **Status**: 🟢 Verified.

- **Large Language Monkeys: Scaling Inference Compute with Repeated Sampling** (2024) — *Brown et al.* [arXiv:2407.21787](https://arxiv.org/abs/2407.21787).
  - **Contribution**: Pass@K scaling: with many samples, weak models approach strong-model performance on tasks with checkable answers.
  - **Why it matters**: Quantifies what sample coverage buys *before* you add a verifier. Frame for everything else in this chapter.
  - **Status**: 🟢 Verified.

- **Taming Imperfect Process Verifiers: Better Inference with Worse Reward Models** (2025) — *Rohatgi et al.* [arXiv:2509.21219](https://arxiv.org/abs/2509.21219).
  - **Contribution**: Analyzes BoN under imperfect PRMs; proposes calibration and ensembling fixes that recover most of the perfect-verifier performance.
  - **Why it matters**: Closes the loop on the "verifier failures amplify under BoN" problem. Practical guidance for deployed pipelines.
  - **Status**: 🟢 Verified.

- **Inference-Time Scaling for Generalist Reward Modeling** (2025) — *Liu et al.* [arXiv:2504.02495](https://arxiv.org/abs/2504.02495).
  - **Contribution**: Scaling the *verifier's* inference compute (rather than the generator's) materially improves BoN. The compute-allocation question between G and V is non-trivial.
  - **Why it matters**: Bridges Ch 2 and Ch 3. Most pipelines underspend on the verifier.
  - **Status**: 🟢 Verified.

- **Generative Verifiers: Reward Modeling as Next-Token Prediction** (2024) — *Zhang et al.* [arXiv:2408.15240](https://arxiv.org/abs/2408.15240).
  - **Contribution**: Instead of a scalar reward head, train the verifier to *generate* a verification trace. Improves accuracy and provides natural explainability.
  - **Why it matters**: The current open-source default for verifiers. Lets the verifier itself be a CoT model.
  - **Status**: 🟢 Verified.

- **The Lessons of Developing Process Reward Models in Mathematical Reasoning** (2024) — *Zhang, Zhoubian, Hu, Yue, Dong, Tang.* [arXiv:2501.07301](https://arxiv.org/abs/2501.07301).
  - **Contribution**: Practitioner-oriented analysis of PRM training pitfalls (label noise, scale effects, transfer across math domains). Identifies systematic failure modes.
  - **Why it matters**: The kind of paper a deployment team actually needs. Saves rediscovering the same gotchas.
  - **Status**: 🟢 Verified.

## Debates

- **PRMs vs ORMs at frontier label budgets.** Lightman et al. establishes PRM > ORM at the budgets they studied. Whether the gap holds at much larger budgets (or whether ORMs catch up given enough labels) is open.

- **Synthetic-label PRMs vs human-label PRMs.** Math-Shepherd-style automatic labels are cheap but noisier. The 2024 Zhang et al. lessons paper documents specific failure patterns. Some labs report no usable gap on math; others report human labels still dominate.

- **Self-consistency floor.** On many tasks, plain self-consistency comes within a few percentage points of best-of-N with the best available PRM. The marginal value of a learned verifier may be smaller than reported when the comparator is well-tuned self-consistency rather than greedy decoding.

- **Verifier capability ≥ policy capability?** A verifier needs to be at least as discriminating as the policy is generative, on the relevant dimension. As reasoning models climb to the point where their outputs exceed available verifier accuracy, the BoN advantage diminishes. Active research area in 2025–2026.

## Where to start

- **Skim path (90 min)**: Cobbe et al. (verifier reranking) → Wang et al. (self-consistency) → Lightman et al. (PRM > ORM).
- **Deep path (1 weekend)**: + Uesato et al. (DeepMind angle), Brown et al. (pass@K), Math-Shepherd (auto-labeling), Zhang et al. 2024 lessons.
- **Research path**: full chapter + Liu et al. (inference-time RM scaling) + Rohatgi et al. (imperfect verifiers).

## Reproduction

- **Notebook**: [`notebooks/02-best-of-n-vs-self-consistency.ipynb`](../notebooks/02-best-of-n-vs-self-consistency.ipynb).
- **What it shows**: At a fixed total token budget on a MATH sample, BoN with a small PRM beats self-consistency by a measurable margin, and both beat single-sample long-CoT. The crossover budget where BoN > self-consistency is task-dependent.

Companion: [`notebooks/05-process-reward-model-toy.ipynb`](../notebooks/05-process-reward-model-toy.ipynb) trains a tiny PRM on a synthetic stepwise task and demonstrates that it identifies bad intermediate steps with above-chance accuracy.

## Open problems

- **Verifier scaling laws (the verifier side of Snell et al.).** Liu et al. is a start; we want a full Pareto frontier.
- **Robustness of PRMs to distribution shift.** Trained on MATH, used on AIME — how much accuracy is lost?
- **Combining ORMs and PRMs.** The trade-off in label cost vs accuracy admits an obvious ensemble; no clean reference.
- **Non-math domains.** PRMs are mostly studied on math because step-labeling is tractable. Code (intermediate compilation), reasoning (intermediate fact-checking), and theorem proving each need their own.

---

*Previous: [Chapter 2 — Test-Time Compute Scaling](02-test-time-compute-scaling.md). Next: [Chapter 4 — Search at Inference](04-search-at-inference.md).*
