# Repository-Leitfaden

Wie dieses Repository aufgebaut ist, wie Pakete erzeugt werden und wie sie in die SupraWorx AI Workbench gelangen.

## Struktur

```text
.
├── packages/                       # 147 importierbare .supra-Pakete, ein Ordner je Domäne
│   ├── finance_cash/               #   jeder Ordner hat einen generierten README.md-Index
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
│   ├── README.md                   # Vollständiger Katalog nach Domäne (EN/DE)
│   ├── packages/<key>.{en,de}.md   # Generierte Paketdokumentation
│   ├── import-evaluation.{en,de}.md
│   ├── repository-guide.{en,de}.md
│   ├── supra-v1-standard.md / supra-v1-standard-fix.md
│   └── assets/                     # SVG-/PNG-Diagramme
├── scripts/
│   ├── validate_supra.py           # .supra-v1-Standard + SupraWorx-Importer-Kompatibilität
│   ├── new_sme_package.py          # Erzeugt SME-Pakete aus scripts/data/sme_use_cases.json
│   ├── render_sme_shortcut_specs.py# Erzeugt die Registry-Einträge für verwaltete SupraWorx-Shortcuts
│   ├── fix_supraworx_compat.py     # Schreibt Metadaten auf die Importer-Allowlist um
│   ├── generate_docs.py            # Paketdokus, Katalog, Domänen-Indizes, Manifest
│   ├── render_assets.py            # Diagramm-Assets
│   ├── install_to_supraworx_examples.sh
│   └── data/
│       ├── sme_use_cases.json      # 100 SME-Use-Case-Spezifikationen (Beschreibung EN/DE, Fokus, Szenario)
│       ├── sme_registry_extras.json# Alt-Shortcut-IDs, die mitregistriert werden
│       ├── descriptions.de.json    # Deutsche Beschreibungen der handgeschriebenen Pakete
│       ├── domains.json            # Domänenbezeichnungen (EN/DE) und Zuordnung Paket→Domäne
│       └── supraworx_managed_shortcuts.json # Shortcut-IDs, die der SupraWorx-Importer akzeptiert
├── schemas/                        # JSON-Schemas und Vertragsnotizen
├── tests/                          # pytest-Prüfungen, identisch mit CI
├── examples_manifest.json          # Maschinenlesbarer Katalog (Schema V2, mit Domäne + Pfad)
└── .github/                        # CI-Workflow, Issue- und PR-Vorlagen
```

## Domänen

| Ordner | Englisch | Deutsch |
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

Die Domäne eines Pakets ist schlicht der Ordner, in dem es liegt. Handgeschriebene Pakete sind in `scripts/data/domains.json` zugeordnet; generierte Pakete tragen `domain` in ihrer Spezifikation.

## Zwei Arten von Paketen

**Handgeschriebene Pakete** (die ursprünglichen 47, z. B. `kmu_tender_factory`, `workforce_intelligence_platform`) werden direkt bearbeitet. Ihre deutsche Beschreibung liegt in `scripts/data/descriptions.de.json`.

**Generierte SME-Pakete** (die 100 mit der Umstrukturierung hinzugefügten `sme_*`-Pakete) erzeugt `scripts/new_sme_package.py` aus je einer Spezifikation in `scripts/data/sme_use_cases.json`. Die `.supra`-Datei nicht von Hand bearbeiten – Spezifikation ändern und neu erzeugen, sonst schlägt die CI (`new_sme_package.py --check`) fehl. Jedes generierte Paket hat dieselbe prüfbare Vier-Schritt-Struktur:

| # | Spalte | Kategorie | Tool | Output-Vertrag |
| --- | --- | --- | --- | --- |
| 1 | Business context | `manual` | `user_input` | — |
| 2 | Signal map | `ai_tool` | `<key>_signals` | summary, signals, constraints, assumptions, risks, evidence_gaps |
| 3 | Decision plan | `ai_tool` | `<key>_decision` | summary, decision, actions, metrics, risks, evidence_gaps |
| 4 | Execution brief | `shortcut` | `<key>` (verwalteter SME-Shortcut) | summary, decision, actions, risks, evidence_gaps |

Jede Spezifikation hat diese Felder:

| Feld | Verwendung |
| --- | --- |
| `key`, `domain`, `title` | Identität, Ordner, Titel |
| `description_en`, `description_de` | Paketbeschreibung, Dokumentation, Katalog |
| `focus` | Wird in alle drei Prompts und in den System-Prompt des SupraWorx-Shortcuts eingesetzt |
| `textarea_label`, `result_title` | Beschriftungen der SupraWorx-Shortcut-Karte |
| `scenario` | Realistische, synthetische Starter-Eingabe (`Business context: …`) |

## Ein Paket hinzufügen

### Generiertes SME-Paket

1. Ein Spezifikationsobjekt an `scripts/data/sme_use_cases.json` anhängen (eindeutiger `key`, `^[a-z0-9_]+$`, vorhandene `domain`).
2. Erzeugen und validieren:

   ```bash
   python3 scripts/new_sme_package.py .
   python3 scripts/render_sme_shortcut_specs.py . --registry
   python3 scripts/validate_supra.py .
   python3 scripts/generate_docs.py .
   ```

3. Den Shortcut in SupraWorx registrieren (siehe unten), damit das Paket dort hochgeladen werden kann.

### Handgeschriebenes Paket

1. `packages/<domain>/<key>.supra` gemäß [`.supra`-v1-Standard](supra-v1-standard.md) anlegen. Nur vom Importer erlaubte Metadatenfelder verwenden (`scripts/fix_supraworx_compat.py . --check` meldet Abweichungen).
2. Deutsche Beschreibung in `scripts/data/descriptions.de.json` und Domänenzuordnung in `scripts/data/domains.json` ergänzen.
3. Ist der letzte Schritt eine `shortcut`-Spalte, muss ihr `tool` ein SupraWorx bekannter Shortcut sein: ein verwalteter SME-Shortcut, `gpt` oder eine ID aus `scripts/data/supraworx_managed_shortcuts.json`.
4. Die oben genannten Validierungs- und Doku-Befehle ausführen.

## Pakete nach SupraWorx bringen

### Option A – Datei-Upload (je Paket)

Die `.supra`-Datei in der AI Workbench hochladen (`ai_workbench_supra_file_import`). Voraussetzungen: Das Paket besteht den strikten Validator, und jede Shortcut-Spalte verweist auf einen registrierten Shortcut. 145 von 147 Paketen erfüllen das; die zwei Ausnahmen sind in der [Import-Bewertung](import-evaluation.de.md) dokumentiert.

### Option B – Bündeln in die Vorlagen-Galerie

```bash
./scripts/install_to_supraworx_examples.sh /pfad/zu/supraworxv30/mint/workbench/examples            # alle Domänen
./scripts/install_to_supraworx_examples.sh /pfad/zu/supraworxv30/mint/workbench/examples finance_cash sales_growth
```

Das Skript validiert zuerst, kopiert nur `.supra`-Dateien (flach) und gibt die neue Dateianzahl aus – `test_supra_catalog.py` entsprechend anpassen.

### Verwaltete Shortcuts in SupraWorx registrieren

```bash
python3 scripts/render_sme_shortcut_specs.py . --apply /pfad/zu/supraworxv30/mint/shortcuts/services/sme_shortcuts.py
```

Das fügt einen durch Marker begrenzten Block von `_DISRUPTIVE_SME_SHORTCUT_SPECS`-Einträgen ein (oder aktualisiert ihn). `shortcuts/tasks.py` bindet jede Definition automatisch an `sme_shortcut_task`, Änderungen am Task-Code sind nicht nötig. Bestehende SupraWorx-Instanzen legen die `ShortCut`-Datensätze beim ersten Import (`ensure_sme_shortcut`) oder über `ensure_sme_shortcuts()` an.

## Validierungsschichten

`scripts/validate_supra.py` prüft jedes Paket auf zwei Ebenen und lässt die CI beim ersten Fehler fehlschlagen:

1. **`.supra`-v1-Standard** – Identität, Metadaten-Abgleich, Spalten, Prompt-Ausführung, Output-Verträge, Workflows, `main_workbench`-Spiegel.
2. **SupraWorx-Importer-Kompatibilität** – Allowlists für Root/Metadaten/Commerce/Starter-Zeilen, 1 MiB Payload, 64 Spalten, 4000 Zeichen Starter-Text, 12 KiB Output-Schemas, 64 KiB Erweiterungsobjekte sowie das Gate für verwaltete Shortcuts (dokumentierte Alt-Ausnahmen erzeugen Warnungen).

`tests/test_validate_examples.py` führt den Validator sowie die `--check`-Modi der Generatoren aus und prüft, dass das Manifest zu den Paketdateien passt.
