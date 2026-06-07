#!/usr/bin/env python3
"""Generate EN/DE docs and a manifest from .supra package files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


MANIFEST_SCHEMA = "SUPRA_EXAMPLES_MANIFEST_V1"
MANIFEST_TARGET = "AI Workbench .supra examples repository"


def table(rows: list[list[str]]) -> str:
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
    out = ["| " + " | ".join(str(rows[0][i]).ljust(widths[i]) for i in range(len(widths))) + " |"]
    out.append("| " + " | ".join("-" * widths[i] for i in range(len(widths))) + " |")
    for row in rows[1:]:
        out.append("| " + " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(widths))) + " |")
    return "\n".join(out)


def doc(pkg: dict, lang: str) -> str:
    de = lang == "de"
    labels = {
        "overview": "Paketüberblick" if de else "Package Overview",
        "purpose": "Zweck" if de else "Purpose",
        "starter": "Starter-Eingabe" if de else "Starter Intake",
        "workflow": "Workflow",
        "columns": "Spalten und Tools" if de else "Columns and Tools",
        "prompts": "Prompt- und Vertragsreferenz" if de else "Prompt and Contract Reference",
        "governance": "Governance-Hinweise" if de else "Governance Notes",
    }
    lines = [f"# {pkg['title']}", ""]
    lines.append("Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt." if de else "This documentation is generated from the `.supra` package content.")
    lines += ["", f"## {labels['overview']}", ""]
    lines += [
        f"- **Source package:** [`../{pkg['key']}.supra`](../{pkg['key']}.supra)",
        f"- **Workbench title:** {pkg.get('workbench_title', '')}",
        f"- **Package key:** `{pkg['key']}`",
        f"- **Vendor:** {pkg.get('metadata', {}).get('vendor', '')}",
        f"- **Schema version:** `{pkg.get('schemaVersion', '')}`",
        f"- **Columns:** {len(pkg.get('columns', []))}",
        f"- **Workflows:** {len(pkg.get('workflows', []))}",
        "",
        f"## {labels['purpose']}",
        "",
        pkg.get("description", ""),
        "",
        f"## {labels['starter']}",
        "",
    ]
    for starter in pkg.get("metadata", {}).get("starter_rows", []):
        lines += [f"### {starter.get('title', 'Starter')}", "", f"- **Request:** {starter.get('request', '')}", f"- **Source type:** `{starter.get('source_type', '')}`", "", "```json"]
        try:
            lines.append(json.dumps(json.loads(starter.get("text", "{}")), indent=2, ensure_ascii=False))
        except Exception:
            lines.append(starter.get("text", ""))
        lines += ["```", ""]
    lines += [f"## {labels['workflow']}", ""]
    if pkg.get("workflows"):
        for wf in pkg["workflows"]:
            lines += [f"### {wf.get('title', '')}", "", wf.get("description", ""), ""]
            rows = [["#", "Step", "ID", "Backlog"]]
            for i, step in enumerate(wf.get("steps", []), 1):
                rows.append([str(i), step.get("title", ""), f"`{step.get('id', '')}`", "yes" if step.get("backlog") else "no"])
            lines += [table(rows), ""]
    else:
        lines += ["_No workflow is configured._", ""]
    lines += [f"## {labels['columns']}", ""]
    rows = [["#", "Key", "Title", "Category", "Tool", "Review", "Required output"]]
    for i, col in enumerate(pkg.get("columns", []), 1):
        pe = col.get("tooling", {}).get("prompt_execution", {})
        contract = col.get("tooling", {}).get("output_contract", {})
        rows.append([str(i), f"`{col.get('key', '')}`", col.get("title", ""), f"`{col.get('tool_category', '')}`", f"`{col.get('tool', '')}`", "yes" if pe.get("requires_review") else "no", "<br>".join(f"`{x}`" for x in contract.get("required_fields", [])) or "-"])
    lines += [table(rows), "", f"## {labels['prompts']}", ""]
    for col in pkg.get("columns", []):
        pe = col.get("tooling", {}).get("prompt_execution", {})
        contract = col.get("tooling", {}).get("output_contract")
        lines += [f"### {col.get('title', '')}", "", f"- **Key:** `{col.get('key', '')}`", f"- **Tool:** `{col.get('tool', '')}`", f"- **Execution:** execute_prompt={'yes' if pe.get('execute_prompt') else 'no'}; mode=`{pe.get('mode', '-')}`; requires_review={'yes' if pe.get('requires_review') else 'no'}", ""]
        if col.get("prompt"):
            lines += ["```text", col["prompt"], "```", ""]
        if contract:
            lines += [f"- **Schema:** `{contract.get('schema_version', '')}`", f"- **Required fields:** {', '.join(f'`{x}`' for x in contract.get('required_fields', []))}", f"- **Evidence policy:** `{contract.get('evidence_policy', '')}`", ""]
    lines += [f"## {labels['governance']}", "", "- Manual columns collect user or file input and do not execute prompts.", "- Executable columns default to manual review where configured.", "- Output contracts keep downstream checks predictable.", ""]
    return "\n".join(lines)


def manifest(packages: list[dict]) -> dict:
    return {
        "schema": MANIFEST_SCHEMA,
        "generated_for": MANIFEST_TARGET,
        "package_count": len(packages),
        "packages": [
            {
                "key": pkg["key"],
                "title": pkg["title"],
                "description": pkg.get("description", ""),
                "columns": len(pkg.get("columns", [])),
                "workflows": len(pkg.get("workflows", [])),
                "source": f"{pkg['key']}.supra",
                "docs": {
                    "en": f"docs/{pkg['key']}.en.md",
                    "de": f"docs/{pkg['key']}.de.md",
                },
            }
            for pkg in packages
        ],
    }


def docs_readme(packages: list[dict]) -> str:
    rows = [["Package", "Description", "Columns", "Workflows", "Deutsch", "English"]]
    for pkg in packages:
        rows.append([
            pkg["title"],
            pkg.get("description", ""),
            str(len(pkg.get("columns", []))),
            str(len(pkg.get("workflows", []))),
            f"[`{pkg['key']}.de.md`]({pkg['key']}.de.md)",
            f"[`{pkg['key']}.en.md`]({pkg['key']}.en.md)",
        ])
    return "\n".join([
        "# `.supra` Example Documentation",
        "",
        "Generated German and English Markdown documentation for every `.supra` package in this examples repository.",
        "Descriptions are read from the source package metadata so this catalog stays aligned with the importable examples.",
        "",
        "![Workflow pipeline](assets/supra-workflow-pipeline.svg)",
        "",
        table(rows),
        "",
        "## Diagrams",
        "",
        "- [Architecture](assets/supra-workbench-architecture.svg)",
        "- [Package anatomy](assets/supra-package-anatomy.svg)",
        "- [Workflow pipeline](assets/supra-workflow-pipeline.svg)",
        "- [Import/export flow](assets/supra-import-export-flow.svg)",
        "- [Governance loop](assets/supra-governance-loop.svg)",
        "",
        "## Regeneration",
        "",
        "```bash",
        "python3 scripts/generate_docs.py .",
        "python3 scripts/render_assets.py .",
        "```",
        "",
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--check", action="store_true", help="Fail if expected docs are missing")
    args = parser.parse_args()
    root = Path(args.root)
    docs = root / "docs"
    docs.mkdir(exist_ok=True)
    packages = []
    for path in sorted(root.glob("*.supra")):
        pkg = json.loads(path.read_text(encoding="utf-8"))
        packages.append(pkg)
        for lang in ["en", "de"]:
            target = docs / f"{pkg['key']}.{lang}.md"
            if args.check and not target.exists():
                raise SystemExit(f"Missing generated doc: {target}")
            if not args.check:
                target.write_text(doc(pkg, lang), encoding="utf-8")
    if args.check and not (docs / "README.md").exists():
        raise SystemExit("Missing docs/README.md")
    if args.check and not (root / "examples_manifest.json").exists():
        raise SystemExit("Missing examples_manifest.json")
    if not args.check:
        (docs / "README.md").write_text(docs_readme(packages), encoding="utf-8")
        (root / "examples_manifest.json").write_text(json.dumps(manifest(packages), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Documentation {'checked' if args.check else 'generated'} for {len(packages)} packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
