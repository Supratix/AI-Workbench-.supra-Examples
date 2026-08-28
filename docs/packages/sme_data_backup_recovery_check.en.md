# SME Backup And Recovery Check

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`packages/it_digital_data/sme_data_backup_recovery_check.supra`](../../packages/it_digital_data/sme_data_backup_recovery_check.supra)
- **Domain:** IT, Digital & Data (`it_digital_data`)
- **Workbench title:** SME Backup And Recovery Check Desk
- **Package key:** `sme_data_backup_recovery_check`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 4
- **Workflows:** 1

## Purpose

Assess backup coverage, frequency, retention, offsite copies, and restore testing against the company's tolerance for data loss and downtime, and propose a prioritized fix list.

## Starter Intake

### SME Backup And Recovery Check starter

- **Request:** Paste the source context for SME Backup And Recovery Check.
- **Source type:** `business_context`

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "sme_data_backup_recovery_check",
  "focus": "backup coverage, recovery objectives, offsite copies, restore testing, and prioritized fixes",
  "intake": "Business context: Architecture office stores project files on a NAS with nightly backup to a USB drive kept in the same room. Cloud email is not backed up. Last restore test: never. Acceptable data loss per owner: one day.\nCurrent situation: Inputs are incomplete, owners need an answer this week, and leadership wants visible assumptions.\nKnown constraint: Do not invent facts; mark evidence gaps and human-review items.",
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

### SME Backup And Recovery Check workflow

Assess backup coverage, frequency, retention, offsite copies, and restore testing against the company's tolerance for data loss and downtime, and propose a prioritized fix list.

| # | Step             | ID                 | Backlog |
| - | ---------------- | ------------------ | ------- |
| 1 | Business context | `business_context` | yes     |
| 2 | Signal map       | `signal_map`       | no      |
| 3 | Decision plan    | `decision_plan`    | no      |
| 4 | Execution brief  | `execution_brief`  | no      |

## Columns and Tools

| # | Key                | Title            | Category   | Tool                                      | Review | Required output                                                                        |
| - | ------------------ | ---------------- | ---------- | ----------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `business_context` | Business context | `manual`   | `user_input`                              | no     | -                                                                                      |
| 2 | `signal_map`       | Signal map       | `ai_tool`  | `sme_data_backup_recovery_check_signals`  | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `decision_plan`    | Decision plan    | `ai_tool`  | `sme_data_backup_recovery_check_decision` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 4 | `execution_brief`  | Execution brief  | `shortcut` | `sme_data_backup_recovery_check`          | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt and Contract Reference

### Business context

- **Key:** `business_context`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Signal map

- **Key:** `signal_map`
- **Tool:** `sme_data_backup_recovery_check_signals`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Analyze the SME context for backup coverage, recovery objectives, offsite copies, restore testing, and prioritized fixes. Extract the most important facts, weak signals, constraints, assumptions, risks, and evidence gaps. Estimate likely impact qualitatively when numbers are missing. Do not invent facts. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Decision plan

- **Key:** `decision_plan`
- **Tool:** `sme_data_backup_recovery_check_decision`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Create a pragmatic owner decision plan for backup coverage, recovery objectives, offsite copies, restore testing, and prioritized fixes. Include the recommended decision, rejected alternatives, first 72-hour actions, owners, metrics, and review triggers. Keep advice bounded by the provided facts and mark anything that needs finance, legal, safety, or compliance review. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Execution brief

- **Key:** `execution_brief`
- **Tool:** `sme_data_backup_recovery_check`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the intake, signal map, and decision plan to produce the managed SME execution brief for backup coverage, recovery objectives, offsite copies, restore testing, and prioritized fixes. Respond in the same language as the user, keep assumptions visible, and make the next actions concrete.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
