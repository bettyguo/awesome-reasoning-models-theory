# Competitor audit

A field map of adjacent awesome-lists, paper trackers, and survey-style resources, with a candid assessment of what each does well and where this list adds value. Internal document — informs README *Related lists* selection and PR redirects.

*Audit date: 2026-05-14. Update at major release windows (e.g., new survey paper, new tracker repo crossing 1k stars).*

## Methodology

Searched GitHub for: `awesome reasoning`, `awesome cot`, `awesome chain of thought`, `awesome o1`, `awesome r1`, `awesome llm reasoning`, `awesome test time compute`. Also: Google Scholar for surveys with "long chain-of-thought" or "reasoning models" in 2024–2026. For each entry: read the README, scanned the curation structure, checked freshness (last-commit date).

## Direct competitors

### `hijkzzz/Awesome-LLM-Strawberry`

- **Scope**: o1-centric paper list, started Sept 2024 right after the o1 announcement.
- **Strengths**: rapid early aggregation; was the de-facto landing page for "o1 papers" in late 2024.
- **Weaknesses**:
  - Flat list, no chapter structure or mechanism framing.
  - Heavy on conjectural reverse-engineering of o1 with little marker for what's verified vs speculation.
  - Has been less actively maintained as R1 / Claude-thinking / Gemini-reasoning shifted the center of gravity.
- **What we do that they don't**: theory-first chapters; explicit open-vs-closed flagging; reproduction notebooks; benchmarks tracker.

### `atfortes/Awesome-LLM-Reasoning`

- **Scope**: Broad reasoning paper list, CoT → o1 → DeepSeek-R1 era. One of the most-starred reasoning awesome-lists.
- **Strengths**: comprehensive coverage; well-organized into sub-topics; updated.
- **Weaknesses**:
  - Aggregator pattern (title + URL + one-line description per paper).
  - No engagement with debates or open problems.
  - Mixes prompt-engineering tricks with theoretical results without distinguishing them.
- **What we do that they don't**: the chapters argue *positions*, not just list papers; we explicitly engage with the faithfulness, overthinking, and search-vs-RL debates. We also exclude prompt-engineering recipes by policy.
- **Cross-link strategy**: list them in README *Related lists* as the place to go for *methods coverage*.

### `EvolvingLMMs-Lab/AwesomeReasoning`

- **Scope**: Reasoning across modalities (text + multimodal).
- **Strengths**: useful for multimodal reasoning practitioners.
- **Weaknesses**: scope mismatch with this list; we deliberately exclude multimodal CoT.
- **Cross-link strategy**: do not list — too off-axis.

### `srush/awesome-o1`

- **Scope**: o1-focused bibliography by Sasha Rush (well-known academic).
- **Strengths**: high-quality curation; influential author.
- **Weaknesses**: o1-centric framing has become dated post-R1; not regularly updated.
- **Cross-link strategy**: list as "o1-centric bibliography (largely stale post-R1)".

### `hemingkx/Awesome-Efficient-Reasoning`

- **Scope**: efficient reasoning (inference compute, KV cache, speculative decoding).
- **Strengths**: dense coverage of the efficiency angle.
- **Weaknesses**: orthogonal to mechanism — fine.
- **Cross-link strategy**: list in *Related lists*.

### `luban-agi/Awesome-LLM-reasoning`

- **Scope**: broad reasoning paper list.
- **Strengths**: coverage.
- **Weaknesses**: very flat; no organizing argument.
- **Cross-link strategy**: list briefly.

### `reasoning-survey/Awesome-Reasoning-Foundation-Models`

- **Scope**: companion to a survey paper on foundation models for reasoning.
- **Strengths**: backed by a published survey, so curation is calibrated.
- **Weaknesses**: scope is broader (foundation models generally); less depth on o-series / R1 specifics.
- **Cross-link strategy**: list as survey companion.

## Sister list (not competitor)

### `bettyguo/awesome-llm-reasoning-foundations`

- **Scope**: formal expressivity / circuit complexity / CoT error bounds / learnability of ICL / knowledge editing impossibility.
- **Relationship**: deliberately disjoint scope; see [DECISIONS.md](../DECISIONS.md) for the boundary cases.
- **Cross-link strategy**: prominent feature, "sister list", in *Related lists*. Bidirectional link.

## Survey papers (not lists, but functional substitutes)

- **Chen et al. (2025), "Towards reasoning era: a survey of long chain-of-thought for reasoning large language models"** ([arXiv:2503.09567](https://arxiv.org/abs/2503.09567)). Comprehensive, well-cited survey of the long-CoT literature. *Implication*: cite as the canonical recent survey; our list adds value by being a *living* resource with reproductions and a benchmark tracker.

- **Sui et al. (2025), "Stop overthinking: a survey on efficient reasoning for large language models"** ([arXiv:2503.16419](https://arxiv.org/abs/2503.16419)). Efficiency-axis survey overlapping with our Chapter 6.

- **The "When more thinking hurts" line** (a cluster of 2025–2026 papers): functions as a position rather than a survey; treated as primary literature in Chapter 6.

## Influencer / pre-seed map

Public figures who shape this discourse — informs Twitter/X tagging at launch and newsletter pitches (handles to be verified at launch time, not hard-coded here):

- **Noam Brown** — OpenAI; reasoning lead; pre-LLM was the AlphaZero-poker pipeline. His tweets define the scaling-law-of-test-time framing.
- **Jason Wei** — OpenAI; CoT paper first author; long-form posts on the trajectory from CoT prompting to o1.
- **Nathan Lambert (Interconnects)** — runs the most-read RL-for-LLMs newsletter; deep on RLVR / R1.
- **Sasha Rush** — Cornell; bridges academic theory and o1 reverse-engineering.
- **Andrej Karpathy** — independent; high-distribution explainers, often the entry point for the broader audience.
- **DeepSeek-AI** — the org account; R1 release shifted the field.
- **Costa Huang / Lewis Tunstall** — TRL maintainers; closest thing to a canonical OSS RL-for-LLMs stack.
- **Tri Dao** — compute-efficiency authority; occasional reasoning-model commentary.

These names go into the launch playbook ([_internal/launch_playbook.md](launch_playbook.md)), not the README.

## Gap analysis

Things *no* existing list does well, which our list is positioned to do:

1. **Theory-first chapter structure** with a stated mechanism per chapter.
2. **Open-vs-closed flag** on every closed-model claim.
3. **Engagement with the faithfulness debate** — most lists tiptoe around Turpin / Lanham / Chen 2025.
4. **Reproduction notebooks** at single-GPU scale.
5. **Benchmarks tracker** with a monthly digest cadence — gives re-trending eligibility.
6. **Glossary** at the depth needed by someone new to the GRPO / RLVR / PRM / ORM vocabulary.

Things existing lists do well that we should *not* try to compete on:

- Sheer breadth of method coverage (atfortes).
- Multimodal reasoning (EvolvingLMMs).
- Efficiency-specific depth (hemingkx).

We send readers to those lists explicitly.

## Action items extracted from this audit

- README *Related lists* section names: atfortes, srush, luban-agi, reasoning-survey, hemingkx, plus the sister list.
- *Decision*: do not absorb prompt-engineering tricks. Redirects to atfortes.
- *Decision*: do not absorb multimodal-CoT papers. Redirects to EvolvingLMMs.
- Track: any new reasoning awesome-list crossing 500 stars during launch window — may warrant re-audit.
