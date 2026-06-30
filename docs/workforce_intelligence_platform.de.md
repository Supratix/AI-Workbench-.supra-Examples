# SupraWorx Workforce Intelligence Platform

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../workforce_intelligence_platform.supra`](../workforce_intelligence_platform.supra)
- **Workbench-Titel:** Workforce Intelligence Platform
- **Paket-Key:** `workforce_intelligence_platform`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 9
- **Workflows:** 1

## Zweck

Bewahrt Expertenwissen, kartiert Kompetenzrisiken und orchestriert Lern-, Nachfolge- und Recruiting-Workflows mit erklärbaren KI-Belegen.

## Starter-Eingabe

### Workforce Intelligence Platform Starter

- **Anfrage:** Fügen Sie Workforce-, Expertenwissen-, SpeakSphere-, HRIS-, LMS-, ATS-, Projekt- und SOP-Kontext für die Analyse ein.
- **Quelltyp:** `business_context`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

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

### SupraWorx Workforce Intelligence Workflow

Bewahrt Expertenwissen, kartiert Kompetenzrisiken und orchestriert Lern-, Nachfolge- und Recruiting-Workflows mit erklärbaren KI-Belegen.

| # | Schritt                  | ID                         | Backlog |
| - | ------------------------ | -------------------------- | ------- |
| 1 | Workforce intake         | `workforce_intake`         | ja      |
| 2 | SpeakSphere capture      | `speaksphere_capture`      | nein    |
| 3 | Competence graph         | `competence_graph`         | nein    |
| 4 | GraphRAG retrieval       | `graphrag_retrieval`       | nein    |
| 5 | Expert digital twins     | `expert_digital_twins`     | nein    |
| 6 | Skill gap analysis       | `skill_gap_analysis`       | nein    |
| 7 | Learning recommendations | `learning_recommendations` | nein    |
| 8 | Recruiting assistant     | `recruiting_assistant`     | nein    |
| 9 | Governance receipts      | `governance_receipts`      | nein    |

## Spalten und Tools

| # | Key                        | Titel                    | Kategorie  | Tool                                     | Prüfung | Pflichtausgabe                                                                                                                             |
| - | -------------------------- | ------------------------ | ---------- | ---------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| 1 | `workforce_intake`         | Workforce intake         | `manual`   | `user_input`                             | nein    | -                                                                                                                                          |
| 2 | `speaksphere_capture`      | SpeakSphere capture      | `ai_tool`  | `speaksphere_capture_ingest`             | ja      | `summary`<br>`normalized_sources`<br>`consent_status`<br>`retention_flags`<br>`action_receipts`<br>`evidence_gaps`                         |
| 3 | `competence_graph`         | Competence graph         | `ai_tool`  | `competence_graph_engine`                | ja      | `summary`<br>`nodes`<br>`edges`<br>`critical_skills`<br>`confidence`<br>`evidence_gaps`                                                    |
| 4 | `graphrag_retrieval`       | GraphRAG retrieval       | `ai_tool`  | `workforce_graphrag_retriever`           | ja      | `query_answer`<br>`citations`<br>`graph_paths`<br>`source_chunks`<br>`confidence`<br>`evidence_gaps`                                       |
| 5 | `expert_digital_twins`     | Expert digital twins     | `ai_tool`  | `expert_digital_twin_builder`            | ja      | `summary`<br>`expert_twins`<br>`knowledge_domains`<br>`risk_scores`<br>`transfer_tasks`<br>`explainability`                                |
| 6 | `skill_gap_analysis`       | Skill gap analysis       | `ai_tool`  | `skill_gap_risk_analyzer`                | ja      | `summary`<br>`gaps`<br>`heatmap`<br>`impact`<br>`risk_ranking`<br>`assumptions`<br>`evidence_gaps`                                         |
| 7 | `learning_recommendations` | Learning recommendations | `ai_tool`  | `learning_path_recommender`              | ja      | `summary`<br>`learning_paths`<br>`interventions`<br>`owners`<br>`metrics`<br>`checkpoints`<br>`evidence_gaps`                              |
| 8 | `recruiting_assistant`     | Recruiting assistant     | `ai_tool`  | `workforce_recruiting_assistant`         | ja      | `summary`<br>`role_scorecards`<br>`sourcing_brief`<br>`interview_rubric`<br>`bias_checks`<br>`approval_items`<br>`evidence_gaps`           |
| 9 | `governance_receipts`      | Governance receipts      | `shortcut` | `workforce_intelligence_action_receipts` | ja      | `summary`<br>`action_plan`<br>`action_receipts`<br>`explainable_ai_logs`<br>`approvals`<br>`tenant_controls`<br>`risks`<br>`evidence_gaps` |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Workforce intake

- **Key:** `workforce_intake`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### SpeakSphere capture

- **Key:** `speaksphere_capture`
- **Tool:** `speaksphere_capture_ingest`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Normalize SpeakSphere transcripts, video notes, meeting summaries, uploaded SOPs, HRIS/LMS/ATS exports, and ERP context into tenant-scoped knowledge-capture records. Preserve consent and retention flags, separate facts from inferred statements, redact sensitive personal data where policy requires it, and emit action receipts for every transformation. Return JSON only.
```

- **Schema:** `WORKFORCE_CAPTURE_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `normalized_sources`, `consent_status`, `retention_flags`, `action_receipts`, `evidence_gaps`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

### Competence graph

- **Key:** `competence_graph`
- **Tool:** `competence_graph_engine`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Build a competence graph from captured knowledge, roles, tasks, machines, projects, certificates, teams, and experts. Create nodes and edges with evidence references, confidence scores, criticality, succession risk, and tenant isolation metadata. Do not infer employment decisions; flag HR review items. Return JSON only.
```

- **Schema:** `WORKFORCE_GRAPH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `nodes`, `edges`, `critical_skills`, `confidence`, `evidence_gaps`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

### GraphRAG retrieval

- **Key:** `graphrag_retrieval`
- **Tool:** `workforce_graphrag_retriever`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Answer workforce, skill, SOP, and expert-knowledge questions using graph-aware retrieval. Traverse competence graph paths, retrieve source chunks, cite evidence IDs, expose confidence, and return a response that distinguishes verified knowledge from missing evidence. Return JSON only.
```

- **Schema:** `WORKFORCE_GRAPHRAG_OUTPUT_V1`
- **Pflichtfelder:** `query_answer`, `citations`, `graph_paths`, `source_chunks`, `confidence`, `evidence_gaps`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

### Expert digital twins

- **Key:** `expert_digital_twins`
- **Tool:** `expert_digital_twin_builder`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Create or update digital competence twins for experts using captured knowledge, skill evidence, mentoring signals, project history, and documented tacit knowledge. Produce knowledge domains, coverage, knowledge-transfer priorities, confidence explanations, and human-review flags. Return JSON only.
```

- **Schema:** `WORKFORCE_EXPERT_TWIN_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `expert_twins`, `knowledge_domains`, `risk_scores`, `transfer_tasks`, `explainability`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

### Skill gap analysis

- **Key:** `skill_gap_analysis`
- **Tool:** `skill_gap_risk_analyzer`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Compare required capabilities against available competence evidence for teams, projects, machines, compliance obligations, retirements, and growth plans. Produce role-level gaps, heatmap data, impact estimates, succession risk, assumptions, and evidence gaps. Return JSON only.
```

- **Schema:** `WORKFORCE_SKILL_GAP_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `gaps`, `heatmap`, `impact`, `risk_ranking`, `assumptions`, `evidence_gaps`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

### Learning recommendations

- **Key:** `learning_recommendations`
- **Tool:** `learning_path_recommender`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Generate targeted learning paths, mentoring interventions, capture sessions, micro-SOP assignments, certificate refreshes, and manager checkpoints. Prioritize actions that close critical skill gaps while respecting availability, budget, and compliance constraints. Return JSON only.
```

- **Schema:** `WORKFORCE_LEARNING_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `learning_paths`, `interventions`, `owners`, `metrics`, `checkpoints`, `evidence_gaps`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

### Recruiting assistant

- **Key:** `recruiting_assistant`
- **Tool:** `workforce_recruiting_assistant`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Convert unresolved skill gaps into recruiting briefs, role scorecards, interview rubrics, onboarding knowledge-capture tasks, and approval items. Include bias checks, evidence limits, and handoff notes for HR. Return JSON only.
```

- **Schema:** `WORKFORCE_RECRUITING_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `role_scorecards`, `sourcing_brief`, `interview_rubric`, `bias_checks`, `approval_items`, `evidence_gaps`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

### Governance receipts

- **Key:** `governance_receipts`
- **Tool:** `workforce_intelligence_action_receipts`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Create the managed Workforce Intelligence action plan. Include action receipts, explainable AI logs, RBAC-sensitive approvals, tenant controls, audit notes, unresolved risks, and evidence gaps. Respond in the same language as the user and keep all HR-sensitive decisions in human-review mode. Return JSON only.
```

- **Schema:** `WORKFORCE_ACTION_RECEIPT_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `action_plan`, `action_receipts`, `explainable_ai_logs`, `approvals`, `tenant_controls`, `risks`, `evidence_gaps`
- **Evidenzregel:** `tenant_scoped_grounded_evidence`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
