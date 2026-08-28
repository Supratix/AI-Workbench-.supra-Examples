#!/usr/bin/env python3
"""Generate EN/DE docs and a manifest from .supra package files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


MANIFEST_SCHEMA = "SUPRA_EXAMPLES_MANIFEST_V2"
MANIFEST_TARGET = "AI Workbench .supra examples repository"
PACKAGES_DIR = "packages"
DOCS_PACKAGES_DIR = "packages"
DATA_DIR = Path("scripts/data")

GERMAN_DESCRIPTIONS: dict[str, str] = {}
GERMAN_STARTER_REQUESTS: dict[str, str] = {}
DOMAINS: dict[str, dict[str, str]] = {}


def load_data(root: Path) -> None:
    """Load German descriptions, starter-request translations, and domain labels."""
    de = json.loads((root / DATA_DIR / "descriptions.de.json").read_text(encoding="utf-8"))
    GERMAN_DESCRIPTIONS.update(de.get("descriptions", {}))
    GERMAN_STARTER_REQUESTS.update(de.get("starter_requests", {}))
    for data_file in ("sme_use_cases.json",):
        path = root / DATA_DIR / data_file
        if path.exists():
            for spec in json.loads(path.read_text(encoding="utf-8")):
                GERMAN_DESCRIPTIONS.setdefault(spec["key"], spec["description_de"])
    domains = json.loads((root / DATA_DIR / "domains.json").read_text(encoding="utf-8"))
    DOMAINS.update(domains.get("domains", {}))


def domain_label(domain: str, lang: str) -> str:
    labels = DOMAINS.get(domain, {})
    return labels.get(lang) or labels.get("en") or domain.replace("_", " ").title()


def table(rows: list[list[str]]) -> str:
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
    out = ["| " + " | ".join(str(rows[0][i]).ljust(widths[i]) for i in range(len(widths))) + " |"]
    out.append("| " + " | ".join("-" * widths[i] for i in range(len(widths))) + " |")
    for row in rows[1:]:
        out.append("| " + " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(widths))) + " |")
    return "\n".join(out)


def localized_description(pkg: dict, lang: str) -> str:
    if lang == "de":
        return GERMAN_DESCRIPTIONS[pkg["key"]]
    return pkg.get("description", "")


def yn(value: bool, lang: str) -> str:
    if lang == "de":
        return "ja" if value else "nein"
    return "yes" if value else "no"


def localized_starter_request(pkg: dict, starter: dict, lang: str) -> str:
    request = starter.get("request", "")
    if lang == "de":
        if not request:
            return f"Fügen Sie den Quellkontext für {pkg['title']} ein."
        if request in GERMAN_STARTER_REQUESTS:
            return GERMAN_STARTER_REQUESTS[request]
        if request.startswith("Paste the source context for ") and request.endswith("."):
            name = request.removeprefix("Paste the source context for ").removesuffix(".")
            return f"Fügen Sie den Quellkontext für {name} ein."
    return request


def localized_title(value: str, lang: str) -> str:
    if lang != "de":
        return value
    if value.endswith(" starter"):
        return value.removesuffix(" starter") + " Starter"
    if value.endswith(" workflow"):
        return value.removesuffix(" workflow") + " Workflow"
    return value


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
    overview_labels = {
        "source": "Quellpaket" if de else "Source package",
        "workbench": "Workbench-Titel" if de else "Workbench title",
        "key": "Paket-Key" if de else "Package key",
        "vendor": "Anbieter" if de else "Vendor",
        "schema": "Schemaversion" if de else "Schema version",
        "columns": "Spalten" if de else "Columns",
        "workflows": "Workflows",
        "request": "Anfrage" if de else "Request",
        "source_type": "Quelltyp" if de else "Source type",
        "step": "Schritt" if de else "Step",
        "review": "Prüfung" if de else "Review",
        "required_output": "Pflichtausgabe" if de else "Required output",
        "execution": "Ausführung" if de else "Execution",
        "required_fields": "Pflichtfelder" if de else "Required fields",
        "evidence_policy": "Evidenzregel" if de else "Evidence policy",
    }
    lines = [f"# {pkg['title']}", ""]
    lines.append("Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt." if de else "This documentation is generated from the `.supra` package content.")
    lines += ["", f"## {labels['overview']}", ""]
    lines += [
        f"- **{overview_labels['source']}:** [`{pkg['_path']}`](../../{pkg['_path']})",
        f"- **{'Domäne' if de else 'Domain'}:** {domain_label(pkg['_domain'], lang)} (`{pkg['_domain']}`)",
        f"- **{overview_labels['workbench']}:** {pkg.get('workbench_title', '')}",
        f"- **{overview_labels['key']}:** `{pkg['key']}`",
        f"- **{overview_labels['vendor']}:** {pkg.get('metadata', {}).get('vendor', '')}",
        f"- **{overview_labels['schema']}:** `{pkg.get('schemaVersion', '')}`",
        f"- **{overview_labels['columns']}:** {len(pkg.get('columns', []))}",
        f"- **{overview_labels['workflows']}:** {len(pkg.get('workflows', []))}",
        "",
        f"## {labels['purpose']}",
        "",
        localized_description(pkg, lang),
        "",
        f"## {labels['starter']}",
        "",
    ]
    for starter in pkg.get("metadata", {}).get("starter_rows", []):
        lines += [f"### {localized_title(starter.get('title', 'Starter'), lang)}", "", f"- **{overview_labels['request']}:** {localized_starter_request(pkg, starter, lang)}", f"- **{overview_labels['source_type']}:** `{starter.get('source_type', '')}`", ""]
        if de:
            lines += ["_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._", ""]
        lines += ["```json"]
        try:
            lines.append(json.dumps(json.loads(starter.get("text", "{}")), indent=2, ensure_ascii=False))
        except Exception:
            lines.append(starter.get("text", ""))
        lines += ["```", ""]
    lines += [f"## {labels['workflow']}", ""]
    if pkg.get("workflows"):
        for wf in pkg["workflows"]:
            workflow_description = localized_description(pkg, lang) if wf.get("description") == pkg.get("description") else wf.get("description", "")
            lines += [f"### {localized_title(wf.get('title', ''), lang)}", "", workflow_description, ""]
            rows = [["#", overview_labels["step"], "ID", "Backlog"]]
            for i, step in enumerate(wf.get("steps", []), 1):
                rows.append([str(i), step.get("title", ""), f"`{step.get('id', '')}`", yn(step.get("backlog"), lang)])
            lines += [table(rows), ""]
    else:
        lines += ["_Es ist kein Workflow konfiguriert._" if de else "_No workflow is configured._", ""]
    lines += [f"## {labels['columns']}", ""]
    rows = [["#", "Key", "Titel" if de else "Title", "Kategorie" if de else "Category", "Tool", overview_labels["review"], overview_labels["required_output"]]]
    for i, col in enumerate(pkg.get("columns", []), 1):
        pe = col.get("tooling", {}).get("prompt_execution", {})
        contract = col.get("tooling", {}).get("output_contract", {})
        rows.append([str(i), f"`{col.get('key', '')}`", col.get("title", ""), f"`{col.get('tool_category', '')}`", f"`{col.get('tool', '')}`", yn(pe.get("requires_review"), lang), "<br>".join(f"`{x}`" for x in contract.get("required_fields", [])) or "-"])
    lines += [table(rows), "", f"## {labels['prompts']}", ""]
    if de:
        lines += ["_Prompts werden als Originalauszüge aus dem Paket angezeigt._", ""]
    for col in pkg.get("columns", []):
        pe = col.get("tooling", {}).get("prompt_execution", {})
        contract = col.get("tooling", {}).get("output_contract")
        lines += [f"### {col.get('title', '')}", "", f"- **Key:** `{col.get('key', '')}`", f"- **Tool:** `{col.get('tool', '')}`", f"- **{overview_labels['execution']}:** execute_prompt={yn(pe.get('execute_prompt'), lang)}; mode=`{pe.get('mode', '-')}`; requires_review={yn(pe.get('requires_review'), lang)}", ""]
        if col.get("prompt"):
            lines += ["```text", col["prompt"], "```", ""]
        if contract:
            lines += [f"- **Schema:** `{contract.get('schema_version', '')}`", f"- **{overview_labels['required_fields']}:** {', '.join(f'`{x}`' for x in contract.get('required_fields', []))}", f"- **{overview_labels['evidence_policy']}:** `{contract.get('evidence_policy', '')}`", ""]
    governance = [
        "- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.",
        "- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.",
        "- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.",
    ] if de else [
        "- Manual columns collect user or file input and do not execute prompts.",
        "- Executable columns default to manual review where configured.",
        "- Output contracts keep downstream checks predictable.",
    ]
    lines += [f"## {labels['governance']}", "", *governance, ""]
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
                "domain": pkg["_domain"],
                "source": pkg["_path"],
                "docs": {
                    "en": f"docs/{DOCS_PACKAGES_DIR}/{pkg['key']}.en.md",
                    "de": f"docs/{DOCS_PACKAGES_DIR}/{pkg['key']}.de.md",
                },
            }
            for pkg in packages
        ],
    }


def package_rows(packages: list[dict], *, link_prefix: str) -> str:
    rows = [["Package", "Description / Beschreibung", "Columns", "Deutsch", "English"]]
    for pkg in packages:
        rows.append([
            pkg["title"],
            f"{pkg.get('description', '')}<br>_{GERMAN_DESCRIPTIONS.get(pkg['key'], '')}_",
            str(len(pkg.get("columns", []))),
            f"[DE]({link_prefix}{pkg['key']}.de.md)",
            f"[EN]({link_prefix}{pkg['key']}.en.md)",
        ])
    return table(rows)


def grouped(packages: list[dict]) -> dict[str, list[dict]]:
    groups: dict[str, list[dict]] = {}
    for pkg in packages:
        groups.setdefault(pkg["_domain"], []).append(pkg)
    return {domain: groups[domain] for domain in sorted(groups, key=lambda d: domain_label(d, "en"))}


def docs_readme(packages: list[dict]) -> str:
    lines = [
        "# `.supra` Example Documentation",
        "",
        "Generated German and English Markdown documentation for every `.supra` package in this repository.",
        "Descriptions are read from the source package metadata and `scripts/data/*.json`, so this catalog stays aligned with the importable examples.",
        "",
        "Generierte deutsche und englische Dokumentation für jedes `.supra`-Paket in diesem Repository. Die Paketdokumente liegen unter [`packages/`](packages/), gruppiert nach Domäne.",
        "",
        "![Workflow pipeline](assets/supra-workflow-pipeline.svg)",
        "",
        f"**{len(packages)} packages / Pakete** in {len(grouped(packages))} domains / Domänen.",
        "",
    ]
    for domain, pkgs in grouped(packages).items():
        lines += [
            f"## {domain_label(domain, 'en')} / {domain_label(domain, 'de')}",
            "",
            f"Folder / Ordner: [`packages/{domain}/`](../packages/{domain}/README.md) — {len(pkgs)} packages",
            "",
            package_rows(pkgs, link_prefix=f"{DOCS_PACKAGES_DIR}/"),
            "",
        ]
    lines += [
        "## Guides",
        "",
        "- [The `.supra` v1 Standard](supra-v1-standard.md)",
        "- [`.supra` v1 Standard Fix Playbook](supra-v1-standard-fix.md)",
        "- [SupraWorx import evaluation (EN)](import-evaluation.en.md) · [Import-Bewertung (DE)](import-evaluation.de.md)",
        "- [Repository guide (EN)](repository-guide.en.md) · [Repository-Leitfaden (DE)](repository-guide.de.md)",
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
        "python3 scripts/new_sme_package.py .",
        "python3 scripts/generate_docs.py .",
        "python3 scripts/render_assets.py .",
        "```",
        "",
    ]
    return "\n".join(lines)


def domain_readme(domain: str, packages: list[dict]) -> str:
    lines = [
        f"# {domain_label(domain, 'en')} / {domain_label(domain, 'de')}",
        "",
        f"`packages/{domain}/` contains {len(packages)} importable `.supra` packages. Generated documentation lives in [`docs/packages/`](../../docs/packages/).",
        "",
        f"`packages/{domain}/` enthält {len(packages)} importierbare `.supra`-Pakete. Die generierte Dokumentation liegt unter [`docs/packages/`](../../docs/packages/).",
        "",
        package_rows(packages, link_prefix=f"../../docs/{DOCS_PACKAGES_DIR}/"),
        "",
        "```bash",
        "python3 scripts/validate_supra.py .   # validate all packages",
        "```",
        "",
    ]
    return "\n".join(lines)


def load_packages(root: Path) -> list[dict]:
    packages_dir = root / PACKAGES_DIR
    files = sorted(packages_dir.rglob("*.supra")) if packages_dir.is_dir() else sorted(root.glob("*.supra"))
    packages = []
    for path in files:
        pkg = json.loads(path.read_text(encoding="utf-8"))
        pkg["_path"] = path.relative_to(root).as_posix()
        pkg["_domain"] = path.parent.name if path.parent != root else "uncategorized"
        packages.append(pkg)
    return sorted(packages, key=lambda pkg: pkg["key"])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--check", action="store_true", help="Fail if expected docs are missing or outdated")
    args = parser.parse_args()
    root = Path(args.root)
    load_data(root)
    docs = root / "docs"
    docs_packages = docs / DOCS_PACKAGES_DIR
    docs_packages.mkdir(parents=True, exist_ok=True)
    packages = load_packages(root)
    missing_de = [pkg["key"] for pkg in packages if pkg["key"] not in GERMAN_DESCRIPTIONS]
    if missing_de:
        raise SystemExit(f"Missing German descriptions (scripts/data/descriptions.de.json) for: {', '.join(missing_de)}")

    outputs: dict[Path, str] = {}
    for pkg in packages:
        for lang in ["en", "de"]:
            outputs[docs_packages / f"{pkg['key']}.{lang}.md"] = doc(pkg, lang)
    outputs[docs / "README.md"] = docs_readme(packages)
    for domain, pkgs in grouped(packages).items():
        outputs[root / PACKAGES_DIR / domain / "README.md"] = domain_readme(domain, pkgs)
    outputs[root / "examples_manifest.json"] = json.dumps(manifest(packages), indent=2, ensure_ascii=False) + "\n"

    if args.check:
        stale = [str(path.relative_to(root)) for path, content in outputs.items()
                 if not path.exists() or path.read_text(encoding="utf-8") != content]
        if stale:
            raise SystemExit("Generated files are missing or outdated (run scripts/generate_docs.py):\n- " + "\n- ".join(stale))
    else:
        for path, content in outputs.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    print(f"Documentation {'checked' if args.check else 'generated'} for {len(packages)} packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
