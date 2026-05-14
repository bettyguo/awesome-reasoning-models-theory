# The closed–open gap, tracked

*Essay. Updated 2026-05-14.*

A persistent question in the reasoning-model era: how big is the gap between the closed-source frontier and the best open-weight model, and is it closing?

This essay tracks the empirical answer across the four major capability transitions of 2024–2026, then argues about what is timing and what is structural.

---

## The four transitions

### Transition 1 — pre-o1 (early 2024)

Open and closed models are roughly comparable on reasoning benchmarks. CoT prompting plus self-consistency is the standard recipe; PRMs (Lightman 2023) are known but not yet driving SOTA. GPT-4 and Claude-3-Opus lead on most leaderboards; open-weight Llama-3 and Qwen-2 lag by a few points but not catastrophically.

Gap: small, ~ 5-10 percentage points on hard benchmarks.

### Transition 2 — o1 (2024-09)

OpenAI releases o1. The headline scaling curve on AIME and Codeforces shows accuracy growing log-linearly with test-time compute. No public model approaches o1 on these tasks. The methodology is undisclosed; community speculation runs from "MCTS over CoT" to "process reward models in the loss" to "internalized search."

Gap: large, dramatic. AIME-24 jumps from ~ 10-20% (best open) to ~ 80%+ (o1). The community has nothing comparable.

Duration of the gap: about 4 months.

### Transition 3 — DeepSeek-R1 (2025-01)

DeepSeek releases R1, with the full pipeline documented. R1-Zero reaches AIME 79.8% pass@1, MATH-500 97.3%, GPQA Diamond 71.5% — within the o1-class envelope on multiple benchmarks. Most importantly: open weights and open methodology.

Gap: collapses on math/code. Where o1 led, R1 matches or comes within a few points. Where o3 leads (announced in late 2024, rolled out in 2025), R1 is behind but the absolute gap is in single-digit benchmark points on most tasks.

This is the field's epistemic shock. The recipe was not exotic. The hardware was not unique. The recipe involved a strong base, GRPO, and verifiable rewards — all reproducible.

### Transition 4 — the o3 + Claude-3.7 thinking + Gemini-Deep-Think era (2025-Q1 onward)

OpenAI's o3 family, Anthropic's Claude with extended thinking, and Google's Gemini Deep Think push the frontier on closed-source again. ARC-AGI-2 and ARC-AGI-3 become test cases where closed models lead. Gemini Deep Think reaches gold-medal IMO score (vendor-reported, summer 2025); AlphaProof reaches silver IMO in formal settings (Nature, 2025).

Gap: re-opens, narrower than transition 2 and shorter-lived. Open community is reproducing within 3-6 months on most public benchmarks; some closed-only capabilities (proprietary tool use, very long context handling, ARC-AGI-3-class) hold longer.

---

## Pattern across the four transitions

A *cycle* emerges:

1. Closed lab makes a methodology / scale / compute jump.
2. Headline numbers diverge dramatically from open SOTA.
3. Community speculates about what the closed lab is doing.
4. Within 3–6 months, an open recipe is published that closes most of the gap on public benchmarks.
5. Closed labs make another jump.

The cycle shortens slightly each iteration. From transition 1 → 2 → 3 → 4, the lag from closed-jump to open-catch-up went from "never closed" (transition 1: no jump) → "4 months" (o1 → R1) → "3–6 months" (o3 era).

---

## What is timing, what is structural

The clear timing argument: a sufficiently large closed lab can always make the next jump first. They have more compute, less external scrutiny, and dedicated proprietary infrastructure. As long as compute access is asymmetric, closed labs will lead the frontier *first*.

The structural argument cuts the other way: each jump has, in practice, been reproducible by the open community given a few months. The methodology gap is narrower than it appears in real time. Methods like RLVR are not proprietary moats — the moat is the base-model strength and the compute, both of which have public substitutes (DeepSeek-V3, Qwen3, Llama-4).

Where structural gap persists in 2026:

- **Proprietary data**. Frontier labs increasingly train on data not available to the open community. Quality of math / code / scientific reasoning data is the area where this matters most.
- **Inference infrastructure**. Closed labs serve frontier models at scale that is hard to match for open-weight reproductions. This matters for evaluation regimes that require many samples (best-of-N with very large N).
- **Tool integration**. Closed models with browser, code execution, and proprietary search integration outperform the same model used "naked." This is the area where most of the 2026 closed-open gap actually lives.

Where structural gap has *closed* by 2026:

- **Math benchmarks** (AIME, MATH-500): saturating for both closed and open at the top tier.
- **Code benchmarks** (HumanEval, LiveCodeBench): comparable.
- **The basic methodology of reasoning training**: R1's recipe is openly documented and reproduced.

---

## Why this matters

For practitioners: the open-weight ecosystem is, by 2026, sufficient for most reasoning use cases. The closed-source advantage now lives in tool use, very long context, and brand-new capabilities — not in the basic "produce a chain of thought, get a math answer" loop.

For researchers: the most interesting capability gaps are the *structural* ones, not the timing ones. Asking "why does Gemini Deep Think do better on FrontierMath than R1?" is more useful than "when will R1 catch up?" because the latter is largely a function of release schedules.

For the community: the closed-open gap is a *feature* of the current ecosystem, not a bug. The cyclical structure produces a sequence of empirical anchors (o1 → R1 → o3 → R1.5 → ...) that lets the field calibrate. Without the open releases, the closed numbers would be ungrounded.

---

## What likely happens 2026 → 2028

Forecasts I'd defend, with confidence calibration:

- **Closed labs will continue to lead the frontier first** (high confidence). Compute asymmetry is durable.
- **Open recipes will continue to follow within 6 months on public benchmarks** (high confidence on math/code, medium on ARC-AGI-3-class, low on agent / tool-use).
- **A structural gap in tool integration will widen, then narrow** (medium confidence). Open agent infrastructure is improving but lags.
- **At least one open recipe will *match* a closed model on a benchmark the closed model leads on, within a quarter of release** (high confidence). This is what R1 did to o1.
- **At least one closed-model claim will fail public reproduction when an open model approaches it** (high confidence). This will be embarrassing for that lab and useful for the community.

---

## How to read closed-source announcements

A checklist:

1. Is the methodology described, or only the result?
2. Is the evaluation infrastructure public, or vendor-only?
3. Are the test conditions specified (pass@1 vs cons@k, tool use, prompt format)?
4. Has any independent party run the same evaluation on the same model?
5. Has the same lab previously reported numbers that were later revised down?

Closed-model announcements that pass these checks are stronger evidence; ones that fail are weaker. The numbers in this list's [tracker](../tracker/benchmarks.md) reflect these criteria.

---

*Filed 2026-05-14. Will be updated at the next major closed-source release. The cycle described here is empirical observation, not principle — it could break either direction.*
