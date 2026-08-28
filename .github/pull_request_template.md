## Summary

Describe the `.supra` package or documentation change.

## Validation

- [ ] `python3 scripts/validate_supra.py .` (standard + SupraWorx importer compatibility)
- [ ] `python3 scripts/new_sme_package.py .` (if a spec in `scripts/data/sme_use_cases.json` changed)
- [ ] `python3 scripts/generate_docs.py .`
- [ ] Shortcut IDs registered (`python3 scripts/render_sme_shortcut_specs.py . --registry`)

## Governance

- [ ] No secrets or sensitive customer data.
- [ ] Evidence gaps and assumptions are visible.
- [ ] Human review is enabled for consequential outputs.
