#!/usr/bin/env python3
"""Regenerate simple PNG README previews for existing SVG assets.

The committed SVG files are the source of truth. This helper creates lightweight
PNG preview cards using Pillow when it is available.
"""
from __future__ import annotations

import sys
from pathlib import Path


def main() -> int:
    try:
        from PIL import Image, ImageDraw, ImageFont
    except Exception:
        print("Pillow is not installed; SVG assets remain usable.")
        return 0
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    asset_dir = root / "docs" / "assets"
    asset_dir.mkdir(parents=True, exist_ok=True)
    try:
        font_title = ImageFont.truetype("DejaVuSans-Bold.ttf", 54)
        font_sub = ImageFont.truetype("DejaVuSans.ttf", 26)
    except Exception:
        font_title = ImageFont.load_default()
        font_sub = ImageFont.load_default()
    specs = {
        "social-preview.png": ("AI Workbench .supra Examples", "Packages • docs • schemas • CI • diagrams", (1200, 630)),
        "supra-workbench-architecture.png": ("AI Workbench .supra Architecture", "Package files to reviewable workflow outputs", (1200, 680)),
        "supra-workflow-pipeline.png": (".supra Workflow Pipeline", "Intake → Signal map → Decision plan → Execution brief", (1200, 520)),
        "supra-package-anatomy.png": (".supra Package Anatomy", "metadata • columns • workflows • contracts", (1200, 650)),
        "supra-import-export-flow.png": (".supra Import / Export Flow", "Author → validate → document → import → review", (1200, 560)),
        "supra-governance-loop.png": (".supra Governance Loop", "Guardrails • contracts • review • audit", (1200, 650)),
        "supra-logo-mark.png": (".supra", "AI Workbench examples", (512, 512)),
    }
    for name, (title, subtitle, size) in specs.items():
        w, h = size
        img = Image.new("RGB", size, (7, 17, 31))
        draw = ImageDraw.Draw(img)
        for y in range(h):
            draw.line([(0, y), (w, y)], fill=(7 + y // 80, 17 + y // 30, 31 + y // 18))
        draw.rounded_rectangle((55, 55, w - 55, h - 55), radius=30, outline=(123, 223, 242), width=3)
        draw.text((90, 100), title, fill=(255, 255, 255), font=font_title)
        draw.text((92, 180), subtitle, fill=(200, 226, 238), font=font_sub)
        img.save(asset_dir / name)
    print(f"Rendered {len(specs)} PNG assets in {asset_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
