# Launch playbook

Internal — not part of the public list. Pre-launch checklist, launch-day procedure, and post-launch cadence.

## Pre-launch checklist

### Content readiness

- [ ] README narrative reads cleanly from top to bottom for a reader with no prior context. Test: hand to someone in adjacent field; can they explain back the one-page narrative?
- [ ] All eight chapters have a TL;DR, mechanism description, ≥ 8 annotated papers, and at least one open problem.
- [ ] Reproduction notebooks 01 and 04 have been actually run end-to-end on a small GPU and the cell outputs are committed.
- [ ] `tracker/benchmarks.md` has at least one column per benchmark with a *cited, verified* current SOTA and a `last-verified` date within 30 days.
- [ ] Glossary covers every acronym that appears in the README and any chapter TL;DR.
- [ ] `_internal/` directory is in `.gitignore` for the public branch, OR explicitly published as internal-but-public (decide per launch).
- [ ] Sister-list cross-link is bidirectional (both READMEs link the other).

### Citation discipline

- [ ] Every URL in `chapters/`, `essays/`, `tracker/`, `README.md` is verified by `scripts/verify_citations.py`.
- [ ] Every closed-model claim is annotated with `(closed-model, vendor-reported)`.
- [ ] No fabricated arXiv IDs. (Bot-generated content with hallucinated IDs is the single most common failure mode in this corner of the field.)

### Repo hygiene

- [ ] LICENSE files in place.
- [ ] `CITATION.cff` populated.
- [ ] Banner image (`assets/banner.svg`) exists and renders on GitHub mobile.
- [ ] Star history badge commented out until repo is public (private repos cause the badge to 404 and the README to look broken on the moment-of-publish).
- [ ] CI green: link-check workflow runs and passes.

### Launch timing

The reasoning-model news cycle is hot. Aim to publish within **one week of a major-model release or benchmark drop**, leveraging the attention:

- New OpenAI / Anthropic / DeepSeek / Google reasoning-model release.
- ARC-AGI-3 quarterly result reveal (the prize structure ensures recurring news).
- FrontierMath quarterly score update.
- A high-profile survey paper or position piece going viral.

Avoid launching during NeurIPS / ICML deadline weeks (researchers are heads-down; HN ML traffic is suppressed).

## Launch-day procedure

### Channels and timing (US-Eastern reference)

1. **Tuesday 09:00 EST** — push public commit and tag `v1.0.0`. Enable GitHub Pages if using.
2. **09:15** — uncomment star-history badge in README; bump CITATION date.
3. **09:30** — submit to **Hacker News** with title:
   > Show HN: A theoretical map of why reasoning models work (with reproductions)

   Comment immediately with the one-paragraph "why this is different from other awesome-lists" framing.
4. **10:00** — **Twitter/X thread**, ~ 12 tweets. Anchor: a single high-contrast slide (the timeline.svg as a PNG, or the eight-chapter matrix). Tag practitioners *only where their work is cited* (otherwise reads as spam).
5. **11:00** — **r/MachineLearning** post titled "I built a theory-first map of the reasoning-model literature; what's missing?". Frame as a request for community input, not a launch.
6. **12:00** — **LinkedIn** longer-form post for the practitioner audience.
7. **14:00** — pitch by email to **Nathan Lambert (Interconnects)**, **AlphaSignal**, **The Sequence**. Each pitch: one-sentence hook + the one-paragraph differentiation from existing lists + the chapter most relevant to their audience.

### Pitch template (newsletter)

> Subject: Theory-first reasoning-model literature map (for $NEWSLETTER readers)
>
> Hi $NAME,
>
> I've put together a theory-and-mechanism-first map of the reasoning-model literature — eight chapters, each stating a *mechanism* for what o1/R1/etc. are doing, with annotated papers, reproduction notebooks, and a benchmarks tracker. Live at $URL.
>
> Differentiator from existing awesome-lists: each chapter argues a position rather than aggregating titles, and we engage explicitly with the faithfulness / overthinking debates that most lists hedge.
>
> The chapter most relevant to $NEWSLETTER readers is $CHAPTER ($URL/chapter-link).
>
> Happy to write a short cross-post if useful. No reply needed if not a fit.
>
> — $NAME

## Post-launch cadence

### Week 1–2

- Monitor HN front page, X mentions, r/MachineLearning karma. Respond on-thread within 2 hours during US daytime.
- Triage PRs: aim for first response within 24h. Initial reviewer is the curator; we may invite co-maintainers after week 2 if PR volume warrants.

### Week 2–8 — re-trending eligibility

- Push a substantive update at least every 7 days. A "substantive update" is one of:
  - New chapter section (e.g. a new debate joins the field).
  - Monthly tracker digest with a new SOTA.
  - New essay.
  - Reproduction notebook with a new finding.

GitHub trending requires recent activity; bursty updates won't trend.

### Month 2–3 — content compounding

- Recruit chapter co-maintainers from active PR submitters.
- Pitch a panel / blog crossover with one of the cited authors (e.g. an interview essay).
- File issues labeled `wanted` for under-covered debates; promote on social.

### Failure modes during launch

- **HN flameout**: post lands at the bottom of /new, no traction. Mitigation: have a single high-quality first comment ready, do not re-post (HN penalizes), try again 6+ weeks later with a meaningful update.
- **Citation error caught in public**: respond, fix, thank the reporter, link the fix in a public comment. Do not delete or hide.
- **Scope-creep PR rush**: a viral moment brings off-scope PRs (prompt tricks, agent frameworks). Have CONTRIBUTING.md scope section ready to link.
- **Closed-model-marketing rebuttal**: someone claims we're being unfair to o1 / Claude. Hold the line — the open-vs-closed flag is a feature, not a bug.

### Metrics

- **Vanity metrics**: stars, forks, HN points.
- **Substantive metrics**: PRs that pass scope, issues with substantive discussion, citations of the repo in arXiv papers (search arXiv for the repo URL), invitations from newsletters / conferences.
- **Failure metric**: PRs that try to add prompt-engineering tricks (indicates the README scope statement isn't doing its job).
