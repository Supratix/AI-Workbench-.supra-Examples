# Changelog

## 0.2.0

- Restructured the repository: packages now live under `packages/<domain>/` in 12 SME domain folders, generated docs under `docs/packages/`, each domain has a generated README index.
- Added 100 generated SME packages (`scripts/data/sme_use_cases.json` + `scripts/new_sme_package.py`), bringing the catalog to 147 packages with English and German documentation.
- Evaluated every package against the SupraWorx v3.0 (`mint/workbench`) importer and fixed the blockers: removed the non-allow-listed `metadata.github_example`, moved extension metadata into `metadata.process`, registered shortcut IDs (`scripts/render_sme_shortcut_specs.py`). See `docs/import-evaluation.{en,de}.md`.
- `scripts/validate_supra.py` now enforces SupraWorx importer compatibility (allow-lists, size limits, managed-shortcut gate) in addition to the `.supra` v1 standard.
- `scripts/install_to_supraworx_examples.sh` copies only `.supra` files (flat, optionally per domain) instead of the whole repository.
- Added `README.de.md`, `docs/repository-guide.{en,de}.md`, `examples_manifest.json` schema V2 (domain + path), CI checks for generator drift, and pytest coverage for the manifest and shortcut registry.

## 0.1.0

- Initial GitHub-ready `.supra` example repository scaffold.
- Added example package catalog, bilingual generated docs, schemas, validation scripts, GitHub workflow, and diagram assets.
