from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_validate_examples() -> None:
    root = Path(__file__).resolve().parents[1]
    result = subprocess.run([sys.executable, str(root / "scripts" / "validate_supra.py"), str(root)], capture_output=True, text=True)
    assert result.returncode == 0, result.stderr
