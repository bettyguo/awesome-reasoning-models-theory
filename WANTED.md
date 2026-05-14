# Wanted

Gaps the curators know about, in the form of "if you have time and the relevant skills, here is where this list visibly lacks coverage and a contribution would be high-impact."

A *wanted* entry is one of:

- A paper or set of papers we know exists but haven't yet annotated to the standard of [CONTRIBUTING.md](CONTRIBUTING.md).
- A chapter section or essay that we know should exist but currently doesn't.
- A reproduction notebook gap.
- A tracker cell we haven't been able to verify against a primary source.

Pull requests against these items get priority review.

---

## Papers / paper clusters

### Mechanistic interpretability of reasoning circuits (chapter 7 + chapter 1)

We currently have only the *fact* that mech-interp on reasoning models is sparse (the [mech-interp essay](essays/reasoning-and-mechanistic-interpretability.md)). The 2026 wave of preprints starting to address this — sparse-autoencoder features for self-correction, circuit identification for backtracking tokens, activation-level differences between R1 and its base — should be tracked as it appears.

What we want: a 4–6 paper cluster annotated at chapter quality, added to Chapter 7 (faithfulness side) and Chapter 1 (compute-extension side).

### Faithfulness reproductions on RL-trained reasoners

Anthropic's *Reasoning Models Don't Always Say What They Think* (2025) is the anchor. We want independent reproductions on DeepSeek-R1, Qwen-QwQ, open Claude-distilled models — both for "does the finding generalize across organizations?" and "how does faithfulness vary with RL training compute?"

### Verifier scaling laws beyond Liu et al. (2025)

Liu et al. (arXiv:2504.02495) established that scaling verifier compute matters. Follow-ups quantifying the verifier/generator compute exchange rate are likely already in flight; we want them.

### Process reward models outside math

PRMs are heavily studied on math (where step-labeling is tractable). Code (where intermediate compilation gives free labels), formal theorem proving (Lean step-level labels are intrinsic), and multi-hop QA each need their own PRM literature surveyed.

### Test-time training as an alternative scaling axis

Akyurek et al. (arXiv:2411.07279) is in the chapter; follow-ups extending test-time training to other benchmarks (FrontierMath, HLE, SWE-bench) are not yet curated.

### "When more thinking hurts" cluster (2025–2026)

A line of papers documenting cases where chain extension hurts even on hard tasks. Currently in chapter 6 as a placeholder; we want the cluster pinned to specific arXiv IDs.

### Speculative reasoning / draft-and-verify at the step level

The draft-and-verify pattern (speculative decoding) has been adapted to *reasoning steps* in several 2025 papers. We want a 3–5 paper cluster pinned and added to Chapter 4.

### Sandbagging and capability elicitation literature

Currently chapter 7 cites Apollo Research and Greenblatt et al. (alignment faking); the broader 2024–2025 sandbagging/capability-elicitation literature is under-curated. Could be its own chapter section.

---

## Chapter / essay gaps

### A chapter on distillation of reasoning capability

Per [DECISIONS.md](DECISIONS.md) we decided *not* to spin this out as a chapter. But a chapter-section under Chapter 5 ("Distillation: R1 → small students") would be useful given the practical importance.

### An essay on closed-vs-open reasoner gap

The closed/open gap has been the field's most-discussed phenomenon (o1 in Sept 2024, R1 closing the gap in Jan 2025, the recurring cycle). A 1,500-word essay tracking that gap over 2024–2026 and arguing about what's permanent vs timing would be reader-pulling.

### An essay on benchmark contamination

Most reasoning benchmarks (AIME, MATH, Codeforces) appear in training data. The contamination-corrected story of "what reasoning models actually improve" deserves an essay.

### An essay on reasoning + tool use

Tool-augmented reasoning is intentionally out of scope (DECISIONS.md), but a *frame* essay explaining the boundary and pointing readers to the relevant lists would help.

---

## Reproduction notebook gaps

### Faithfulness test battery on small models

The Lanham et al. truncation / paraphrase / mistake-injection / filler-token battery, applied to a small open reasoning model (Qwen-R1-distill, etc.). Mentioned in Chapter 7 as not-in-V1.

### Tree-of-Thoughts demo on a small model

Chapter 4 currently has only the negative-result demo of self-refine inside notebook 02. An explicit ToT-style search demo on Game of 24 or similar tractable task would be valuable.

### Process-reward-model training on real math data

Notebook 05 uses a synthetic toy. A scaled-up version that trains a tiny PRM on Math-Shepherd-style automatic labels from a real GSM8K subset would bridge to deployment intuition.

### Test-time training reproduction

Akyurek et al.'s ARC-AGI test-time-training result on a small open model. Non-trivial but achievable.

---

## Tracker cells

The [benchmarks tracker](tracker/benchmarks.md) has several cells flagged ⏳ or marked "TBD verify" because we haven't found a primary source we trust. Specifically:

- AIME 2025 SOTA (pass@1, single-attempt): need a clean primary-source number, not vendor-marketing-blended.
- LiveCodeBench (pass@1, most recent slice): need the slice-date-aware number for the top open and top closed model.
- SWE-bench Verified: agent-mode vs no-tools disambiguation, with primary-source citations.
- Codeforces Elo: closed-model numbers are vendor-reported; we'd ideally have an independent-verification-or-public-account citation. (Unlikely to exist.)
- ARC-AGI-2 SOTA at end-of-2025: need verified primary source.
- ARC-AGI-3: track as the leaderboard matures.

---

## Infrastructure

### A chapter-schema validator

`scripts/validate_structure.py` should check each chapters/*.md file for: TL;DR present, mechanism section present, ≥ 8 key papers, debates section, reading paths section, open problems section, links resolvable internally.

### Pre-commit hooks

Markdown lint + the citation verifier + the structure validator on staged content files. Saves CI cycles.

### Citation export

A `docs/bibtex.md` of the 30 most-cited anchor papers, machine-readable. Useful for researchers who want to use this list as a literature pointer.

### A "How to find the right chapter" decision tree

The README has a chapter matrix; a short decision tree in the README ("Are you asking about expressivity? → sister list. Are you asking about why o1's scaling curve looks the way it does? → Chapter 2.") would help first-time visitors land correctly.

---

## How to claim

1. Open an issue with title `[wanted] <which-gap>` referencing this file.
2. Note your intended approach and timeline.
3. Submit a PR following [CONTRIBUTING.md](CONTRIBUTING.md).

A `wanted` label exists on GitHub Issues for tracking.
