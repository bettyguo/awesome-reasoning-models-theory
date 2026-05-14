#!/usr/bin/env python3
"""Help the monthly benchmark-tracker sweep.

This script does NOT automatically update benchmark numbers — every cell must be
human-verified against a primary source per CONTRIBUTING.md. What it does:

  1. Reports the age of each `Last verified` date in tracker/benchmarks.md.
  2. Flags cells older than 90 days.
  3. Prints a candidate digest skeleton for the current month so you can fill
     it in by hand.

Run:
    python scripts/update_benchmarks.py [--max-age-days 90]
"""
from __future__ import annotations

import argparse
import datetime as dt
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
TRACKER = REPO_ROOT / "tracker" / "benchmarks.md"
DIGESTS_DIR = REPO_ROOT / "tracker" / "digests"

DATE_RE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def parse_table_dates(text: str) -> list[tuple[int, dt.date]]:
    out: list[tuple[int, dt.date]] = []
    for i, line in enumerate(text.splitlines()):
        if not line.startswith("|"):
            continue
        matches = DATE_RE.findall(line)
        if not matches:
            continue
        # Take the last YYYY-MM-DD on the line as the "last verified".
        try:
            out.append((i, dt.date.fromisoformat(matches[-1])))
        except ValueError:
            continue
    return out


def write_digest_skeleton(today: dt.date) -> pathlib.Path:
    fname = DIGESTS_DIR / f"{today.strftime('%Y-%m')}-digest.md"
    if fname.exists():
        print(f"Digest for {today.strftime('%Y-%m')} already exists at {fname}.")
        return fname
    fname.parent.mkdir(parents=True, exist_ok=True)
    skel = f"""# Tracker digest — {today.strftime('%Y-%m')}

*Compiled {today.isoformat()}.*

## What moved this month

- (fill in: which cells changed, what direction, brief context)

## Methodological notes

- (fill in: any new conventions, contamination discoveries, evaluation drift)

## What to watch over the next 90 days

- (fill in: model release expectations, leaderboard maturity, benchmark refresh dates)

## Verification log

- (fill in per-cell with source URL + section reference)
"""
    fname.write_text(skel, encoding="utf-8")
    print(f"Wrote digest skeleton at {fname}.")
    return fname


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-age-days", type=int, default=90)
    parser.add_argument("--no-write-digest", action="store_true")
    args = parser.parse_args()

    if not TRACKER.exists():
        print(f"Missing {TRACKER}.", file=sys.stderr)
        return 2

    today = dt.date.today()
    text = TRACKER.read_text(encoding="utf-8")
    rows = parse_table_dates(text)

    stale = []
    for line_idx, d in rows:
        age = (today - d).days
        if age > args.max_age_days:
            stale.append((line_idx, d, age))

    if not rows:
        print("No verified dates found in tracker. Have you populated benchmarks.md?")
        return 1

    print(f"Tracker has {len(rows)} dated cells.")
    if stale:
        print(f"\n{len(stale)} cell(s) stale (> {args.max_age_days} days):")
        for line_idx, d, age in stale:
            print(f"  line {line_idx + 1}: last verified {d.isoformat()} ({age} days ago)")
    else:
        print("All cells within the freshness window.")

    if not args.no_write_digest:
        write_digest_skeleton(today)

    # Exit non-zero if any cell is stale; lets CI flag drift.
    return 0 if not stale else 3


if __name__ == "__main__":
    sys.exit(main())
