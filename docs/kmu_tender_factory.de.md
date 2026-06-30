# KMU Tender Factory

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../kmu_tender_factory.supra`](../kmu_tender_factory.supra)
- **Workbench-Titel:** Tender Factory Workbench
- **Paket-Key:** `kmu_tender_factory`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 5
- **Workflows:** 1

## Zweck

Analysiert Ausschreibungs-PDFs und erstellt für KMU-Angebote einen kriterienbasierten Angebotsentwurf, eine Bewertungsmatrix, eine Compliance-Checkliste und ein Evidenzpaket.

## Starter-Eingabe

### KMU Tender Factory Starter

- **Anfrage:** Fügen Sie Ausschreibungs-PDF-Text oder OCR, Bewertungskriterien, Unternehmensprofil und Referenzfragmente ein.
- **Quelltyp:** `tender_context`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

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

### KMU Tender Factory Workflow

Analysiert Ausschreibungs-PDFs und erstellt für KMU-Angebote einen kriterienbasierten Angebotsentwurf, eine Bewertungsmatrix, eine Compliance-Checkliste und ein Evidenzpaket.

| # | Schritt             | ID                    | Backlog |
| - | ------------------- | --------------------- | ------- |
| 1 | Tender context      | `tender_context`      | ja      |
| 2 | Requirements matrix | `requirements_matrix` | nein    |
| 3 | Capability scoring  | `capability_scoring`  | nein    |
| 4 | Proposal draft      | `proposal_draft`      | nein    |
| 5 | Compliance pack     | `compliance_pack`     | nein    |

## Spalten und Tools

| # | Key                   | Titel               | Kategorie  | Tool                              | Prüfung | Pflichtausgabe                                                                                                                                          |
| - | --------------------- | ------------------- | ---------- | --------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | `tender_context`      | Tender context      | `manual`   | `user_input`                      | nein    | -                                                                                                                                                       |
| 2 | `requirements_matrix` | Requirements matrix | `ai_tool`  | `kmu_tender_factory_requirements` | ja      | `summary`<br>`tender_document`<br>`evaluation_criteria`<br>`mandatory_requirements`<br>`compliance_issues`<br>`evidence_gaps`                           |
| 3 | `capability_scoring`  | Capability scoring  | `ai_tool`  | `kmu_tender_factory_matcher`      | ja      | `summary`<br>`scoring_matrix`<br>`evidence_refs`<br>`confidence`<br>`mandatory_pass`<br>`remediation_tasks`<br>`evidence_gaps`                          |
| 4 | `proposal_draft`      | Proposal draft      | `ai_tool`  | `kmu_tender_factory_proposal`     | ja      | `proposal_text`<br>`executive_summary`<br>`criteria_responses`<br>`cost_table`<br>`risk_note`<br>`mitigation_tasks`<br>`compliance_issues`              |
| 5 | `compliance_pack`     | Compliance pack     | `shortcut` | `kmu_tender_factory`              | ja      | `proposal_draft`<br>`scoring_matrix`<br>`compliance_checklist`<br>`evidence_bundle`<br>`acceptance_status`<br>`reviewer_actions`<br>`compliance_issues` |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Tender context

- **Key:** `tender_context`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### Requirements matrix

- **Key:** `requirements_matrix`
- **Tool:** `kmu_tender_factory_requirements`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Extract tender_id, agency, submission_deadline, mandatory_requirements, budget_limit, attachments, and evaluation_criteria [{id,text,weight}] from the tender context. Flag missing mandatory fields and evidence gaps. Return JSON only.
```

- **Schema:** `KMU_TENDER_REQUIREMENTS_V1`
- **Pflichtfelder:** `summary`, `tender_document`, `evaluation_criteria`, `mandatory_requirements`, `compliance_issues`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Capability scoring

- **Key:** `capability_scoring`
- **Tool:** `kmu_tender_factory_matcher`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Match evaluation criteria to company_profile and reference_fragments. For each criterion emit criterion_id, match_sentence, evidence_refs, confidence, and remediation task. Use only provided evidence anchors. Return JSON only.
```

- **Schema:** `KMU_TENDER_SCORING_V1`
- **Pflichtfelder:** `summary`, `scoring_matrix`, `evidence_refs`, `confidence`, `mandatory_pass`, `remediation_tasks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Proposal draft

- **Key:** `proposal_draft`
- **Tool:** `kmu_tender_factory_proposal`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Act as a Procurement Response Generator. Produce proposal_text in Markdown, a max-200-word executive summary mapped to the top five weighted criteria, per-criterion evidence-backed responses, a one-page cost table, three risks, and owner mitigation tasks. Return JSON only.
```

- **Schema:** `KMU_TENDER_PROPOSAL_V1`
- **Pflichtfelder:** `proposal_text`, `executive_summary`, `criteria_responses`, `cost_table`, `risk_note`, `mitigation_tasks`, `compliance_issues`
- **Evidenzregel:** `no_invented_facts`

### Compliance pack

- **Key:** `compliance_pack`
- **Tool:** `kmu_tender_factory`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Assemble the final bundle: proposal_draft target DOCX, scoring_matrix target JSON, compliance_checklist target PDF, evidence_bundle target ZIP, evidence_manifest, reviewer_actions, and bid/no-bid synopsis. Apply acceptance criteria: mandatory fields present and scoring consistency >= 0.9. Return JSON only.
```

- **Schema:** `KMU_TENDER_COMPLIANCE_PACK_V1`
- **Pflichtfelder:** `proposal_draft`, `scoring_matrix`, `compliance_checklist`, `evidence_bundle`, `acceptance_status`, `reviewer_actions`, `compliance_issues`
- **Evidenzregel:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
