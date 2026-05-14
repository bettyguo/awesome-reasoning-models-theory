# Changelog

All notable changes to this list. Format inspired by [Keep a Changelog](https://keepachangelog.com/), but lighter — entries describe *content* changes, not just commits.

## [Unreleased]

### Added
- `WANTED.md` — explicit gaps for community contribution.
- `docs/reading-paths.md` — 7 cross-chapter reading sequences.
- `docs/FAQ.md` — common questions about scope and curation.
- `docs/bibtex.md` — machine-readable citations for anchor papers.
- `docs/model-families.md` — catalog of the major reasoning model families.
- `scripts/validate_structure.py` — chapter schema validator.
- 2024-07 AlphaProof IMO silver and 2025-07 Gemini Deep Think IMO gold added to the timeline asset.

### Changed
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
