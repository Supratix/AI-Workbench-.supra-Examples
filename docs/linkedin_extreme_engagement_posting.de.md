# LinkedIn Extreme Engagement Posting

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../linkedin_extreme_engagement_posting.supra`](../linkedin_extreme_engagement_posting.supra)
- **Workbench-Titel:** LinkedIn Extreme Engagement Posting Desk
- **Paket-Key:** `linkedin_extreme_engagement_posting`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 9
- **Workflows:** 1

## Zweck

Erstellt ein LinkedIn-Publishing-Paket für hohe Interaktion mit Hooks, Post-Varianten, Positionierungsnotizen, Risikoprüfungen und Follow-up-Impulsen.

## Starter-Eingabe

### LinkedIn Extreme Engagement Posting Starter

- **Anfrage:** Fügen Sie den Quellkontext für LinkedIn Extreme Engagement Posting ein.
- **Quelltyp:** `content_goal`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "linkedin_extreme_engagement_posting",
  "focus": "audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks",
  "intake": "Topic: Why most SME AI pilots fail after the demo. Audience: owners and operators. Position: start with measurable workflow pain, not tools. Constraint: provocative but respectful.",
  "guardrails": [
    "Do not invent facts.",
    "Mark assumptions and evidence gaps.",
    "Prefer actions that can be started this week.",
    "Keep financial, legal, safety, and compliance advice reviewable by a responsible human."
  ],
  "target_outputs": [
    "execution_brief"
  ]
}
```

## Workflow

### LinkedIn Extreme Engagement Posting Workflow

Erstellt ein LinkedIn-Publishing-Paket für hohe Interaktion mit Hooks, Post-Varianten, Positionierungsnotizen, Risikoprüfungen und Follow-up-Impulsen.

| # | Schritt                | ID                | Backlog |
| - | ---------------------- | ----------------- | ------- |
| 1 | Content goal           | `content_goal`    | ja      |
| 2 | Audience signal map    | `audience_signal` | nein    |
| 3 | Trend scan             | `trend_scan`      | nein    |
| 4 | Hook bank              | `hook_bank`       | nein    |
| 5 | Post draft             | `post_draft`      | nein    |
| 6 | Engagement plan        | `engagement_plan` | nein    |
| 7 | Tone and risk check    | `risk_check`      | nein    |
| 8 | Publishing plan        | `publishing_plan` | nein    |
| 9 | Final LinkedIn package | `execution_brief` | nein    |

## Spalten und Tools

| # | Key               | Titel                  | Kategorie  | Tool                                                  | Prüfung | Pflichtausgabe                                                                         |
| - | ----------------- | ---------------------- | ---------- | ----------------------------------------------------- | ------- | -------------------------------------------------------------------------------------- |
| 1 | `content_goal`    | Content goal           | `manual`   | `user_input`                                          | nein    | -                                                                                      |
| 2 | `audience_signal` | Audience signal map    | `ai_tool`  | `linkedin_extreme_engagement_posting_audience_signal` | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `trend_scan`      | Trend scan             | `ai_tool`  | `linkedin_extreme_engagement_posting_trend_scan`      | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 4 | `hook_bank`       | Hook bank              | `ai_tool`  | `linkedin_extreme_engagement_posting_hook_bank`       | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 5 | `post_draft`      | Post draft             | `ai_tool`  | `linkedin_extreme_engagement_posting_post_draft`      | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 6 | `engagement_plan` | Engagement plan        | `ai_tool`  | `linkedin_extreme_engagement_posting_engagement_plan` | ja      | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 7 | `risk_check`      | Tone and risk check    | `ai_tool`  | `linkedin_extreme_engagement_posting_risk_check`      | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 8 | `publishing_plan` | Publishing plan        | `ai_tool`  | `linkedin_extreme_engagement_posting_publishing_plan` | ja      | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 9 | `execution_brief` | Final LinkedIn package | `shortcut` | `linkedin_extreme_engagement_posting`                 | ja      | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Content goal

- **Key:** `content_goal`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### Audience signal map

- **Key:** `audience_signal`
- **Tool:** `linkedin_extreme_engagement_posting_audience_signal`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce audience signal map for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize audience pain and urgency. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Trend scan

- **Key:** `trend_scan`
- **Tool:** `linkedin_extreme_engagement_posting_trend_scan`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce trend scan for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize relevant zeitgeist without unsupported claims. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Hook bank

- **Key:** `hook_bank`
- **Tool:** `linkedin_extreme_engagement_posting_hook_bank`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce hook bank for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize clear, punchy hooks. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Post draft

- **Key:** `post_draft`
- **Tool:** `linkedin_extreme_engagement_posting_post_draft`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce post draft for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize post structure and point of view. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Engagement plan

- **Key:** `engagement_plan`
- **Tool:** `linkedin_extreme_engagement_posting_engagement_plan`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce engagement plan for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize comments, follow-up prompts, and reply angles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Tone and risk check

- **Key:** `risk_check`
- **Tool:** `linkedin_extreme_engagement_posting_risk_check`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce tone and risk check for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize claims, tone, and reputational risk. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Publishing plan

- **Key:** `publishing_plan`
- **Tool:** `linkedin_extreme_engagement_posting_publishing_plan`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce publishing plan for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize timing, owner actions, and variants. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Final LinkedIn package

- **Key:** `execution_brief`
- **Tool:** `linkedin_extreme_engagement_posting`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce final linkedin package for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize ready-to-use post package. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
