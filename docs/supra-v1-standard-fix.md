# `.supra` v1 Standard Fix Playbook

Use this playbook when repairing an existing package so it conforms to the
canonical [`.supra` v1 standard](supra-v1-standard.md).

## Repair Flow

1. Read the package and confirm the intended business workflow.
2. Check the filename, top-level `key`, and `schemaVersion`.
3. Verify required metadata and starter rows.
4. Verify column order, `input_from` dependencies, and prompt execution settings.
5. Add or repair output contracts for every executable column.
6. Verify workflow steps reference existing columns in contiguous order.
7. Synchronize top-level package content with `main_workbench`.
8. Regenerate docs and manifest.
9. Run the acceptance gates.

## Required Gates

```bash
python3 scripts/validate_supra.py .
python3 scripts/generate_docs.py . --check
python3 -m py_compile scripts/validate_supra.py scripts/generate_docs.py
```

If pytest is available, also run:

```bash
python3 -m pytest tests
```

## Reviewer Shortcut

A repaired package is not finished until a reviewer can answer these questions:

- What source context enters the package?
- Which columns are manual and which are executable?
- Which prior outputs feed each executable column?
- What JSON shape must each executable column return?
- What evidence policy prevents unsupported claims?
- Which workflow steps require human review?
- Does `main_workbench` import the same package that the top level describes?
- Are generated docs and `examples_manifest.json` current?
- Are local paths, secrets, and user-specific references absent?

For the full normative description, use
[`docs/supra-v1-standard.md`](supra-v1-standard.md).
