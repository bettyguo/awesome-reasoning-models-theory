#!/usr/bin/env python3
"""Suggest candidate new papers from arXiv for review.

Queries the arXiv API for papers matching reasoning-model keywords and recent
date windows. Outputs a candidate list to stdout (JSON) for human review.

NOTHING in this script touches the repository content. Every paper a human
adds to a chapter must pass the CONTRIBUTING.md bar by hand.

Usage:
    python scripts/ingest_arxiv.py [--days 30] [--max 50]
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import sys
import urllib.parse
from urllib import request

ARXIV_API = "http://export.arxiv.org/api/query"

# Conservative; expand as the field shifts.
QUERIES = [
    # CoT / chain of thought
    'abs:"chain of thought" AND abs:"reasoning"',
    # Test-time compute scaling
    'abs:"test-time compute" OR abs:"test time scaling"',
    # RL for reasoning
    'abs:"reinforcement learning" AND abs:"reasoning"',
    'abs:"GRPO" OR abs:"RLVR"',
    'abs:"verifiable reward"',
    # Process reward models
    'abs:"process reward model" OR abs:"PRM" AND abs:"reasoning"',
    # Overthinking
    'abs:"overthinking" AND abs:"reasoning"',
    # Faithfulness
    'abs:"faithfulness" AND abs:"chain of thought"',
    # Reasoning model releases
    'abs:"DeepSeek-R1" OR abs:"o1" AND abs:"reasoning"',
]

NS = "{http://www.w3.org/2005/Atom}"


def parse_atom(xml_bytes: bytes) -> list[dict]:
    import xml.etree.ElementTree as ET
    root = ET.fromstring(xml_bytes)
    out: list[dict] = []
    for entry in root.findall(f"{NS}entry"):
        title = (entry.findtext(f"{NS}title") or "").strip().replace("\n", " ")
        summary = (entry.findtext(f"{NS}summary") or "").strip().replace("\n", " ")
        published = entry.findtext(f"{NS}published") or ""
        link = ""
        for l in entry.findall(f"{NS}link"):
            if l.attrib.get("type") == "text/html":
                link = l.attrib.get("href", "")
                break
        authors = []
        for a in entry.findall(f"{NS}author"):
            name = a.findtext(f"{NS}name")
            if name:
                authors.append(name.strip())
        out.append({
            "title": title,
            "authors": authors,
            "summary": summary[:400] + ("..." if len(summary) > 400 else ""),
            "published": published,
            "url": link,
        })
    return out


def query_arxiv(q: str, days: int, max_results: int) -> list[dict]:
    cutoff = (dt.datetime.now(dt.timezone.utc) - dt.timedelta(days=days)).strftime("%Y%m%d%H%M%S")
    full = f"({q}) AND submittedDate:[{cutoff} TO 999912312359]"
    params = {
        "search_query": full,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(max_results),
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = request.Request(url, headers={"User-Agent": "awesome-reasoning-models-theory/1.0"})
    with request.urlopen(req, timeout=30) as r:
        data = r.read()
    return parse_atom(data)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--days", type=int, default=30)
    parser.add_argument("--max", type=int, default=50)
    args = parser.parse_args()

    seen: set[str] = set()
    aggregated: list[dict] = []
    for q in QUERIES:
        try:
            results = query_arxiv(q, args.days, args.max)
        except Exception as e:
            print(f"# arxiv query failed: {q}: {e}", file=sys.stderr)
            continue
        for r in results:
            if r["url"] in seen:
                continue
            seen.add(r["url"])
            aggregated.append({"query": q, **r})

    aggregated.sort(key=lambda r: r["published"], reverse=True)
    print(json.dumps(aggregated, indent=2, ensure_ascii=False))
    print(f"# {len(aggregated)} candidate papers from last {args.days} days.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
