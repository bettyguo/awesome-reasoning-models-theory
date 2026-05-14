#!/usr/bin/env python3
"""Render a simple SVG timeline of reasoning-model milestones.

Generates assets/timeline.svg and, optionally, assets/timeline.png. The
timeline is a hand-curated list of milestones — edit MILESTONES below.

Usage:
    python scripts/render_timeline.py
"""
from __future__ import annotations

import pathlib

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "assets"

# (date_label, short_label, kind)
# kind: "model" | "paper" | "benchmark"
MILESTONES: list[tuple[str, str, str]] = [
    ("2022-01", "CoT prompting (Wei et al.)",              "paper"),
    ("2022-03", "Self-consistency (Wang et al.)",          "paper"),
    ("2023-05", "PRMs / Let's Verify (Lightman et al.)",   "paper"),
    ("2023-05", "Tree of Thoughts (Yao et al.)",           "paper"),
    ("2024-07", "AlphaProof IMO silver",                   "model"),
    ("2024-08", "Test-time scaling (Snell et al.)",        "paper"),
    ("2024-09", "OpenAI o1 announcement",                  "model"),
    ("2024-11", "Tülu 3 (RLVR named)",                     "model"),
    ("2024-12", "'Don't think 2+3=' overthinking",         "paper"),
    ("2025-01", "DeepSeek-R1 / R1-Zero",                   "model"),
    ("2025-01", "s1: simple test-time scaling",            "paper"),
    ("2025-02", "Claude 3.7 with extended thinking",       "model"),
    ("2025-05", "Anthropic reasoning-faithfulness",        "paper"),
    ("2025-07", "Gemini Deep Think IMO gold",              "model"),
    ("2026-03", "ARC-AGI-3 launch",                        "benchmark"),
]

KIND_COLORS = {
    "model": "#3a7afe",
    "paper": "#16a34a",
    "benchmark": "#dc2626",
}


def render_svg() -> str:
    width = 1100
    height = 220
    margin_x = 40
    track_y = 110
    text_y_above = 70
    text_y_below = 170

    n = len(MILESTONES)
    span = width - 2 * margin_x
    step = span / max(1, n - 1)

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'  <rect width="100%" height="100%" fill="white"/>',
        f'  <line x1="{margin_x}" y1="{track_y}" x2="{width - margin_x}" y2="{track_y}" '
        f'stroke="#222" stroke-width="2"/>',
    ]

    for i, (date, label, kind) in enumerate(MILESTONES):
        x = margin_x + i * step
        color = KIND_COLORS.get(kind, "#666")
        parts.append(f'  <circle cx="{x:.1f}" cy="{track_y}" r="6" fill="{color}"/>')
        text_y = text_y_above if i % 2 == 0 else text_y_below
        anchor = "middle"
        parts.append(
            f'  <text x="{x:.1f}" y="{text_y}" font-family="Inter, sans-serif" font-size="11" '
            f'text-anchor="{anchor}" fill="#222">{label}</text>'
        )
        date_text_y = text_y_above - 16 if i % 2 == 0 else text_y_below + 16
        parts.append(
            f'  <text x="{x:.1f}" y="{date_text_y}" font-family="Inter, sans-serif" font-size="10" '
            f'text-anchor="{anchor}" fill="#555">{date}</text>'
        )

    parts.append(
        '  <text x="40" y="30" font-family="Inter, sans-serif" font-size="16" font-weight="bold" '
        'fill="#111">Reasoning models — a timeline</text>'
    )
    # Legend.
    lx = width - 280
    for i, (kind, color) in enumerate(KIND_COLORS.items()):
        cx = lx + i * 90
        parts.append(f'  <circle cx="{cx}" cy="30" r="5" fill="{color}"/>')
        parts.append(
            f'  <text x="{cx + 10}" y="34" font-family="Inter, sans-serif" font-size="11" '
            f'fill="#333">{kind}</text>'
        )
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> int:
    OUT_DIR.mkdir(exist_ok=True)
    svg = render_svg()
    out = OUT_DIR / "timeline.svg"
    out.write_text(svg, encoding="utf-8")
    print(f"Wrote {out}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
