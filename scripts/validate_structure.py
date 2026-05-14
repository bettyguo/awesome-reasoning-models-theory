#!/usr/bin/env python3
"""Validate that each chapter file follows the required structural schema.

Each chapters/0N-*.md must contain, in order:
  - A H1 heading
  - A TL;DR section (## TL;DR ...)
  - A mechanism section (## The mechanism)
  - A key papers section (## Key papers) with >= MIN_PAPERS entries
  - A debates section (## Debates)
  - A reading paths section (## Where to start)
  - A reproduction section (## Reproduction)
  - An open problems section (## Open problems)

Exit code 0 if all chapters pass, 1 otherwise.
"""
from __future__ import annotations

import argparse
import pathlib
import re
import sys

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
CHAPTERS_DIR = REPO_ROOT / "chapters"
MIN_PAPERS = 8

REQUIRED_SECTIONS = [
    ("TL;DR", re.compile(r"^##\s+TL;DR", re.MULTILINE)),
    ("Mechanism", re.compile(r"^##\s+The mechanism", re.MULTILINE)),
    ("Key papers", re.compile(r"^##\s+Key papers", re.MULTILINE)),
    ("Debates", re.compile(r"^##\s+Debates", re.MULTILINE)),
    ("Reading paths", re.compile(r"^##\s+Where to start", re.MULTILINE)),
    ("Reproduction", re.compile(r"^##\s+Reproduction", re.MULTILINE)),
    ("Open problems", re.compile(r"^##\s+Open problems", re.MULTILINE)),
]

# A "key paper" is a top-level bullet starting with "- **<Title>**".
PAPER_RE = re.compile(r"^- \*\*[^*]+\*\*", re.MULTILINE)


def count_papers_in_section(text: str) -> int:
    """Count top-level paper bullets in the 'Key papers' section."""
    start_m = REQUIRED_SECTIONS[2][1].search(text)
    if not start_m:
        return 0
    after = text[start_m.end():]
    end_m = re.search(r"^##\s+", after, re.MULTILINE)
    body = after[: end_m.start()] if end_m else after
    return len(PAPER_RE.findall(body))


def validate_chapter(path: pathlib.Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")

    if not text.startswith("# "):
        errors.append("missing H1 heading at top of file")

    for name, pat in REQUIRED_SECTIONS:
        if not pat.search(text):
            errors.append(f"missing required section: {name}")

    n_papers = count_papers_in_section(text)
    if n_papers < MIN_PAPERS:
        errors.append(f"only {n_papers} papers in Key papers section (need ≥ {MIN_PAPERS})")

    # Sanity: no "TODO" or "TBD" markers left in committed prose.
    todo_count = len(re.findall(r"\b(TODO|TBD|FIXME)\b", text))
    if todo_count > 0:
        errors.append(f"contains {todo_count} unresolved TODO/TBD/FIXME marker(s)")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-todo", action="store_true",
                        help="Fail on TODO/TBD/FIXME markers (default: warn only).")
    args = parser.parse_args()

    if not CHAPTERS_DIR.exists():
        print(f"missing {CHAPTERS_DIR}", file=sys.stderr)
        return 2

    files = sorted(CHAPTERS_DIR.glob("[0-9][0-9]-*.md"))
    if not files:
        print("no chapter files found", file=sys.stderr)
        return 2

    any_errors = False
    for f in files:
        errs = validate_chapter(f)
        if errs:
            # Filter TODO errors unless --strict-todo.
            if not args.strict_todo:
                errs = [e for e in errs if "TODO" not in e]
        rel = f.relative_to(REPO_ROOT)
        if errs:
            any_errors = True
            print(f"FAIL  {rel}")
            for e in errs:
                print(f"      - {e}")
        else:
            print(f"OK    {rel}")

    return 1 if any_errors else 0


if __name__ == "__main__":
    sys.exit(main())
