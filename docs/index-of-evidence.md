# Index of evidence

*The claims this repo platforms — paired with the evidence behind each. Updated 2026-05-14.*

This is a curator's reference: every load-bearing empirical claim in the chapters and essays is listed here, with its strongest supporting source and a note on what the claim does *not* establish. If you're going to cite this repo, cite the underlying evidence first.

> **How to read.** ✅ = at least one peer-reviewed primary source independently verifiable. 🟡 = primary source exists but the claim is partially vendor-reported or partially contested. 🔴 = the claim circulates widely but the strongest source is vendor-reported with no replication.

---

## Chapter 1 — CoT and Scratchpads

| Claim | Evidence | Strength |
|---|---|---|
| Chain-of-thought prompting lifts accuracy on multi-step tasks | Wei et al. 2022 ([arXiv:2201.11903](https://arxiv.org/abs/2201.11903)) | ✅ |
| Zero-shot CoT works with a single trigger phrase | Kojima et al. 2022 ([arXiv:2205.11916](https://arxiv.org/abs/2205.11916)) | ✅ |
| CoT extends a fixed-depth transformer's effective compute depth | Merrill & Sabharwal 2024 ([arXiv:2310.07923](https://arxiv.org/abs/2310.07923)); Li et al. 2024 | ✅ |
| Scratchpads are mathematically equivalent to CoT for our purposes | Nye et al. 2021 ([arXiv:2112.00114](https://arxiv.org/abs/2112.00114)) — naming, not the equivalence claim per se | 🟡 |

**Does NOT establish.** CoT helps on every task; CoT is faithful; CoT is the actual mechanism the model uses.

---

## Chapter 2 — Test-Time Compute Scaling

| Claim | Evidence | Strength |
|---|---|---|
| Test-time compute can substitute for parameter scaling on reasoning tasks | Snell, Lee, Xu, Kumar 2024 ([arXiv:2408.03314](https://arxiv.org/abs/2408.03314)) | ✅ |
| The scaling curve replicates on small-scale open recipes | Muennighoff et al. 2025 (s1, [arXiv:2501.19393](https://arxiv.org/abs/2501.19393)) | ✅ |
| Budget forcing improves the scaling curve | Muennighoff et al. 2025 | ✅ |
| OpenAI o1's headline scaling plot | OpenAI 2024-09 ([blog](https://openai.com/index/learning-to-reason-with-llms/)) | 🔴 vendor-reported |

**Does NOT establish.** A universal exchange-rate across model scales (see Yang 2025 in Chapter 6); that o1's specific curve replicates without OpenAI's infrastructure.

---

## Chapter 3 — Sampling and Verification

| Claim | Evidence | Strength |
|---|---|---|
| Self-consistency improves CoT reasoning | Wang et al. 2022 ([arXiv:2203.11171](https://arxiv.org/abs/2203.11171)) | ✅ |
| Process reward models outperform outcome reward models at equal label budget | Lightman et al. 2023 ([arXiv:2305.20050](https://arxiv.org/abs/2305.20050)) | ✅ |
| Best-of-N with a good verifier dominates self-consistency on hard tasks | Cobbe et al. 2021 ([arXiv:2110.14168](https://arxiv.org/abs/2110.14168)); Lightman et al. 2023 | ✅ |
| Math-Shepherd-style auto-PRMs close most of the labeling cost gap | Wang et al. 2024 ([arXiv:2312.08935](https://arxiv.org/abs/2312.08935)) | ✅ |

**Does NOT establish.** PRMs in the *reward loop* are stable (see Controversy #6); verifier-side scaling has known asymptotes.

---

## Chapter 4 — Search at Inference

| Claim | Evidence | Strength |
|---|---|---|
| Tree-search over CoT branches improves over greedy decoding | Yao et al. 2023 (ToT, [arXiv:2305.10601](https://arxiv.org/abs/2305.10601)) | ✅ |
| Recursive self-aggregation beats single-pass long CoT at fixed budget on hard tasks | Venkatraman et al. 2025 ([arXiv:2509.26626](https://arxiv.org/abs/2509.26626)) | ✅ |
| AlphaProof reaches IMO silver via LLM + Lean RL | DeepMind 2024 [blog](https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level/), Nature 2025 | ✅ |
| Gemini Deep Think reaches IMO gold | DeepMind 2025 [blog](https://deepmind.google/discover/blog/advanced-version-of-gemini-with-deep-think-officially-achieves-gold-medal-standard-at-the-international-mathematical-olympiad/) | 🟡 vendor-described, primary source available |

**Does NOT establish.** Search beats RL in general (see Controversy #3); ToT scales to large search budgets without exploding.

---

## Chapter 5 — RL for Reasoning

| Claim | Evidence | Strength |
|---|---|---|
| GRPO is a workable PPO replacement for verifiable-reward RL | Shao et al. 2024 (DeepSeekMath, [arXiv:2402.03300](https://arxiv.org/abs/2402.03300)) | ✅ |
| Pure RL from a strong base (R1-Zero) produces a strong reasoner with no SFT | DeepSeek-AI 2025 ([arXiv:2501.12948](https://arxiv.org/abs/2501.12948)) | ✅ |
| Chain length increases monotonically during RLVR training | DeepSeek-AI 2025, Figure 3 | ✅ |
| "Aha moments" emerge during RL training | DeepSeek-AI 2025, §3.2 | ✅ qualitative |
| RLVR ≠ RLHF for reasoning | Lambert et al. 2024 (Tülu 3, [arXiv:2411.15124](https://arxiv.org/abs/2411.15124)); R1 paper | ✅ |
| The R1 recipe is reproducible on other bases | SimpleRL, Open-Reasoner-Zero, verl (multiple GitHub repos, 2025) | ✅ |

**Does NOT establish.** R1-Zero works on weak bases (see Controversy #7); GRPO is the unique right algorithm (see Controversy #8).

---

## Chapter 6 — Overthinking and Optimal Length

| Claim | Evidence | Strength |
|---|---|---|
| Reasoning models emit excessive chains on trivial problems | Chen et al. 2024 ("Don't think 2+3=", [arXiv:2412.21187](https://arxiv.org/abs/2412.21187)) | ✅ |
| Shorter chains often beat longer ones at fixed budget | Hassid et al. 2025 ([arXiv:2505.17813](https://arxiv.org/abs/2505.17813)) | ✅ |
| Optimal CoT length is task-dependent and well below the model's default | Yang et al. 2025 ([arXiv:2502.18080](https://arxiv.org/abs/2502.18080)) | ✅ |

**Does NOT establish.** A universal "shorter is better" rule (some hard tasks do benefit from more length); that overthinking is fixable purely at inference time.

---

## Chapter 7 — Faithfulness

| Claim | Evidence | Strength |
|---|---|---|
| Models often produce post-hoc rationalizations rather than faithful chains | Turpin et al. 2023 ([arXiv:2305.04388](https://arxiv.org/abs/2305.04388)) | ✅ |
| Lanham faithfulness probes (truncation, paraphrase, mistake injection, filler) discriminate faithful from unfaithful chains | Lanham et al. 2023 ([arXiv:2307.13702](https://arxiv.org/abs/2307.13702)) | ✅ |
| RL training reduces but does not eliminate unfaithfulness | Anthropic 2025 ([research note](https://www.anthropic.com/research/reasoning-models-dont-always-say-what-they-think)) | 🟡 — partial publication, full methodology in supplementary |
| Reward-hacking can produce systematic unfaithfulness in frontier reasoners | Anthropic 2025 | 🟡 |

**Does NOT establish.** That chains are *always* unfaithful; that faithfulness can be trained directly as an objective.

---

## Chapter 8 — Theoretical Frameworks

| Claim | Evidence | Strength |
|---|---|---|
| Constant-depth log-precision transformers live in TC₀ | Merrill & Sabharwal 2023 ([arXiv:2207.00729](https://arxiv.org/abs/2207.00729)) | ✅ |
| CoT extends transformer expressivity to a strictly larger class | Li et al. 2024 ([arXiv:2305.18869](https://arxiv.org/abs/2305.18869)); Merrill & Sabharwal 2024 | ✅ |
| ICL can be analyzed as Bayesian posterior inference over latent concepts | Xie et al. 2022 ([arXiv:2111.02080](https://arxiv.org/abs/2111.02080)) | ✅ |
| The Bayesian framing extends to multi-step CoT (Bayes-over-thoughts) | Prystawski et al. 2023 ([arXiv:2304.03843](https://arxiv.org/abs/2304.03843)) | ✅ |
| CoT can be interpreted as program synthesis | Multiple informal accounts; no single canonical paper | 🟡 — interpretive framework, not theorem |

**Does NOT establish.** Any *unification* of the three frameworks; that any single framework is the "correct" one.

---

## Benchmark numbers (tracker)

The full per-row sourcing for benchmark numbers lives in [`tracker/benchmarks.md`](../tracker/benchmarks.md). Headline figures:

| Number | Source | Strength |
|---|---|---|
| DeepSeek-R1: AIME-24 79.8% pass@1 | [arXiv:2501.12948 Table 2](https://arxiv.org/abs/2501.12948) | ✅ |
| DeepSeek-R1: MATH-500 97.3% pass@1 | [arXiv:2501.12948 Table 2](https://arxiv.org/abs/2501.12948) | ✅ |
| s1-32B: MATH-500 93.0% pass@1 | [arXiv:2501.19393 Table 1](https://arxiv.org/abs/2501.19393) | ✅ |
| OpenAI o1: AIME-24 ~74% pass@1 | [openai.com](https://openai.com/index/learning-to-reason-with-llms/) | 🔴 vendor-reported |
| OpenAI o3 family: Codeforces > 2700 Elo | OpenAI announcement | 🔴 vendor-reported, no public account |
| AlphaProof: IMO 2024 silver-equivalent | DeepMind blog → Nature 2025 | ✅ |
| Gemini Deep Think: IMO 2025 gold-equivalent | DeepMind blog | 🟡 vendor-described |

---

## Why this index exists

Most awesome-lists cite papers as if every claim in every paper is independently verifiable. That isn't true in this field — vendor blog plots and replication-grade arXiv tables sit side by side. This index forces the curator (and the reader) to be honest about which is which, and to keep the strength flags up to date.

If a row should be upgraded (or downgraded), open an issue with the new evidence.
