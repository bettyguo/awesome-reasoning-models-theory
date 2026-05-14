# Decisions

Non-obvious scope and structural decisions, with reasoning. Append-only.

## 2026-05-14 — Eight chapters, not nine or ten

**Decision.** Stay at the eight chapters from the master prompt; do not add separate chapters for *distillation of reasoning capability*, *tool-augmented reasoning*, or *reasoning-specific preference modeling*.

**Why.**
- Distillation of R1 → smaller students is methodologically interesting but is a special case of *training-time* application of a reasoning model and would skew the repo away from theory-of-mechanism.
- Tool-augmented reasoning bleeds into agent design, which is the scope of a different awesome-list category.
- Reasoning-specific RLHF / preference modeling overlaps with RL-for-reasoning (Ch 5) on one side and faithfulness (Ch 7) on the other; splitting it out fragments rather than illuminates.

Each of these gets a *cross-references* paragraph in the most-relevant chapter and a one-line entry in the *Related lists* of the README.

## 2026-05-14 — Scope split with the sister list

**Decision.** This list intentionally does **not** carry pure formal expressivity / circuit-complexity / logical-characterization papers. Those belong in [awesome-llm-reasoning-foundations](https://github.com/bettyguo/awesome-llm-reasoning-foundations).

**Why.** Two reasons.

1. Avoid duplication; readers should land on the right list the first time.
2. The "formal proofs about transformers" literature and the "what makes o1 work" literature have *different* methodologies, evidence standards, and reader expectations. Putting them in one list dilutes both.

**Boundary cases** — settled once, applied consistently:

- Merrill & Sabharwal (2024), "The Expressive Power of Transformers with Chain of Thought" → **foundations** (formal characterization theorem).
- Feng et al. (2024), "Towards Revealing the Mystery behind Chain of Thought" → **foundations** (constructive separation).
- Li et al. (2024), "CoT Empowers Transformers to Solve Inherently Serial Problems" → **foundations**.
- Snell et al. (2024), test-time compute scaling → **this list** (empirical scaling law).
- DeepSeek-R1 → **this list** (methodology, no theorem).
- Lightman et al. (2023), "Let's Verify Step by Step" → **this list** (PRM methodology).
- Lanham et al. (2023), CoT faithfulness → **this list** (empirical measurement).
- Prystawski et al. (2023), "Why think step by step?" → **this list** (the experiment-driven Bayesian-network result is closer to the empirical/explanatory frame here than the formal-theorem frame of the sister list).

In a few cases — notably the *theoretical frameworks* chapter (Ch 8) — we re-cite a foundations paper and explicitly note the cross-listing, because Ch 8's *purpose* is to bridge the two. That is the documented exception, not the rule.

## 2026-05-14 — Closed-model claims are flagged, not laundered

**Decision.** Any quoted result from a closed model (o1/o3/Claude/Gemini reasoning variants) is annotated with `(closed-model, vendor-reported)` next to the number, and a one-line note about what independent reproduction does or does not exist. We do not state these numbers as established empirical facts.

**Why.** The o1 scaling plot is the most-screenshotted figure in the reasoning-model era; it appears in slide decks as if it were a Snell-equivalent. It is not — it is vendor marketing with no public test infrastructure. Treating it as primary-source evidence (which it is) without flagging the verification gap (which exists) would be dishonest.

## 2026-05-14 — Reproduction notebooks demonstrate the *signal*, not benchmark

**Decision.** The five notebooks ([01–05](notebooks/)) are designed to fit on a single small GPU (or CPU for the inference-only ones) and to demonstrate the *qualitative claim* of each chapter. They are not attempts to reproduce SOTA benchmark numbers.

**Why.** Full reproduction of e.g. DeepSeek-R1 requires hundreds of GPU-hours and a specific cluster; pretending otherwise wastes the reader's time. The notebooks aim at: "after running this on a $0.50/hour GPU, you have hands-on intuition for the claim."

## 2026-05-14 — Faithfulness chapter (Ch 7) engages the debate; no hedging

**Decision.** Chapter 7 will state, in its TL;DR, that CoTs are often post-hoc rationalizations, and will not soften this finding to preserve interpretive plausibility of CoT-as-thought.

**Why.** This is the chapter most commonly hedged in survey papers, and the hedging is itself part of why the field has not converged on a position. The repo's value-add is precisely *not* doing that.

## 2026-05-14 — Pure-markdown V1; YAML entries deferred

**Decision.** Chapter content is hand-authored Markdown for V1. We do **not** start with the YAML-per-paper + build-script pattern used in [awesome-llm-reasoning-foundations](https://github.com/bettyguo/awesome-llm-reasoning-foundations) — chapters here are essayistic, not flat lists, and the YAML pattern fights against that.

**Why.** This list's primary structure is the chapter-as-mechanism, with the paper list as supporting material. A YAML-driven build would either (a) flatten the chapter into a list, undoing the point, or (b) duplicate the annotation into both the chapter and the YAML, doubling the maintenance surface for no gain.

If link rot becomes a real problem we can add a `scripts/verify_citations.py` that scrapes URLs out of the Markdown — same outcome without the architectural cost.

## 2026-05-14 — No reasoning-model jailbreaks, no sandbagging examples that work

**Decision.** Discussion of reasoning-model safety (sandbagging, deceptive CoT, alignment-faking) refers to *published* findings without reproducing exploits. We cite Anthropic / OpenAI / Apollo Research papers but do not include playable jailbreak prompts.

**Why.** This is a theory map, not a red-team toolkit. The audience is researchers and serious practitioners; including working exploits creates dual-use risk without serving the educational goal.
