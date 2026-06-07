# SME Local SEO Content Engine

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../sme_local_seo_content_engine.supra`](../sme_local_seo_content_engine.supra)
- **Workbench-Titel:** SME Local SEO Content Engine Desk
- **Paket-Key:** `sme_local_seo_content_engine`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 4
- **Workflows:** 1

## Zweck

Erstellt lokale SEO-Content-Briefings aus Geschäftskontext, Servicegebieten, Kundennachweisen, Suchintention und seitenbezogenen Handlungshinweisen.

## Starter-Eingabe

### SME Local SEO Content Engine Starter

- **Anfrage:** Fügen Sie den Quellkontext für SME Local SEO Content Engine ein.
- **Quelltyp:** `business_context`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "sme_local_seo_content_engine",
  "focus": "local intent, service proof, differentiators, keywords, content topics, and reviewable publishing tasks",
  "intake": "Business context: We need a reliable decision support flow for SME Local SEO Content Engine.\nCurrent situation: Inputs are incomplete, owners need an answer this week, and leadership wants visible assumptions.\nKnown constraint: Do not invent facts; mark evidence gaps and human-review items.",
  "guardrails": [
    "Do not invent facts.",
    "Mark assumptions and evidence gaps.",
    "Prefer actions that can be started this week.",
    "Keep financial, legal, safety, and compliance advice reviewable by a responsible human."
  ],
  "target_outputs": [
    "signal_map",
    "decision_plan",
    "execution_brief"
  ]
}
```

## Workflow

### SME Local SEO Content Engine Workflow

Erstellt lokale SEO-Content-Briefings aus Geschäftskontext, Servicegebieten, Kundennachweisen, Suchintention und seitenbezogenen Handlungshinweisen.

| # | Schritt          | ID                 | Backlog |
| - | ---------------- | ------------------ | ------- |
| 1 | Business context | `business_context` | ja      |
| 2 | Signal map       | `signal_map`       | nein    |
| 3 | Decision plan    | `decision_plan`    | nein    |
| 4 | Execution brief  | `execution_brief`  | nein    |

## Spalten und Tools

| # | Key                | Titel            | Kategorie  | Tool                                    | Prüfung | Pflichtausgabe                                                                         |
| - | ------------------ | ---------------- | ---------- | --------------------------------------- | ------- | -------------------------------------------------------------------------------------- |
| 1 | `business_context` | Business context | `manual`   | `user_input`                            | nein    | -                                                                                      |
| 2 | `signal_map`       | Signal map       | `ai_tool`  | `sme_local_seo_content_engine_signals`  | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `decision_plan`    | Decision plan    | `ai_tool`  | `sme_local_seo_content_engine_decision` | ja      | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 4 | `execution_brief`  | Execution brief  | `shortcut` | `sme_local_seo_content_engine`          | ja      | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Business context

- **Key:** `business_context`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### Signal map

- **Key:** `signal_map`
- **Tool:** `sme_local_seo_content_engine_signals`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Analyze the SME context for local intent, service proof, differentiators, keywords, content topics, and reviewable publishing tasks. Extract the most important facts, weak signals, constraints, assumptions, risks, and evidence gaps. Estimate likely impact qualitatively when numbers are missing. Do not invent facts. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Decision plan

- **Key:** `decision_plan`
- **Tool:** `sme_local_seo_content_engine_decision`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Create a pragmatic owner decision plan for local intent, service proof, differentiators, keywords, content topics, and reviewable publishing tasks. Include the recommended decision, rejected alternatives, first 72-hour actions, owners, metrics, and review triggers. Keep advice bounded by the provided facts and mark anything that needs finance, legal, safety, or compliance review. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Execution brief

- **Key:** `execution_brief`
- **Tool:** `sme_local_seo_content_engine`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the intake, signal map, and decision plan to produce the managed SME execution brief for local intent, service proof, differentiators, keywords, content topics, and reviewable publishing tasks. Respond in the same language as the user, keep assumptions visible, and make the next actions concrete.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
