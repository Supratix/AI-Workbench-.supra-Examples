#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ $# -gt 0 ]]; then
  TARGET="$1"
elif [[ -n "${SUPRAWORX_EXAMPLES_DIR:-}" ]]; then
  TARGET="${SUPRAWORX_EXAMPLES_DIR}"
else
  echo "Usage: $0 /path/to/ai-workbench/examples" >&2
  echo "Or set SUPRAWORX_EXAMPLES_DIR before running this script." >&2
  exit 2
fi

mkdir -p "${TARGET}"
rsync -av --exclude .git "${REPO_ROOT}/" "${TARGET}/"
cd "${TARGET}"
python3 scripts/validate_supra.py .

echo "Installed .supra examples into ${TARGET}"
