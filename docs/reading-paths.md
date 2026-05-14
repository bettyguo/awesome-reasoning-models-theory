# Reading paths

Curated cross-chapter sequences. Each path picks 6–12 papers and sequences them to build a coherent picture of a sub-topic in a weekend or less.

These supplement the per-chapter *Reading paths* sections; this file is the place for sequences that cross chapter boundaries.

---

## Path 1 — *What is the o1 / R1 paradigm, in two evenings?*

For the practitioner who needs to understand the dominant 2024–2026 reasoning recipe end-to-end.

**Evening 1 — the empirical anchor**:

1. [Wei et al. 2022, "Chain-of-Thought Prompting"](https://arxiv.org/abs/2201.11903) — the origin.
2. [Lightman et al. 2023, "Let's Verify Step by Step"](https://arxiv.org/abs/2305.20050) — process reward models.
3. [Snell et al. 2024, "Scaling LLM Test-Time Compute Optimally"](https://arxiv.org/abs/2408.03314) — the test-time-compute scaling law.
4. [OpenAI 2024, "Learning to Reason with LLMs"](https://openai.com/index/learning-to-reason-with-llms/) — o1 announcement (read for context, flagged closed-model).

**Evening 2 — the reproductions**:

5. [DeepSeek-AI 2025, "DeepSeek-R1"](https://arxiv.org/abs/2501.12948) — full RLVR recipe with open weights.
6. [Muennighoff et al. 2025, "s1: Simple Test-Time Scaling"](https://arxiv.org/abs/2501.19393) — the cleanest open scaling-curve reproduction.
7. [Shao et al. 2024, "DeepSeekMath"](https://arxiv.org/abs/2402.03300) — where GRPO originates.

After this path you can read most of arXiv's reasoning-model papers with context.

---

## Path 2 — *I don't trust CoT-as-thought. Convince me one way or the other.*

For the reader skeptical (or persuaded) by the faithfulness debate.

1. [Turpin et al. 2023, "Language Models Don't Always Say What They Think"](https://arxiv.org/abs/2305.04388) — the originating demonstration.
2. [Lanham et al. 2023, "Measuring Faithfulness in Chain-of-Thought Reasoning"](https://arxiv.org/abs/2307.13702) — the measurement framework.
3. [Pfau, Merrill, Bowman 2024, "Hidden Computation in Transformer Language Models"](https://arxiv.org/abs/2404.15758) — filler tokens partly substitute for content.
4. [Chen et al. 2024, "Premise Order Matters in Reasoning"](https://arxiv.org/abs/2402.08939) — different angle, same phenomenon.
5. [Anthropic 2025, "Reasoning Models Don't Always Say What They Think"](https://arxiv.org/abs/2505.05410) — the RL-trained-reasoner version.
6. Read the [faithfulness essay](../essays/is-cot-faithful-the-state-of-the-debate.md) for the synthesis.

Optional dual-use end: [Greenblatt et al. 2024, "Alignment Faking"](https://arxiv.org/abs/2412.14093).

---

## Path 3 — *Is reasoning search or RL?*

For the reader interested in the deep methodological question of whether reasoning model behavior is best explained as inference-time search, RL-amortized policy, or both.

1. [Yao et al. 2023, "Tree of Thoughts"](https://arxiv.org/abs/2305.10601) — the search-side framing.
2. [Gandhi et al. 2024, "Stream of Search"](https://arxiv.org/abs/2404.03683) — search as a learnable behavior.
3. [DeepSeek-AI 2025, "DeepSeek-R1"](https://arxiv.org/abs/2501.12948) — pure RL, no explicit search, reaches o1-class.
4. [Huang et al. 2024, "Large Language Models Cannot Self-Correct Reasoning Yet"](https://arxiv.org/abs/2310.01798) — the self-refine negative result.
5. [DeepMind 2024, AlphaProof (blog)](https://deepmind.google/blog/ai-solves-imo-problems-at-silver-medal-level/) — where explicit search still dominates.
6. Read the [search-vs-RL essay](../essays/search-vs-rl-the-deep-tension.md).

---

## Path 4 — *Theory of why CoT helps (formal + informal)*

For the researcher wanting both the formal-expressivity story and the empirical-explanatory one. Mixes papers from this list and the [sister list](https://github.com/bettyguo/awesome-llm-reasoning-foundations).

1. *(foundations list)* [Merrill & Sabharwal 2024, "CoT expressivity"](https://arxiv.org/abs/2310.07923).
2. *(foundations list)* [Li et al. 2024, "CoT empowers serial problems"](https://arxiv.org/abs/2402.12875).
3. *(this list)* [Prystawski et al. 2023, "Why think step by step?"](https://arxiv.org/abs/2304.03843).
4. *(this list)* [Pfau et al. 2024, "Dot by dot"](https://arxiv.org/abs/2404.15758) — filler-token evidence.
5. *(this list)* [Sprague et al. 2024, "To CoT or not to CoT?"](https://arxiv.org/abs/2409.12183) — meta-analysis of when CoT helps.
6. Read the [synthesis essay](../essays/why-do-reasoning-models-work-a-synthesis.md).

---

## Path 5 — *The overthinking debate*

For the reader interested in chain-length calibration and the empirical line that "longer is not always better."

1. [Chen et al. 2024, "Do Not Think That Much for 2+3=?"](https://arxiv.org/abs/2412.21187) — naming paper.
2. [Hassid et al. 2025, "Don't Overthink it"](https://arxiv.org/abs/2505.17813) — training-time fix.
3. [Xu et al. 2025, "Chain of Draft"](https://arxiv.org/abs/2502.18600) — prompt-time fix.
4. [Yang et al. 2025, "Towards Thinking-Optimal Scaling"](https://arxiv.org/abs/2502.18080) — the principled framing.
5. [Muennighoff et al. 2025, "s1"](https://arxiv.org/abs/2501.19393) §3-4 — budget forcing as the formal knob.
6. [Sui et al. 2025, "Stop Overthinking" (survey)](https://arxiv.org/abs/2503.16419) — the comprehensive index.

---

## Path 6 — *RL-for-reasoning, fast track*

For someone implementing RLVR on their own model.

1. [Shao et al. 2024, "DeepSeekMath"](https://arxiv.org/abs/2402.03300) — GRPO algorithm.
2. [Lambert et al. 2024, "Tulu 3"](https://arxiv.org/abs/2411.15124) — open RLVR recipe.
3. [DeepSeek-AI 2025, "DeepSeek-R1"](https://arxiv.org/abs/2501.12948) — full pipeline.
4. [Luong et al. 2024, "ReFT"](https://arxiv.org/abs/2401.08967) — pre-R1 reference.
5. [Gao, Schulman, Hilton 2022, "Scaling Laws for Reward Model Overoptimization"](https://arxiv.org/abs/2210.10760) — the load-bearing prior result on reward hacking.
6. The [TRL library](https://github.com/huggingface/trl) `GRPOTrainer` source code.
7. Reproduce on a tiny model with [notebook 03](../notebooks/03-tiny-r1-zero-style-training.ipynb).

---

## Path 7 — *Sampling and verification, fast track*

For the inference-side practitioner.

1. [Cobbe et al. 2021, "Training Verifiers"](https://arxiv.org/abs/2110.14168) — origin of BoN-with-verifier.
2. [Wang et al. 2022, "Self-Consistency"](https://arxiv.org/abs/2203.11171) — the verifier-free baseline.
3. [Lightman et al. 2023, "Let's Verify Step by Step"](https://arxiv.org/abs/2305.20050) — PRMs.
4. [Wang et al. 2023, "Math-Shepherd"](https://arxiv.org/abs/2312.08935) — auto-labeled PRMs.
5. [Brown et al. 2024, "Large Language Monkeys"](https://arxiv.org/abs/2407.21787) — pass@K scaling.
6. [Liu et al. 2025, "Inference-Time Scaling for Generalist Reward Modeling"](https://arxiv.org/abs/2504.02495) — verifier-side scaling.
7. [Rohatgi et al. 2025, "Taming Imperfect Process Verifiers"](https://arxiv.org/abs/2509.21219) — practical guidance.
8. Reproduce on a small model with [notebook 02](../notebooks/02-best-of-n-vs-self-consistency.ipynb) and [notebook 05](../notebooks/05-process-reward-model-toy.ipynb).

---

## Calibrating depth

- **Skim path** = ~ 90 minutes. Headlines + abstracts + a single figure per paper.
- **Deep path** = a weekend. Full read of each paper, including methods and ablations.
- **Research path** = a week. Full read + reading the cited papers' citations one layer out.

If a chapter's *Reading paths* section conflicts with a path here, the chapter version is the authoritative one for that chapter — this file's value is the *cross-chapter* sequences.

---

*Filed: 2026-05-14. PR-friendly — propose new paths or revisions via issue.*
