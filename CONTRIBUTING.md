# Contributing

Thanks for considering a contribution. The goal of this list is *theoretical and empirical understanding* of why reasoning models work — not breadth of coverage. A small list of carefully annotated papers is more useful than a long list of titles.

## The bar for a new entry

Every new paper, blog post, or talk added to this list must satisfy **all five**:

1. **Primary-source URL** — arXiv abstract page, OpenReview forum, ACL Anthology, official lab blog, or PDF on the authors' page. Not a Notion, Medium, or aggregator link.
2. **In scope** — see the scope section of the [README](README.md) and the boundary cases in [DECISIONS.md](DECISIONS.md). If unsure, file an issue first.
3. **Annotation that adds value** — not a paraphrase of the abstract. ≤ 40 words, says *why this paper matters for the chapter it sits in*. Use the format used by existing entries.
4. **Mechanism, not phenomenon** — the paper should make a claim about *how* reasoning models do what they do (or about the limits of such claims). "X benchmark scores Y" without a mechanistic claim is out of scope.
5. **Open-vs-closed flag** — if the paper's main result is on a closed model, the annotation must say so. We do not launder vendor claims into the canon.

## Workflow

1. Open an issue describing the addition (paper, chapter, debate) before opening a PR — this catches scope and de-dup issues early.
2. For an entry: add it to the relevant `chapters/0N-*.md` file under the **Key papers** list, alphabetically by first author within the chapter.
3. For a chapter-level change (new debate, updated TL;DR, new open problem): edit the chapter file; explain the rationale in the PR description.
4. For a tracker update: edit `tracker/benchmarks.md` and add a one-line entry to the relevant monthly digest in `tracker/digests/`.
5. Run `python scripts/verify_citations.py` (when implemented) to confirm no broken links.

## What we will *not* accept

- CoT prompt-engineering recipes without a mechanism claim. (Try [atfortes/Awesome-LLM-Reasoning](https://github.com/atfortes/Awesome-LLM-Reasoning).)
- Pure formal expressivity / circuit-complexity papers. (Try [awesome-llm-reasoning-foundations](https://github.com/bettyguo/awesome-llm-reasoning-foundations).)
- Jailbreaks, prompt-injection techniques, or working sandbagging exploits — even when illustrative.
- Leaderboard-only papers (new SOTA on benchmark X with no methodological insight).
- Multi-modal reasoning unless the paper is essentially text-CoT mechanism with images as data.
- Marketing posts from labs that are not accompanied by a methods writeup or reproducible measurement.

## Annotation style

Examples of *good* annotations (mechanism, not summary):

> Proves a constant-size CoT transformer solves arithmetic and dynamic-programming tasks unreachable by any fixed-depth no-CoT transformer — an unconditional separation between with-CoT and without-CoT expressivity.

> Shows that letting a reasoning model sample multiple chains and rerank them with a verifier matches the accuracy of a 10× larger model at fixed compute, *only* for tasks where verification is cheaper than generation.

Examples of *bad* annotations (paraphrase):

> The paper proposes a new method for chain-of-thought reasoning and evaluates it on MATH and GSM8K.

> The authors introduce a process reward model and show improvements on math benchmarks.

## Reviewing pull requests

When reviewing, check:

- Does the annotation pass the "mechanism, not phenomenon" test?
- Is the open-vs-closed flag honest?
- Does the entry duplicate a related-list entry, or is it genuinely in scope for this list?
- Is the URL the primary source, not a re-host?

## Code style for `scripts/` and `notebooks/`

- Python 3.10+, type hints encouraged, no required ones.
- `notebooks/` are designed to run on a single small GPU (e.g. A10G / RTX 3090) or CPU. Document the assumed hardware at the top.
- No telemetry, no auto-downloads of large datasets without prompting.

## Code of conduct

Be substantive, be specific, be kind. Disagreement on the science is the *point* of this list — the field has not converged, and our job here is to make the disagreement legible.
