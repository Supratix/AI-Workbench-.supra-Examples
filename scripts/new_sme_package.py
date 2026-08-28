#!/usr/bin/env python3
"""Generate SME `.supra` v1 packages from a compact use-case spec.

The spec file (default: ``scripts/data/sme_use_cases.json``) holds one object per
package with the keys ``key``, ``domain``, ``title``, ``description_en``,
``description_de``, ``focus``, ``textarea_label``, ``result_title`` and
``scenario``. The same spec is used by ``scripts/render_sme_shortcut_specs.py``
to produce the managed shortcut registry entries for SupraWorx, so the shortcut
IDs used by the ``execution_brief`` column always match.

Usage::

    python3 scripts/new_sme_package.py .                 # generate all specs
    python3 scripts/new_sme_package.py . --only sme_x    # generate one package
    python3 scripts/new_sme_package.py . --check         # fail if files differ

Generated packages only use metadata fields that the SupraWorx importer's
strict allow-list accepts (see docs/import-evaluation.en.md).
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

SPEC_PATH = Path("scripts/data/sme_use_cases.json")
PACKAGES_DIR = Path("packages")
VENDOR = "SupraTix"
SCHEMA_INTAKE = "DISRUPTIVE_SME_INTAKE_V1"
SCHEMA_OUTPUT = "DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1"
SCHEMA_SHORTCUT = "DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1"
QUALITY_GATE = (
    "Return JSON only. Separate facts from assumptions, identify missing evidence, "
    "and recommend concrete next actions."
)
SHORTCUT_GATE = (
    "Return the managed SME shortcut response with explicit evidence gaps and "
    "owner-ready actions."
)
GUARDRAILS = [
    "Do not invent facts.",
    "Mark assumptions and evidence gaps.",
    "Prefer actions that can be started this week.",
    "Keep financial, legal, safety, and compliance advice reviewable by a responsible human.",
]
REPO_URL = "https://github.com/Supratix/AI-Workbench-.supra-Examples"


def contract(schema_version: str, fields: list[str], gate: str) -> dict:
    return {
        "schema_version": schema_version,
        "content_type": "application/json",
        "expects_json": True,
        "required_fields": fields,
        "json_schema": {
            "type": "object",
            "additionalProperties": True,
            "required": fields,
            "properties": {
                field: {"type": "string" if field in {"summary", "decision"} else "array"}
                for field in fields
            },
        },
        "quality_gate": gate,
        "evidence_policy": "no_invented_facts",
    }


def execution(label: str, enabled: bool) -> dict:
    return {
        "prompt_execution": {
            "execute_prompt": enabled,
            "selected": enabled,
            "mode": "manual_review" if enabled else "disabled",
            "requires_review": enabled,
            "label": label,
            "reason": "sme_example_package",
        }
    }


def column(key: str, title: str, icon: str, **extra) -> dict:
    col = {
        "key": key,
        "title": title,
        "column_kind": "step",
        "type": icon,
        "type_tool_input_dropdown": icon,
    }
    col.update(extra)
    return col


def build_package(spec: dict) -> dict:
    key = spec["key"]
    title = spec["title"]
    focus = spec["focus"]
    description = spec["description_en"]

    starter_text = {
        "schema": SCHEMA_INTAKE,
        "use_case": key,
        "focus": focus,
        "intake": (
            f"Business context: {spec['scenario']}\n"
            "Current situation: Inputs are incomplete, owners need an answer this week, "
            "and leadership wants visible assumptions.\n"
            "Known constraint: Do not invent facts; mark evidence gaps and human-review items."
        ),
        "guardrails": GUARDRAILS,
        "target_outputs": ["signal_map", "decision_plan", "execution_brief"],
    }
    starter_json = json.dumps(starter_text, ensure_ascii=False, separators=(",", ":"))
    assert len(starter_json) <= 4000, f"{key}: starter text exceeds importer limit"

    columns = [
        column(
            "business_context",
            "Business context",
            "fa-solid fa-file",
            tool_category="manual",
            tool="user_input",
            tooling=execution("Manual intake", False),
        ),
        column(
            "signal_map",
            "Signal map",
            "fa-solid fa-list-radio",
            input_from=["business_context"],
            tool_category="ai_tool",
            tool=f"{key}_signals",
            prompt=(
                f"Analyze the SME context for {focus}. Extract the most important facts, "
                "weak signals, constraints, assumptions, risks, and evidence gaps. Estimate "
                "likely impact qualitatively when numbers are missing. Do not invent facts. "
                "Return JSON only."
            ),
            tooling={
                **execution("Map signals", True),
                "output_contract": contract(
                    SCHEMA_OUTPUT,
                    ["summary", "signals", "constraints", "assumptions", "risks", "evidence_gaps"],
                    QUALITY_GATE,
                ),
            },
        ),
        column(
            "decision_plan",
            "Decision plan",
            "fa-solid fa-route",
            input_from=["business_context", "signal_map"],
            tool_category="ai_tool",
            tool=f"{key}_decision",
            prompt=(
                f"Create a pragmatic owner decision plan for {focus}. Include the recommended "
                "decision, rejected alternatives, first 72-hour actions, owners, metrics, and "
                "review triggers. Keep advice bounded by the provided facts and mark anything "
                "that needs finance, legal, safety, or compliance review. Return JSON only."
            ),
            tooling={
                **execution("Build plan", True),
                "output_contract": contract(
                    SCHEMA_OUTPUT,
                    ["summary", "decision", "actions", "metrics", "risks", "evidence_gaps"],
                    QUALITY_GATE,
                ),
            },
        ),
        column(
            "execution_brief",
            "Execution brief",
            "fa-solid fa-square-check",
            input_from=["business_context", "signal_map", "decision_plan"],
            tool_category="shortcut",
            tool=key,
            prompt=(
                "Use the intake, signal map, and decision plan to produce the managed SME "
                f"execution brief for {focus}. Respond in the same language as the user, keep "
                "assumptions visible, and make the next actions concrete."
            ),
            tooling={
                **execution("Generate execution brief", True),
                "output_contract": contract(
                    SCHEMA_SHORTCUT,
                    ["summary", "decision", "actions", "risks", "evidence_gaps"],
                    SHORTCUT_GATE,
                ),
            },
        ),
    ]

    workflows = [
        {
            "id": f"{key}_workflow",
            "title": f"{title} workflow",
            "description": description,
            "workflow_pipe": True,
            "steps": [
                {
                    "id": col["key"],
                    "title": col["title"],
                    "step_position": position,
                    "backlog": position == 0,
                    "auto_finished": False,
                    "auto_close": False,
                }
                for position, col in enumerate(columns)
            ],
        }
    ]

    workbench_title = f"{title} Desk"
    return {
        "key": key,
        "title": title,
        "description": description,
        "workbench_title": workbench_title,
        "schemaVersion": 1,
        "metadata": {
            "module_name": key,
            "vendor": VENDOR,
            "global_product_pk": "",
            "content_name": title,
            "content_description": description,
            "export_version": "1.0.0",
            "import_version": "1.0.0",
            "starter_rows": [
                {
                    "title": f"{title} starter",
                    "source_type": "business_context",
                    "external_urls": [],
                    "request": f"Paste the source context for {title}.",
                    "text": starter_json,
                }
            ],
            "commerce": {
                "business_model": "free_of_use",
                "product_typ": "workflows",
                "usage_unit": "cloud_credits",
                "quota": {"unit": "cloud_credits"},
            },
            "source_attribution": {
                "text": "AI Workbench .supra examples repository",
                "url": REPO_URL,
            },
        },
        "columns": columns,
        "workflows": workflows,
        "main_workbench": {
            "key": key,
            "title": title,
            "description": description,
            "workbench_title": workbench_title,
            "columns": columns,
            "workflows": workflows,
        },
    }


def render(pkg: dict) -> str:
    return json.dumps(pkg, indent=2, ensure_ascii=False) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--spec", default=None, help="Spec JSON path (default scripts/data/sme_use_cases.json)")
    parser.add_argument("--only", action="append", default=[], help="Only generate the given key(s)")
    parser.add_argument("--check", action="store_true", help="Do not write; fail if generated output differs")
    args = parser.parse_args()

    root = Path(args.root)
    spec_path = Path(args.spec) if args.spec else root / SPEC_PATH
    specs = json.loads(spec_path.read_text(encoding="utf-8"))
    if args.only:
        specs = [spec for spec in specs if spec["key"] in set(args.only)]

    changed = []
    for spec in specs:
        target = root / PACKAGES_DIR / spec["domain"] / f"{spec['key']}.supra"
        content = render(build_package(spec))
        if args.check:
            if not target.exists() or target.read_text(encoding="utf-8") != content:
                changed.append(str(target))
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8")

    if args.check:
        if changed:
            print("Generated packages are out of date:")
            for item in changed:
                print(f"- {item}")
            return 1
        print(f"Checked {len(specs)} generated packages")
        return 0
    print(f"Generated {len(specs)} packages under {root / PACKAGES_DIR}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
