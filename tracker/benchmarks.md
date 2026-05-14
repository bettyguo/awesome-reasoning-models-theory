# Benchmarks tracker

*Last full sweep: 2026-05-14. Next scheduled: 2026-06-01.*

This is a living table. Each cell is a published, verifiable score. See [README](README.md) for sourcing rules.

**Legend.**
- 🟢 open weights, methods public.
- 🟡 open methods, closed weights, or partial release.
- 🔴 closed model, vendor-reported only.
- 🕰️ cell is > 90 days since last verification — treat with caution.
- ⏳ benchmark too new / no stable SOTA yet, or curator unable to verify yet.

---

## Math (school + competition)

| Benchmark | Model | Score | Type | Source | Last verified |
|---|---|---|---|---|---|
| GSM8K (pass@1) | top frontier reasoners (R1, o-class, Claude w/thinking, Gemini) | ≥ 97% | 🟢/🔴 mixed | various | 2026-05-14 |
| MATH-500 (pass@1) | DeepSeek-R1 | **97.3%** | 🟢 open | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948), Table 2 | 2026-05-14 |
| MATH-500 (pass@1) | s1-32B | 93.0% | 🟢 open | [arXiv:2501.19393](https://arxiv.org/abs/2501.19393), Table 1 | 2026-05-14 |
| AIME 2024 (pass@1) | DeepSeek-R1 | **79.8%** | 🟢 open | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948), Table 2 | 2026-05-14 |
| AIME 2024 (cons@64) | DeepSeek-R1 | 86.7% | 🟢 open | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948), Table 2 | 2026-05-14 |
| AIME 2024 (pass@1) | s1-32B | 56.7% | 🟢 open | [arXiv:2501.19393](https://arxiv.org/abs/2501.19393), Table 1 | 2026-05-14 |
| AIME 2025 (pass@1) | various | ⏳ | — | numbers in flux as 2025 contest is re-evaluated | 2026-05-14 |
| FrontierMath (pass@1) | top closed reasoners | reportedly low-teens % | 🔴 vendor | verify against Epoch AI announcements | 2026-05-14 |
| FrontierMath (pass@1) | open reasoners | single-digit % | 🟢 open | various | 2026-05-14 |

**Methodological notes.**
- AIME pass@1 vs. cons@64 are not directly comparable. The DeepSeek-R1 table reports both; consult primary source before headline-comparing across models.
- MATH-500 is saturated for top reasoners; differences below 2% are noise.

## Code

| Benchmark | Model | Score | Type | Source | Last verified |
|---|---|---|---|---|---|
| HumanEval (pass@1) | top reasoners | ≥ 95% | mixed | saturated; not a discriminator | 2026-05-14 |
| LiveCodeBench (pass@1) | DeepSeek-R1 | 65.9% (slice not specified at this row) | 🟢 open | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948), Table 2 — note benchmark dates matter | 2026-05-14 |
| Codeforces (percentile) | DeepSeek-R1 | 96.3 | 🟢 open | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948), Table 2 | 2026-05-14 |
| Codeforces (Elo) | OpenAI o3 family | reportedly > 2700 (Grandmaster) | 🔴 vendor | vendor-reported, no public account | 2026-05-14 |
| SWE-bench Verified | Claude with extended thinking | ⏳ verify | 🔴 vendor | track via Anthropic release notes | 2026-05-14 |
| SWE-bench Verified | open agents | ⏳ verify | 🟢 open | track via SWE-bench leaderboard | 2026-05-14 |

**Methodological notes.**
- LiveCodeBench is date-cutoff designed to avoid contamination; the *slice* (problem date range) materially affects scores. Always state the slice.
- SWE-bench Verified scores depend heavily on agent harness (tool use, retries). Headline numbers without the harness named are not comparable.

## Science / general

| Benchmark | Model | Score | Type | Source | Last verified |
|---|---|---|---|---|---|
| GPQA Diamond (pass@1) | DeepSeek-R1 | **71.5%** | 🟢 open | [arXiv:2501.12948](https://arxiv.org/abs/2501.12948), Table 2 | 2026-05-14 |
| GPQA Diamond (pass@1) | OpenAI o1 (Sept 2024) | reportedly ~ 78% | 🔴 vendor | [openai.com/index/learning-to-reason-with-llms](https://openai.com/index/learning-to-reason-with-llms/) | 2026-05-14 |
| GPQA Diamond (pass@1) | top Anthropic Claude thinking | ⏳ verify | 🔴 vendor | Anthropic system card | 2026-05-14 |
| MMLU (pass@1) | top reasoners | ≥ 88% | mixed | saturated | 2026-05-14 |
| MMLU-Pro (pass@1) | top reasoners | ≥ 80% | mixed | approaching saturation | 2026-05-14 |
| HLE (% solved) | top reasoners | low double digits | mixed | designed not to saturate | 2026-05-14 |

## Abstraction / reasoning

| Benchmark | Model | Score | Type | Source | Last verified |
|---|---|---|---|---|---|
| ARC-AGI-2 (% solved, public set) | leaderboard top | ⏳ verify | mixed | [arcprize.org leaderboard](https://arcprize.org/) | 2026-05-14 |
| ARC-AGI-3 | — | ⏳ | — | launched 2026-03-25; SOTA not yet stable | 2026-05-14 |
| BIG-Bench Hard | top reasoners | ≥ 90% | mixed | use BBH subsets selectively | 2026-05-14 |

---

## How to read this table

- **pass@1** is single-attempt accuracy. The standard for reasoning-model comparison post-o1.
- **pass@k** is the probability that *at least one* of k attempts is correct; relates to Chapters 3 and 4.
- **cons@k** is consensus / majority-vote over k samples — *not* the same as pass@k. DeepSeek-R1's table reports cons@64 alongside pass@1.
- **Closed-model numbers** (🔴) are vendor-reported and not independently verifiable. They appear for completeness; do not stake research claims on them.
- **Open-model numbers** (🟢) come from public papers / model cards with reproducible inference settings.

## Notes on benchmark integrity

Several reasoning benchmarks have documented problems:

- **Contamination**: AIME, MATH, and Codeforces problem statements appear widely on the web (forums, solution archives). Models pretrained after the contest date may have seen them. Where contamination-controlled comparisons exist (LiveCodeBench's date-cutoff design, recent FrontierMath releases) we prefer those.
- **Inconsistent pass@k disclosure**: some headline "pass@1" numbers silently include majority-vote-over-k. Always read the methodology section, not the abstract.
- **Tool use ambiguity** on SWE-bench: "Verified" can mean "the model produces a patch alone" or "the model uses repository search / shell tools to navigate first." Different numbers.
- **Vendor cherry-picking**: closed-model reports sometimes use bespoke prompting or evaluation harnesses that aren't replicable. The numbers in this table for closed models prefer system-card / paper sources over blog screenshots.

## Digests

Monthly summaries of what moved on the table:

- [2026-05-digest.md](digests/2026-05-digest.md) — initial sweep at repo launch.

---

*Suggested by an audit gap? File an issue with the `tracker` label and the [tracker-update form](../.github/ISSUE_TEMPLATE/tracker-update.yml).*
