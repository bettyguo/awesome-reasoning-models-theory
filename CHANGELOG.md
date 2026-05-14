# Changelog

All notable changes to this list. Format inspired by [Keep a Changelog](https://keepachangelog.com/), but lighter — entries describe *content* changes, not just commits.

## [Unreleased]

### Added
- **GitHub Pages live site** at `docs/` with custom HTML pages (`index.html`, `timeline.html`, `explore.html`) and a shared dark-theme stylesheet. Markdown docs (FAQ, reading-paths, bibtex, model-families, cheatsheet) render via Jekyll.
- **Interactive timeline** at `docs/timeline.html` — filterable by paper / model / benchmark, click-for-detail.
- **Field map page** at `docs/explore.html` — embeds the eight-chapter dependency graph + reading-path index.
- **Pages deploy workflow** `.github/workflows/pages.yml` — builds and deploys on push to main.
- **Field map SVG** (`assets/field-map.svg`) — eight chapters with mechanism / debate arrows, embedded in README and the live site.
- **Scaling regimes SVG** (`assets/scaling-regimes.svg`) — embedded at the top of Chapter 2.
- **R1 recipe SVG** (`assets/r1-recipe.svg`) — embedded at the top of Chapter 5.
- **Rewritten hero banner** (`assets/banner.svg`) — stats, schematic, gradient design.
- **Three new essays**: `common-misconceptions.md` (twelve claims to dismantle), `closed-open-gap-tracked.md` (the four transitions), `how-to-read-a-reasoning-paper.md` (triage checklist).
- **Cheat sheet** at `docs/cheatsheet.md` — one-page reference.
- **More chapter papers**: Chapter 1 adds Wei et al. emergent abilities (arXiv:2206.07682) and Suzgun BBH (arXiv:2210.09261). Chapter 4 adds LATS (arXiv:2310.04406). Chapter 5 adds RLOO (arXiv:2402.14740) and KTO (arXiv:2402.01306). Chapter 7 adds Lyu et al. Faithful CoT (arXiv:2301.13379).
- `WANTED.md` — explicit gaps for community contribution.
- `docs/reading-paths.md` — 7 cross-chapter reading sequences.
- `docs/FAQ.md` — common questions about scope and curation.
- `docs/bibtex.md` — machine-readable citations for anchor papers.
- `docs/model-families.md` — catalog of the major reasoning model families.
- `scripts/validate_structure.py` — chapter schema validator.
- 2024-07 AlphaProof IMO silver and 2025-07 Gemini Deep Think IMO gold added to the timeline asset.

### Changed
- README now leads with a stat-row, badges (incl. live-site link), and explicit CTAs to the live site.
- `verify_citations.py` skip-pattern list: site self-references no longer break CI before Pages deploys.
- Updated AlphaProof reference in Chapter 4 to cite the Nov 2025 Nature paper and the silver-medal blog instead of the now-404 project page.
- Downgraded 🟡 status flags to 🟢 on several entries whose arXiv IDs were verified live (Hassid 2505.17813, Anthropic 2505.05410, Rohatgi 2509.21219, Venkatraman 2509.26626, ReFT 2401.08967).

## 2026-05-14 — initial publication

### Added
- README with one-page narrative and eight-chapter matrix.
- All eight chapters under `chapters/`:
  1. CoT and Scratchpads
  2. Test-Time Compute Scaling
  3. Sampling and Verification
  4. Search at Inference
  5. RL for Reasoning
  6. Overthinking and Optimal Length
  7. Faithfulness of Reasoning Traces
  8. Theoretical Frameworks
- Four synthesis essays.
- Five reproduction notebooks (small-GPU runnable demonstrations).
- Benchmarks tracker with launch digest.
- `GLOSSARY.md` (60+ terms), `DECISIONS.md` (8 scope decisions), `CONTRIBUTING.md`.
- Scripts: `verify_citations.py`, `update_benchmarks.py`, `ingest_arxiv.py`, `render_timeline.py`.
- CI: weekly link check + monthly tracker sweep.
- Internal: `_internal/competitor_audit.md`, `_internal/launch_playbook.md`.
- Dual license (CC0 for content, MIT for code).

---

*This file is appended to with substantive changes. Trivial typo / formatting commits don't get an entry.*
