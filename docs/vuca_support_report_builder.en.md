# VUCA Support Report Builder

This documentation is generated from the `.supra` package content. Internal column titles, tool identifiers, prompts, and required fields are kept as source data.

## Package Overview

- **Source package:** [`../vuca_support_report_builder.supra`](../vuca_support_report_builder.supra)
- **Workbench title:** VUCA Support Report Builder Desk
- **Package key:** `vuca_support_report_builder`
- **Module:** `vuca_support_report_builder`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Export / import version:** `1.0.0` / `1.0.0`
- **Columns:** 15
- **Workflows:** 1
- **Commerce:** `free_of_use`, usage unit `cloud_credits`

## Purpose

Build a structured support report for volatile, uncertain, complex, and ambiguous operating contexts.

## Starter Intake

### VUCA Support Report Builder starter

- **Request:** Paste the source context for VUCA Support Report Builder.
- **Source type:** `intake_context`

**Starter payload:**

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "vuca_support_report_builder",
  "focus": "facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting",
  "intake": "Situation: Supplier interruption, customer deadlines at risk, conflicting signals from logistics partners. Need: board-ready support report with scenarios and owner actions.",
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

### VUCA Support Report Builder workflow

Build a structured support report for volatile, uncertain, complex, and ambiguous operating contexts.

| #  | Step                        | ID                  | Backlog | Auto finished | Auto close |
| -- | --------------------------- | ------------------- | ------- | ------------- | ---------- |
| 1  | Situation intake            | `intake_context`    | yes     | no            | no         |
| 2  | Facts map                   | `facts_map`         | no      | no            | no         |
| 3  | Weak signal map             | `signal_map`        | no      | no            | no         |
| 4  | Stakeholder map             | `stakeholder_map`   | no      | no            | no         |
| 5  | VUCA assessment             | `vuca_assessment`   | no      | no            | no         |
| 6  | Scenario options            | `scenario_options`  | no      | no            | no         |
| 7  | Risk register               | `risk_register`     | no      | no            | no         |
| 8  | Response strategy           | `response_strategy` | no      | no            | no         |
| 9  | Message map                 | `message_map`       | no      | no            | no         |
| 10 | Action plan                 | `action_plan`       | no      | no            | no         |
| 11 | Owner matrix                | `owner_matrix`      | no      | no            | no         |
| 12 | Metric board                | `metric_board`      | no      | no            | no         |
| 13 | Review calendar             | `review_calendar`   | no      | no            | no         |
| 14 | Compliance and safety check | `compliance_check`  | no      | no            | no         |
| 15 | Support report              | `execution_brief`   | no      | no            | no         |

## Columns and Tools

| #  | Key                 | Title                       | Category   | Tool                                            | Inputs                                                                                                                                                                                                                                                                     | Execution       | Review | Required output                                                                        |
| -- | ------------------- | --------------------------- | ---------- | ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------ | -------------------------------------------------------------------------------------- |
| 1  | `intake_context`    | Situation intake            | `manual`   | `user_input`                                    | -                                                                                                                                                                                                                                                                          | `disabled`      | no     | -                                                                                      |
| 2  | `facts_map`         | Facts map                   | `ai_tool`  | `vuca_support_report_builder_facts_map`         | `intake_context`                                                                                                                                                                                                                                                           | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3  | `signal_map`        | Weak signal map             | `ai_tool`  | `vuca_support_report_builder_signal_map`        | `intake_context`<br>`facts_map`                                                                                                                                                                                                                                            | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 4  | `stakeholder_map`   | Stakeholder map             | `ai_tool`  | `vuca_support_report_builder_stakeholder_map`   | `intake_context`<br>`facts_map`<br>`signal_map`                                                                                                                                                                                                                            | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 5  | `vuca_assessment`   | VUCA assessment             | `ai_tool`  | `vuca_support_report_builder_vuca_assessment`   | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`                                                                                                                                                                                                       | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 6  | `scenario_options`  | Scenario options            | `ai_tool`  | `vuca_support_report_builder_scenario_options`  | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`                                                                                                                                                                                  | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 7  | `risk_register`     | Risk register               | `ai_tool`  | `vuca_support_report_builder_risk_register`     | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`                                                                                                                                                            | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 8  | `response_strategy` | Response strategy           | `ai_tool`  | `vuca_support_report_builder_response_strategy` | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`                                                                                                                                         | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 9  | `message_map`       | Message map                 | `ai_tool`  | `vuca_support_report_builder_message_map`       | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`<br>`response_strategy`                                                                                                                  | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 10 | `action_plan`       | Action plan                 | `ai_tool`  | `vuca_support_report_builder_action_plan`       | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`<br>`response_strategy`<br>`message_map`                                                                                                 | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 11 | `owner_matrix`      | Owner matrix                | `ai_tool`  | `vuca_support_report_builder_owner_matrix`      | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`<br>`response_strategy`<br>`message_map`<br>`action_plan`                                                                                | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 12 | `metric_board`      | Metric board                | `ai_tool`  | `vuca_support_report_builder_metric_board`      | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`<br>`response_strategy`<br>`message_map`<br>`action_plan`<br>`owner_matrix`                                                              | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 13 | `review_calendar`   | Review calendar             | `ai_tool`  | `vuca_support_report_builder_review_calendar`   | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`<br>`response_strategy`<br>`message_map`<br>`action_plan`<br>`owner_matrix`<br>`metric_board`                                            | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 14 | `compliance_check`  | Compliance and safety check | `ai_tool`  | `vuca_support_report_builder_compliance_check`  | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`<br>`response_strategy`<br>`message_map`<br>`action_plan`<br>`owner_matrix`<br>`metric_board`<br>`review_calendar`                       | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 15 | `execution_brief`   | Support report              | `shortcut` | `vuca_support_report_builder`                   | `intake_context`<br>`facts_map`<br>`signal_map`<br>`stakeholder_map`<br>`vuca_assessment`<br>`scenario_options`<br>`risk_register`<br>`response_strategy`<br>`message_map`<br>`action_plan`<br>`owner_matrix`<br>`metric_board`<br>`review_calendar`<br>`compliance_check` | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt and Contract Reference

### Situation intake

- **Key:** `intake_context`
- **Tool category:** `manual`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no; label=Manual intake

No prompt is stored for this column; it calls the configured shortcut/tool directly.

### Facts map

- **Key:** `facts_map`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_facts_map`
- **Inputs:** `intake_context`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Facts map

**Prompt:**

```text
Use the available inputs to produce facts map for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize verified facts and source gaps. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Weak signal map

- **Key:** `signal_map`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_signal_map`
- **Inputs:** `intake_context`, `facts_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Weak signal map

**Prompt:**

```text
Use the available inputs to produce weak signal map for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize early indicators and contradictory signals. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Stakeholder map

- **Key:** `stakeholder_map`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_stakeholder_map`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Stakeholder map

**Prompt:**

```text
Use the available inputs to produce stakeholder map for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize affected groups and decision rights. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### VUCA assessment

- **Key:** `vuca_assessment`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_vuca_assessment`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=VUCA assessment

**Prompt:**

```text
Use the available inputs to produce vuca assessment for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize volatility, uncertainty, complexity, ambiguity. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Scenario options

- **Key:** `scenario_options`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_scenario_options`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Scenario options

**Prompt:**

```text
Use the available inputs to produce scenario options for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize plausible scenarios and triggers. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Risk register

- **Key:** `risk_register`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_risk_register`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Risk register

**Prompt:**

```text
Use the available inputs to produce risk register for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize risks, likelihood, impact, and controls. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Response strategy

- **Key:** `response_strategy`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_response_strategy`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Response strategy

**Prompt:**

```text
Use the available inputs to produce response strategy for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize response posture and trade-offs. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Message map

- **Key:** `message_map`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_message_map`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`, `response_strategy`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Message map

**Prompt:**

```text
Use the available inputs to produce message map for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize stakeholder messaging and caveats. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Action plan

- **Key:** `action_plan`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_action_plan`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`, `response_strategy`, `message_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Action plan

**Prompt:**

```text
Use the available inputs to produce action plan for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize first actions and owners. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Owner matrix

- **Key:** `owner_matrix`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_owner_matrix`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`, `response_strategy`, `message_map`, `action_plan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Owner matrix

**Prompt:**

```text
Use the available inputs to produce owner matrix for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize decision owners and support roles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Metric board

- **Key:** `metric_board`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_metric_board`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`, `response_strategy`, `message_map`, `action_plan`, `owner_matrix`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Metric board

**Prompt:**

```text
Use the available inputs to produce metric board for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize signals to monitor. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Review calendar

- **Key:** `review_calendar`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_review_calendar`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`, `response_strategy`, `message_map`, `action_plan`, `owner_matrix`, `metric_board`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Review calendar

**Prompt:**

```text
Use the available inputs to produce review calendar for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize cadence and escalation gates. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Compliance and safety check

- **Key:** `compliance_check`
- **Tool category:** `ai_tool`
- **Tool:** `vuca_support_report_builder_compliance_check`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`, `response_strategy`, `message_map`, `action_plan`, `owner_matrix`, `metric_board`, `review_calendar`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Compliance and safety check

**Prompt:**

```text
Use the available inputs to produce compliance and safety check for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize regulated review items. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Support report

- **Key:** `execution_brief`
- **Tool category:** `shortcut`
- **Tool:** `vuca_support_report_builder`
- **Inputs:** `intake_context`, `facts_map`, `signal_map`, `stakeholder_map`, `vuca_assessment`, `scenario_options`, `risk_register`, `response_strategy`, `message_map`, `action_plan`, `owner_matrix`, `metric_board`, `review_calendar`, `compliance_check`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Support report

**Prompt:**

```text
Use the available inputs to produce support report for facts, weak signals, stakeholders, uncertainty, scenarios, mitigation actions, owner matrix, and support reporting. Emphasize board-ready report. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable AI and shortcut columns are configured for manual review when the package marks `requires_review`.
- Output contracts define expected JSON shape, required fields, quality gates, and evidence policies for downstream checks.
