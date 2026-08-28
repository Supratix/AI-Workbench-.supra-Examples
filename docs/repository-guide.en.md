# Repository Guide

How this repository is organised, how packages are generated, and how to get them into SupraWorx AI Workbench.

## Layout

```text
.
├── packages/                       # 147 importable .supra packages, one folder per domain
│   ├── finance_cash/               #   each folder has a generated README.md index
│   ├── sales_growth/
│   ├── marketing_content/
│   ├── customer_service/
│   ├── operations_production/
│   ├── supply_chain_procurement/
│   ├── people_hr/
│   ├── compliance_risk_esg/
│   ├── it_digital_data/
│   ├── strategy_analytics/
│   ├── public_funding_tenders/
│   └── education_learning/
├── docs/
│   ├── README.md                   # Full catalog grouped by domain (EN/DE)
│   ├── packages/<key>.{en,de}.md   # Generated per-package documentation
│   ├── import-evaluation.{en,de}.md
│   ├── repository-guide.{en,de}.md
│   ├── supra-v1-standard.md / supra-v1-standard-fix.md
│   └── assets/                     # SVG/PNG diagrams
├── scripts/
│   ├── validate_supra.py           # .supra v1 standard + SupraWorx importer compatibility
│   ├── new_sme_package.py          # Generates SME packages from scripts/data/sme_use_cases.json
│   ├── render_sme_shortcut_specs.py# Renders the SupraWorx managed-shortcut registry entries
│   ├── fix_supraworx_compat.py     # Rewrites metadata to the importer allow-list
│   ├── generate_docs.py            # Per-package docs, catalog, domain indexes, manifest
│   ├── render_assets.py            # Diagram assets
│   ├── install_to_supraworx_examples.sh
│   └── data/
│       ├── sme_use_cases.json      # 100 SME use-case specs (EN/DE descriptions, focus, scenario)
│       ├── sme_registry_extras.json# Legacy shortcut IDs to register alongside
│       ├── descriptions.de.json    # German descriptions for hand-written packages
│       ├── domains.json            # Domain labels (EN/DE) and package→domain mapping
│       └── supraworx_managed_shortcuts.json # Shortcut IDs the SupraWorx importer accepts
├── schemas/                        # JSON schemas and contract notes
├── tests/                          # pytest checks mirrored by CI
├── examples_manifest.json          # Machine-readable catalog (schema V2, with domain + path)
└── .github/                        # CI workflow, issue and PR templates
```

## Domains

| Folder | English | Deutsch |
| --- | --- | --- |
| `finance_cash` | Finance & Cash | Finanzen & Liquidität |
| `sales_growth` | Sales & Growth | Vertrieb & Wachstum |
| `marketing_content` | Marketing & Content | Marketing & Content |
| `customer_service` | Customer Service | Kundenservice |
| `operations_production` | Operations & Production | Betrieb & Produktion |
| `supply_chain_procurement` | Supply Chain & Procurement | Lieferkette & Einkauf |
| `people_hr` | People & HR | Personal & HR |
| `compliance_risk_esg` | Compliance, Risk & ESG | Compliance, Risiko & ESG |
| `it_digital_data` | IT, Digital & Data | IT, Digitalisierung & Daten |
| `strategy_analytics` | Strategy & Analytics | Strategie & Analytik |
| `public_funding_tenders` | Public Funding & Tenders | Förderung & Ausschreibungen |
| `education_learning` | Education & Learning | Bildung & Lernen |

A package's domain is simply the folder it lives in. Hand-written packages are mapped in `scripts/data/domains.json`; generated packages carry `domain` in their spec.

## Two kinds of packages

**Hand-written packages** (the original 47, e.g. `kmu_tender_factory`, `workforce_intelligence_platform`) are edited directly. Their German description lives in `scripts/data/descriptions.de.json`.

**Generated SME packages** (the 100 `sme_*` packages added with the restructure) are produced by `scripts/new_sme_package.py` from one spec each in `scripts/data/sme_use_cases.json`. Do not edit the `.supra` file by hand — edit the spec and regenerate, otherwise CI (`new_sme_package.py --check`) fails. Every generated package has the same reviewable four-step shape:

| # | Column | Category | Tool | Output contract |
| --- | --- | --- | --- | --- |
| 1 | Business context | `manual` | `user_input` | — |
| 2 | Signal map | `ai_tool` | `<key>_signals` | summary, signals, constraints, assumptions, risks, evidence_gaps |
| 3 | Decision plan | `ai_tool` | `<key>_decision` | summary, decision, actions, metrics, risks, evidence_gaps |
| 4 | Execution brief | `shortcut` | `<key>` (managed SME shortcut) | summary, decision, actions, risks, evidence_gaps |

Each spec has these fields:

| Field | Used for |
| --- | --- |
| `key`, `domain`, `title` | Identity, folder, titles |
| `description_en`, `description_de` | Package description, docs, catalog |
| `focus` | Inserted into all three prompts and into the SupraWorx shortcut system prompt |
| `textarea_label`, `result_title` | SupraWorx shortcut card labels |
| `scenario` | Realistic, synthetic starter intake (`Business context: …`) |

## Adding a package

### Generated SME package

1. Append a spec object to `scripts/data/sme_use_cases.json` (unique `key`, `^[a-z0-9_]+$`, existing `domain`).
2. Regenerate and validate:

   ```bash
   python3 scripts/new_sme_package.py .
   python3 scripts/render_sme_shortcut_specs.py . --registry
   python3 scripts/validate_supra.py .
   python3 scripts/generate_docs.py .
   ```

3. Register the shortcut in SupraWorx (see below) so the package can be uploaded there.

### Hand-written package

1. Create `packages/<domain>/<key>.supra` following [the `.supra` v1 standard](supra-v1-standard.md). Use only importer-allowed metadata fields (`scripts/fix_supraworx_compat.py . --check` tells you if not).
2. Add the German description to `scripts/data/descriptions.de.json` and the domain mapping to `scripts/data/domains.json`.
3. If the final step is a `shortcut` column, its `tool` must be a shortcut SupraWorx knows: a managed SME shortcut, `gpt`, or an ID listed in `scripts/data/supraworx_managed_shortcuts.json`.
4. Run the validation and docs commands above.

## Getting packages into SupraWorx

### Option A — file upload (per package)

Upload the `.supra` file in AI Workbench (`ai_workbench_supra_file_import`). Requirements: the package passes the strict validator and every shortcut column references a registered shortcut. 145 of 147 packages qualify; the two exceptions are documented in the [import evaluation](import-evaluation.en.md).

### Option B — bundle into the template gallery

```bash
./scripts/install_to_supraworx_examples.sh /path/to/supraworxv30/mint/workbench/examples            # all domains
./scripts/install_to_supraworx_examples.sh /path/to/supraworxv30/mint/workbench/examples finance_cash sales_growth
```

The script validates first, copies only `.supra` files (flat), and prints the new file count — update `test_supra_catalog.py` accordingly.

### Registering the managed shortcuts in SupraWorx

```bash
python3 scripts/render_sme_shortcut_specs.py . --apply /path/to/supraworxv30/mint/shortcuts/services/sme_shortcuts.py
```

This inserts (or refreshes) a marker-delimited block of `_DISRUPTIVE_SME_SHORTCUT_SPECS` entries. `shortcuts/tasks.py` binds every definition to `sme_shortcut_task` automatically, so no task code changes are required. Existing SupraWorx instances create the `ShortCut` rows lazily on first import (`ensure_sme_shortcut`) or via `ensure_sme_shortcuts()`.

## Validation layers

`scripts/validate_supra.py` checks every package against two layers and fails CI on the first error:

1. **`.supra` v1 standard** — identity, metadata alignment, columns, prompt execution, output contracts, workflows, `main_workbench` mirror.
2. **SupraWorx importer compatibility** — root/metadata/commerce/starter-row allow-lists, 1 MiB payload, 64 columns, 4000-character starter text, 12 KiB output schemas, 64 KiB extension objects, and the managed-shortcut gate (documented legacy exceptions produce warnings).

`tests/test_validate_examples.py` runs the validator plus the `--check` modes of the generators and asserts the manifest matches the package files.
