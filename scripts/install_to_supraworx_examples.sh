#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-/Users/tobiasgoecke/supraworxv30/mint/workbench/examples}"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

mkdir -p "${TARGET}"
rsync -av --exclude .git "${REPO_ROOT}/" "${TARGET}/"
cd "${TARGET}"
python3 scripts/validate_supra.py .

echo "Installed .supra examples into ${TARGET}"
