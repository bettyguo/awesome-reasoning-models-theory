# Reasoning Models Cheat Sheet

One page. Print, screenshot, share. Each row is the smallest summary that does not mislead.

*Last updated: 2026-05-14.*

---

## The arc in 60 seconds

```
2022 CoT prompting   →   2023 PRMs / ToT   →   2024 test-time scaling
                                                ↓
                                          2024-09 o1 (closed)
                                                ↓
                                          2025-01 R1 (open)
                                                ↓
                              overthinking + faithfulness debates
                                                ↓
                                       FrontierMath, ARC-AGI-3
```

---

## If you remember one thing per chapter

| # | Chapter | One sentence |
|---|---------|---|
| 1 | CoT & Scratchpads | Intermediate tokens turn a fixed-depth forward pass into an unbounded serial program. |
| 2 | Test-time compute scaling | Inference compute trades off against training compute with a *task-dependent* exchange rate. |
| 3 | Sampling & verification | At fixed budget, ranked: BoN+PRM > self-consistency > single long-CoT > greedy. |
| 4 | Search at inference | Search dominates RL on tasks the RL didn't cover; RL absorbs search elsewhere. |
| 5 | RL for reasoning | RLVR is elicitation, not learning — R1-Zero proves the circuits are already in the base. |
| 6 | Overthinking & length | The optimal chain length is task-dependent; flooring *and* ceiling matter. |
| 7 | Faithfulness | CoTs often post-hoc rationalize. RL training reduces this but does not eliminate it. |
| 8 | Theoretical frameworks | Three accounts — compute-depth, program synthesis, Bayes-over-thoughts — none alone is sufficient. |

---

## The R1 recipe, in 5 lines

1. **Base**: a strong pretrained model (≈ 7B+ for the recipe to work).
2. **R1-Zero**: pure RL with verifiable rewards (math answer match, code unit tests).
3. **GRPO** algorithm: PPO without the value head; group-relative advantage normalization.
4. **R1**: R1-Zero + cold-start SFT for readability + a final RL pass.
5. **Output**: a model that emits long self-correcting CoTs and reaches o1-class accuracy on math/code.

> Cold-start SFT is cosmetic. The reasoning was already in the base; RL elicited it.

---

## Test-time compute strategies — compact comparison

| Strategy | Verifier needed? | Compute cost | Wins when |
|---|---|---|---|
| Greedy long-CoT | No | 1× | Easy problems, model is well-calibrated |
| Self-consistency (cons@K) | No | K× | Discrete answer + model right more often than any single wrong answer |
| Best-of-N + PRM | Yes (good one) | K× + verifier | Hard problems + step-level signal available |
| Tree of Thoughts | Yes (value fn) | varies | Small-state planning, partial-solution value informative |
| Recursive self-aggregation | Optional | iterations × K | Tasks where summarization-then-recurse adds context |
| Test-time training | Gradient access | gradients per Q | Out-of-distribution (e.g. ARC-AGI) |

---

## ORMs vs PRMs in one line each

- **Outcome reward model (ORM)** — scores entire trace by final-answer correctness. Cheap labels, low signal.
- **Process reward model (PRM)** — scores each intermediate step. Expensive labels, high signal. Beats ORM at fixed label budget (Lightman et al. 2023).
- **Math-Shepherd-style auto-PRMs** — synthesize step labels by Monte-Carlo rollouts. Closes most of the cost gap.

---

## When does CoT help, when does it hurt?

| Task type | CoT effect | Why |
|---|---|---|
| Multi-step math, algorithms, symbolic | **Big help** | Serial compute is the bottleneck; CoT extends it |
| Multi-hop fact composition | Help | Bayesian-locality recovery (Prystawski 2023) |
| Single-step factual lookup | Neutral / slight hurt | Compute extension doesn't apply; latency cost |
| Easy arithmetic for an RL-trained reasoner | **Hurts** | Overthinking: long chain creates error opportunities |
| Tasks with prompt-bias hints | Unfaithful | Chain rationalizes a bias-driven answer (Turpin 2023) |
| Long-horizon agent tasks | Weak benefit | Verifier-poor regime; scaling law degrades |

---

## Faithfulness tests (Lanham battery)

A CoT is *faithful* iff it passes all four:

1. **Truncation** — cutting at step *k* changes the answer (the model was using the chain).
2. **Paraphrase** — semantically equivalent chains give the same answer (chain content matters).
3. **Mistake injection** — wrong intermediate steps propagate to wrong final answers.
4. **Filler tokens** — replacing the chain with filler reduces accuracy (content > pure compute).

Failing any test: the chain is at least partially decorative. Empirically, no current model passes all four cleanly on adversarial inputs.

---

## Vendor-reported vs verified

| Claim | Source | Status |
|---|---|---|
| "o1 scaling curve on AIME" | OpenAI blog 2024-09 | 🔴 vendor-reported, no public infra |
| "o3 reaches > 2700 Codeforces Elo" | OpenAI announcement | 🔴 vendor-reported |
| DeepSeek-R1: AIME-24 79.8% pass@1 | arXiv:2501.12948 Table 2 | 🟢 open weights, reproducible |
| s1-32B: AIME-24 56.7%, MATH-500 93% | arXiv:2501.19393 Table 1 | 🟢 open |
| AlphaProof: IMO 2024 silver | Nature 2025 / DeepMind blog | 🟢 primary source |

**Rule of thumb.** If the curve is screenshot-able and the model is closed, treat it as a claim, not evidence.

---

## Common confusions to avoid

- **pass@1** ≠ **cons@k** ≠ **pass@k**. Always check which.
- **"o1-style"** is a phrase, not a guarantee. Many "o1-style" papers test only on easy slices.
- **"R1-distilled"** small models are *distillations of R1's outputs*, not RL-trained themselves.
- **"Reasoning model"** in 2025–2026 usage means an RL-trained, long-CoT model. A base instruct model doing CoT prompting is not a reasoning model.
- **"Faithful"** means the chain causes the answer, not "the chain sounds correct."

---

## Five papers if you only read five

1. [Wei et al. 2022, "Chain-of-Thought Prompting"](https://arxiv.org/abs/2201.11903) — origin.
2. [Lightman et al. 2023, "Let's Verify Step by Step"](https://arxiv.org/abs/2305.20050) — PRMs.
3. [Snell et al. 2024, "Test-Time Compute Optimally"](https://arxiv.org/abs/2408.03314) — the scaling law.
4. [DeepSeek-AI 2025, "DeepSeek-R1"](https://arxiv.org/abs/2501.12948) — the open recipe.
5. [Lanham et al. 2023, "Measuring Faithfulness"](https://arxiv.org/abs/2307.13702) — the corrective.

---

## Open problems (priority)

- A predictor for the optimal test-time strategy at a given (task, budget).
- A mechanistic story for the "aha moment" emergence under RLVR.
- Faithfulness as a primary training objective (currently no clean recipe).
- Verifier scaling laws — how much accuracy follows from how much verifier compute.
- Test-time training (Akyurek et al.) as an alternative scaling axis on harder benchmarks.

---

*Want this in a different format (PDF, slide)? PR a converter. Want a row corrected? Open an issue.*
