# Schemas

This folder contains lightweight JSON Schema references for `.supra` example packages and their output contracts.

The local validator in `scripts/validate_supra.py` uses standard-library checks so CI does not need dependencies. These schemas are included for editor support, documentation, and future stricter validation.

## Files

- `supra-package.schema.json` — top-level `.supra` package shape.
- `supra-output-contract.schema.json` — reusable output contract shape for executable columns.

## Standard Guides

- [`../docs/supra-v1-standard.md`](../docs/supra-v1-standard.md) — canonical Markdown description of the `.supra` v1 standard.
- [`../docs/supra-v1-standard-fix.md`](../docs/supra-v1-standard-fix.md) — repair playbook for bringing packages into conformance.
