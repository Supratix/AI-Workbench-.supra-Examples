# AI Workbench `.supra`-Beispiele

![AI Workbench .supra Examples](docs/assets/social-preview.png)

🇬🇧 [English version](README.md)

Eine portable, sofort nutzbare Sammlung von **147 `.supra`-Paketen** für die SupraTix AI Workbench (SupraWorx v3.0), gegliedert in **12 KMU-Domänen**. Jedes Paket ist eine vollständige, prüfbare Workbench: Eingabe, Evidenz-Extraktion, Entscheidungsplan und ein verwaltetes Umsetzungsbriefing – mit Output-Verträgen, Starterdaten und zweisprachiger Dokumentation.

Jedes Paket wird gegen den [`.supra`-v1-Standard](docs/supra-v1-standard.md) **und** gegen den strikten SupraWorx-Importer (Allowlists, Größenlimits, Gate für verwaltete Shortcuts) validiert. Die [Import-Bewertung](docs/import-evaluation.de.md) beschreibt, was getestet und was korrigiert wurde.

## Inhalt

- **147 `.supra`-Pakete** unter [`packages/<domain>/`](packages/) – 47 handgeschriebene Pakete plus 100 generierte KMU-Pakete.
- **Deutsche und englische Dokumentation** zu jedem Paket unter [`docs/packages/`](docs/README.md) sowie zweisprachige Leitfäden.
- **Generatoren**: Die 100 KMU-Pakete entstehen aus einer kompakten Spezifikation (`scripts/data/sme_use_cases.json`); die passenden Registry-Einträge für SupraWorx-Shortcuts werden aus derselben Spezifikation erzeugt.
- **Validierung**, die den SupraWorx-Importer nachbildet, ein GitHub-Actions-Workflow, pytest-Prüfungen, JSON-Schemas und Diagramm-Assets.

## Domänen

| Ordner | Englisch | Deutsch | Pakete | Beispiele |
| --- | --- | --- | ---: | --- |
| [`finance_cash`](packages/finance_cash/README.md) | Finance & Cash | Finanzen & Liquidität | 16 | `sme_cashflow_war_room`, `sme_thirteen_week_cash_forecast`, `sme_credit_risk_screener`, … |
| [`sales_growth`](packages/sales_growth/README.md) | Sales & Growth | Vertrieb & Wachstum | 15 | `sme_lead_qualifier`, `sme_cold_outreach_sequencer`, `sme_discount_approval_gate`, … |
| [`marketing_content`](packages/marketing_content/README.md) | Marketing & Content | Marketing & Content | 12 | `sme_brand_messaging_kit`, `sme_ad_campaign_brief_builder`, `linkedin_extreme_engagement_posting`, … |
| [`customer_service`](packages/customer_service/README.md) | Customer Service | Kundenservice | 10 | `sme_customer_reply`, `sme_complaint_root_cause_clusterer`, `sme_service_recovery_playbook`, … |
| [`operations_production`](packages/operations_production/README.md) | Operations & Production | Betrieb & Produktion | 15 | `sme_downtime_triage`, `sme_production_bottleneck_finder`, `sme_work_instruction_writer`, … |
| [`supply_chain_procurement`](packages/supply_chain_procurement/README.md) | Supply Chain & Procurement | Lieferkette & Einkauf | 12 | `sme_vendor_negotiation_brief`, `sme_supplier_risk_scorecard`, `sme_make_or_buy_decider`, … |
| [`people_hr`](packages/people_hr/README.md) | People & HR | Personal & HR | 13 | `sme_hiring_scorecard_kit`, `sme_shift_roster_builder`, `sme_employee_retention_risk_radar`, … |
| [`compliance_risk_esg`](packages/compliance_risk_esg/README.md) | Compliance, Risk & ESG | Compliance, Risiko & ESG | 12 | `sme_compliance_evidence_pack`, `sme_gdpr_processing_register`, `sme_carbon_footprint_estimator`, … |
| [`it_digital_data`](packages/it_digital_data/README.md) | IT, Digital & Data | IT, Digitalisierung & Daten | 11 | `sme_ai_adoption_readiness_sprint`, `sme_ai_use_policy_drafter`, `sme_data_backup_recovery_check`, … |
| [`strategy_analytics`](packages/strategy_analytics/README.md) | Strategy & Analytics | Strategie & Analytik | 14 | `data_analytics_kpi_framework_designer`, `sme_okr_drafting_assistant`, `sme_scenario_stress_tester`, … |
| [`public_funding_tenders`](packages/public_funding_tenders/README.md) | Public Funding & Tenders | Förderung & Ausschreibungen | 10 | `kmu_tender_factory`, `sme_grant_application_drafter`, `sme_public_tender_compliance_matrix`, … |
| [`education_learning`](packages/education_learning/README.md) | Education & Learning | Bildung & Lernen | 7 | `mint_study_planning`, `sme_expert_knowledge_capture`, `sme_micro_learning_series_planner`, … |

Der vollständige Katalog mit Beschreibungen in beiden Sprachen steht in [`docs/README.md`](docs/README.md); die maschinenlesbare Fassung ist [`examples_manifest.json`](examples_manifest.json).

## Schnellstart

```bash
cd AI-Workbench-.supra-Examples

# Alle Pakete validieren (.supra-v1-Standard + SupraWorx-Importer-Kompatibilität)
python3 scripts/validate_supra.py .

# Nach Änderungen: die 100 KMU-Pakete, Dokumentation, Katalog, Domänen-Indizes und Manifest neu erzeugen
python3 scripts/new_sme_package.py .
python3 scripts/generate_docs.py .

# Optional: Bild-Assets neu rendern
python3 scripts/render_assets.py .
```

## Repository-Struktur

```text
.
├── packages/<domain>/*.supra       # 147 AI-Workbench-Pakete in 12 Domänenordnern (+ README je Domäne)
├── docs/
│   ├── README.md                   # Katalog nach Domäne (EN/DE)
│   ├── packages/*.en.md / *.de.md  # Generierte Paketdokumentation
│   ├── import-evaluation.{en,de}.md# Import-Bewertung SupraWorx v3.0
│   ├── repository-guide.{en,de}.md # Struktur, Generatoren, Pakete hinzufügen, Installation
│   ├── supra-v1-standard*.md       # Der Standard und sein Fix-Playbook
│   └── assets/                     # SVG- und PNG-Diagramme
├── scripts/                        # Validierung, Generatoren, Doku, Assets, Installation
│   └── data/                       # Use-Case-Spezifikationen, Übersetzungen, Domänenzuordnung, Shortcut-Registry
├── schemas/                        # JSON-Schemas und Vertragsnotizen
├── tests/                          # pytest-Prüfungen (identisch mit CI)
├── examples_manifest.json          # Maschinenlesbarer Katalog
└── .github/                        # CI, Issue-Vorlagen, PR-Vorlage
```

## Konventionen für `.supra`-Pakete

Jedes Paket ist JSON mit der Endung `.supra`. Die wichtigsten Abschnitte:

1. `metadata` – Anbieter, Version, Starter-Zeilen, Commerce-Metadaten und `source_attribution`. Es werden nur Felder verwendet, die auf der Allowlist des SupraWorx-Importers stehen.
2. `columns` – manuelle, KI-Tool- und Shortcut-Spalten mit Einstellungen zur Prompt-Ausführung.
3. `workflows` – geordnete Workbench-Schritte.
4. `main_workbench` – eine portable Workbench-Definition, die Spalten und Workflows des Pakets spiegelt.
5. `tooling.output_contract` – erwartete JSON-Struktur, Pflichtfelder, Qualitäts-Gate und Evidenzregel.

Die 100 generierten KMU-Pakete teilen sich eine prüfbare Struktur: *Business context → Signal map → Decision plan → Execution brief*. Der letzte Schritt ist ein verwalteter SME-Shortcut, dessen ID dem Paket-Key entspricht. Die normative Beschreibung steht im [`.supra`-v1-Standard](docs/supra-v1-standard.md); für Reparaturen dient das [Fix-Playbook](docs/supra-v1-standard-fix.md).

## Import in die SupraWorx AI Workbench

![Import flow](docs/assets/supra-import-export-flow.svg)

Zwei Wege werden unterstützt:

1. **Datei-Upload** in der AI Workbench – das Paket muss den strikten Validator bestehen und darf nur registrierte Shortcuts referenzieren. 145 von 147 Paketen erfüllen das (zwei dokumentierte Ausnahmen, siehe [Bewertung](docs/import-evaluation.de.md)).
2. **Vorlagen-Galerie** – Pakete nach `mint/workbench/examples/` kopieren:

   ```bash
   ./scripts/install_to_supraworx_examples.sh pfad/zu/supraworxv30/mint/workbench/examples          # alle Domänen
   ./scripts/install_to_supraworx_examples.sh pfad/zu/supraworxv30/mint/workbench/examples finance_cash
   ```

Die Shortcut-IDs der neuen Pakete einmalig in SupraWorx registrieren (keine Änderungen am Task-Code nötig):

```bash
python3 scripts/render_sme_shortcut_specs.py . --apply pfad/zu/supraworxv30/mint/shortcuts/services/sme_shortcuts.py
```

Details, Voraussetzungen und der Hinweis zur Dateianzahl in `test_supra_catalog.py` stehen im [Repository-Leitfaden](docs/repository-guide.de.md).

## Governance-Grundlage

Die Beispiele sind bewusst auf menschlich prüfbare Ausführung ausgelegt. Prompts verlangen, Fakten von Annahmen zu trennen, Evidenzlücken zu markieren und keine Fakten zu erfinden. Finanz-, Rechts-, Sicherheits-, Personal- und Compliance-relevante Empfehlungen sind für die Prüfung durch verantwortliche Personen gekennzeichnet. Starterdaten sind synthetisch.

## Mitwirken

Siehe [CONTRIBUTING.md](CONTRIBUTING.md) und den [Repository-Leitfaden](docs/repository-guide.de.md), um ein generiertes KMU-Paket (Spezifikation bearbeiten, neu erzeugen) oder ein handgeschriebenes Paket hinzuzufügen.

## Hinweise für Maintainer

Das Repository ist bewusst abhängigkeitsarm. Alle Skripte nutzen ausschließlich die Python-Standardbibliothek; die PNG-Erzeugung verwendet Pillow, sofern vorhanden, und fällt sonst auf reine SVG-Ausgabe zurück.
