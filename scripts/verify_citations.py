#!/usr/bin/env python3
"""Extract and verify URLs in repo markdown files.

Scans chapters/, essays/, tracker/, README.md, and GLOSSARY.md for URLs.
Issues a HEAD request to each (with a small concurrency limit) and reports
non-2xx responses.

Usage:
    python scripts/verify_citations.py [--report PATH]

Exit code 0 if all URLs are healthy, 1 if any are broken.
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import json
import pathlib
import re
import sys
from dataclasses import dataclass
from urllib import error, request

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
SCAN_DIRS = ["chapters", "essays", "tracker"]
SCAN_FILES = ["README.md", "GLOSSARY.md", "DECISIONS.md", "CONTRIBUTING.md"]
URL_RE = re.compile(r"\((https?://[^)\s]+)\)")
TIMEOUT_S = 15
WORKERS = 8

# URLs the checker should skip without failing.
# Use for self-references that resolve only after deployment (live site, CI badges).
SKIP_PATTERNS = [
    "bettyguo.github.io/awesome-reasoning-models-theory",
    "actions/workflows/linkcheck.yml/badge.svg",
]


def _skip(url: str) -> bool:
    return any(pat in url for pat in SKIP_PATTERNS)


@dataclass
class CheckResult:
    url: str
    status: int | None
    error: str | None
    source: str


def collect_urls() -> dict[str, list[str]]:
    """Map source-file-path -> list of urls."""
    out: dict[str, list[str]] = {}
    paths: list[pathlib.Path] = []
    for d in SCAN_DIRS:
        paths.extend((REPO_ROOT / d).rglob("*.md"))
    for f in SCAN_FILES:
        p = REPO_ROOT / f
        if p.exists():
            paths.append(p)
    for p in sorted(paths):
        text = p.read_text(encoding="utf-8")
        urls = sorted(set(URL_RE.findall(text)))
        if urls:
            out[str(p.relative_to(REPO_ROOT))] = urls
    return out


def check_url(url: str, source: str) -> CheckResult:
    headers = {"User-Agent": "awesome-reasoning-models-theory linkcheck/1.0"}
    try:
        req = request.Request(url, method="HEAD", headers=headers)
        with request.urlopen(req, timeout=TIMEOUT_S) as resp:
            return CheckResult(url=url, status=resp.status, error=None, source=source)
    except error.HTTPError as e:
        if e.code in (405, 403):
            # some servers don't allow HEAD; retry GET (no body read)
            try:
                req = request.Request(url, method="GET", headers=headers)
                with request.urlopen(req, timeout=TIMEOUT_S) as resp:
                    return CheckResult(url=url, status=resp.status, error=None, source=source)
            except Exception as e2:
                return CheckResult(url=url, status=None, error=str(e2), source=source)
        return CheckResult(url=url, status=e.code, error=str(e), source=source)
    except Exception as e:
        return CheckResult(url=url, status=None, error=str(e), source=source)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--report", type=pathlib.Path, default=None)
    args = parser.parse_args()

    url_map = collect_urls()
    flat: list[tuple[str, str]] = []
    skipped = 0
    for src, us in url_map.items():
        for u in us:
            if _skip(u):
                skipped += 1
                continue
            flat.append((src, u))
    print(f"Checking {len(flat)} unique URLs across {len(url_map)} files (skipped {skipped} self-references).")

    results: list[CheckResult] = []
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futures = {ex.submit(check_url, u, src): (src, u) for src, u in flat}
        for fut in cf.as_completed(futures):
            r = fut.result()
            results.append(r)
            mark = "OK " if r.status and 200 <= r.status < 400 else "BAD"
            print(f"  {mark} {r.status or '---'} {r.url}")

    broken = [r for r in results if not (r.status and 200 <= r.status < 400)]

    if args.report:
        args.report.write_text(
            json.dumps(
                {"total": len(results), "broken": len(broken), "results": [r.__dict__ for r in results]},
                indent=2,
            ),
            encoding="utf-8",
        )

    if broken:
        print(f"\n{len(broken)} broken URL(s):", file=sys.stderr)
        for r in broken:
            print(f"  {r.source}: {r.url}  -> {r.status or 'error'} {r.error or ''}", file=sys.stderr)
        return 1
    print(f"\nAll {len(results)} URLs healthy.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
