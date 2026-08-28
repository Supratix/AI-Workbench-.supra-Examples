#!/usr/bin/env python3
"""Rewrite `.supra` metadata so the SupraWorx importer's strict allow-list accepts it.

The importer (``mint/workbench/config_security.py``) rejects a package whose
``metadata`` contains any field outside its allow-list. This script:

* removes ``metadata.github_example`` (repository note, not importer metadata),
* moves other unknown metadata objects/lists into ``metadata.process`` (an
  allowed extension object, max 64 KiB) so no information is lost,
* adds ``metadata.source_attribution`` pointing at this repository when missing,
* keeps ``main_workbench`` untouched.

Usage::

    python3 scripts/fix_supraworx_compat.py .            # rewrite packages/**/*.supra
    python3 scripts/fix_supraworx_compat.py . --check    # exit 1 if a rewrite would change a file
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED_METADATA = {
    "module_name", "modul_name", "vendor", "global_product_pk", "global_pim_product_nr",
    "content_name", "content_title", "content_description", "export_version",
    "import_version", "starter_rows", "source_attribution", "business_model", "commerce",
    "tenant_binding", "source_issue", "scoring", "account_universe", "last_config_review",
    "process", "governance", "operating_cadence",
}
DROP_KEYS = {"github_example"}
REPO_URL = "https://github.com/Supratix/AI-Workbench-.supra-Examples"


def fix_package(data: dict) -> tuple[dict, list[str]]:
    notes: list[str] = []
    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        return data, notes
    for key in list(metadata):
        if key in DROP_KEYS:
            metadata.pop(key)
            notes.append(f"dropped metadata.{key}")
        elif key not in ALLOWED_METADATA:
            process = metadata.get("process")
            if not isinstance(process, dict):
                process = {}
            process[key] = metadata.pop(key)
            metadata["process"] = process
            notes.append(f"moved metadata.{key} -> metadata.process.{key}")
    if "source_attribution" not in metadata:
        metadata["source_attribution"] = {
            "text": "AI Workbench .supra examples repository",
            "url": REPO_URL,
        }
        notes.append("added metadata.source_attribution")
    return data, notes


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    root = Path(args.root)
    packages = root / "packages"
    files = sorted(packages.rglob("*.supra")) if packages.is_dir() else sorted(root.glob("*.supra"))
    changed = 0
    for path in files:
        original = path.read_text(encoding="utf-8")
        data = json.loads(original)
        data, notes = fix_package(data)
        rendered = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
        if rendered != original and notes:
            changed += 1
            print(f"{path}: " + "; ".join(notes))
            if not args.check:
                path.write_text(rendered, encoding="utf-8")
    if args.check and changed:
        print(f"{changed} package(s) need scripts/fix_supraworx_compat.py")
        return 1
    print(f"{'Would rewrite' if args.check else 'Rewrote'} {changed} of {len(files)} packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
