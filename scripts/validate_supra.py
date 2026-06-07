#!/usr/bin/env python3
"""Validate AI Workbench .supra example packages.

This script intentionally uses only the Python standard library so it can run in
local developer machines and GitHub Actions without dependency installation.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_TOP_LEVEL = ["key", "title", "description", "workbench_title", "schemaVersion", "metadata", "columns", "workflows", "main_workbench"]
REQUIRED_METADATA = ["module_name", "vendor", "content_name", "content_description", "export_version", "import_version", "commerce"]
REQUIRED_COLUMN = ["key", "title", "column_kind", "tool_category", "tool", "tooling"]
REQUIRED_PROMPT_EXECUTION = ["execute_prompt", "selected", "mode", "requires_review", "label"]


def fail(path: Path, message: str, errors: list[str]) -> None:
    errors.append(f"{path}: {message}")


def validate_contract(path: Path, col: dict[str, Any], errors: list[str]) -> None:
    contract = col.get("tooling", {}).get("output_contract")
    if col.get("tool_category") == "manual":
        return
    if not isinstance(contract, dict):
        fail(path, f"column {col.get('key')} is executable but has no tooling.output_contract", errors)
        return
    for key in ["schema_version", "content_type", "expects_json", "required_fields", "json_schema", "quality_gate", "evidence_policy"]:
        if key not in contract:
            fail(path, f"column {col.get('key')} output_contract missing {key}", errors)
    required = contract.get("required_fields", [])
    json_schema = contract.get("json_schema", {})
    if not isinstance(required, list) or not required:
        fail(path, f"column {col.get('key')} output_contract.required_fields must be a non-empty list", errors)
    if isinstance(json_schema, dict):
        schema_required = json_schema.get("required", [])
        missing = [field for field in required if field not in schema_required]
        if missing:
            fail(path, f"column {col.get('key')} json_schema.required missing {missing}", errors)


def validate_package(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        return [f"{path}: invalid JSON: {exc}"]

    if not isinstance(data, dict):
        return [f"{path}: top-level document must be an object"]
    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            fail(path, f"missing top-level key {key}", errors)
    if errors:
        return errors

    if data["key"] != path.stem:
        fail(path, f"top-level key {data['key']!r} should match filename stem {path.stem!r}", errors)
    if not isinstance(data.get("schemaVersion"), int):
        fail(path, "schemaVersion must be an integer", errors)

    metadata = data.get("metadata", {})
    if not isinstance(metadata, dict):
        fail(path, "metadata must be an object", errors)
    else:
        for key in REQUIRED_METADATA:
            if key not in metadata:
                fail(path, f"metadata missing {key}", errors)
        for starter in metadata.get("starter_rows", []):
            try:
                json.loads(starter.get("text", ""))
            except Exception as exc:
                fail(path, f"starter row {starter.get('title', '<unnamed>')} text is not JSON: {exc}", errors)

    columns = data.get("columns")
    if not isinstance(columns, list) or not columns:
        fail(path, "columns must be a non-empty list", errors)
        return errors
    column_keys = set()
    for col in columns:
        if not isinstance(col, dict):
            fail(path, "each column must be an object", errors)
            continue
        for key in REQUIRED_COLUMN:
            if key not in col:
                fail(path, f"column missing {key}", errors)
        key = col.get("key")
        if key in column_keys:
            fail(path, f"duplicate column key {key}", errors)
        column_keys.add(key)
        pe = col.get("tooling", {}).get("prompt_execution")
        if not isinstance(pe, dict):
            fail(path, f"column {key} missing tooling.prompt_execution", errors)
        else:
            for pe_key in REQUIRED_PROMPT_EXECUTION:
                if pe_key not in pe:
                    fail(path, f"column {key} prompt_execution missing {pe_key}", errors)
        for input_key in col.get("input_from", []):
            if input_key not in column_keys:
                fail(path, f"column {key} input_from references {input_key!r} before it exists", errors)
        validate_contract(path, col, errors)

    workflows = data.get("workflows", [])
    if not isinstance(workflows, list):
        fail(path, "workflows must be a list", errors)
    for workflow in workflows:
        if not isinstance(workflow, dict):
            fail(path, "workflow must be an object", errors)
            continue
        steps = workflow.get("steps", [])
        if not isinstance(steps, list):
            fail(path, f"workflow {workflow.get('id')} steps must be a list", errors)
            continue
        positions = []
        for step in steps:
            step_id = step.get("id")
            if step_id not in column_keys:
                fail(path, f"workflow {workflow.get('id')} references unknown step {step_id!r}", errors)
            positions.append(step.get("step_position"))
        if positions != list(range(len(positions))):
            fail(path, f"workflow {workflow.get('id')} step_position values should be contiguous from 0", errors)

    main = data.get("main_workbench", {})
    if isinstance(main, dict):
        main_columns = main.get("columns", [])
        if len(main_columns) != len(columns):
            fail(path, "main_workbench.columns should mirror top-level columns", errors)
    else:
        fail(path, "main_workbench must be an object", errors)
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
