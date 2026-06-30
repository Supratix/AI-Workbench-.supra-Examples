# SME ESG Sustainability Copilot

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`../sme_esg_sustainability_copilot.supra`](../sme_esg_sustainability_copilot.supra)
- **Workbench title:** SME ESG Sustainability Copilot Desk
- **Package key:** `sme_esg_sustainability_copilot`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 3
- **Workflows:** 1

## Purpose

Consolidate sustainability evidence into an ESG readiness scorecard, gap analysis and action plan.

## Starter Intake

### starter

- **Request:** 
- **Source type:** `business_context`

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1"
}
```

## Workflow

### 



| # | Step | ID                 | Backlog |
| - | ---- | ------------------ | ------- |
| 1 |      | `business_context` | no      |
| 2 |      | `esg_evidence_map` | no      |
| 3 |      | `reporting_brief`  | no      |

## Columns and Tools

| # | Key                | Title            | Category   | Tool                             | Review | Required output |
| - | ------------------ | ---------------- | ---------- | -------------------------------- | ------ | --------------- |
| 1 | `business_context` | Business context | `manual`   | `user_input`                     | no     | -               |
| 2 | `esg_evidence_map` | ESG evidence map | `ai_tool`  | `sme_esg_evidence`               | yes    | `summary`       |
| 3 | `reporting_brief`  | Reporting brief  | `shortcut` | `sme_esg_sustainability_copilot` | yes    | `summary`       |

## Prompt and Contract Reference

### Business context

- **Key:** `business_context`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### ESG evidence map

- **Key:** `esg_evidence_map`
- **Tool:** `sme_esg_evidence`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`
- **Evidence policy:** `no_invented_facts`

### Reporting brief

- **Key:** `reporting_brief`
- **Tool:** `sme_esg_sustainability_copilot`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Required fields:** `summary`
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
