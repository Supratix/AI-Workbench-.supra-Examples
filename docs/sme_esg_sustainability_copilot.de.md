# SME ESG Sustainability Copilot

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../sme_esg_sustainability_copilot.supra`](../sme_esg_sustainability_copilot.supra)
- **Workbench-Titel:** SME ESG Sustainability Copilot Desk
- **Paket-Key:** `sme_esg_sustainability_copilot`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 3
- **Workflows:** 1

## Zweck

Konsolidiert Nachhaltigkeitsnachweise zu einer ESG-Readiness-Scorecard mit Gap-Analyse und Maßnahmenplan.

## Starter-Eingabe

### starter

- **Anfrage:** Fügen Sie den Quellkontext für SME ESG Sustainability Copilot ein.
- **Quelltyp:** `business_context`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1"
}
```

## Workflow

### SME ESG Sustainability Copilot Workflow

Konsolidiert Nachhaltigkeitsnachweise zu einer ESG-Readiness-Scorecard mit Gap-Analyse und Maßnahmenplan.

| # | Schritt          | ID                 | Backlog |
| - | ---------------- | ------------------ | ------- |
| 1 | Business context | `business_context` | nein    |
| 2 | ESG evidence map | `esg_evidence_map` | nein    |
| 3 | Reporting brief  | `reporting_brief`  | nein    |

## Spalten und Tools

| # | Key                | Titel            | Kategorie  | Tool                             | Prüfung | Pflichtausgabe |
| - | ------------------ | ---------------- | ---------- | -------------------------------- | ------- | -------------- |
| 1 | `business_context` | Business context | `manual`   | `user_input`                     | nein    | -              |
| 2 | `esg_evidence_map` | ESG evidence map | `ai_tool`  | `sme_esg_evidence`               | ja      | `summary`      |
| 3 | `reporting_brief`  | Reporting brief  | `shortcut` | `sme_esg_sustainability_copilot` | ja      | `summary`      |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Business context

- **Key:** `business_context`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### ESG evidence map

- **Key:** `esg_evidence_map`
- **Tool:** `sme_esg_evidence`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`
- **Evidenzregel:** `no_invented_facts`

### Reporting brief

- **Key:** `reporting_brief`
- **Tool:** `sme_esg_sustainability_copilot`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Pflichtfelder:** `summary`
- **Evidenzregel:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
