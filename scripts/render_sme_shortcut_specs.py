#!/usr/bin/env python3
"""Render managed SME shortcut registry entries for SupraWorx from the use-case spec.

SupraWorx (``mint/shortcuts/services/sme_shortcuts.py``) only accepts an uploaded
``.supra`` file when every ``shortcut`` column references a registered managed
shortcut. This script prints the ``_DISRUPTIVE_SME_SHORTCUT_SPECS`` entries for
every package in ``scripts/data/sme_use_cases.json`` so they can be appended to
that tuple (or applied with ``--apply path/to/sme_shortcuts.py``).

Usage::

    python3 scripts/render_sme_shortcut_specs.py .                       # print entries
    python3 scripts/render_sme_shortcut_specs.py . --apply ../mint/shortcuts/services/sme_shortcuts.py
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

SPEC_PATH = Path("scripts/data/sme_use_cases.json")
EXTRAS_PATH = Path("scripts/data/sme_registry_extras.json")
REGISTRY_PATH = Path("scripts/data/supraworx_managed_shortcuts.json")
BEGIN_MARK = "    # --- begin: generated from AI-Workbench-.supra-Examples scripts/data/sme_use_cases.json ---"
END_MARK = "    # --- end: generated from AI-Workbench-.supra-Examples ---"
TUPLE_CLOSE_RE = re.compile(r"^\)\n", re.MULTILINE)


def _py(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def render_entry(spec: dict) -> str:
    return "\n".join(
        [
            "    {",
            f"        \"shortcut_id\": {_py(spec['key'])},",
            f"        \"title\": {_py(spec['title'])},",
            f"        \"description\": {_py(spec['description_en'])},",
            f"        \"textarea_label\": {_py(spec['textarea_label'])},",
            f"        \"result_title\": {_py(spec['result_title'])},",
            f"        \"focus\": {_py(spec['focus'])},",
            "    },",
        ]
    )


def render_block(specs: list[dict]) -> str:
    return "\n".join([BEGIN_MARK, *(render_entry(spec) for spec in specs), END_MARK]) + "\n"


def apply(target: Path, block: str) -> str:
    source = target.read_text(encoding="utf-8")
    if BEGIN_MARK in source and END_MARK in source:
        start = source.index(BEGIN_MARK)
        end = source.index(END_MARK) + len(END_MARK) + 1
        return source[:start] + block + source[end:]

    anchor = "_DISRUPTIVE_SME_SHORTCUT_SPECS: tuple[dict[str, object], ...] = ("
    if anchor not in source:
        raise SystemExit(f"{target}: could not find _DISRUPTIVE_SME_SHORTCUT_SPECS tuple")
    tuple_start = source.index(anchor)
    close = TUPLE_CLOSE_RE.search(source, tuple_start)
    if close is None:
        raise SystemExit(f"{target}: could not find the end of _DISRUPTIVE_SME_SHORTCUT_SPECS")
    return source[: close.start()] + block + source[close.start():]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--apply", default=None, help="Path to SupraWorx sme_shortcuts.py to patch in place")
    parser.add_argument("--registry", action="store_true", help="Update scripts/data/supraworx_managed_shortcuts.json with the generated IDs")
    args = parser.parse_args()

    root = Path(args.root)
    specs = json.loads((root / SPEC_PATH).read_text(encoding="utf-8"))
    extras_path = root / EXTRAS_PATH
    if extras_path.exists():
        specs = specs + json.loads(extras_path.read_text(encoding="utf-8"))
    block = render_block(specs)
    if args.registry:
        registry_path = root / REGISTRY_PATH
        registry = json.loads(registry_path.read_text(encoding="utf-8"))
        ids = set(registry.get("registered_shortcut_ids", [])) | {spec["key"] for spec in specs}
        registry["registered_shortcut_ids"] = sorted(ids)
        registry_path.write_text(json.dumps(registry, indent=2) + "\n", encoding="utf-8")
        print(f"Registry now lists {len(ids)} managed shortcut IDs")
        return 0
    if args.apply:
        target = Path(args.apply)
        target.write_text(apply(target, block), encoding="utf-8")
        print(f"Applied {len(specs)} managed SME shortcut entries to {target}")
        return 0
    print(block, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
