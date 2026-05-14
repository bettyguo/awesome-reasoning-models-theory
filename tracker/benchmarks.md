# Benchmarks tracker

*Last full sweep: 2026-05-14. Next scheduled: 2026-06-01.*

This is a living table. Each cell is a published, verifiable score. See [README](README.md) for sourcing rules.

**Legend.**
- 🟢 open weights, methods public.
- 🟡 open methods, closed weights, or partial release.
- 🔴 closed model, vendor-reported only.
- 🕰️ cell is > 90 days since last verification — treat with caution.
- ⏳ benchmark too new / no stable SOTA yet.

---

## Math (school + competition)

| Benchmark | Current SOTA | Model | Org | Date reported | Last verified | Notes |
|---|---|---|---|---|---|---|
| **GSM8K** (pass@1) | ~ 97% | several frontier reasoners | various | 2025 | 2026-05-14 | Saturated. Used as a calibration baseline, not a discriminator. |
| **MATH-500** (pass@1) | ~ 97% (closed), ~ 94% (open) | o3 (closed) / R1-class (open) | OpenAI / DeepSeek | 2025-Q1 | 2026-05-14 | 🔴 closed value; 🟢 open value from DeepSeek-R1 report. Saturated for top tier. |
| **AIME 2024** (pass@1, single-attempt) | high-80s to mid-90s % | o3 / R1 / Claude reasoning | various | 2025 | 2026-05-14 | Used as a primary reasoner discriminator throughout 2025. |
| **AIME 2025** (pass@1) | ⏳ | — | — | — | 2026-05-14 | Recent; numbers in flux as 2025 contest set is re-evaluated. |
| **FrontierMath** (pass@1) | single-digit % (closed) to low-teens % (top closed) | o3 / Claude reasoning | OpenAI / Anthropic | 2025 | 2026-05-14 | 🔴 vendor-reported. Verify against Epoch AI announcements. |
| **Putnam 2024/2025** (problems solved) | ⏳ | — | — | — | 2026-05-14 | Increasing community attention; no settled SOTA. |

## Code

| Benchmark | Current SOTA | Model | Org | Date reported | Last verified | Notes |
|---|---|---|---|---|---|---|
| **HumanEval** (pass@1) | > 95% | many models | various | 2024+ | 2026-05-14 | Saturated. Not a discriminator. |
| **LiveCodeBench** (pass@1, recent slice) | TBD verify | varies | various | 2025+ | 2026-05-14 | Refresh quarterly; record cutoff date with each entry. |
| **SWE-bench Verified** (% resolved) | ~ 70-80% (closed top) | Claude / OpenAI agent reasoners | Anthropic / OpenAI | 2025 | 2026-05-14 | Verify exact number against agent-mode reports. |
| **Codeforces Elo** (model rating) | reportedly > 2700 (closed) | o3 / o4 class | OpenAI | 2025 | 2026-05-14 | 🔴 vendor-reported. No public CF account, no independent verification. |

## Science / general

| Benchmark | Current SOTA | Model | Org | Date reported | Last verified | Notes |
|---|---|---|---|---|---|---|
| **GPQA Diamond** (pass@1) | ~ 85-90% | top closed reasoners | OpenAI / Anthropic / Google | 2025 | 2026-05-14 | Verify exact best from each lab's latest model card. |
| **HLE** (% solved) | low double digits | top reasoners | various | 2024-2025 | 2026-05-14 | Designed not to saturate. Track movement, not absolute. |
| **MMLU-Pro** (pass@1) | ~ 80%+ | frontier reasoners | various | 2024-2025 | 2026-05-14 | Approaching saturation at top tier. |

## Abstraction / reasoning

| Benchmark | Current SOTA | Model | Org | Date reported | Last verified | Notes |
|---|---|---|---|---|---|---|
| **ARC-AGI-2** | TBD verify | varies | varies | 2024-2025 | 2026-05-14 | Numbers move with leaderboard activity; verify at update time. |
| **ARC-AGI-3** | ⏳ | — | — | 2026-03-25 launch | 2026-05-14 | Launched 2026-03-25. SOTA not yet stable. |
| **BIG-Bench Hard** | varies | varies | varies | 2024+ | 2026-05-14 | Use BBH subsets selectively. |

---

## How to read this table

- **Pass@1** is single-attempt accuracy, the standard for reasoning-model comparison post-o1.
- **Pass@k** is the probability *at least one* of k attempts is correct — relevant to Ch 3 / 4. We track both where reported.
- **Closed-model numbers** (🔴) are vendor-reported and not independently verifiable. They appear on the table for completeness; do not stake research arguments on them.
- **Open-model numbers** (🟢) come from public papers / model cards with reproducible inference settings.

## Notes on benchmark integrity

Several reasoning benchmarks have been documented to suffer from:

- **Contamination**: models trained on web data that includes problem-set leaks (AIME, MATH solutions on Reddit / forums).
- **Prompt-engineering inflation**: small prompt changes affecting reported numbers by several points; not always disclosed.
- **Pass@k vs pass@1 confusion**: numbers labeled `pass@1` that actually use a hidden voting strategy.

Where these matter, we annotate the relevant cell.

## Digests

Monthly summaries of what moved on the table:

- [2026-05-digest.md](digests/2026-05-digest.md) — initial sweep at repo launch.

---

*Suggested by an audit gap? File an issue with the `tracker` label.*
