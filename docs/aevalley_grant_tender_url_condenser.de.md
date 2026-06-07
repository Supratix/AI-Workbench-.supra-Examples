# AE Valley Grant/Tender/Project URL Condenser

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt. Interne Spaltentitel, Tool-IDs, Prompts und Pflichtfelder bleiben als Quelldaten erhalten.

## Paketüberblick

- **Quellpaket:** [`../aevalley_grant_tender_url_condenser.supra`](../aevalley_grant_tender_url_condenser.supra)
- **Workbench-Titel:** AE Valley Grant/Tender/Project URL Condenser Desk
- **Paket-Key:** `aevalley_grant_tender_url_condenser`
- **Modul:** `aevalley_grant_tender_url_condenser`
- **Anbieter:** SupraTix
- **Schema-Version:** `1`
- **Export-/Import-Version:** `1.0.0` / `1.0.0`
- **Columns:** 17
- **Workflows:** 1
- **Commerce:** `free_of_use`, usage unit `cloud_credits`

## Zweck

Condense grant, tender, and project URLs into an evidence-backed funding and bid-readiness brief.

## Starter-Eingabe

### AE Valley Grant/Tender/Project URL Condenser starter

- **Request:** Paste the source context for AE Valley Grant/Tender/Project URL Condenser.
- **Source type:** `intake_context`

**Starter-Payload:**

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

Condense grant, tender, and project URLs into an evidence-backed funding and bid-readiness brief.

| #  | Step                        | ID                    | Backlog | Auto finished | Auto close |
| -- | --------------------------- | --------------------- | ------- | ------------- | ---------- |
| 1  | Opportunity intake          | `intake_context`      | yes     | no            | no         |
| 2  | Source URLs                 | `source_urls`         | no      | no            | no         |
| 3  | Eligibility scan            | `eligibility_scan`    | no      | no            | no         |
| 4  | Entity and partner map      | `entity_map`          | no      | no            | no         |
| 5  | Deadline map                | `deadline_map`        | no      | no            | no         |
| 6  | Funding fit                 | `funding_fit`         | no      | no            | no         |
| 7  | Consortium needs            | `consortium_needs`    | no      | no            | no         |
| 8  | Tender requirements         | `tender_requirements` | no      | no            | no         |
| 9  | Risk flags                  | `risk_flags`          | no      | no            | no         |
| 10 | Document checklist          | `document_checklist`  | no      | no            | no         |
| 11 | Bid/no-bid gate             | `no_bid_gate`         | no      | no            | no         |
| 12 | Bid strategy                | `bid_strategy`        | no      | no            | no         |
| 13 | Partner outreach            | `partner_outreach`    | no      | no            | no         |
| 14 | Budget notes                | `budget_notes`        | no      | no            | no         |
| 15 | Submission plan             | `submission_plan`     | no      | no            | no         |
| 16 | Review pack                 | `review_pack`         | no      | no            | no         |
| 17 | Condensed opportunity brief | `execution_brief`     | no      | no            | no         |

## Spalten und Tools

| #  | Key                   | Title                       | Category   | Tool                                                      | Inputs                                                                                                                                                                                                                                                                                                             | Execution       | Review | Required output                                                                        |
| -- | --------------------- | --------------------------- | ---------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------- | ------ | -------------------------------------------------------------------------------------- |
| 1  | `intake_context`      | Opportunity intake          | `manual`   | `user_input`                                              | -                                                                                                                                                                                                                                                                                                                  | `disabled`      | no     | -                                                                                      |
| 2  | `source_urls`         | Source URLs                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_source_urls`         | `intake_context`                                                                                                                                                                                                                                                                                                   | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3  | `eligibility_scan`    | Eligibility scan            | `ai_tool`  | `aevalley_grant_tender_url_condenser_eligibility_scan`    | `intake_context`<br>`source_urls`                                                                                                                                                                                                                                                                                  | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 4  | `entity_map`          | Entity and partner map      | `ai_tool`  | `aevalley_grant_tender_url_condenser_entity_map`          | `intake_context`<br>`source_urls`<br>`eligibility_scan`                                                                                                                                                                                                                                                            | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 5  | `deadline_map`        | Deadline map                | `ai_tool`  | `aevalley_grant_tender_url_condenser_deadline_map`        | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`                                                                                                                                                                                                                                            | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 6  | `funding_fit`         | Funding fit                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_funding_fit`         | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`                                                                                                                                                                                                                          | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 7  | `consortium_needs`    | Consortium needs            | `ai_tool`  | `aevalley_grant_tender_url_condenser_consortium_needs`    | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`                                                                                                                                                                                                         | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 8  | `tender_requirements` | Tender requirements         | `ai_tool`  | `aevalley_grant_tender_url_condenser_tender_requirements` | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`                                                                                                                                                                                   | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 9  | `risk_flags`          | Risk flags                  | `ai_tool`  | `aevalley_grant_tender_url_condenser_risk_flags`          | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`                                                                                                                                                          | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 10 | `document_checklist`  | Document checklist          | `ai_tool`  | `aevalley_grant_tender_url_condenser_document_checklist`  | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`                                                                                                                                          | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 11 | `no_bid_gate`         | Bid/no-bid gate             | `ai_tool`  | `aevalley_grant_tender_url_condenser_no_bid_gate`         | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`<br>`document_checklist`                                                                                                                  | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 12 | `bid_strategy`        | Bid strategy                | `ai_tool`  | `aevalley_grant_tender_url_condenser_bid_strategy`        | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`<br>`document_checklist`<br>`no_bid_gate`                                                                                                 | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 13 | `partner_outreach`    | Partner outreach            | `ai_tool`  | `aevalley_grant_tender_url_condenser_partner_outreach`    | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`<br>`document_checklist`<br>`no_bid_gate`<br>`bid_strategy`                                                                               | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 14 | `budget_notes`        | Budget notes                | `ai_tool`  | `aevalley_grant_tender_url_condenser_budget_notes`        | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`<br>`document_checklist`<br>`no_bid_gate`<br>`bid_strategy`<br>`partner_outreach`                                                         | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 15 | `submission_plan`     | Submission plan             | `ai_tool`  | `aevalley_grant_tender_url_condenser_submission_plan`     | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`<br>`document_checklist`<br>`no_bid_gate`<br>`bid_strategy`<br>`partner_outreach`<br>`budget_notes`                                       | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 16 | `review_pack`         | Review pack                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_review_pack`         | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`<br>`document_checklist`<br>`no_bid_gate`<br>`bid_strategy`<br>`partner_outreach`<br>`budget_notes`<br>`submission_plan`                  | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 17 | `execution_brief`     | Condensed opportunity brief | `shortcut` | `aevalley_grant_tender_url_condenser`                     | `intake_context`<br>`source_urls`<br>`eligibility_scan`<br>`entity_map`<br>`deadline_map`<br>`funding_fit`<br>`consortium_needs`<br>`tender_requirements`<br>`risk_flags`<br>`document_checklist`<br>`no_bid_gate`<br>`bid_strategy`<br>`partner_outreach`<br>`budget_notes`<br>`submission_plan`<br>`review_pack` | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

### Opportunity intake

- **Key:** `intake_context`
- **Tool category:** `manual`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no; label=Manual intake

No prompt is stored for this column; it calls the configured shortcut/tool directly.

### Source URLs

- **Key:** `source_urls`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_source_urls`
- **Inputs:** `intake_context`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Source URLs

**Prompt:**

```text
Use the available inputs to produce source urls for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize URLs and page-level evidence. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Eligibility scan

- **Key:** `eligibility_scan`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_eligibility_scan`
- **Inputs:** `intake_context`, `source_urls`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Eligibility scan

**Prompt:**

```text
Use the available inputs to produce eligibility scan for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize eligibility conditions and uncertainty. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Entity and partner map

- **Key:** `entity_map`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_entity_map`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Entity and partner map

**Prompt:**

```text
Use the available inputs to produce entity and partner map for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize organizations, partners, and roles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Deadline map

- **Key:** `deadline_map`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_deadline_map`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Deadline map

**Prompt:**

```text
Use the available inputs to produce deadline map for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize dates, milestones, and submission gates. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Funding fit

- **Key:** `funding_fit`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_funding_fit`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Funding fit

**Prompt:**

```text
Use the available inputs to produce funding fit for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize strategic fit and expected benefit. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Consortium needs

- **Key:** `consortium_needs`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_consortium_needs`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Consortium needs

**Prompt:**

```text
Use the available inputs to produce consortium needs for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize required partners and capabilities. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Tender requirements

- **Key:** `tender_requirements`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_tender_requirements`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Tender requirements

**Prompt:**

```text
Use the available inputs to produce tender requirements for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize formal requirements and evidence. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Risk flags

- **Key:** `risk_flags`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_risk_flags`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Risk flags

**Prompt:**

```text
Use the available inputs to produce risk flags for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize deal-breakers and compliance risks. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Document checklist

- **Key:** `document_checklist`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_document_checklist`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Document checklist

**Prompt:**

```text
Use the available inputs to produce document checklist for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize required artifacts and owners. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Bid/no-bid gate

- **Key:** `no_bid_gate`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_no_bid_gate`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`, `document_checklist`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Bid/no-bid gate

**Prompt:**

```text
Use the available inputs to produce bid/no-bid gate for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize recommendation and alternatives. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Bid strategy

- **Key:** `bid_strategy`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_bid_strategy`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`, `document_checklist`, `no_bid_gate`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Bid strategy

**Prompt:**

```text
Use the available inputs to produce bid strategy for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize win themes and work packages. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Partner outreach

- **Key:** `partner_outreach`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_partner_outreach`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`, `document_checklist`, `no_bid_gate`, `bid_strategy`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Partner outreach

**Prompt:**

```text
Use the available inputs to produce partner outreach for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize outreach list and message angles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Budget notes

- **Key:** `budget_notes`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_budget_notes`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`, `document_checklist`, `no_bid_gate`, `bid_strategy`, `partner_outreach`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Budget notes

**Prompt:**

```text
Use the available inputs to produce budget notes for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize budget assumptions and finance review. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Submission plan

- **Key:** `submission_plan`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_submission_plan`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`, `document_checklist`, `no_bid_gate`, `bid_strategy`, `partner_outreach`, `budget_notes`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Submission plan

**Prompt:**

```text
Use the available inputs to produce submission plan for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize tasks, dates, and owners. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Review pack

- **Key:** `review_pack`
- **Tool category:** `ai_tool`
- **Tool:** `aevalley_grant_tender_url_condenser_review_pack`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`, `document_checklist`, `no_bid_gate`, `bid_strategy`, `partner_outreach`, `budget_notes`, `submission_plan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Review pack

**Prompt:**

```text
Use the available inputs to produce review pack for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize human-review checklist. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Condensed opportunity brief

- **Key:** `execution_brief`
- **Tool category:** `shortcut`
- **Tool:** `aevalley_grant_tender_url_condenser`
- **Inputs:** `intake_context`, `source_urls`, `eligibility_scan`, `entity_map`, `deadline_map`, `funding_fit`, `consortium_needs`, `tender_requirements`, `risk_flags`, `document_checklist`, `no_bid_gate`, `bid_strategy`, `partner_outreach`, `budget_notes`, `submission_plan`, `review_pack`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Condensed opportunity brief

**Prompt:**

```text
Use the available inputs to produce condensed opportunity brief for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize decision-ready condensed brief. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare KI- und Shortcut-Spalten sind auf manuelle Prüfung gesetzt, wenn das Paket `requires_review` markiert.
- Output Contracts definieren erwartete JSON-Strukturen, Pflichtfelder, Quality Gates und Evidence Policies für nachgelagerte Prüfungen.
