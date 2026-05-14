# Reasoning Benchmarks Tracker

A living view of the benchmarks the reasoning-model field is currently chasing. Updated monthly.

## What this tracks

The benchmarks that *current* (2025–2026) reasoning models are evaluated on, with the **most recent verifiable score** from a public source. Sources of record, in order of preference:

1. The model's release paper / report (with section / table cited).
2. The model card on Hugging Face.
3. The official leaderboard for the benchmark.
4. A clearly-cited independent reproduction.

We do **not** record numbers from vendor marketing materials without a methods writeup. We do **not** record numbers from leaderboard submissions that lack a paper / model-card cross-reference.

Every cell carries a `last-verified` date. If a number's `last-verified` is more than 90 days old, it gets a 🕰️ flag on the table.

## Files

- [`benchmarks.md`](benchmarks.md) — the living table.
- [`digests/`](digests/) — monthly digest commits summarizing what moved.

## Update cadence

- **Monthly** (1st of each month, US-Eastern): run [`scripts/update_benchmarks.py`](../scripts/update_benchmarks.py), inspect candidate updates, manually verify each, commit with a digest summary.
- **Event-driven**: when a major model is released (any frontier-lab release, any open-source release crossing a SOTA mark), update within 1 week.

## How to contribute an update

See [CONTRIBUTING.md](../CONTRIBUTING.md). For tracker-specific updates: the PR description must include (a) the source URL, (b) the exact table / section cited, (c) the test conditions (pass@1 or pass@k, with-tools or without, single-attempt or majority-vote, dataset version), (d) the date the score was reported.

## What not to expect from this tracker

- A complete leaderboard. Several public leaderboards exist for each benchmark; we surface only the SOTA and one or two notable comparators.
- Live updates. We are explicitly *monthly+event-driven*; if you need real-time, use the benchmark's own leaderboard.
- Closed-model gold-standard numbers. We list them when officially reported, with the `(closed-model, vendor-reported)` flag. Treat with the appropriate skepticism.
