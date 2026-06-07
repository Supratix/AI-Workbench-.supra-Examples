# AE Valley Grant/Tender/Project URL Condenser

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Source package:** [`../aevalley_grant_tender_url_condenser.supra`](../aevalley_grant_tender_url_condenser.supra)
- **Workbench title:** AE Valley Grant/Tender/Project URL Condenser Desk
- **Package key:** `aevalley_grant_tender_url_condenser`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 17
- **Workflows:** 1

## Zweck

Turn grant, tender, and project URLs into a compact evidence brief that summarizes fit, bid readiness, funding risks, and next validation steps.

## Starter-Eingabe

### AE Valley Grant/Tender/Project URL Condenser starter

- **Request:** Paste the source context for AE Valley Grant/Tender/Project URL Condenser.
- **Source type:** `intake_context`

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "aevalley_grant_tender_url_condenser",
  "focus": "grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership",
  "intake": "URLs: https://example.org/grant-a, https://example.org/tender-b. Organization: SME manufacturer. Goal: decide whether to pursue within 5 business days. Constraint: mark eligibility assumptions.",
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

### AE Valley Grant/Tender/Project URL Condenser workflow

Turn grant, tender, and project URLs into a compact evidence brief that summarizes fit, bid readiness, funding risks, and next validation steps.

| #  | Step                        | ID                    | Backlog |
| -- | --------------------------- | --------------------- | ------- |
| 1  | Opportunity intake          | `intake_context`      | yes     |
| 2  | Source URLs                 | `source_urls`         | no      |
| 3  | Eligibility scan            | `eligibility_scan`    | no      |
| 4  | Entity and partner map      | `entity_map`          | no      |
| 5  | Deadline map                | `deadline_map`        | no      |
| 6  | Funding fit                 | `funding_fit`         | no      |
| 7  | Consortium needs            | `consortium_needs`    | no      |
| 8  | Tender requirements         | `tender_requirements` | no      |
| 9  | Risk flags                  | `risk_flags`          | no      |
| 10 | Document checklist          | `document_checklist`  | no      |
| 11 | Bid/no-bid gate             | `no_bid_gate`         | no      |
| 12 | Bid strategy                | `bid_strategy`        | no      |
| 13 | Partner outreach            | `partner_outreach`    | no      |
| 14 | Budget notes                | `budget_notes`        | no      |
| 15 | Submission plan             | `submission_plan`     | no      |
| 16 | Review pack                 | `review_pack`         | no      |
| 17 | Condensed opportunity brief | `execution_brief`     | no      |

## Spalten und Tools

| #  | Key                   | Title                       | Category   | Tool                                                      | Review | Required output                                                                        |
| -- | --------------------- | --------------------------- | ---------- | --------------------------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| 1  | `intake_context`      | Opportunity intake          | `manual`   | `user_input`                                              | no     | -                                                                                      |
| 2  | `source_urls`         | Source URLs                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_source_urls`         | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3  | `eligibility_scan`    | Eligibility scan            | `ai_tool`  | `aevalley_grant_tender_url_condenser_eligibility_scan`    | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 4  | `entity_map`          | Entity and partner map      | `ai_tool`  | `aevalley_grant_tender_url_condenser_entity_map`          | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 5  | `deadline_map`        | Deadline map                | `ai_tool`  | `aevalley_grant_tender_url_condenser_deadline_map`        | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 6  | `funding_fit`         | Funding fit                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_funding_fit`         | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 7  | `consortium_needs`    | Consortium needs            | `ai_tool`  | `aevalley_grant_tender_url_condenser_consortium_needs`    | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 8  | `tender_requirements` | Tender requirements         | `ai_tool`  | `aevalley_grant_tender_url_condenser_tender_requirements` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 9  | `risk_flags`          | Risk flags                  | `ai_tool`  | `aevalley_grant_tender_url_condenser_risk_flags`          | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 10 | `document_checklist`  | Document checklist          | `ai_tool`  | `aevalley_grant_tender_url_condenser_document_checklist`  | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 11 | `no_bid_gate`         | Bid/no-bid gate             | `ai_tool`  | `aevalley_grant_tender_url_condenser_no_bid_gate`         | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 12 | `bid_strategy`        | Bid strategy                | `ai_tool`  | `aevalley_grant_tender_url_condenser_bid_strategy`        | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 13 | `partner_outreach`    | Partner outreach            | `ai_tool`  | `aevalley_grant_tender_url_condenser_partner_outreach`    | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 14 | `budget_notes`        | Budget notes                | `ai_tool`  | `aevalley_grant_tender_url_condenser_budget_notes`        | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 15 | `submission_plan`     | Submission plan             | `ai_tool`  | `aevalley_grant_tender_url_condenser_submission_plan`     | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 16 | `review_pack`         | Review pack                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_review_pack`         | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 17 | `execution_brief`     | Condensed opportunity brief | `shortcut` | `aevalley_grant_tender_url_condenser`                     | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

### Opportunity intake

- **Key:** `intake_context`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Source URLs

- **Key:** `source_urls`
- **Tool:** `aevalley_grant_tender_url_condenser_source_urls`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce source urls for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize URLs and page-level evidence. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Eligibility scan

- **Key:** `eligibility_scan`
- **Tool:** `aevalley_grant_tender_url_condenser_eligibility_scan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce eligibility scan for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize eligibility conditions and uncertainty. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Entity and partner map

- **Key:** `entity_map`
- **Tool:** `aevalley_grant_tender_url_condenser_entity_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce entity and partner map for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize organizations, partners, and roles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Deadline map

- **Key:** `deadline_map`
- **Tool:** `aevalley_grant_tender_url_condenser_deadline_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce deadline map for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize dates, milestones, and submission gates. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Funding fit

- **Key:** `funding_fit`
- **Tool:** `aevalley_grant_tender_url_condenser_funding_fit`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce funding fit for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize strategic fit and expected benefit. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Consortium needs

- **Key:** `consortium_needs`
- **Tool:** `aevalley_grant_tender_url_condenser_consortium_needs`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce consortium needs for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize required partners and capabilities. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Tender requirements

- **Key:** `tender_requirements`
- **Tool:** `aevalley_grant_tender_url_condenser_tender_requirements`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce tender requirements for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize formal requirements and evidence. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Risk flags

- **Key:** `risk_flags`
- **Tool:** `aevalley_grant_tender_url_condenser_risk_flags`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce risk flags for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize deal-breakers and compliance risks. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Document checklist

- **Key:** `document_checklist`
- **Tool:** `aevalley_grant_tender_url_condenser_document_checklist`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce document checklist for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize required artifacts and owners. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Bid/no-bid gate

- **Key:** `no_bid_gate`
- **Tool:** `aevalley_grant_tender_url_condenser_no_bid_gate`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce bid/no-bid gate for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize recommendation and alternatives. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Bid strategy

- **Key:** `bid_strategy`
- **Tool:** `aevalley_grant_tender_url_condenser_bid_strategy`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce bid strategy for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize win themes and work packages. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Partner outreach

- **Key:** `partner_outreach`
- **Tool:** `aevalley_grant_tender_url_condenser_partner_outreach`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce partner outreach for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize outreach list and message angles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Budget notes

- **Key:** `budget_notes`
- **Tool:** `aevalley_grant_tender_url_condenser_budget_notes`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce budget notes for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize budget assumptions and finance review. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Submission plan

- **Key:** `submission_plan`
- **Tool:** `aevalley_grant_tender_url_condenser_submission_plan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce submission plan for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize tasks, dates, and owners. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Review pack

- **Key:** `review_pack`
- **Tool:** `aevalley_grant_tender_url_condenser_review_pack`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce review pack for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize human-review checklist. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Condensed opportunity brief

- **Key:** `execution_brief`
- **Tool:** `aevalley_grant_tender_url_condenser`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Use the available inputs to produce condensed opportunity brief for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize decision-ready condensed brief. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

## Governance-Hinweise

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
