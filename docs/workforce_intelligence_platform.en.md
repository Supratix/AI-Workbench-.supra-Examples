# SupraWorx Workforce Intelligence Platform

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`../workforce_intelligence_platform.supra`](../workforce_intelligence_platform.supra)
- **Workbench title:** Workforce Intelligence Platform
- **Package key:** `workforce_intelligence_platform`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 9
- **Workflows:** 1

## Purpose

Preserve expert knowledge, map competency risk, and orchestrate learning, succession, and recruiting workflows with explainable AI receipts.

## Starter Intake

### Workforce Intelligence Platform starter

- **Request:** Paste workforce, expert-knowledge, SpeakSphere, HRIS, LMS, ATS, project, and SOP context for analysis.
- **Source type:** `business_context`

```json
{
  "schema": "SUPRAWORX_WORKFORCE_INTAKE_V1",
  "tenant": {
    "id": "demo_sme",
    "region": "EU",
    "rbac_profile": "hr_ops"
  },
  "use_case": "knowledge_preservation_and_skill_gap_intelligence",
  "focus": "SpeakSphere capture, competence graph, GraphRAG retrieval, expert digital twins, learning paths, skill gap analysis, recruiting assistant, action receipts, explainable logs",
  "intake": "Experts are approaching retirement, knowledge is fragmented across meetings, SOPs, videos, and ERP records, and leadership needs a tenant-scoped plan for capture, training, succession, and hiring.",
  "sources": [
    "SpeakSphere transcript",
    "expert video",
    "SOP document",
    "LMS export",
    "ATS pipeline",
    "HRIS skills",
    "ERP project history"
  ],
  "guardrails": [
    "Do not invent facts.",
    "Keep personal and HR-sensitive outputs tenant-scoped and RBAC-protected.",
    "Separate evidence from assumptions and confidence estimates.",
    "Mark all employment, compensation, compliance, and sensitive people decisions for responsible human review.",
    "Produce action receipts for transformations, recommendations, and approvals."
  ],
  "target_outputs": [
    "competence_graph",
    "expert_digital_twins",
    "skill_gap_heatmap",
    "learning_paths",
    "recruiting_brief",
    "governance_receipts"
  ]
}
```

## Workflow

### SupraWorx Workforce Intelligence workflow

Preserve expert knowledge, map competency risk, and orchestrate learning, succession, and recruiting workflows with explainable AI receipts.

| # | Step | ID | Backlog |
| - | ---- | -- | ------- |
| 1 | Workforce intake | `workforce_intake` | yes |
| 2 | SpeakSphere capture | `speaksphere_capture` | no |
| 3 | Competence graph | `competence_graph` | no |
| 4 | GraphRAG retrieval | `graphrag_retrieval` | no |
| 5 | Expert digital twins | `expert_digital_twins` | no |
| 6 | Skill gap analysis | `skill_gap_analysis` | no |
| 7 | Learning recommendations | `learning_recommendations` | no |
| 8 | Recruiting assistant | `recruiting_assistant` | no |
| 9 | Governance receipts | `governance_receipts` | no |

## Columns and Tools

| # | Key | Title | Category | Tool | Review | Required output |
| - | --- | ----- | -------- | ---- | ------ | --------------- |
| 1 | `workforce_intake` | Workforce intake | `manual` | `user_input` | no | - |
| 2 | `speaksphere_capture` | SpeakSphere capture | `ai_tool` | `speaksphere_capture_ingest` | yes | `summary`, `normalized_sources`, `consent_status`, `retention_flags`, `action_receipts`, `evidence_gaps` |
| 3 | `competence_graph` | Competence graph | `ai_tool` | `competence_graph_engine` | yes | `summary`, `nodes`, `edges`, `critical_skills`, `confidence`, `evidence_gaps` |
| 4 | `graphrag_retrieval` | GraphRAG retrieval | `ai_tool` | `workforce_graphrag_retriever` | yes | `query_answer`, `citations`, `graph_paths`, `source_chunks`, `confidence`, `evidence_gaps` |
| 5 | `expert_digital_twins` | Expert digital twins | `ai_tool` | `expert_digital_twin_builder` | yes | `summary`, `expert_twins`, `knowledge_domains`, `risk_scores`, `transfer_tasks`, `explainability` |
| 6 | `skill_gap_analysis` | Skill gap analysis | `ai_tool` | `skill_gap_risk_analyzer` | yes | `summary`, `gaps`, `heatmap`, `impact`, `risk_ranking`, `assumptions`, `evidence_gaps` |
| 7 | `learning_recommendations` | Learning recommendations | `ai_tool` | `learning_path_recommender` | yes | `summary`, `learning_paths`, `interventions`, `owners`, `metrics`, `checkpoints`, `evidence_gaps` |
| 8 | `recruiting_assistant` | Recruiting assistant | `ai_tool` | `workforce_recruiting_assistant` | yes | `summary`, `role_scorecards`, `sourcing_brief`, `interview_rubric`, `bias_checks`, `approval_items`, `evidence_gaps` |
| 9 | `governance_receipts` | Governance receipts | `shortcut` | `workforce_intelligence_action_receipts` | yes | `summary`, `action_plan`, `action_receipts`, `explainable_ai_logs`, `approvals`, `tenant_controls`, `risks`, `evidence_gaps` |

## Prompt and Contract Reference

### SpeakSphere capture

```text
Normalize SpeakSphere transcripts, video notes, meeting summaries, uploaded SOPs, HRIS/LMS/ATS exports, and ERP context into tenant-scoped knowledge-capture records. Preserve consent and retention flags, separate facts from inferred statements, redact sensitive personal data where policy requires it, and emit action receipts for every transformation. Return JSON only.
```

- **Schema:** `WORKFORCE_CAPTURE_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

### Competence graph

```text
Build a competence graph from captured knowledge, roles, tasks, machines, projects, certificates, teams, and experts. Create nodes and edges with evidence references, confidence scores, criticality, succession risk, and tenant isolation metadata. Do not infer employment decisions; flag HR review items. Return JSON only.
```

- **Schema:** `WORKFORCE_GRAPH_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

### GraphRAG retrieval

```text
Answer workforce, skill, SOP, and expert-knowledge questions using graph-aware retrieval. Traverse competence graph paths, retrieve source chunks, cite evidence IDs, expose confidence, and return a response that distinguishes verified knowledge from missing evidence. Return JSON only.
```

- **Schema:** `WORKFORCE_GRAPHRAG_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

### Expert digital twins

```text
Create or update digital competence twins for experts using captured knowledge, skill evidence, mentoring signals, project history, and documented tacit knowledge. Produce knowledge domains, coverage, knowledge-transfer priorities, confidence explanations, and human-review flags. Return JSON only.
```

- **Schema:** `WORKFORCE_EXPERT_TWIN_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

### Skill gap analysis

```text
Compare required capabilities against available competence evidence for teams, projects, machines, compliance obligations, retirements, and growth plans. Produce role-level gaps, heatmap data, impact estimates, succession risk, assumptions, and evidence gaps. Return JSON only.
```

- **Schema:** `WORKFORCE_SKILL_GAP_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

### Learning recommendations

```text
Generate targeted learning paths, mentoring interventions, capture sessions, micro-SOP assignments, certificate refreshes, and manager checkpoints. Prioritize actions that close critical skill gaps while respecting availability, budget, and compliance constraints. Return JSON only.
```

- **Schema:** `WORKFORCE_LEARNING_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

### Recruiting assistant

```text
Convert unresolved skill gaps into recruiting briefs, role scorecards, interview rubrics, onboarding knowledge-capture tasks, and approval items. Include bias checks, evidence limits, and handoff notes for HR. Return JSON only.
```

- **Schema:** `WORKFORCE_RECRUITING_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

### Governance receipts

```text
Create the managed Workforce Intelligence action plan. Include action receipts, explainable AI logs, RBAC-sensitive approvals, tenant controls, audit notes, unresolved risks, and evidence gaps. Respond in the same language as the user and keep all HR-sensitive decisions in human-review mode. Return JSON only.
```

- **Schema:** `WORKFORCE_ACTION_RECEIPT_OUTPUT_V1`
- **Evidence policy:** `tenant_scoped_grounded_evidence`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review.
- Output contracts keep downstream checks predictable.
- HR-sensitive recommendations remain reviewable by responsible humans.
- Tenant isolation, RBAC, action receipts, and explainable AI logs are first-class requirements in the reference implementation.
