# SME Micro-Learning Series Planner

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`packages/education_learning/sme_micro_learning_series_planner.supra`](../../packages/education_learning/sme_micro_learning_series_planner.supra)
- **Domain:** Education & Learning (`education_learning`)
- **Workbench title:** SME Micro-Learning Series Planner Desk
- **Package key:** `sme_micro_learning_series_planner`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 4
- **Workflows:** 1

## Purpose

Plan a series of short learning units for staff on a specific topic with objectives, sequencing, formats, practice tasks, and knowledge checks that fit into daily work.

## Starter Intake

### SME Micro-Learning Series Planner starter

- **Request:** Paste the source context for SME Micro-Learning Series Planner.
- **Source type:** `business_context`

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "sme_micro_learning_series_planner",
  "focus": "learning objectives, unit sequencing, formats, practice tasks, and knowledge checks",
  "intake": "Business context: Logistics company wants all 70 warehouse staff to learn the new hazardous goods handling rules. Staff have 10 minutes per shift, mixed language levels, and access to a shared tablet per team.\nCurrent situation: Inputs are incomplete, owners need an answer this week, and leadership wants visible assumptions.\nKnown constraint: Do not invent facts; mark evidence gaps and human-review items.",
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

### SME Micro-Learning Series Planner workflow

Plan a series of short learning units for staff on a specific topic with objectives, sequencing, formats, practice tasks, and knowledge checks that fit into daily work.

| # | Step             | ID                 | Backlog |
| - | ---------------- | ------------------ | ------- |
| 1 | Business context | `business_context` | yes     |
| 2 | Signal map       | `signal_map`       | no      |
| 3 | Decision plan    | `decision_plan`    | no      |
| 4 | Execution brief  | `execution_brief`  | no      |

## Columns and Tools

| # | Key                | Title            | Category   | Tool                                         | Review | Required output                                                                        |
| - | ------------------ | ---------------- | ---------- | -------------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `business_context` | Business context | `manual`   | `user_input`                                 | no     | -                                                                                      |
| 2 | `signal_map`       | Signal map       | `ai_tool`  | `sme_micro_learning_series_planner_signals`  | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `decision_plan`    | Decision plan    | `ai_tool`  | `sme_micro_learning_series_planner_decision` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 4 | `execution_brief`  | Execution brief  | `shortcut` | `sme_micro_learning_series_planner`          | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt and Contract Reference

### Business context

- **Key:** `business_context`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Signal map

- **Key:** `signal_map`
- **Tool:** `sme_micro_learning_series_planner_signals`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Analyze the SME context for learning objectives, unit sequencing, formats, practice tasks, and knowledge checks. Extract the most important facts, weak signals, constraints, assumptions, risks, and evidence gaps. Estimate likely impact qualitatively when numbers are missing. Do not invent facts. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Decision plan

- **Key:** `decision_plan`
- **Tool:** `sme_micro_learning_series_planner_decision`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Create a pragmatic owner decision plan for learning objectives, unit sequencing, formats, practice tasks, and knowledge checks. Include the recommended decision, rejected alternatives, first 72-hour actions, owners, metrics, and review triggers. Keep advice bounded by the provided facts and mark anything that needs finance, legal, safety, or compliance review. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Execution brief

- **Key:** `execution_brief`
- **Tool:** `sme_micro_learning_series_planner`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the intake, signal map, and decision plan to produce the managed SME execution brief for learning objectives, unit sequencing, formats, practice tasks, and knowledge checks. Respond in the same language as the user, keep assumptions visible, and make the next actions concrete.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
