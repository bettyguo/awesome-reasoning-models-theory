<p align="center">
  <img src="assets/banner.svg" alt="Awesome Reasoning Models Theory" width="720"/>
</p>

<h1 align="center">Awesome Reasoning Models Theory</h1>

<p align="center">
  <a href="https://awesome.re"><img src="https://awesome.re/badge.svg" alt="Awesome"></a>
  <a href="LICENSE-content"><img src="https://img.shields.io/badge/content-CC0%201.0-blue.svg" alt="CC0"></a>
  <a href="LICENSE-code"><img src="https://img.shields.io/badge/code-MIT-green.svg" alt="MIT"></a>
</p>

> *Why do reasoning models actually work? A theoretical and empirical map of the o-series / R1 / Claude-thinking paradigm.*

The 2024–2026 emergence of reasoning models — OpenAI o1/o3, DeepSeek-R1, Qwen-QwQ, Claude with thinking, Gemini reasoning variants — is the most consequential paradigm shift in LLM behavior since the transformer. **But the theoretical foundations are surprisingly disputed.** Is the gain coming from:

- search over chain-of-thought space?
- implicit program synthesis?
- RL-shaped policy distributions?
- compute-time circuit-depth extension?
- Bayesian posterior refinement over latent solutions?

Most likely several at once, in different proportions for different tasks. This repo is a *theory-and-mechanism-first* map of the literature — not a prompt-engineering trick aggregator, not a flat paper list. Every claim is grounded in a measurable behavior, and every closed-model claim is flagged as such.

## Scope

**IN scope:**
- Test-time compute scaling (Snell, s1, OpenAI o1 reports, follow-ups)
- Chain-of-thought *mechanism* (does it extend compute? extract serial structure? rationalize?)
- Sampling and verification (best-of-N, self-consistency, outcome and process reward models)
- Search at inference (ToT, GoT, recursive aggregation, MCTS over CoT)
- RL-for-reasoning (R1-Zero, GRPO, RLVR, verifier-free)
- Overthinking, optimal CoT length, refusal-to-think
- Faithfulness of reasoning traces (Turpin, Lanham, 2025 follow-ups)
- Theoretical frameworks bridging the above (compute-depth equivalence, CoT-as-program-synthesis, ICL-as-Bayes extended to multi-step)
- Reasoning benchmarks tracker (AIME, MATH-500, GSM8K, LiveCodeBench, SWE-bench Verified, FrontierMath, ARC-AGI-2/3, HLE, GPQA Diamond)

**OUT of scope (intentionally):**
- CoT prompting tricks without an underlying mechanistic claim
- Application-of-CoT recipes (multi-modal CoT, agent frameworks, retrieval-CoT)
- Pure formal expressivity / circuit-complexity results — covered by the sister list [awesome-llm-reasoning-foundations](https://github.com/bettyguo/awesome-llm-reasoning-foundations).
- Jailbreaks, prompt injection, reasoning-model red-teaming techniques
- Leaderboard-only papers without a methodological contribution

## Reading the narrative in one page

The field's recent arc, compressed:

1. **CoT prompting (2022)** showed that letting models emit intermediate tokens lifts performance on multi-step tasks — but the *why* was unclear.
2. **Process reward models (Lightman et al. 2023)** showed that grading the *steps*, not just the answer, trains better verifiers than outcome-only signals.
3. **Test-time compute scaling (Snell et al. 2024)** crystallized the empirical regularity: throwing more inference-time compute at the right CoT search / verification scheme is often more effective than throwing more pretraining compute.
4. **o1 (OpenAI, Sept 2024)** turned this into a product: long internal CoTs trained via RL with verifiable rewards on math, code, science. The scaling plot became a meme.
5. **DeepSeek-R1 (Jan 2025)** showed the recipe was reproducible *and* much of the gain came from *pure RL* (R1-Zero) without supervised CoT seeding — implying the base model already contained the reasoning circuits, RL elicits them.
6. **The "overthinking" reaction (late 2024–2025)** showed long CoTs *hurt* on easy problems and that shorter chains often beat longer ones at fixed budget.
7. **The faithfulness debate (Turpin 2023; Lanham 2023; Chen et al. 2025)** showed CoTs are often post-hoc rationalizations, complicating their use as evidence about the model's actual computation.

Where this leaves us: a partly-shared set of empirical facts, multiple competing theoretical accounts, and a vibrant disagreement about whether reasoning models are doing *more* than amortized search + RL-shaped policy selection.

## The eight chapters

Each chapter has a TL;DR, the proposed *mechanism*, 8–15 annotated papers, the live debates, reading paths, an open-problems list, and a pointer to its reproduction notebook.

| # | Chapter | Mechanism in one line |
|---|---------|------------------------|
| 1 | [CoT and Scratchpads](chapters/01-cot-and-scratchpads.md) | Intermediate tokens turn a fixed-depth forward pass into an unbounded serial program. |
| 2 | [Test-Time Compute Scaling](chapters/02-test-time-compute-scaling.md) | Inference compute trades off against parameters with task-dependent exchange rate. |
| 3 | [Sampling and Verification](chapters/03-sampling-and-verification.md) | Reranking / voting over samples extracts answer-quality faster than improving any single sample. |
| 4 | [Search at Inference](chapters/04-search-at-inference.md) | Structured exploration over CoT prefixes recovers solutions a greedy decode misses. |
| 5 | [RL for Reasoning](chapters/05-rl-for-reasoning.md) | RL with verifiable rewards reshapes the policy toward long, self-correcting chains. |
| 6 | [Overthinking and Optimal Length](chapters/06-overthinking-and-optimal-length.md) | Beyond a task-dependent optimum, more CoT *hurts* — long chains compound errors. |
| 7 | [Faithfulness of Reasoning Traces](chapters/07-faithfulness-of-reasoning.md) | CoTs are often post-hoc rationalizations; the visible chain ≠ the computation. |
| 8 | [Theoretical Frameworks](chapters/08-theoretical-frameworks.md) | Candidate unifying accounts: compute-depth, program synthesis, Bayes-over-thoughts. |

## Reproduction notebooks

Each notebook isolates a single chapter's *empirical claim* and reproduces it at a scale runnable on a single small GPU (or CPU, for the inference-only notebooks).

- [01 — Test-time compute scaling on a small model](notebooks/01-test-time-compute-scaling.ipynb)
- [02 — Best-of-N vs self-consistency at fixed budget](notebooks/02-best-of-n-vs-self-consistency.ipynb)
- [03 — Tiny R1-Zero-style GRPO run](notebooks/03-tiny-r1-zero-style-training.ipynb)
- [04 — Overthinking on trivial problems](notebooks/04-overthinking-demo.ipynb)
- [05 — Process reward model toy](notebooks/05-process-reward-model-toy.ipynb)

The notebooks are *demonstrations of the signal*, not benchmark contributions. Where compute prohibits a faithful reproduction, the notebook documents the gap and links a fuller hosted run.

## Benchmarks tracker

The [`tracker/`](tracker/) directory hosts a living table of the reasoning benchmarks the field is currently chasing: AIME 2024/2025, MATH-500, GSM8K, HumanEval, LiveCodeBench, SWE-bench Verified, FrontierMath, ARC-AGI-2, HLE, GPQA Diamond, Codeforces Elo. Updated monthly via [`scripts/update_benchmarks.py`](scripts/update_benchmarks.py); each refresh ships with a digest summary in [`tracker/digests/`](tracker/digests/).

## Essays

Longer-form synthesis pieces — the kind a survey would compress to a paragraph and lose the argument:

- [Why do reasoning models work? A synthesis.](essays/why-do-reasoning-models-work-a-synthesis.md)
- [Is CoT faithful? The state of the debate.](essays/is-cot-faithful-the-state-of-the-debate.md)
- [Search vs RL: the deep tension.](essays/search-vs-rl-the-deep-tension.md)
- [Reasoning and mechanistic interpretability.](essays/reasoning-and-mechanistic-interpretability.md)

## Glossary

Field-specific terminology is dense and shifting. The [`GLOSSARY.md`](GLOSSARY.md) defines 50+ terms (GRPO, RLVR, PRM, ORM, verifier-free, R1-Zero, refusal-to-think, sandbagging, ...).

## How to use this repo

- **Practitioner picking a recipe:** start with the chapter intros and the *Reading paths* sections — they are calibrated for skim / weekend / research depth.
- **Researcher entering the field:** read the essays in order, then the chapter open-problems lists.
- **Reviewer or instructor:** the YAML-discoverable annotations + reproduction notebooks are designed to be cite-and-assign-able.

## Related lists

Adjacent lists with deliberately disjoint scope:

- [bettyguo/awesome-llm-reasoning-foundations](https://github.com/bettyguo/awesome-llm-reasoning-foundations) — *formal* foundations: transformer expressivity, CoT error bounds, circuit complexity, logical characterizations, learnability. Sister to this list.
- [atfortes/Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning) — broad CoT → o1 → R1 method list.
- [srush/awesome-o1](https://github.com/srush/awesome-o1) — o1-centric bibliography (largely stale post-R1).
- [hemingkx/Awesome-Efficient-Reasoning](https://github.com/hemingkx/Awesome-Efficient-Reasoning) — efficiency-focused.
- [reasoning-survey/Awesome-Reasoning-Foundation-Models](https://github.com/reasoning-survey/Awesome-Reasoning-Foundation-Models) — foundation-models-for-reasoning survey.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Bar to entry: every paper needs a primary-source URL (arXiv, OpenReview, ACL Anthology, official blog) and an annotation that adds value beyond the title. Out-of-scope PRs may be redirected to a related list — that's the boundary of *this* list, not a judgment of the work.

## Decisions log

Non-obvious scope and structural decisions are recorded in [DECISIONS.md](DECISIONS.md).

## Citation

If this list is useful to your research, please cite it via the [CITATION.cff](CITATION.cff) file.

## License

- List content (`README.md`, `chapters/`, `essays/`, `tracker/`, `GLOSSARY.md`, `DECISIONS.md`) — [CC0 1.0](LICENSE-content) (public domain).
- Source code under `scripts/`, `notebooks/` — [MIT](LICENSE-code).
