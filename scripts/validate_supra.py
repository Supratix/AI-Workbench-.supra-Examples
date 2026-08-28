#!/usr/bin/env python3
"""Validate AI Workbench .supra example packages.

Two layers are checked for every ``packages/**/*.supra`` file:

1. The ``.supra`` v1 standard (docs/supra-v1-standard.md).
2. SupraWorx importer compatibility: the strict allow-lists, size limits and the
   managed-shortcut gate that ``mint/workbench`` applies on upload
   (docs/import-evaluation.en.md). Registered shortcut IDs are read from
   ``scripts/data/supraworx_managed_shortcuts.json``.

This script intentionally uses only the Python standard library so it can run in
local developer machines and GitHub Actions without dependency installation.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = [
    "key",
    "title",
    "description",
    "workbench_title",
    "schemaVersion",
    "metadata",
    "columns",
    "workflows",
    "main_workbench",
]
REQUIRED_METADATA = [
    "module_name",
    "vendor",
    "content_name",
    "content_description",
    "export_version",
    "import_version",
    "commerce",
]
REQUIRED_COLUMN = ["key", "title", "column_kind", "tool_category", "tool", "tooling"]
REQUIRED_PROMPT_EXECUTION = ["execute_prompt", "selected", "mode", "requires_review", "label"]
REQUIRED_CONTRACT = [
    "schema_version",
    "content_type",
    "expects_json",
    "required_fields",
    "json_schema",
    "quality_gate",
    "evidence_policy",
]
REQUIRED_WORKFLOW = ["id", "title", "description", "workflow_pipe", "steps"]
MAIN_WORKBENCH_FIELDS = ["key", "title", "description", "workbench_title"]
KEY_RE = re.compile(r"^[a-z0-9_]+$")
PACKAGES_DIR = "packages"
MANAGED_SHORTCUTS_FILE = Path("scripts/data/supraworx_managed_shortcuts.json")

# --- SupraWorx importer compatibility (mirrors mint/workbench/config_security.py) ---
SUPRAWORX_MAX_PAYLOAD_BYTES = 1024 * 1024
SUPRAWORX_MAX_COLUMNS = 64
SUPRAWORX_MAX_DESCRIPTION_LENGTH = 2000
SUPRAWORX_MAX_STARTER_ROWS = 200
SUPRAWORX_MAX_STARTER_TEXT_LENGTH = 4000
SUPRAWORX_MAX_OUTPUT_SCHEMA_BYTES = 12 * 1024
SUPRAWORX_MAX_EXTENSION_BYTES = 64 * 1024
SUPRAWORX_ALLOWED_ROOT = {
    "key", "title", "description", "workbench_title", "metadata", "columns",
    "workflows", "main_workbench", "schemaVersion", "exportedAt", "workbenchId",
}
SUPRAWORX_ALLOWED_METADATA = {
    "module_name", "modul_name", "vendor", "global_product_pk", "global_pim_product_nr",
    "content_name", "content_title", "content_description", "export_version",
    "import_version", "starter_rows", "source_attribution", "business_model", "commerce",
    "tenant_binding", "source_issue", "scoring", "account_universe", "last_config_review",
    "process", "governance", "operating_cadence",
}
SUPRAWORX_EXTENSION_OBJECT_KEYS = {"scoring", "account_universe", "process", "governance", "operating_cadence"}
SUPRAWORX_ALLOWED_STARTER_ROW = {"title", "source_type", "external_urls", "request", "text"}
SUPRAWORX_ALLOWED_SOURCE_ATTRIBUTION = {"text", "license", "license_url", "morphology", "citation", "doi", "url"}
SUPRAWORX_ALLOWED_COMMERCE = {
    "business_model", "product_pk", "product_slug", "product_typ", "product_global_product_nr",
    "product_global_pim_product_nr", "membership_pk", "membership_slug", "membership_title",
    "membership_global_product_nr", "membership_global_pim_product_nr", "currency", "usage_unit", "quota",
}
SUPRAWORX_TRUSTED_SHORTCUT_IDS = {"gpt", "contact.tasks.osc_people_contact_upsert"}

LOCAL_PATH_MARKERS = [
    "".join(parts)
    for parts in [
        ("/", "Users", "/"),
        ("supra", "worxv30"),
        ("mint", "/", "workbench", "/", "examples"),
    ]
]


def fail(path: Path, message: str, errors: list[str]) -> None:
    errors.append(f"{path}: {message}")


def non_empty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_key(path: Path, value: Any, label: str, errors: list[str]) -> None:
    if not non_empty_string(value):
        fail(path, f"{label} must be a non-empty string", errors)
    elif not KEY_RE.fullmatch(value):
        fail(path, f"{label} {value!r} must match ^[a-z0-9_]+$", errors)


def validate_contract(path: Path, col: dict[str, Any], errors: list[str]) -> None:
    contract = col.get("tooling", {}).get("output_contract")
    key = col.get("key")

    if col.get("tool_category") == "manual":
        if contract is not None:
            fail(path, f"manual column {key} must not define tooling.output_contract", errors)
        return

    if not isinstance(contract, dict):
        fail(path, f"column {key} is executable but has no tooling.output_contract", errors)
        return

    for contract_key in REQUIRED_CONTRACT:
        if contract_key not in contract:
            fail(path, f"column {key} output_contract missing {contract_key}", errors)

    if not non_empty_string(contract.get("schema_version")):
        fail(path, f"column {key} output_contract.schema_version must be a non-empty string", errors)
    if contract.get("content_type") != "application/json":
        fail(path, f"column {key} output_contract.content_type must be application/json", errors)
    if contract.get("expects_json") is not True:
        fail(path, f"column {key} output_contract.expects_json must be true", errors)
    if not non_empty_string(contract.get("quality_gate")):
        fail(path, f"column {key} output_contract.quality_gate must be a non-empty string", errors)
    if not non_empty_string(contract.get("evidence_policy")):
        fail(path, f"column {key} output_contract.evidence_policy must be a non-empty string", errors)

    required = contract.get("required_fields")
    if not isinstance(required, list) or not required or not all(non_empty_string(item) for item in required):
        fail(path, f"column {key} output_contract.required_fields must be a non-empty string list", errors)
        required = []

    json_schema = contract.get("json_schema")
    if not isinstance(json_schema, dict):
        fail(path, f"column {key} output_contract.json_schema must be an object", errors)
        return
    if json_schema.get("type") != "object":
        fail(path, f"column {key} json_schema.type must be object", errors)

    schema_required = json_schema.get("required")
    if not isinstance(schema_required, list):
        fail(path, f"column {key} json_schema.required must be a list", errors)
        schema_required = []
    missing_required = [field for field in required if field not in schema_required]
    if missing_required:
        fail(path, f"column {key} json_schema.required missing {missing_required}", errors)

    properties = json_schema.get("properties")
    if not isinstance(properties, dict):
        fail(path, f"column {key} json_schema.properties must be an object", errors)
        properties = {}
    missing_properties = [field for field in required if field not in properties]
    if missing_properties:
        fail(path, f"column {key} json_schema.properties missing {missing_properties}", errors)


def validate_prompt_execution(path: Path, col: dict[str, Any], errors: list[str]) -> None:
    key = col.get("key")
    pe = col.get("tooling", {}).get("prompt_execution")
    if not isinstance(pe, dict):
        fail(path, f"column {key} missing tooling.prompt_execution", errors)
        return
    for pe_key in REQUIRED_PROMPT_EXECUTION:
        if pe_key not in pe:
            fail(path, f"column {key} prompt_execution missing {pe_key}", errors)
    for bool_key in ["execute_prompt", "selected", "requires_review"]:
        if not isinstance(pe.get(bool_key), bool):
            fail(path, f"column {key} prompt_execution.{bool_key} must be boolean", errors)
    if not non_empty_string(pe.get("label")):
        fail(path, f"column {key} prompt_execution.label must be a non-empty string", errors)

    if col.get("tool_category") == "manual":
        if pe.get("execute_prompt") is not False:
            fail(path, f"manual column {key} prompt_execution.execute_prompt must be false", errors)
        if pe.get("requires_review") is not False:
            fail(path, f"manual column {key} prompt_execution.requires_review must be false", errors)
        if pe.get("mode") != "disabled":
            fail(path, f"manual column {key} prompt_execution.mode must be disabled", errors)
    else:
        if pe.get("execute_prompt") is not True:
            fail(path, f"executable column {key} prompt_execution.execute_prompt must be true", errors)
        if pe.get("selected") is not True:
            fail(path, f"executable column {key} prompt_execution.selected must be true", errors)
        if pe.get("requires_review") is not True:
            fail(path, f"executable column {key} prompt_execution.requires_review must be true", errors)


LEGACY_EXCEPTIONS: dict[str, str] = {}
WARNINGS: list[str] = []


def load_managed_shortcuts(root: Path) -> set[str]:
    """Return shortcut IDs registered in SupraWorx (mint/shortcuts sme_shortcuts.py)."""
    target = root / MANAGED_SHORTCUTS_FILE
    if not target.exists():
        return set()
    data = json.loads(target.read_text(encoding="utf-8"))
    LEGACY_EXCEPTIONS.update(data.get("legacy_unregistered_shortcut_ids", {}))
    return set(data.get("registered_shortcut_ids", [])) | SUPRAWORX_TRUSTED_SHORTCUT_IDS


def validate_supraworx_compat(path: Path, raw: str, data: dict[str, Any], managed: set[str], errors: list[str]) -> None:
    """Check the strict allow-lists and gates of the SupraWorx .supra importer."""
    prefix = "supraworx"
    if len(raw.encode("utf-8")) > SUPRAWORX_MAX_PAYLOAD_BYTES:
        fail(path, f"{prefix}: payload exceeds 1 MiB upload limit", errors)
    unknown_root = sorted(set(data) - SUPRAWORX_ALLOWED_ROOT)
    if unknown_root:
        fail(path, f"{prefix}: unknown top-level fields rejected by importer: {unknown_root}", errors)
    if len(str(data.get("description") or "")) > SUPRAWORX_MAX_DESCRIPTION_LENGTH:
        fail(path, f"{prefix}: description longer than {SUPRAWORX_MAX_DESCRIPTION_LENGTH} characters", errors)

    metadata = data.get("metadata")
    if isinstance(metadata, dict):
        unknown_meta = sorted(set(metadata) - SUPRAWORX_ALLOWED_METADATA)
        if unknown_meta:
            fail(path, f"{prefix}: metadata fields rejected by importer: {unknown_meta}", errors)
        for key in SUPRAWORX_EXTENSION_OBJECT_KEYS & set(metadata):
            value = metadata.get(key)
            if not isinstance(value, dict):
                fail(path, f"{prefix}: metadata.{key} must be an object", errors)
            elif len(json.dumps(value, ensure_ascii=False).encode("utf-8")) > SUPRAWORX_MAX_EXTENSION_BYTES:
                fail(path, f"{prefix}: metadata.{key} exceeds 64 KiB", errors)
        attribution = metadata.get("source_attribution")
        if isinstance(attribution, dict):
            unknown_attr = sorted(set(attribution) - SUPRAWORX_ALLOWED_SOURCE_ATTRIBUTION)
            if unknown_attr:
                fail(path, f"{prefix}: source_attribution fields rejected by importer: {unknown_attr}", errors)
        commerce = metadata.get("commerce")
        if isinstance(commerce, dict):
            unknown_commerce = sorted(set(commerce) - SUPRAWORX_ALLOWED_COMMERCE)
            if unknown_commerce:
                fail(path, f"{prefix}: commerce fields rejected by importer: {unknown_commerce}", errors)
        starter_rows = metadata.get("starter_rows")
        if isinstance(starter_rows, list):
            if len(starter_rows) > SUPRAWORX_MAX_STARTER_ROWS:
                fail(path, f"{prefix}: more than {SUPRAWORX_MAX_STARTER_ROWS} starter rows", errors)
            for starter in starter_rows:
                if not isinstance(starter, dict):
                    continue
                unknown_starter = sorted(set(starter) - SUPRAWORX_ALLOWED_STARTER_ROW)
                if unknown_starter:
                    fail(path, f"{prefix}: starter row fields rejected by importer: {unknown_starter}", errors)
                if len(str(starter.get("text") or "")) > SUPRAWORX_MAX_STARTER_TEXT_LENGTH:
                    fail(path, f"{prefix}: starter row text longer than {SUPRAWORX_MAX_STARTER_TEXT_LENGTH} characters", errors)

    columns = data.get("columns")
    if isinstance(columns, list):
        if len(columns) > SUPRAWORX_MAX_COLUMNS:
            fail(path, f"{prefix}: more than {SUPRAWORX_MAX_COLUMNS} columns", errors)
        for col in columns:
            if not isinstance(col, dict):
                continue
            contract = col.get("tooling", {}).get("output_contract") if isinstance(col.get("tooling"), dict) else None
            if isinstance(contract, dict) and isinstance(contract.get("json_schema"), dict):
                schema_bytes = len(json.dumps(contract["json_schema"], ensure_ascii=False).encode("utf-8"))
                if schema_bytes > SUPRAWORX_MAX_OUTPUT_SCHEMA_BYTES:
                    fail(path, f"{prefix}: column {col.get('key')} json_schema exceeds 12 KiB", errors)
            if col.get("tool_category") == "shortcut" and managed:
                tool = str(col.get("tool") or "").strip()
                if tool in LEGACY_EXCEPTIONS:
                    WARNINGS.append(f"{path}: {prefix}: shortcut {tool!r} is a documented exception - {LEGACY_EXCEPTIONS[tool]}")
                elif tool not in managed:
                    fail(
                        path,
                        f"{prefix}: shortcut column {col.get('key')} references unregistered shortcut {tool!r}; "
                        "file upload would be rejected (register it in mint/shortcuts sme_shortcuts.py or "
                        "add it to scripts/data/supraworx_managed_shortcuts.json)",
                        errors,
                    )


def validate_package(path: Path, managed: set[str] | None = None) -> list[str]:
    errors: list[str] = []
    try:
        raw = path.read_text(encoding="utf-8")
        data = json.loads(raw)
    except Exception as exc:
        return [f"{path}: invalid JSON: {exc}"]

    for marker in LOCAL_PATH_MARKERS:
        if marker in raw:
            fail(path, f"must not reference local machine path marker {marker!r}", errors)

    if not isinstance(data, dict):
        return [f"{path}: top-level document must be an object"]
    validate_supraworx_compat(path, raw, data, managed or set(), errors)
    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            fail(path, f"missing top-level key {key}", errors)
    if errors:
        return errors

    validate_key(path, data.get("key"), "top-level key", errors)
    for text_key in ["title", "description", "workbench_title"]:
        if not non_empty_string(data.get(text_key)):
            fail(path, f"{text_key} must be a non-empty string", errors)
    if data.get("key") != path.stem:
        fail(path, f"top-level key {data.get('key')!r} should match filename stem {path.stem!r}", errors)
    if data.get("schemaVersion") != 1:
        fail(path, "schemaVersion must be the integer 1", errors)

    metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        fail(path, "metadata must be an object", errors)
    else:
        for key in REQUIRED_METADATA:
            if key not in metadata:
                fail(path, f"metadata missing {key}", errors)
        for meta_key in ["module_name", "vendor", "content_name", "content_description", "export_version", "import_version"]:
            if meta_key in metadata and not non_empty_string(metadata.get(meta_key)):
                fail(path, f"metadata.{meta_key} must be a non-empty string", errors)
        aligned = {
            "module_name": "key",
            "content_name": "title",
            "content_description": "description",
        }
        for meta_key, package_key in aligned.items():
            if metadata.get(meta_key) != data.get(package_key):
                fail(path, f"metadata.{meta_key} must match top-level {package_key}", errors)
        if not isinstance(metadata.get("commerce"), dict):
            fail(path, "metadata.commerce must be an object", errors)
        starter_rows = metadata.get("starter_rows", [])
        if not isinstance(starter_rows, list):
            fail(path, "metadata.starter_rows must be a list when present", errors)
            starter_rows = []
        for starter in starter_rows:
            if not isinstance(starter, dict):
                fail(path, "metadata.starter_rows entries must be objects", errors)
                continue
            if not non_empty_string(starter.get("title")):
                fail(path, "metadata.starter_rows entries must include a non-empty title", errors)
            try:
                starter_text = json.loads(starter.get("text", ""))
            except Exception as exc:
                fail(path, f"starter row {starter.get('title', '<unnamed>')} text is not JSON: {exc}", errors)
                continue
            if not isinstance(starter_text, dict):
                fail(path, f"starter row {starter.get('title', '<unnamed>')} text must decode to an object", errors)

    columns = data.get("columns")
    if not isinstance(columns, list) or not columns:
        fail(path, "columns must be a non-empty list", errors)
        return errors
    column_keys: set[str] = set()
    for col in columns:
        if not isinstance(col, dict):
            fail(path, "each column must be an object", errors)
            continue
        for key in REQUIRED_COLUMN:
            if key not in col:
                fail(path, f"column missing {key}", errors)

        key = col.get("key")
        validate_key(path, key, "column key", errors)
        if key in column_keys:
            fail(path, f"duplicate column key {key}", errors)
        if isinstance(key, str):
            column_keys.add(key)

        if not non_empty_string(col.get("title")):
            fail(path, f"column {key} title must be a non-empty string", errors)
        if col.get("column_kind") != "step":
            fail(path, f"column {key} column_kind must be step", errors)
        if col.get("tool_category") not in {"manual", "ai_tool", "shortcut"}:
            fail(path, f"column {key} tool_category must be manual, ai_tool, or shortcut", errors)
        if not non_empty_string(col.get("tool")):
            fail(path, f"column {key} tool must be a non-empty string", errors)
        if not isinstance(col.get("tooling"), dict):
            fail(path, f"column {key} tooling must be an object", errors)

        input_from = col.get("input_from", [])
        if input_from is None:
            input_from = []
        if not isinstance(input_from, list):
            fail(path, f"column {key} input_from must be a list when present", errors)
            input_from = []
        if col.get("tool_category") != "manual" and not input_from:
            fail(path, f"executable column {key} input_from must name upstream columns", errors)
        for input_key in input_from:
            if input_key not in column_keys:
                fail(path, f"column {key} input_from references {input_key!r} before it exists", errors)

        validate_prompt_execution(path, col, errors)
        validate_contract(path, col, errors)

    workflows = data.get("workflows")
    if not isinstance(workflows, list) or not workflows:
        fail(path, "workflows must be a non-empty list", errors)
        workflows = []
    for workflow in workflows:
        if not isinstance(workflow, dict):
            fail(path, "workflow must be an object", errors)
            continue
        for key in REQUIRED_WORKFLOW:
            if key not in workflow:
                fail(path, f"workflow missing {key}", errors)
        if not non_empty_string(workflow.get("id")):
            fail(path, "workflow id must be a non-empty string", errors)
        if not non_empty_string(workflow.get("title")):
            fail(path, f"workflow {workflow.get('id')} title must be a non-empty string", errors)
        if not non_empty_string(workflow.get("description")):
            fail(path, f"workflow {workflow.get('id')} description must be a non-empty string", errors)
        if workflow.get("workflow_pipe") is not True:
            fail(path, f"workflow {workflow.get('id')} workflow_pipe must be true", errors)
        steps = workflow.get("steps")
        if not isinstance(steps, list) or not steps:
            fail(path, f"workflow {workflow.get('id')} steps must be a non-empty list", errors)
            continue
        positions = []
        for step in steps:
            if not isinstance(step, dict):
                fail(path, f"workflow {workflow.get('id')} step must be an object", errors)
                continue
            step_id = step.get("id")
            if step_id not in column_keys:
                fail(path, f"workflow {workflow.get('id')} references unknown step {step_id!r}", errors)
            if not non_empty_string(step.get("title")):
                fail(path, f"workflow {workflow.get('id')} step {step_id!r} title must be a non-empty string", errors)
            if not isinstance(step.get("step_position"), int):
                fail(path, f"workflow {workflow.get('id')} step {step_id!r} step_position must be an integer", errors)
            positions.append(step.get("step_position"))
        if positions != list(range(len(positions))):
            fail(path, f"workflow {workflow.get('id')} step_position values should be contiguous from 0", errors)

    main = data.get("main_workbench")
    if not isinstance(main, dict):
        fail(path, "main_workbench must be an object", errors)
    else:
        for field in MAIN_WORKBENCH_FIELDS:
            if main.get(field) != data.get(field):
                fail(path, f"main_workbench.{field} must match top-level {field}", errors)
        if main.get("columns") != columns:
            fail(path, "main_workbench.columns must exactly mirror top-level columns", errors)
        if main.get("workflows") != workflows:
            fail(path, "main_workbench.workflows must exactly mirror top-level workflows", errors)

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate .supra packages")
    parser.add_argument("root", nargs="?", default=".", help="Repository/examples root")
    args = parser.parse_args()
    root = Path(args.root)
    packages_dir = root / PACKAGES_DIR
    files = sorted(packages_dir.rglob("*.supra")) if packages_dir.is_dir() else sorted(root.glob("*.supra"))
    if not files:
        print(f"No .supra files found in {root}", file=sys.stderr)
        return 2
    managed = load_managed_shortcuts(root)
    errors: list[str] = []
    seen_keys: dict[str, Path] = {}
    for path in files:
        errors.extend(validate_package(path, managed))
        if path.stem in seen_keys:
            errors.append(f"{path}: duplicate package key also found at {seen_keys[path.stem]}")
        seen_keys.setdefault(path.stem, path)
    for warning in WARNINGS:
        print(f"warning: {warning}", file=sys.stderr)
    if errors:
        print(".supra validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(files)} .supra packages in {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
