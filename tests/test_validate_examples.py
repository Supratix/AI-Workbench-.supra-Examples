from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(script: str, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run([sys.executable, str(ROOT / "scripts" / script), str(ROOT), *args], capture_output=True, text=True)


def test_validate_examples() -> None:
    result = run("validate_supra.py")
    assert result.returncode == 0, result.stderr


def test_generated_docs_are_current() -> None:
    result = run("generate_docs.py", "--check")
    assert result.returncode == 0, result.stdout + result.stderr


def test_generated_sme_packages_are_current() -> None:
    result = run("new_sme_package.py", "--check")
    assert result.returncode == 0, result.stdout + result.stderr


def test_packages_are_supraworx_compatible() -> None:
    result = run("fix_supraworx_compat.py", "--check")
    assert result.returncode == 0, result.stdout + result.stderr


def test_manifest_matches_packages() -> None:
    manifest = json.loads((ROOT / "examples_manifest.json").read_text(encoding="utf-8"))
    files = sorted(ROOT.glob("packages/*/*.supra"))
    assert manifest["package_count"] == len(files)
    assert {entry["source"] for entry in manifest["packages"]} == {path.relative_to(ROOT).as_posix() for path in files}


def test_every_shortcut_id_is_registered_or_documented() -> None:
    registry = json.loads((ROOT / "scripts/data/supraworx_managed_shortcuts.json").read_text(encoding="utf-8"))
    known = set(registry["registered_shortcut_ids"]) | set(registry.get("legacy_unregistered_shortcut_ids", {})) | {"gpt"}
    for path in ROOT.glob("packages/*/*.supra"):
        pkg = json.loads(path.read_text(encoding="utf-8"))
        for col in pkg["columns"]:
            if col["tool_category"] == "shortcut":
                assert col["tool"] in known, f"{path.name}: {col['tool']}"
