from __future__ import annotations

import json
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]
GOLDEN_DIR = ROOT / "golden_outputs"
PACKAGE_FILES = {
    "sme_thirteen_week_cash_forecast": ROOT / "packages/finance_cash/sme_thirteen_week_cash_forecast.supra",
    "field_service_maintenance_report": ROOT / "packages/operations_production/field_service_maintenance_report.supra",
}
STEP_KEYS = {
    ("field_service_maintenance_report", "evidence"): "transcribed_evidence",
    ("field_service_maintenance_report", "maintenance_report"): "maintenance_report",
    ("field_service_maintenance_report", "customer_summary"): "customer_summary",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def test_golden_outputs_match_package_contracts() -> None:
    sample_paths = sorted(GOLDEN_DIR.glob("*/*.json"))
    assert sample_paths, "expected committed golden output examples"

    for sample_path in sample_paths:
        package_key = sample_path.parent.name
        step_key = STEP_KEYS.get((package_key, sample_path.stem), sample_path.stem)
        package = load_json(PACKAGE_FILES[package_key])
        column = next(column for column in package["columns"] if column["key"] == step_key)
        contract = column["tooling"]["output_contract"]
        schema = contract["json_schema"]
        sample = load_json(sample_path)

        assert set(contract["required_fields"]) == set(schema["required"])
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema)
        validator.validate(sample)

        # Prove the contract rejects an otherwise valid output when a required
        # root field is missing, rather than only checking the happy path.
        invalid_sample = dict(sample)
        invalid_sample.pop(contract["required_fields"][0])
        errors = list(validator.iter_errors(invalid_sample))
        assert any(error.validator == "required" for error in errors), sample_path
