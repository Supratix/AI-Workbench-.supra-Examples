#!/usr/bin/env bash
# Copy the importable .supra packages (only the packages, flat) into a SupraWorx
# AI Workbench examples directory, e.g. mint/workbench/examples.
#
# The SupraWorx template gallery reads *.supra files directly from that
# directory (not from sub-folders) and its test-suite counts the bundled files
# (test_supra_catalog.py::test_all_bundled_supra_examples_pass_production_validation),
# so this script copies packages flat and prints the resulting count.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

if [[ $# -gt 0 ]]; then
  TARGET="$1"
elif [[ -n "${SUPRAWORX_EXAMPLES_DIR:-}" ]]; then
  TARGET="${SUPRAWORX_EXAMPLES_DIR}"
else
  echo "Usage: $0 /path/to/ai-workbench/examples [domain ...]" >&2
  echo "Or set SUPRAWORX_EXAMPLES_DIR before running this script." >&2
  exit 2
fi
shift || true

python3 "${REPO_ROOT}/scripts/validate_supra.py" "${REPO_ROOT}"

mkdir -p "${TARGET}"
if [[ $# -gt 0 ]]; then
  DOMAINS=("$@")
else
  DOMAINS=($(ls "${REPO_ROOT}/packages"))
fi

COPIED=0
for domain in "${DOMAINS[@]}"; do
  for pkg in "${REPO_ROOT}/packages/${domain}"/*.supra; do
    [[ -e "${pkg}" ]] || continue
    cp "${pkg}" "${TARGET}/"
    COPIED=$((COPIED + 1))
  done
done

TOTAL=$(ls "${TARGET}"/*.supra 2>/dev/null | wc -l | tr -d ' ')
echo "Installed ${COPIED} .supra packages into ${TARGET} (now ${TOTAL} *.supra files)."
echo "Reminder: update the expected file count in mint/workbench/test_supra_catalog.py if it asserts len(files)."
