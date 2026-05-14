# Reasoning model families (catalog)

A short reference catalog of the major reasoning-model families circa 2025–2026. Not exhaustive — the goal is to disambiguate names that appear across chapters and essays.

For each family: release date(s), open-vs-closed status, key public claims, and where in this list it's discussed.

---

## Closed-weights families

### OpenAI o-series

- **o1** (2024-09): the announcement that triggered the field's pivot. RL-trained reasoning over long internal CoTs.
- **o1-mini** (2024-09): smaller, faster, math-focused.
- **o1-pro** (2024-Q4): inference-time-scaled o1.
- **o3** family (2024-12 announcement, 2025 rollout): successor with reportedly stronger Codeforces/Frontier benchmarks. Vendor-reported gold-class numbers; no public weights or test infrastructure.
- **o4** family (2025-Q3+): the rolling successor line.

Status: 🔴 closed weights, vendor-reported numbers. Cited carefully throughout the list; never as "the canonical scaling curve."

### Anthropic Claude with extended thinking

- **Claude 3.5 Sonnet** introduced visible thinking traces in select interfaces.
- **Claude 3.7 Sonnet** (2025-02) — first Anthropic model with a publicly-documented "extended thinking" mode and explicit reasoning-budget control.
- **Claude Opus 4.x** with thinking — the line discussed throughout this list when "Claude with thinking" appears.

Status: 🟡 partial — methods writeups are substantive, weights closed. Faithfulness work (Anthropic 2025) gives some research-grade access.

### Google Gemini reasoning variants

- **Gemini 2.5 Flash / Pro** with thinking (2025-Q1+).
- **Gemini Deep Think** (2025-Q2-Q3) — reportedly achieved a gold-medal-equivalent score at IMO 2025 (vendor-reported).

Status: 🔴 closed. Connected to the DeepMind AlphaProof/AlphaGeometry line (Chapter 4) on the formal-proof side.

---

## Open-weights families

### DeepSeek

- **DeepSeek-R1 / R1-Zero** (2025-01): the open-recipe paradigm shift. R1-Zero is the no-SFT pure-RL variant; R1 is R1-Zero plus cold-start SFT.
- **R1-Distill-** *N* — distilled variants on Qwen2.5 (1.5B, 7B, 14B, 32B) and Llama-3 (8B, 70B) bases.
- **DeepSeekMath** (2024) — predecessor; introduces GRPO.
- **DeepSeek-V3** (2024-12) — the base that R1 builds on.

Status: 🟢 open weights, open recipe. The empirical anchor for most of this list.

### Qwen reasoning variants

- **Qwen2.5-Math** family — math-tuned base for many open reproductions; not itself a reasoning model.
- **QwQ-32B-Preview** (2024-11): early open reasoner predating R1.
- **Qwen3** (2025+) reasoning variants.

Status: 🟢 open. Frequently used as a base in open RLVR work; appears in notebooks 01–04.

### Alibaba / Tongyi reasoning models

Several reasoning-mode variants of the Tongyi family in 2025–2026; treated as the Qwen sibling here.

### Open R1 reproductions

- **HuggingFace Open-R1** project (2025): open-source R1 recipe reproduction.
- **SimpleRL** (2025): minimal open RLVR.
- **Open-Reasoner-Zero** (2025): another open R1-Zero-style reproduction.
- **verl** (Volcano Engine RL library, 2024–2025): RL framework heavily used for R1 reproductions.

Status: 🟢 open. Listed in [Chapter 5](../chapters/05-rl-for-reasoning.md).

### Tülu / AI2

- **Tülu 3** (2024-11): open post-training including RLVR. The earliest *named* RLVR recipe.
- **Tülu 3.5** and successors.

Status: 🟢 open.

### Mistral reasoning variants

Mistral has released several reasoning-tuned models in 2025; the lineage is less consolidated than DeepSeek/Qwen and is treated paper-by-paper.

---

## Formal-proof systems (a separate clade)

### DeepMind AlphaProof + AlphaGeometry 2

- AlphaProof: pretrained LM + AlphaZero-style RL over Lean 4 proofs.
- AlphaGeometry 2: geometry-specialized formal prover.
- IMO 2024: 4/6 problems, silver-medal threshold.
- Nature methodology paper, Nov 2025.

Cited in [Chapter 4](../chapters/04-search-at-inference.md) as the regime where explicit search and RL are *complementary*, not competing.

### Other formal-proof RL systems

Several 2025 follow-ups on Lean / Coq with RL and tree search; tracked under [WANTED.md](../WANTED.md).

---

## How to use this catalog

- A paper citing "R1" without further qualification usually means the full SFT+RL pipeline R1, not R1-Zero. When R1-Zero is meant, the paper says so.
- "o1" without a year typically refers to the initial 2024-09 model; "o3" to the 2024-12-announcement / 2025-rollout successor.
- "Claude with thinking" is post-3.5; before that, Claude's CoT was implicit / chat-only.
- "Reasoning model" in this list's prose means an RL-trained, long-CoT-emitting model in the family above. We do not call a base instruct model a "reasoning model" even if it does CoT prompting.

---

## What this catalog deliberately omits

- Performance numbers (those live in [`tracker/benchmarks.md`](../tracker/benchmarks.md)).
- Architectural details when not load-bearing for the methodology story.
- Pre-2024 chain-of-thought-prompted models (those are *not* reasoning models in the post-o1 sense).
- Models without published methodology *and* without a public release (we have nothing to say about them).

*Filed 2026-05-14. Update as the field's families consolidate or split. PR-friendly.*
