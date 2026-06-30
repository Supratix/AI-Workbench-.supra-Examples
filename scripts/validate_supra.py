#!/usr/bin/env python3
"""Validate AI Workbench .supra example packages.

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


def validate_package(path: Path) -> list[str]:
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
    files = sorted(root.glob("*.supra"))
    if not files:
        print(f"No .supra files found in {root}", file=sys.stderr)
        return 2
    errors: list[str] = []
    for path in files:
        errors.extend(validate_package(path))
    if errors:
        print(".supra validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(files)} .supra packages in {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
