# Contributing

Thanks for improving the AI Workbench `.supra` examples. The [repository guide](docs/repository-guide.en.md) ([Deutsch](docs/repository-guide.de.md)) explains the layout and generators in detail.

## Contribution flow

1. Decide the package type:
   - **Generated SME package**: add a spec to `scripts/data/sme_use_cases.json` and run `python3 scripts/new_sme_package.py .`. Never edit generated `.supra` files by hand.
   - **Hand-written package**: create `packages/<domain>/<key>.supra`, add its German description to `scripts/data/descriptions.de.json` and its domain to `scripts/data/domains.json`.
2. Keep package keys lowercase and underscore-separated; the key must equal the file stem.
3. Use only metadata fields the SupraWorx importer accepts (`python3 scripts/fix_supraworx_compat.py . --check`).
4. If the last step is a `shortcut` column, register the ID: `python3 scripts/render_sme_shortcut_specs.py . --registry` (and `--apply` it to SupraWorx).
5. Add or update starter rows with realistic but synthetic, non-sensitive sample data.
6. Run validation and regenerate docs:

   ```bash
   python3 scripts/validate_supra.py .
   python3 scripts/generate_docs.py .
   python3 -m pytest -q tests
   ```

7. Open a pull request with a short package summary and any governance considerations.

## Review checklist

- No secrets, credentials, customer data, or private URLs.
- Prompts require facts, assumptions, evidence gaps, and reviewable actions.
- Output contracts include required fields and JSON expectations.
- Human review remains enabled for consequential outputs.
- CI is green (validation, generator `--check` runs, docs `--check`, tests).
