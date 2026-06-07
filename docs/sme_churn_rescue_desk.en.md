# SME Churn Rescue Desk

This documentation is generated from the `.supra` package content. Internal column titles, tool identifiers, prompts, and required fields are kept as source data.

## Package Overview

- **Source package:** [`../sme_churn_rescue_desk.supra`](../sme_churn_rescue_desk.supra)
- **Workbench title:** SME Churn Rescue Desk Desk
- **Package key:** `sme_churn_rescue_desk`
- **Module:** `sme_churn_rescue_desk`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Export / import version:** `1.0.0` / `1.0.0`
- **Columns:** 4
- **Workflows:** 1
- **Commerce:** `free_of_use`, usage unit `cloud_credits`

## Purpose

Identify churn signals and produce a customer rescue plan with owners and review triggers.

## Starter Intake

### SME Churn Rescue Desk starter

- **Request:** Paste the source context for SME Churn Rescue Desk.
- **Source type:** `business_context`

**Starter payload:**

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "sme_churn_rescue_desk",
  "focus": "customer health, churn signals, relationship risks, retention offers, account owners, and follow-up timing",
  "intake": "Business context: We need a reliable decision support flow for SME Churn Rescue Desk.\nCurrent situation: Inputs are incomplete, owners need an answer this week, and leadership wants visible assumptions.\nKnown constraint: Do not invent facts; mark evidence gaps and human-review items.",
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

### SME Churn Rescue Desk workflow

Identify churn signals and produce a customer rescue plan with owners and review triggers.

| # | Step             | ID                 | Backlog | Auto finished | Auto close |
| - | ---------------- | ------------------ | ------- | ------------- | ---------- |
| 1 | Business context | `business_context` | yes     | no            | no         |
| 2 | Signal map       | `signal_map`       | no      | no            | no         |
| 3 | Decision plan    | `decision_plan`    | no      | no            | no         |
| 4 | Execution brief  | `execution_brief`  | no      | no            | no         |

## Columns and Tools

| # | Key                | Title            | Category   | Tool                             | Inputs                                                | Execution       | Review | Required output                                                                        |
| - | ------------------ | ---------------- | ---------- | -------------------------------- | ----------------------------------------------------- | --------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `business_context` | Business context | `manual`   | `user_input`                     | -                                                     | `disabled`      | no     | -                                                                                      |
| 2 | `signal_map`       | Signal map       | `ai_tool`  | `sme_churn_rescue_desk_signals`  | `business_context`                                    | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `decision_plan`    | Decision plan    | `ai_tool`  | `sme_churn_rescue_desk_decision` | `business_context`<br>`signal_map`                    | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 4 | `execution_brief`  | Execution brief  | `shortcut` | `sme_churn_rescue_desk`          | `business_context`<br>`signal_map`<br>`decision_plan` | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt and Contract Reference

### Business context

- **Key:** `business_context`
- **Tool category:** `manual`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no; label=Manual intake

No prompt is stored for this column; it calls the configured shortcut/tool directly.

### Signal map

- **Key:** `signal_map`
- **Tool category:** `ai_tool`
- **Tool:** `sme_churn_rescue_desk_signals`
- **Inputs:** `business_context`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Map signals

**Prompt:**

```text
Analyze the SME context for customer health, churn signals, relationship risks, retention offers, account owners, and follow-up timing. Extract the most important facts, weak signals, constraints, assumptions, risks, and evidence gaps. Estimate likely impact qualitatively when numbers are missing. Do not invent facts. Return JSON only.
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
- **Tool:** `sme_churn_rescue_desk_decision`
- **Inputs:** `business_context`, `signal_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Build plan

**Prompt:**

```text
Create a pragmatic owner decision plan for customer health, churn signals, relationship risks, retention offers, account owners, and follow-up timing. Include the recommended decision, rejected alternatives, first 72-hour actions, owners, metrics, and review triggers. Keep advice bounded by the provided facts and mark anything that needs finance, legal, safety, or compliance review. Return JSON only.
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
- **Tool:** `sme_churn_rescue_desk`
- **Inputs:** `business_context`, `signal_map`, `decision_plan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Generate execution brief

**Prompt:**

```text
Use the intake, signal map, and decision plan to produce the managed SME execution brief for customer health, churn signals, relationship risks, retention offers, account owners, and follow-up timing. Respond in the same language as the user, keep assumptions visible, and make the next actions concrete.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Quality gate:** Return the managed SME shortcut response with explicit evidence gaps and owner-ready actions.
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable AI and shortcut columns are configured for manual review when the package marks `requires_review`.
- Output contracts define expected JSON shape, required fields, quality gates, and evidence policies for downstream checks.
