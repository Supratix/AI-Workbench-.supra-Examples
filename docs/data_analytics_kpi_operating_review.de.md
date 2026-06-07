# Data Analytics KPI Operating Review

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt. Interne Spaltentitel, Tool-IDs, Prompts und Pflichtfelder bleiben als Quelldaten erhalten.

## Paketüberblick

- **Quellpaket:** [`../data_analytics_kpi_operating_review.supra`](../data_analytics_kpi_operating_review.supra)
- **Workbench-Titel:** Data Analytics KPI Operating Review Desk
- **Paket-Key:** `data_analytics_kpi_operating_review`
- **Modul:** `data_analytics_kpi_operating_review`
- **Anbieter:** SupraTix
- **Schema-Version:** `1`
- **Export-/Import-Version:** `1.0.0` / `1.0.0`
- **Columns:** 4
- **Workflows:** 1
- **Commerce:** `free_of_use`, usage unit `cloud_credits`

## Zweck

Create a structured operating review from KPI context, risks, actions, and follow-up triggers.

## Starter-Eingabe

### Data Analytics KPI Operating Review starter

- **Request:** Paste the source context for Data Analytics KPI Operating Review.
- **Source type:** `business_context`

**Starter-Payload:**

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "data_analytics_kpi_operating_review",
  "focus": "KPI movements, root causes, owner actions, thresholds, and review rituals",
  "intake": "Business context: We need a reliable decision support flow for Data Analytics KPI Operating Review.\nCurrent situation: Inputs are incomplete, owners need an answer this week, and leadership wants visible assumptions.\nKnown constraint: Do not invent facts; mark evidence gaps and human-review items.",
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

### Data Analytics KPI Operating Review workflow

Create a structured operating review from KPI context, risks, actions, and follow-up triggers.

| # | Step             | ID                 | Backlog | Auto finished | Auto close |
| - | ---------------- | ------------------ | ------- | ------------- | ---------- |
| 1 | Business context | `business_context` | yes     | no            | no         |
| 2 | Signal map       | `signal_map`       | no      | no            | no         |
| 3 | Decision plan    | `decision_plan`    | no      | no            | no         |
| 4 | Execution brief  | `execution_brief`  | no      | no            | no         |

## Spalten und Tools

| # | Key                | Title            | Category   | Tool                                           | Inputs                                                | Execution       | Review | Required output                                                                        |
| - | ------------------ | ---------------- | ---------- | ---------------------------------------------- | ----------------------------------------------------- | --------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `business_context` | Business context | `manual`   | `user_input`                                   | -                                                     | `disabled`      | no     | -                                                                                      |
| 2 | `signal_map`       | Signal map       | `ai_tool`  | `data_analytics_kpi_operating_review_signals`  | `business_context`                                    | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `decision_plan`    | Decision plan    | `ai_tool`  | `data_analytics_kpi_operating_review_decision` | `business_context`<br>`signal_map`                    | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 4 | `execution_brief`  | Execution brief  | `shortcut` | `data_analytics_kpi_operating_review`          | `business_context`<br>`signal_map`<br>`decision_plan` | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

### Business context

- **Key:** `business_context`
- **Tool category:** `manual`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no; label=Manual intake

No prompt is stored for this column; it calls the configured shortcut/tool directly.

### Signal map

- **Key:** `signal_map`
- **Tool category:** `ai_tool`
- **Tool:** `data_analytics_kpi_operating_review_signals`
- **Inputs:** `business_context`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Map signals

**Prompt:**

```text
Analyze the SME context for KPI movements, root causes, owner actions, thresholds, and review rituals. Extract the most important facts, weak signals, constraints, assumptions, risks, and evidence gaps. Estimate likely impact qualitatively when numbers are missing. Do not invent facts. Return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Decision plan

- **Key:** `decision_plan`
- **Tool category:** `ai_tool`
- **Tool:** `data_analytics_kpi_operating_review_decision`
- **Inputs:** `business_context`, `signal_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Build plan

**Prompt:**

```text
Create a pragmatic owner decision plan for KPI movements, root causes, owner actions, thresholds, and review rituals. Include the recommended decision, rejected alternatives, first 72-hour actions, owners, metrics, and review triggers. Keep advice bounded by the provided facts and mark anything that needs finance, legal, safety, or compliance review. Return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Execution brief

- **Key:** `execution_brief`
- **Tool category:** `shortcut`
- **Tool:** `data_analytics_kpi_operating_review`
- **Inputs:** `business_context`, `signal_map`, `decision_plan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Generate execution brief

**Prompt:**

```text
Use the intake, signal map, and decision plan to produce the managed SME execution brief for KPI movements, root causes, owner actions, thresholds, and review rituals. Respond in the same language as the user, keep assumptions visible, and make the next actions concrete.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Quality gate:** Return the managed SME shortcut response with explicit evidence gaps and owner-ready actions.
- **Evidence policy:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare KI- und Shortcut-Spalten sind auf manuelle Prüfung gesetzt, wenn das Paket `requires_review` markiert.
- Output Contracts definieren erwartete JSON-Strukturen, Pflichtfelder, Quality Gates und Evidence Policies für nachgelagerte Prüfungen.
