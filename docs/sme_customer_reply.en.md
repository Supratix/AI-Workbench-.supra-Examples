# SME Customer Reply

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`../sme_customer_reply.supra`](../sme_customer_reply.supra)
- **Workbench title:** SME Customer Reply Desk
- **Package key:** `sme_customer_reply`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 4
- **Workflows:** 1

## Purpose

Draft a professional customer response that balances tone, facts, evidence gaps, commitments, and follow-up checks for sensitive service situations.

## Starter Intake

### SME Customer Reply starter

- **Request:** Paste the source context for SME Customer Reply.
- **Source type:** `business_context`

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "sme_customer_reply",
  "focus": "customer intent, relationship risk, response tone, promised facts, and follow-up ownership",
  "intake": "Customer message: We are unhappy with the delayed delivery and need an answer today.\nContext: Shipment left two days late, tracking is now active, account is strategic.\nConstraint: Do not offer discounts without approval.",
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

### SME Customer Reply workflow

Draft a professional customer response that balances tone, facts, evidence gaps, commitments, and follow-up checks for sensitive service situations.

| # | Step             | ID                 | Backlog |
| - | ---------------- | ------------------ | ------- |
| 1 | Customer message | `business_context` | yes     |
| 2 | Signal map       | `signal_map`       | no      |
| 3 | Decision plan    | `decision_plan`    | no      |
| 4 | Reply draft      | `execution_brief`  | no      |

## Columns and Tools

| # | Key                | Title            | Category   | Tool                          | Review | Required output                                                                        |
| - | ------------------ | ---------------- | ---------- | ----------------------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `business_context` | Customer message | `manual`   | `user_input`                  | no     | -                                                                                      |
| 2 | `signal_map`       | Signal map       | `ai_tool`  | `sme_customer_reply_signals`  | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `decision_plan`    | Decision plan    | `ai_tool`  | `sme_customer_reply_decision` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 4 | `execution_brief`  | Reply draft      | `shortcut` | `sme_customer_reply`          | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt and Contract Reference

### Customer message

- **Key:** `business_context`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Signal map

- **Key:** `signal_map`
- **Tool:** `sme_customer_reply_signals`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Analyze the SME context for customer intent, relationship risk, response tone, promised facts, and follow-up ownership. Extract the most important facts, weak signals, constraints, assumptions, risks, and evidence gaps. Estimate likely impact qualitatively when numbers are missing. Do not invent facts. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Decision plan

- **Key:** `decision_plan`
- **Tool:** `sme_customer_reply_decision`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Create a pragmatic owner decision plan for customer intent, relationship risk, response tone, promised facts, and follow-up ownership. Include the recommended decision, rejected alternatives, first 72-hour actions, owners, metrics, and review triggers. Keep advice bounded by the provided facts and mark anything that needs finance, legal, safety, or compliance review. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Reply draft

- **Key:** `execution_brief`
- **Tool:** `sme_customer_reply`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the intake, signal map, and decision plan to produce the managed SME execution brief for customer intent, relationship risk, response tone, promised facts, and follow-up ownership. Respond in the same language as the user, keep assumptions visible, and make the next actions concrete.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
