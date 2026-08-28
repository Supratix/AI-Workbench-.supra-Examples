# SupraWorx v3.0 Import Evaluation

This document records how the packages in this repository behave when they are imported into SupraWorx v3.0 (`mint/workbench`, AI Workbench). It was produced by running the production importer code paths against every package and is the basis for the SupraWorx compatibility layer in `scripts/validate_supra.py`.

Evaluated code (SupraWorx v3.0, `mint/`):

| Component | File | Role |
| --- | --- | --- |
| Strict payload validator | `workbench/config_security.py` → `parse_workbench_example()` | Used by file upload **and** by the local template gallery. Rejects unknown fields (`reject_unknown=True`). |
| File upload view | `workbench/views.py` → `ai_workbench_supra_file_import()` | Decrypts, validates, then applies the shortcut gate `_validate_uploaded_supra_shortcut_references()`. |
| Template gallery | `workbench/views.py` → `_iter_local_workbench_supra_templates()` | Lists `*.supra` files in `workbench/examples/` (flat, no sub-folders); files that fail validation are silently skipped. |
| Workbench builder | `workbench/views.py` → `_apply_workbench_node_to_timeline()` | Creates one `AutomationSettings` per column; shortcut columns are bound via `_ensure_imported_shared_shortcut()`. |
| Managed SME shortcuts | `shortcuts/services/sme_shortcuts.py` | Registry of shortcut IDs; every ID is wired to `sme_shortcut_task` in `shortcuts/tasks.py::SHORTCUT_TASKS`. |
| Catalog test | `workbench/test_supra_catalog.py` | Asserts every bundled example passes `parse_workbench_example` and asserts the bundled file count (`63` at the time of writing). |

## Method

1. `parse_workbench_example()` and its dependencies (`config_security.py`, `rules.py`, `constants.py`, `supra_package.py`, `shortcuts/services/ocr.py`, `sme_shortcuts.py`) were executed unchanged against every `.supra` file, with Django/ORM imports stubbed (no database needed for validation).
2. The upload shortcut gate was replayed: a `shortcut` column is accepted only if its `tool` is a managed SME shortcut (`get_sme_shortcut_definition()`), the generic `gpt` prompt shortcut, or a trusted upload shortcut. Active shared shortcuts that only exist in a specific tenant database cannot be evaluated offline and are treated as unregistered.
3. Results were verified again after the fixes described below.

## Results

| Stage | Before | After |
| --- | --- | --- |
| Packages | 47 | 147 (47 existing + 100 new SME packages) |
| Pass `parse_workbench_example()` (strict validator) | **0 / 47** | **147 / 147** |
| Pass file-upload shortcut gate | 0 / 47 | **145 / 147** (2 documented exceptions) |
| Visible in the local template gallery after install | 0 / 47 | 147 / 147 |

### Finding 1 — `metadata.github_example` blocked every package (fixed)

Every package carried a `metadata.github_example` object. The importer's metadata allow-list (`WORKBENCH_EXAMPLE_ALLOWED_METADATA`) does not contain it, so `_canonicalize_workbench_metadata()` raised *"metadata enthält unbekannte Felder."* for all 47 packages. Consequences: file upload returned HTTP 400, and the gallery silently skipped the files (the copies already living in `workbench/examples/` had this key removed by hand, which is why they worked there).

Fix: `scripts/fix_supraworx_compat.py` removes `github_example` and adds the allowed `metadata.source_attribution` (`text`, `url`) instead. The validator now enforces the importer allow-lists for root, metadata, `source_attribution`, `commerce` and starter rows, so this cannot regress.

### Finding 2 — extension metadata in `workforce_intelligence_platform` (fixed)

`metadata.deployment`, `metadata.integrations` and `metadata.supraagents` are not allowed either. The importer accepts five free-form extension objects (`scoring`, `account_universe`, `process`, `governance`, `operating_cadence`, max 64 KiB each). The three blocks were moved to `metadata.process.{deployment,integrations,supraagents}` without loss of information.

### Finding 3 — unregistered shortcut IDs are rejected on upload (fixed by registration)

The upload view rejects a package whose `shortcut` column references a shortcut that is neither managed nor an active shared shortcut on the instance ("*Die .supra-Datei verweist auf den nicht freigegebenen Shortcut …*"). Only 35 of the 47 packages used a registered ID. The 100 new packages introduce 100 new IDs (`sme_thirteen_week_cash_forecast`, …).

Fix: the IDs are registered as managed SME shortcuts. `scripts/render_sme_shortcut_specs.py` renders the entries for `_DISRUPTIVE_SME_SHORTCUT_SPECS` in `mint/shortcuts/services/sme_shortcuts.py` from `scripts/data/sme_use_cases.json` plus `scripts/data/sme_registry_extras.json` (the 10 legacy IDs that are pure LLM briefs: `sme_esg_sustainability_copilot`, `linkedin_extreme_engagement_posting`, `aevalley_grant_tender_url_condenser`, `kmu_tender_factory`, `mint_study_planning`, the four `data_analytics_*` packages and `field_service_maintenance_report`). Because `SHORTCUT_TASKS` in `shortcuts/tasks.py` maps every definition to `sme_shortcut_task`, **no change to `tasks.py` is needed** — registration alone makes the shortcut importable and executable. The block is delimited by marker comments so it can be regenerated idempotently:

```bash
python3 scripts/render_sme_shortcut_specs.py . --apply ../supraworxv30/mint/shortcuts/services/sme_shortcuts.py
python3 scripts/render_sme_shortcut_specs.py . --registry   # refresh scripts/data/supraworx_managed_shortcuts.json
```

After applying the patch the registry holds 146 managed SME shortcut definitions (36 existing + 110 generated), all with unique IDs.

Documented exceptions (validator prints a warning, upload is rejected, gallery install works):

| Package | Shortcut | Why not registered |
| --- | --- | --- |
| `lieferschein_inventory` | `lieferschein_inventory` | Needs the internal product tasks (delivery-note extractor / inventory updater), not an LLM brief. |
| `workforce_intelligence_platform` | `workforce_intelligence_action_receipts` | Needs a dedicated action-receipt task. |

### Finding 4 — the install script polluted `workbench/examples/` (fixed)

`scripts/install_to_supraworx_examples.sh` used `rsync` of the whole repository, which copied README, docs, schemas and scripts into the examples folder. The gallery only reads `*.supra` at the top level, and `test_supra_catalog.py` asserts an exact file count. The script now copies only `packages/**/*.supra` (flat, optionally per domain) and prints the resulting count so the test assertion can be updated deliberately.

### Finding 5 — limits worth knowing (no violations)

| Limit | Value | Repository status |
| --- | --- | --- |
| Payload size | 1 MiB | Largest package 97 KB |
| Columns per workbench | 64 | Max 17 |
| Description length | 2000 chars | OK |
| Starter rows / starter text | 200 rows / 4000 chars | Longest starter text < 1500 chars |
| Output-contract `json_schema` | 12 KiB | OK |
| Extension objects | 64 KiB | OK |
| Column `key` | no dotted segments (`test_supra_rejects_dotted_semantic_key_segments`) | OK |

All limits are now checked by `scripts/validate_supra.py`.

### Observations (no change made)

* `ai_tool` columns use package-specific tool slugs such as `sme_x_signals`. The importer stores the slug as given (`_resolve_imported_ai_tool_slug()` only rewrites OpenAI-looking references to the OpenAI product slug). At run time the column executes through the tenant's configured GenAI tool; this is the same pattern as the 35 SME packages already bundled with SupraWorx, so behaviour is unchanged.
* Prompts that declare `output_contract.expects_json = true` are automatically run in JSON mode with the contract appended to the prompt (`_apply_declared_json_output_contract()`), which is why every executable column in the generated packages carries a contract.
* After a successful upload SupraWorx queues automatic execution of the starter rows (`_schedule_imported_workbench_execution()`); columns with `requires_review = true` still stop for review.
* The `workbench/examples/` folder in SupraWorx contains 63 files today. Installing all 147 packages there requires updating the count in `test_supra_catalog.py`.

## Reproducing the evaluation

The compatibility checks are part of the normal validation run:

```bash
python3 scripts/validate_supra.py .          # standard + importer allow-lists + shortcut gate
python3 scripts/fix_supraworx_compat.py . --check
```

To replay the production validator itself, run from a SupraWorx checkout:

```bash
cd supraworxv30/mint
python -m pytest workbench/test_supra_catalog.py -k production_validation
```
