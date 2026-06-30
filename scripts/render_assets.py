#!/usr/bin/env python3
"""Regenerate SVG and PNG README assets.

The assets are intentionally dependency-light. SVGs are always generated. PNGs
are generated with Pillow when it is available.
"""
from __future__ import annotations

import math
import sys
from html import escape
from pathlib import Path
from textwrap import wrap

BG_TOP = (8, 17, 31)
BG_BOTTOM = (17, 39, 58)
CARD = (18, 48, 72)
CARD_ALT = (26, 72, 92)
CYAN = (111, 218, 238)
LIME = (186, 238, 111)
AMBER = (246, 189, 96)
ROSE = (238, 111, 164)
INK = (245, 250, 255)
MUTED = (184, 211, 225)
GRID = (42, 76, 102)

FONT_CANDIDATES = {
    "regular": [
        "/System/Library/Fonts/Supplemental/Arial.ttf",
        "/Library/Fonts/Arial.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "DejaVuSans.ttf",
    ],
    "bold": [
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
        "/Library/Fonts/Arial Bold.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
        "DejaVuSans-Bold.ttf",
    ],
}


def rgb(color: tuple[int, int, int]) -> str:
    return f"rgb({color[0]} {color[1]} {color[2]})"


def rgba(color: tuple[int, int, int], opacity: float) -> str:
    return f"rgb({color[0]} {color[1]} {color[2]} / {opacity:.2f})"


def svg_text(x: int, y: int, text: str, size: int, *, weight: int = 400, fill: tuple[int, int, int] = INK) -> str:
    return (
        f'<text x="{x}" y="{y}" fill="{rgb(fill)}" font-size="{size}" '
        f'font-family="Arial, Helvetica, sans-serif" font-weight="{weight}">{escape(text)}</text>'
    )


def svg_multiline(
    x: int,
    y: int,
    lines: list[str],
    size: int,
    *,
    fill: tuple[int, int, int] = MUTED,
    line_gap: int = 22,
) -> str:
    return "\n".join(svg_text(x, y + i * line_gap, line, size, fill=fill) for i, line in enumerate(lines))


def svg_card(
    x: int,
    y: int,
    w: int,
    h: int,
    title: str,
    body: list[str],
    *,
    accent: tuple[int, int, int] = CYAN,
    number: str | None = None,
) -> str:
    pieces = [
        f'<g filter="url(#shadow)">',
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="16" fill="{rgb(CARD)}" stroke="{rgba(accent, 0.72)}" stroke-width="2"/>',
        f'<rect x="{x}" y="{y}" width="{w}" height="7" rx="3.5" fill="{rgb(accent)}"/>',
    ]
    if number:
        pieces.append(f'<circle cx="{x + 30}" cy="{y + 39}" r="18" fill="{rgba(accent, 0.22)}" stroke="{rgb(accent)}" stroke-width="2"/>')
        pieces.append(svg_text(x + 22, y + 46, number, 18, weight=700, fill=INK))
        text_x = x + 58
    else:
        text_x = x + 22
    pieces.append(svg_text(text_x, y + 43, title, 18, weight=700, fill=INK))
    pieces.append(svg_multiline(x + 22, y + 78, body, 14, fill=MUTED, line_gap=22))
    pieces.append("</g>")
    return "\n".join(pieces)


def svg_arrow(x1: int, y1: int, x2: int, y2: int, *, color: tuple[int, int, int] = CYAN) -> str:
    return (
        f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" '
        f'stroke="{rgb(color)}" stroke-width="4" stroke-linecap="round" marker-end="url(#arrow)"/>'
    )


def svg_shell(width: int, height: int, title: str, desc: str, body: str) -> str:
    grid = "\n".join(
        [
            *[
                f'<line x1="{x}" y1="0" x2="{x}" y2="{height}" stroke="{rgba(GRID, 0.16)}" stroke-width="1"/>'
                for x in range(0, width + 1, 80)
            ],
            *[
                f'<line x1="0" y1="{y}" x2="{width}" y2="{y}" stroke="{rgba(GRID, 0.13)}" stroke-width="1"/>'
                for y in range(0, height + 1, 80)
            ],
        ]
    )
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)}</title>
  <desc id="desc">{escape(desc)}</desc>
  <defs>
    <linearGradient id="bg" x1="0" x2="1" y1="0" y2="1">
      <stop offset="0%" stop-color="{rgb(BG_TOP)}"/>
      <stop offset="100%" stop-color="{rgb(BG_BOTTOM)}"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="10" stdDeviation="9" flood-color="#000" flood-opacity="0.24"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{rgb(CYAN)}"/>
    </marker>
  </defs>
  <rect width="{width}" height="{height}" rx="28" fill="url(#bg)"/>
  {grid}
  <path d="M 0 {height - 90} C {width * 0.25:.0f} {height - 160}, {width * 0.68:.0f} {height - 30}, {width} {height - 120}" fill="none" stroke="{rgba(CYAN, 0.28)}" stroke-width="4"/>
  <path d="M {width * 0.62:.0f} 0 C {width * 0.76:.0f} 120, {width * 0.9:.0f} 170, {width} 260" fill="none" stroke="{rgba(LIME, 0.22)}" stroke-width="5"/>
  {body}
</svg>
"""


def svg_social() -> str:
    body = "\n".join(
        [
            '<rect x="36" y="48" width="560" height="466" rx="28" fill="rgb(8 17 31 / 0.72)" stroke="rgb(111 218 238 / 0.18)" stroke-width="1"/>',
            svg_text(56, 78, "AI Workbench", 28, weight=700),
            svg_text(56, 158, ".supra", 66, weight=700),
            svg_text(56, 226, "Examples", 66, weight=700),
            svg_multiline(60, 290, ["47 portable packages aligned to the v1 standard", "Bilingual docs, strict validation, review-first outputs"], 20),
            '<rect x="56" y="372" width="218" height="54" rx="27" fill="rgb(111 218 238 / 0.14)" stroke="rgb(111 218 238 / 0.65)" stroke-width="2"/>',
            svg_text(85, 406, "v1 standard", 20, weight=700, fill=INK),
            '<rect x="300" y="372" width="218" height="54" rx="27" fill="rgb(186 238 111 / 0.12)" stroke="rgb(186 238 111 / 0.58)" stroke-width="2"/>',
            svg_text(329, 406, "EN / DE docs", 20, weight=700, fill=INK),
            '<rect x="56" y="444" width="218" height="54" rx="27" fill="rgb(246 189 96 / 0.14)" stroke="rgb(246 189 96 / 0.58)" stroke-width="2"/>',
            svg_text(85, 478, "CI ready", 20, weight=700, fill=INK),
            svg_card(640, 92, 220, 120, "Contracts", ["JSON output fields", "quality gates"], accent=CYAN),
            svg_card(894, 92, 220, 120, "Validation", ["schema checks", "mirror checks"], accent=LIME),
            svg_card(640, 252, 220, 120, "Workflows", ["ordered steps", "review-first run"], accent=AMBER),
            svg_card(894, 252, 220, 120, "Docs", ["generated package", "references"], accent=ROSE),
            svg_arrow(724, 430, 834, 430, color=CYAN),
            svg_arrow(834, 430, 944, 430, color=LIME),
            svg_card(640, 470, 150, 86, "Author", ["package JSON"], accent=CYAN),
            svg_card(810, 470, 150, 86, "Import", ["workbench"], accent=LIME),
            svg_card(980, 470, 150, 86, "Review", ["approval"], accent=AMBER),
        ]
    )
    return svg_shell(1200, 630, "AI Workbench .supra Examples", "47 packages aligned to the .supra v1 standard", body)


def svg_architecture() -> str:
    body = "\n".join(
        [
            svg_text(48, 72, "AI Workbench .supra Architecture", 36, weight=700),
            svg_text(50, 108, "Identity, columns, workflows, contracts, and mirrored imports", 18, fill=MUTED),
            svg_card(72, 172, 240, 132, ".supra package", ["metadata identity", "columns + prompts"], accent=CYAN),
            svg_arrow(318, 238, 388, 238),
            svg_card(392, 172, 240, 132, "v1 validator", ["contracts present", "mirrors aligned"], accent=LIME),
            svg_arrow(638, 238, 708, 238),
            svg_card(712, 172, 240, 132, "AI Workbench", ["imports workbench", "runs workflows"], accent=AMBER),
            svg_arrow(958, 238, 1040, 238),
            svg_card(976, 172, 164, 132, "Outputs", ["reviewed JSON", "evidence gaps"], accent=ROSE),
            svg_card(232, 420, 230, 120, "Generated docs", ["English + German", "source aligned"], accent=LIME),
            svg_card(506, 420, 230, 120, "Human review", ["manual gates", "responsible use"], accent=AMBER),
            svg_card(780, 420, 230, 120, "Audit trail", ["CI checks", "pull requests"], accent=CYAN),
            svg_arrow(492, 350, 560, 410, color=AMBER),
            svg_arrow(740, 350, 830, 410, color=CYAN),
        ]
    )
    return svg_shell(1200, 680, "AI Workbench .supra Architecture", "Architecture for importable .supra v1 examples", body)


def svg_workflow() -> str:
    cards = [
        (70, "Intake", ["manual context", "files or notes"], CYAN),
        (350, "Evidence", ["facts, sources", "visible gaps"], LIME),
        (630, "Decision", ["actions, owners", "risk checks"], AMBER),
        (910, "Reviewed output", ["contracted JSON", "human approval"], ROSE),
    ]
    body_parts = [
        svg_text(48, 72, ".supra Workflow Pipeline", 36, weight=700),
        svg_text(50, 108, "A review-first pattern for AI-assisted business workflows", 18, fill=MUTED),
    ]
    for i, (x, title, body, color) in enumerate(cards, start=1):
        body_parts.append(svg_card(x, 210, 220, 132, title, body, accent=color, number=str(i)))
        if i < len(cards):
            body_parts.append(svg_arrow(x + 226, 276, x + 276, 276, color=color))
    body_parts.extend(
        [
            '<rect x="114" y="404" width="970" height="54" rx="27" fill="rgb(111 218 238 / 0.10)" stroke="rgb(111 218 238 / 0.35)" stroke-width="2"/>',
            svg_text(170, 439, "Every executable step returns JSON, marks evidence gaps, and stays in manual-review mode.", 21, weight=700, fill=INK),
        ]
    )
    return svg_shell(1200, 520, ".supra Workflow Pipeline", "Intake, evidence, decision, and reviewed output", "\n".join(body_parts))


def svg_anatomy() -> str:
    body = "\n".join(
        [
            svg_text(48, 72, ".supra Package Anatomy", 36, weight=700),
            svg_text(50, 108, "The v1 sections that make a package portable and reviewable", 18, fill=MUTED),
            '<g filter="url(#shadow)">',
            f'<rect x="418" y="150" width="364" height="360" rx="22" fill="{rgb((12, 29, 45))}" stroke="{rgba(CYAN, 0.62)}" stroke-width="2"/>',
            svg_text(454, 202, "{", 44, weight=700, fill=CYAN),
            svg_text(494, 198, '"key": "example"', 21, fill=INK),
            svg_text(494, 248, '"metadata": {...}', 21, fill=LIME),
            svg_text(494, 298, '"columns": [...]', 21, fill=AMBER),
            svg_text(494, 348, '"workflows": [...]', 21, fill=ROSE),
            svg_text(494, 398, '"main_workbench": {...}', 21, fill=CYAN),
            svg_text(454, 468, "}", 44, weight=700, fill=CYAN),
            "</g>",
            svg_card(80, 154, 260, 132, "metadata", ["identity", "versions", "starter rows"], accent=LIME),
            svg_card(80, 374, 260, 116, "output contracts", ["required fields", "quality gates"], accent=ROSE),
            svg_card(860, 154, 260, 132, "columns", ["manual", "ai_tool", "shortcut"], accent=AMBER),
            svg_card(860, 374, 260, 116, "main_workbench", ["exact mirror", "import-ready"], accent=CYAN),
            svg_arrow(346, 220, 418, 236, color=LIME),
            svg_arrow(346, 430, 418, 390, color=ROSE),
            svg_arrow(860, 220, 782, 296, color=AMBER),
            svg_arrow(860, 430, 782, 400, color=CYAN),
        ]
    )
    return svg_shell(1200, 650, ".supra Package Anatomy", "The .supra v1 sections used by AI Workbench examples", body)


def svg_import_export() -> str:
    labels = [
        ("Author", ["edit package", "JSON"]),
        ("Validate", ["run v1", "checks"]),
        ("Document", ["generate", "EN/DE docs"]),
        ("Import", ["load mirror", "to Workbench"]),
        ("Review", ["run safely", "refine"]),
    ]
    colors = [CYAN, LIME, AMBER, ROSE, CYAN]
    xs = [60, 300, 540, 780, 1020]
    body = [
        svg_text(48, 72, ".supra Import / Export Flow", 36, weight=700),
        svg_text(50, 108, "Author, validate, document, import, review, and improve examples", 18, fill=MUTED),
    ]
    for i, (label, lines) in enumerate(labels):
        body.append(svg_card(xs[i], 196, 180 if i < 4 else 130, 118, label, lines, accent=colors[i], number=str(i + 1)))
        if i < 4:
            body.append(svg_arrow(xs[i] + (186 if i < 4 else 136), 255, xs[i + 1] - 18, 255, color=colors[i]))
    body.extend(
        [
            '<path d="M 1085 350 C 840 482, 330 484, 160 350" fill="none" stroke="rgb(111 218 238 / 0.42)" stroke-width="4" marker-end="url(#arrow)"/>',
            svg_text(430, 444, "Improvements return through package JSON, docs, CI, and pull requests.", 22, weight=700, fill=INK),
        ]
    )
    return svg_shell(1200, 560, ".supra Import / Export Flow", "How maintainers improve .supra packages", "\n".join(body))


def svg_governance() -> str:
    body = [
        svg_text(48, 66, ".supra Governance Loop", 34, weight=700),
        svg_text(50, 104, "Facts, assumptions, evidence gaps, and human review for v1 packages", 18, fill=MUTED),
        '<circle cx="600" cy="356" r="108" fill="rgb(111 218 238 / 0.18)" stroke="rgb(111 218 238 / 0.62)" stroke-width="3"/>',
        svg_text(518, 346, "Review-first", 28, weight=700, fill=INK),
        svg_text(544, 381, "execution", 24, weight=700, fill=INK),
    ]
    cards = [
        (102, 172, "Facts", ["separate known", "from inferred"], CYAN),
        (486, 150, "Contracts", ["required JSON", "quality gates"], LIME),
        (870, 172, "Human review", ["approval", "before use"], AMBER),
        (870, 430, "Audit trail", ["docs", "CI and PRs"], CYAN),
        (486, 492, "Evidence gaps", ["missing facts", "stay visible"], ROSE),
        (102, 430, "Actions", ["owners", "next steps"], LIME),
    ]
    anchors = [(330, 226, 486, 204), (714, 204, 870, 226), (985, 290, 985, 430), (870, 482, 714, 546), (486, 546, 330, 482), (215, 430, 215, 290)]
    for x1, y1, x2, y2 in anchors:
        body.append(svg_arrow(x1, y1, x2, y2))
    for x, y, title, lines, color in cards:
        body.append(svg_card(x, y, 228, 110, title, lines, accent=color))
    return svg_shell(1200, 650, ".supra Governance Loop", "Review-first governance for .supra packages", "\n".join(body))


def svg_logo() -> str:
    return """<svg xmlns="http://www.w3.org/2000/svg" width="512" height="512" viewBox="0 0 512 512" role="img" aria-label="AI Workbench .supra v1 examples logo">
  <defs>
    <linearGradient id="g" x1="0" x2="1" y1="0" y2="1">
      <stop stop-color="rgb(8 17 31)"/>
      <stop offset="1" stop-color="rgb(17 39 58)"/>
    </linearGradient>
    <filter id="shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="14" stdDeviation="12" flood-color="#000" flood-opacity="0.32"/>
    </filter>
  </defs>
  <rect width="512" height="512" rx="92" fill="url(#g)"/>
  <path d="M 88 318 C 142 390, 246 414, 336 366 C 386 340, 420 300, 438 250" fill="none" stroke="rgb(111 218 238)" stroke-width="32" stroke-linecap="round" filter="url(#shadow)"/>
  <path d="M 74 232 C 118 142, 226 106, 318 144 C 374 166, 414 208, 438 266" fill="none" stroke="rgb(186 238 111)" stroke-width="32" stroke-linecap="round"/>
  <circle cx="256" cy="256" r="56" fill="rgb(245 250 255)"/>
  <circle cx="256" cy="256" r="26" fill="rgb(17 39 58)"/>
  <text x="256" y="444" text-anchor="middle" fill="rgb(245 250 255)" font-size="58" font-family="Arial, Helvetica, sans-serif" font-weight="700">.supra</text>
  <text x="256" y="476" text-anchor="middle" fill="rgb(184 211 225)" font-size="19" font-family="Arial, Helvetica, sans-serif" font-weight="700">v1 examples</text>
</svg>
"""


def write_svg_assets(asset_dir: Path) -> None:
    svgs = {
        "social-preview.svg": svg_social(),
        "supra-workbench-architecture.svg": svg_architecture(),
        "supra-workflow-pipeline.svg": svg_workflow(),
        "supra-package-anatomy.svg": svg_anatomy(),
        "supra-import-export-flow.svg": svg_import_export(),
        "supra-governance-loop.svg": svg_governance(),
        "supra-logo-mark.svg": svg_logo(),
    }
    for name, content in svgs.items():
        (asset_dir / name).write_text(content, encoding="utf-8")


def load_pillow():
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception:
        return None, None, None
    return Image, ImageDraw, ImageFont


def font_factory(ImageFont):
    cache = {}

    def get(size: int, weight: str = "regular"):
        key = (size, weight)
        if key in cache:
            return cache[key]
        for candidate in FONT_CANDIDATES[weight]:
            try:
                cache[key] = ImageFont.truetype(candidate, size)
                return cache[key]
            except Exception:
                continue
        cache[key] = ImageFont.load_default()
        return cache[key]

    return get


def draw_background(draw, width: int, height: int) -> None:
    for y in range(height):
        t = y / max(height - 1, 1)
        color = tuple(int(BG_TOP[i] * (1 - t) + BG_BOTTOM[i] * t) for i in range(3))
        draw.line([(0, y), (width, y)], fill=color)
    for x in range(0, width, 80):
        draw.line([(x, 0), (x, height)], fill=(*GRID, 34), width=1)
    for y in range(0, height, 80):
        draw.line([(0, y), (width, y)], fill=(*GRID, 28), width=1)
    for i in range(4):
        offset = i * 28
        draw.arc((-260 + offset, height - 270, 680 + offset, height + 210), start=205, end=336, fill=(*CYAN, 45), width=3)
        draw.arc((width - 670 - offset, -270, width + 260 - offset, 380), start=114, end=230, fill=(*LIME, 38), width=4)


def draw_text(draw, xy, text: str, font, fill=INK, anchor=None) -> None:
    draw.text(xy, text, font=font, fill=fill, anchor=anchor)


def wrapped_lines(draw, text: str, font, max_width: int) -> list[str]:
    lines: list[str] = []
    for paragraph in text.split("\n"):
        words = paragraph.split()
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if draw.textlength(candidate, font=font) <= max_width or not current:
                current = candidate
            else:
                lines.append(current)
                current = word
        if current:
            lines.append(current)
    return lines


def draw_multiline(draw, xy, text: str | list[str], font, fill=MUTED, line_gap: int = 24, max_width: int | None = None) -> None:
    if isinstance(text, str):
        lines = wrapped_lines(draw, text, font, max_width) if max_width else text.split("\n")
    else:
        lines = text
    x, y = xy
    for i, line in enumerate(lines):
        draw.text((x, y + i * line_gap), line, font=font, fill=fill)


def rounded_card(draw, xy, radius=18, fill=(*CARD, 238), outline=(*CYAN, 165), width=2, shadow=True) -> None:
    x1, y1, x2, y2 = xy
    if shadow:
        draw.rounded_rectangle((x1 + 8, y1 + 10, x2 + 8, y2 + 10), radius=radius, fill=(0, 0, 0, 46))
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_card(draw, fonts, x, y, w, h, title, lines, accent=CYAN, number=None) -> None:
    rounded_card(draw, (x, y, x + w, y + h), outline=(*accent, 170))
    draw.rounded_rectangle((x, y, x + w, y + 8), radius=4, fill=(*accent, 255))
    title_x = x + 24
    if number:
        draw.ellipse((x + 20, y + 25, x + 58, y + 63), fill=(*accent, 38), outline=(*accent, 220), width=2)
        draw_text(draw, (x + 39, y + 45), number, fonts(20, "bold"), anchor="mm")
        title_x = x + 70
    draw_text(draw, (title_x, y + 28), title, fonts(22, "bold"))
    draw_multiline(draw, (x + 24, y + 66), lines, fonts(16), fill=MUTED, line_gap=24)


def draw_arrow(draw, start, end, color=CYAN, width=4) -> None:
    x1, y1 = start
    x2, y2 = end
    draw.line((x1, y1, x2, y2), fill=(*color, 230), width=width)
    angle = math.atan2(y2 - y1, x2 - x1)
    size = 12
    p1 = (x2, y2)
    p2 = (x2 - size * math.cos(angle - 0.45), y2 - size * math.sin(angle - 0.45))
    p3 = (x2 - size * math.cos(angle + 0.45), y2 - size * math.sin(angle + 0.45))
    draw.polygon([p1, p2, p3], fill=(*color, 230))


def make_canvas(Image, ImageDraw, size):
    img = Image.new("RGBA", size, (*BG_TOP, 255))
    draw = ImageDraw.Draw(img, "RGBA")
    draw_background(draw, *size)
    return img, draw


def render_social(Image, ImageDraw, fonts):
    img, draw = make_canvas(Image, ImageDraw, (1200, 630))
    draw.rounded_rectangle((36, 48, 596, 514), radius=28, fill=(*BG_TOP, 184), outline=(*CYAN, 46), width=1)
    draw_text(draw, (58, 78), "AI Workbench", fonts(34, "bold"))
    draw_text(draw, (56, 140), ".supra", fonts(70, "bold"))
    draw_text(draw, (56, 208), "Examples", fonts(70, "bold"))
    draw_multiline(
        draw,
        (62, 296),
        "47 portable packages aligned to the v1 standard\nBilingual docs, strict validation, review-first outputs",
        fonts(22),
        fill=MUTED,
        line_gap=31,
    )
    for x, y, label, color in [(58, 374, "v1 standard", CYAN), (306, 374, "EN / DE docs", LIME), (58, 444, "CI ready", AMBER)]:
        draw.rounded_rectangle((x, y, x + 218, y + 54), radius=27, fill=(*color, 40), outline=(*color, 170), width=2)
        draw_text(draw, (x + 28, y + 14), label, fonts(22, "bold"), fill=INK)
    draw_card(draw, fonts, 642, 96, 220, 112, "Contracts", ["JSON fields", "quality gates"], CYAN)
    draw_card(draw, fonts, 888, 96, 220, 112, "Validation", ["schema checks", "mirror checks"], LIME)
    draw_card(draw, fonts, 642, 250, 220, 112, "Workflows", ["ordered steps", "manual review"], AMBER)
    draw_card(draw, fonts, 888, 250, 220, 112, "Docs", ["generated EN/DE", "source aligned"], ROSE)
    for x, label, color in [(642, "Author", CYAN), (812, "Import", LIME), (982, "Review", AMBER)]:
        draw_card(draw, fonts, x, 458, 150, 86, label, ["package JSON" if label == "Author" else "workbench" if label == "Import" else "approval"], color)
    draw_arrow(draw, (794, 501), (812, 501), CYAN)
    draw_arrow(draw, (964, 501), (982, 501), LIME)
    return img


def render_architecture(Image, ImageDraw, fonts):
    img, draw = make_canvas(Image, ImageDraw, (1200, 680))
    draw_text(draw, (50, 78), "AI Workbench .supra Architecture", fonts(42, "bold"))
    draw_text(draw, (52, 116), "Identity, columns, workflows, contracts, and mirrored imports", fonts(20), fill=MUTED)
    boxes = [
        (72, 176, 238, 132, ".supra package", ["metadata identity", "columns + prompts"], CYAN),
        (392, 176, 238, 132, "v1 validator", ["contracts present", "mirrors aligned"], LIME),
        (712, 176, 238, 132, "AI Workbench", ["imports mirror", "runs workflows"], AMBER),
        (982, 176, 154, 132, "Outputs", ["reviewed JSON", "evidence gaps"], ROSE),
    ]
    for x, y, w, h, title, lines, color in boxes:
        draw_card(draw, fonts, x, y, w, h, title, lines, color)
    draw_arrow(draw, (318, 242), (386, 242), CYAN)
    draw_arrow(draw, (638, 242), (706, 242), LIME)
    draw_arrow(draw, (958, 242), (978, 242), AMBER)
    lower = [
        (232, 430, "Generated docs", ["English + German", "source aligned"], LIME),
        (506, 430, "Human review", ["manual gates", "responsible use"], AMBER),
        (780, 430, "Audit trail", ["CI checks", "pull requests"], CYAN),
    ]
    for x, y, title, lines, color in lower:
        draw_card(draw, fonts, x, y, 230, 116, title, lines, color)
    draw_arrow(draw, (500, 346), (565, 426), AMBER)
    draw_arrow(draw, (762, 346), (842, 426), CYAN)
    return img


def render_workflow(Image, ImageDraw, fonts):
    img, draw = make_canvas(Image, ImageDraw, (1200, 520))
    draw_text(draw, (50, 78), ".supra Workflow Pipeline", fonts(42, "bold"))
    draw_text(draw, (52, 116), "A review-first pattern for AI-assisted business workflows", fonts(20), fill=MUTED)
    cards = [
        (70, "Intake", ["manual context", "files or notes"], CYAN),
        (350, "Evidence", ["facts, sources", "visible gaps"], LIME),
        (630, "Decision", ["actions, owners", "risk checks"], AMBER),
        (910, "Reviewed output", ["contracted JSON", "human approval"], ROSE),
    ]
    for i, (x, title, lines, color) in enumerate(cards, start=1):
        draw_card(draw, fonts, x, 206, 220, 132, title, lines, color, str(i))
        if i < len(cards):
            draw_arrow(draw, (x + 226, 272), (x + 274, 272), color)
    draw.rounded_rectangle((112, 402, 1088, 458), radius=28, fill=(*CYAN, 28), outline=(*CYAN, 95), width=2)
    draw_text(draw, (170, 417), "Executable steps return JSON, mark evidence gaps, and stay in manual-review mode.", fonts(23, "bold"))
    return img


def render_anatomy(Image, ImageDraw, fonts):
    img, draw = make_canvas(Image, ImageDraw, (1200, 650))
    draw_text(draw, (50, 78), ".supra Package Anatomy", fonts(42, "bold"))
    draw_text(draw, (52, 116), "The v1 sections that make a package portable and reviewable", fonts(20), fill=MUTED)
    rounded_card(draw, (418, 150, 782, 510), radius=24, fill=(12, 29, 45, 248), outline=(*CYAN, 170))
    for i, (label, color) in enumerate(
        [
            ('"key": "example"', CYAN),
            ('"metadata": {...}', LIME),
            ('"columns": [...]', AMBER),
            ('"workflows": [...]', ROSE),
            ('"main_workbench": {...}', CYAN),
        ]
    ):
        draw_text(draw, (490, 205 + i * 50), label, fonts(23, "bold"), fill=color)
    draw_text(draw, (452, 205), "{", fonts(50, "bold"), fill=CYAN)
    draw_text(draw, (452, 472), "}", fonts(50, "bold"), fill=CYAN)
    draw_card(draw, fonts, 80, 154, 260, 132, "metadata", ["identity", "versions", "starter rows"], LIME)
    draw_card(draw, fonts, 80, 374, 260, 116, "output contracts", ["required fields", "quality gates"], ROSE)
    draw_card(draw, fonts, 860, 154, 260, 132, "columns", ["manual", "ai_tool", "shortcut"], AMBER)
    draw_card(draw, fonts, 860, 374, 260, 116, "main_workbench", ["exact mirror", "import-ready"], CYAN)
    draw_arrow(draw, (346, 220), (412, 238), LIME)
    draw_arrow(draw, (346, 430), (412, 390), ROSE)
    draw_arrow(draw, (860, 220), (788, 295), AMBER)
    draw_arrow(draw, (860, 430), (788, 400), CYAN)
    return img


def render_import_export(Image, ImageDraw, fonts):
    img, draw = make_canvas(Image, ImageDraw, (1200, 560))
    draw_text(draw, (50, 78), ".supra Import / Export Flow", fonts(42, "bold"))
    draw_text(draw, (52, 116), "Author, validate, document, import, review, and improve examples", fonts(20), fill=MUTED)
    labels = [
        (60, "Author", ["edit package", "JSON"], CYAN),
        (300, "Validate", ["run v1", "checks"], LIME),
        (540, "Document", ["generate", "EN/DE docs"], AMBER),
        (780, "Import", ["load mirror", "to Workbench"], ROSE),
        (1020, "Review", ["run safely", "refine"], CYAN),
    ]
    for i, (x, title, lines, color) in enumerate(labels, start=1):
        draw_card(draw, fonts, x, 198, 180 if i < 5 else 130, 118, title, lines, color, str(i))
        if i < 5:
            draw_arrow(draw, (x + 186, 258), (x + 236, 258), color)
    draw.arc((146, 320, 1090, 610), start=196, end=340, fill=(*CYAN, 115), width=4)
    draw_arrow(draw, (164, 384), (148, 365), CYAN)
    draw_text(draw, (430, 444), "Improvements return through package JSON, docs, CI, and pull requests.", fonts(24, "bold"))
    return img


def render_governance(Image, ImageDraw, fonts):
    img, draw = make_canvas(Image, ImageDraw, (1200, 650))
    draw_text(draw, (50, 64), ".supra Governance Loop", fonts(39, "bold"))
    draw_text(draw, (52, 112), "Facts, assumptions, evidence gaps, and human review for v1 packages", fonts(20), fill=MUTED)
    draw.ellipse((492, 248, 708, 464), fill=(*CYAN, 42), outline=(*CYAN, 150), width=3)
    draw_text(draw, (600, 340), "Review-first", fonts(31, "bold"), anchor="mm")
    draw_text(draw, (600, 378), "execution", fonts(27, "bold"), fill=INK, anchor="mm")
    cards = [
        (102, 172, "Facts", ["separate known", "from inferred"], CYAN),
        (486, 150, "Contracts", ["required JSON", "quality gates"], LIME),
        (870, 172, "Human review", ["approval", "before use"], AMBER),
        (870, 430, "Audit trail", ["docs", "CI and PRs"], CYAN),
        (486, 492, "Evidence gaps", ["missing facts", "stay visible"], ROSE),
        (102, 430, "Actions", ["owners", "next steps"], LIME),
    ]
    for start, end in [((330, 226), (480, 204)), ((720, 204), (870, 226)), ((985, 290), (985, 426)), ((870, 482), (720, 546)), ((486, 546), (330, 482)), ((215, 426), (215, 290))]:
        draw_arrow(draw, start, end, CYAN)
    for x, y, title, lines, color in cards:
        draw_card(draw, fonts, x, y, 228, 110, title, lines, color)
    return img


def render_logo(Image, ImageDraw, fonts):
    img, draw = make_canvas(Image, ImageDraw, (512, 512))
    draw.rounded_rectangle((0, 0, 512, 512), radius=92, fill=(*BG_TOP, 255))
    draw_background(draw, 512, 512)
    draw.arc((72, 106, 454, 408), start=198, end=338, fill=CYAN, width=32)
    draw.arc((62, 96, 450, 398), start=24, end=205, fill=LIME, width=32)
    draw.ellipse((200, 200, 312, 312), fill=INK)
    draw.ellipse((230, 230, 282, 282), fill=BG_BOTTOM)
    draw_text(draw, (256, 428), ".supra", fonts(62, "bold"), anchor="mm")
    draw_text(draw, (256, 470), "v1 examples", fonts(22, "bold"), fill=MUTED, anchor="mm")
    return img


def write_png_assets(asset_dir: Path) -> int:
    Image, ImageDraw, ImageFont = load_pillow()
    if Image is None:
        print("Pillow is not installed; SVG assets were regenerated.")
        return 0
    fonts = font_factory(ImageFont)
    renderers = {
        "social-preview.png": render_social,
        "supra-workbench-architecture.png": render_architecture,
        "supra-workflow-pipeline.png": render_workflow,
        "supra-package-anatomy.png": render_anatomy,
        "supra-import-export-flow.png": render_import_export,
        "supra-governance-loop.png": render_governance,
        "supra-logo-mark.png": render_logo,
    }
    for name, renderer in renderers.items():
        image = renderer(Image, ImageDraw, fonts).convert("RGB")
        image.save(asset_dir / name, optimize=True)
    return len(renderers)


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    asset_dir = root / "docs" / "assets"
    asset_dir.mkdir(parents=True, exist_ok=True)
    write_svg_assets(asset_dir)
    rendered_pngs = write_png_assets(asset_dir)
    print(f"Rendered 7 SVG assets and {rendered_pngs} PNG assets in {asset_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
