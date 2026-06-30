# KMU Tender Factory

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`../kmu_tender_factory.supra`](../kmu_tender_factory.supra)
- **Workbench title:** Tender Factory Workbench
- **Package key:** `kmu_tender_factory`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 5
- **Workflows:** 1

## Purpose

Parse tender PDFs into a criteria-mapped proposal draft, scoring matrix, compliance checklist, and evidence bundle for SME submissions.

## Starter Intake

### KMU Tender Factory starter

- **Request:** Paste tender PDF text/OCR, evaluation criteria, company profile, and reference fragments.
- **Source type:** `tender_context`

```json
{
  "schema": "KMU_TENDER_FACTORY_INTAKE_V1",
  "use_case": "kmu_tender_factory",
  "focus": "tender PDF text, criteria, company profile, reference fragments, and evidence anchors",
  "intake": "Paste tender text/OCR plus company profile and references. Use only provided evidence. Flag mandatory gaps and human-review items.",
  "target_outputs": [
    "requirements_matrix",
    "capability_scoring",
    "proposal_draft",
    "compliance_pack"
  ],
  "acceptance_criteria": {
    "draft_turnaround_hours": 2,
    "mandatory_fields_present": true,
    "scoring_consistency": 0.9
  },
  "guardrails": [
    "Do not invent facts.",
    "Attach evidence anchors like file://ref#frag_id.",
    "Set mandatory_missing=true when any required item is absent.",
    "Keep procurement, legal, pricing, and compliance decisions human-reviewable."
  ]
}
```

## Workflow

### KMU Tender Factory workflow

Parse tender PDFs into a criteria-mapped proposal draft, scoring matrix, compliance checklist, and evidence bundle for SME submissions.

| # | Step                | ID                    | Backlog |
| - | ------------------- | --------------------- | ------- |
| 1 | Tender context      | `tender_context`      | yes     |
| 2 | Requirements matrix | `requirements_matrix` | no      |
| 3 | Capability scoring  | `capability_scoring`  | no      |
| 4 | Proposal draft      | `proposal_draft`      | no      |
| 5 | Compliance pack     | `compliance_pack`     | no      |

## Columns and Tools

| # | Key                   | Title               | Category   | Tool                              | Review | Required output                                                                                                                                         |
| - | --------------------- | ------------------- | ---------- | --------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | `tender_context`      | Tender context      | `manual`   | `user_input`                      | no     | -                                                                                                                                                       |
| 2 | `requirements_matrix` | Requirements matrix | `ai_tool`  | `kmu_tender_factory_requirements` | yes    | `summary`<br>`tender_document`<br>`evaluation_criteria`<br>`mandatory_requirements`<br>`compliance_issues`<br>`evidence_gaps`                           |
| 3 | `capability_scoring`  | Capability scoring  | `ai_tool`  | `kmu_tender_factory_matcher`      | yes    | `summary`<br>`scoring_matrix`<br>`evidence_refs`<br>`confidence`<br>`mandatory_pass`<br>`remediation_tasks`<br>`evidence_gaps`                          |
| 4 | `proposal_draft`      | Proposal draft      | `ai_tool`  | `kmu_tender_factory_proposal`     | yes    | `proposal_text`<br>`executive_summary`<br>`criteria_responses`<br>`cost_table`<br>`risk_note`<br>`mitigation_tasks`<br>`compliance_issues`              |
| 5 | `compliance_pack`     | Compliance pack     | `shortcut` | `kmu_tender_factory`              | yes    | `proposal_draft`<br>`scoring_matrix`<br>`compliance_checklist`<br>`evidence_bundle`<br>`acceptance_status`<br>`reviewer_actions`<br>`compliance_issues` |

## Prompt and Contract Reference

### Tender context

- **Key:** `tender_context`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Requirements matrix

- **Key:** `requirements_matrix`
- **Tool:** `kmu_tender_factory_requirements`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Extract tender_id, agency, submission_deadline, mandatory_requirements, budget_limit, attachments, and evaluation_criteria [{id,text,weight}] from the tender context. Flag missing mandatory fields and evidence gaps. Return JSON only.
```

- **Schema:** `KMU_TENDER_REQUIREMENTS_V1`
- **Required fields:** `summary`, `tender_document`, `evaluation_criteria`, `mandatory_requirements`, `compliance_issues`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Capability scoring

- **Key:** `capability_scoring`
- **Tool:** `kmu_tender_factory_matcher`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Match evaluation criteria to company_profile and reference_fragments. For each criterion emit criterion_id, match_sentence, evidence_refs, confidence, and remediation task. Use only provided evidence anchors. Return JSON only.
```

- **Schema:** `KMU_TENDER_SCORING_V1`
- **Required fields:** `summary`, `scoring_matrix`, `evidence_refs`, `confidence`, `mandatory_pass`, `remediation_tasks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Proposal draft

- **Key:** `proposal_draft`
- **Tool:** `kmu_tender_factory_proposal`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Act as a Procurement Response Generator. Produce proposal_text in Markdown, a max-200-word executive summary mapped to the top five weighted criteria, per-criterion evidence-backed responses, a one-page cost table, three risks, and owner mitigation tasks. Return JSON only.
```

- **Schema:** `KMU_TENDER_PROPOSAL_V1`
- **Required fields:** `proposal_text`, `executive_summary`, `criteria_responses`, `cost_table`, `risk_note`, `mitigation_tasks`, `compliance_issues`
- **Evidence policy:** `no_invented_facts`

### Compliance pack

- **Key:** `compliance_pack`
- **Tool:** `kmu_tender_factory`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Assemble the final bundle: proposal_draft target DOCX, scoring_matrix target JSON, compliance_checklist target PDF, evidence_bundle target ZIP, evidence_manifest, reviewer_actions, and bid/no-bid synopsis. Apply acceptance criteria: mandatory fields present and scoring consistency >= 0.9. Return JSON only.
```

- **Schema:** `KMU_TENDER_COMPLIANCE_PACK_V1`
- **Required fields:** `proposal_draft`, `scoring_matrix`, `compliance_checklist`, `evidence_bundle`, `acceptance_status`, `reviewer_actions`, `compliance_issues`
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
