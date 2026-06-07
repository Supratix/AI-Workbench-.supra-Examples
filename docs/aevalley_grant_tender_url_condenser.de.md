# AE Valley Grant/Tender/Project URL Condenser

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../aevalley_grant_tender_url_condenser.supra`](../aevalley_grant_tender_url_condenser.supra)
- **Workbench-Titel:** AE Valley Grant/Tender/Project URL Condenser Desk
- **Paket-Key:** `aevalley_grant_tender_url_condenser`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 17
- **Workflows:** 1

## Zweck

Verdichtet Förder-, Ausschreibungs- und Projekt-URLs zu einem kompakten Evidenz-Briefing mit Fit, Angebotsreife, Finanzierungsrisiken und nächsten Validierungsschritten.

## Starter-Eingabe

### AE Valley Grant/Tender/Project URL Condenser Starter

- **Anfrage:** Fügen Sie den Quellkontext für AE Valley Grant/Tender/Project URL Condenser ein.
- **Quelltyp:** `intake_context`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

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

### AE Valley Grant/Tender/Project URL Condenser Workflow

Verdichtet Förder-, Ausschreibungs- und Projekt-URLs zu einem kompakten Evidenz-Briefing mit Fit, Angebotsreife, Finanzierungsrisiken und nächsten Validierungsschritten.

| #  | Schritt                     | ID                    | Backlog |
| -- | --------------------------- | --------------------- | ------- |
| 1  | Opportunity intake          | `intake_context`      | ja      |
| 2  | Source URLs                 | `source_urls`         | nein    |
| 3  | Eligibility scan            | `eligibility_scan`    | nein    |
| 4  | Entity and partner map      | `entity_map`          | nein    |
| 5  | Deadline map                | `deadline_map`        | nein    |
| 6  | Funding fit                 | `funding_fit`         | nein    |
| 7  | Consortium needs            | `consortium_needs`    | nein    |
| 8  | Tender requirements         | `tender_requirements` | nein    |
| 9  | Risk flags                  | `risk_flags`          | nein    |
| 10 | Document checklist          | `document_checklist`  | nein    |
| 11 | Bid/no-bid gate             | `no_bid_gate`         | nein    |
| 12 | Bid strategy                | `bid_strategy`        | nein    |
| 13 | Partner outreach            | `partner_outreach`    | nein    |
| 14 | Budget notes                | `budget_notes`        | nein    |
| 15 | Submission plan             | `submission_plan`     | nein    |
| 16 | Review pack                 | `review_pack`         | nein    |
| 17 | Condensed opportunity brief | `execution_brief`     | nein    |

## Spalten und Tools

| #  | Key                   | Titel                       | Kategorie  | Tool                                                      | Prüfung | Pflichtausgabe                                                                         |
| -- | --------------------- | --------------------------- | ---------- | --------------------------------------------------------- | ------- | -------------------------------------------------------------------------------------- |
| 1  | `intake_context`      | Opportunity intake          | `manual`   | `user_input`                                              | nein    | -                                                                                      |
| 2  | `source_urls`         | Source URLs                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_source_urls`         | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3  | `eligibility_scan`    | Eligibility scan            | `ai_tool`  | `aevalley_grant_tender_url_condenser_eligibility_scan`    | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 4  | `entity_map`          | Entity and partner map      | `ai_tool`  | `aevalley_grant_tender_url_condenser_entity_map`          | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 5  | `deadline_map`        | Deadline map                | `ai_tool`  | `aevalley_grant_tender_url_condenser_deadline_map`        | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 6  | `funding_fit`         | Funding fit                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_funding_fit`         | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 7  | `consortium_needs`    | Consortium needs            | `ai_tool`  | `aevalley_grant_tender_url_condenser_consortium_needs`    | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 8  | `tender_requirements` | Tender requirements         | `ai_tool`  | `aevalley_grant_tender_url_condenser_tender_requirements` | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 9  | `risk_flags`          | Risk flags                  | `ai_tool`  | `aevalley_grant_tender_url_condenser_risk_flags`          | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 10 | `document_checklist`  | Document checklist          | `ai_tool`  | `aevalley_grant_tender_url_condenser_document_checklist`  | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 11 | `no_bid_gate`         | Bid/no-bid gate             | `ai_tool`  | `aevalley_grant_tender_url_condenser_no_bid_gate`         | ja      | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 12 | `bid_strategy`        | Bid strategy                | `ai_tool`  | `aevalley_grant_tender_url_condenser_bid_strategy`        | ja      | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 13 | `partner_outreach`    | Partner outreach            | `ai_tool`  | `aevalley_grant_tender_url_condenser_partner_outreach`    | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 14 | `budget_notes`        | Budget notes                | `ai_tool`  | `aevalley_grant_tender_url_condenser_budget_notes`        | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 15 | `submission_plan`     | Submission plan             | `ai_tool`  | `aevalley_grant_tender_url_condenser_submission_plan`     | ja      | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 16 | `review_pack`         | Review pack                 | `ai_tool`  | `aevalley_grant_tender_url_condenser_review_pack`         | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 17 | `execution_brief`     | Condensed opportunity brief | `shortcut` | `aevalley_grant_tender_url_condenser`                     | ja      | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Opportunity intake

- **Key:** `intake_context`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### Source URLs

- **Key:** `source_urls`
- **Tool:** `aevalley_grant_tender_url_condenser_source_urls`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce source urls for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize URLs and page-level evidence. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Eligibility scan

- **Key:** `eligibility_scan`
- **Tool:** `aevalley_grant_tender_url_condenser_eligibility_scan`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce eligibility scan for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize eligibility conditions and uncertainty. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Entity and partner map

- **Key:** `entity_map`
- **Tool:** `aevalley_grant_tender_url_condenser_entity_map`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce entity and partner map for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize organizations, partners, and roles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Deadline map

- **Key:** `deadline_map`
- **Tool:** `aevalley_grant_tender_url_condenser_deadline_map`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce deadline map for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize dates, milestones, and submission gates. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Funding fit

- **Key:** `funding_fit`
- **Tool:** `aevalley_grant_tender_url_condenser_funding_fit`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce funding fit for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize strategic fit and expected benefit. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Consortium needs

- **Key:** `consortium_needs`
- **Tool:** `aevalley_grant_tender_url_condenser_consortium_needs`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce consortium needs for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize required partners and capabilities. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Tender requirements

- **Key:** `tender_requirements`
- **Tool:** `aevalley_grant_tender_url_condenser_tender_requirements`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce tender requirements for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize formal requirements and evidence. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Risk flags

- **Key:** `risk_flags`
- **Tool:** `aevalley_grant_tender_url_condenser_risk_flags`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce risk flags for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize deal-breakers and compliance risks. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Document checklist

- **Key:** `document_checklist`
- **Tool:** `aevalley_grant_tender_url_condenser_document_checklist`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce document checklist for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize required artifacts and owners. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Bid/no-bid gate

- **Key:** `no_bid_gate`
- **Tool:** `aevalley_grant_tender_url_condenser_no_bid_gate`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce bid/no-bid gate for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize recommendation and alternatives. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Bid strategy

- **Key:** `bid_strategy`
- **Tool:** `aevalley_grant_tender_url_condenser_bid_strategy`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce bid strategy for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize win themes and work packages. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Partner outreach

- **Key:** `partner_outreach`
- **Tool:** `aevalley_grant_tender_url_condenser_partner_outreach`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce partner outreach for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize outreach list and message angles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Budget notes

- **Key:** `budget_notes`
- **Tool:** `aevalley_grant_tender_url_condenser_budget_notes`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce budget notes for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize budget assumptions and finance review. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Submission plan

- **Key:** `submission_plan`
- **Tool:** `aevalley_grant_tender_url_condenser_submission_plan`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce submission plan for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize tasks, dates, and owners. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Review pack

- **Key:** `review_pack`
- **Tool:** `aevalley_grant_tender_url_condenser_review_pack`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce review pack for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize human-review checklist. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Condensed opportunity brief

- **Key:** `execution_brief`
- **Tool:** `aevalley_grant_tender_url_condenser`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Use the available inputs to produce condensed opportunity brief for grant fit, eligibility, deadlines, source URLs, required documents, bid/no-bid logic, and submission ownership. Emphasize decision-ready condensed brief. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
