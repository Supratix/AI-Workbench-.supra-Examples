# Field Service Maintenance Report

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`../field_service_maintenance_report.supra`](../field_service_maintenance_report.supra)
- **Workbench title:** Field Service Maintenance Report Desk
- **Package key:** `field_service_maintenance_report`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 4
- **Workflows:** 1

## Purpose

Turn technician voice notes or transcripts into a traceable maintenance report and customer summary.

## Starter Intake

### Field Service Maintenance Report starter

- **Request:** Paste a technician transcript, audio URI, checklist, photo references, and job metadata.
- **Source type:** `field_service_context`

```json
{
  "schema": "FIELD_SERVICE_MAINTENANCE_INTAKE_V1",
  "job_id": "J-2026-045",
  "asset_id": "HVAC-22",
  "audio_uri": "",
  "transcript": "Arrived on site. Checked filter, replaced with part F123. Test run 10 minutes. No leaks detected. Safety: observed minor corrosion at valve 3. Photos: [\"https://files.example/snap1.jpg\"]",
  "checklist": [
    "Confirm asset",
    "Record steps",
    "Capture parts",
    "Note issues",
    "Create summary"
  ],
  "photos": [
    "https://files.example/snap1.jpg"
  ],
  "guardrails": [
    "Do not invent facts.",
    "Preserve part numbers.",
    "Capture uncertainty."
  ],
  "target_outputs": [
    "evidence",
    "report",
    "summary"
  ]
}
```

## Workflow

### Field Service Maintenance Report workflow

Turn technician voice notes or transcripts into a traceable maintenance report and customer summary.

| # | Step                 | ID                     | Backlog |
| - | -------------------- | ---------------------- | ------- |
| 1 | Service intake       | `service_intake`       | yes     |
| 2 | Transcribed evidence | `transcribed_evidence` | no      |
| 3 | Maintenance report   | `maintenance_report`   | no      |
| 4 | Customer summary     | `customer_summary`     | no      |

## Columns and Tools

| # | Key                    | Title                | Category   | Tool                                        | Review | Required output                                                                                                                             |
| - | ---------------------- | -------------------- | ---------- | ------------------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | `service_intake`       | Service intake       | `manual`   | `user_input`                                | no     | -                                                                                                                                           |
| 2 | `transcribed_evidence` | Transcribed evidence | `ai_tool`  | `field_service_maintenance_report_evidence` | yes    | `job_id`<br>`asset_id`<br>`source_list`<br>`transcript_text`<br>`checklist_items`<br>`photo_uris`<br>`uncertainty_terms`<br>`evidence_gaps` |
| 3 | `maintenance_report`   | Maintenance report   | `ai_tool`  | `field_service_maintenance_report_codex`    | yes    | `job_report`<br>`summary`                                                                                                                   |
| 4 | `customer_summary`     | Customer summary     | `shortcut` | `field_service_maintenance_report`          | yes    | `summary`<br>`attachments`<br>`validation_assertions`<br>`evidence_gaps`                                                                    |

## Prompt and Contract Reference

### Service intake

- **Key:** `service_intake`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Transcribed evidence

- **Key:** `transcribed_evidence`
- **Tool:** `field_service_maintenance_report_evidence`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Extract job_id, asset_id, sources, transcript text, checklist items, photo URIs, uncertainty terms, and evidence gaps. Preserve part numbers. Return JSON only.
```

- **Schema:** `FIELD_SERVICE_EVIDENCE_OUTPUT_V1`
- **Required fields:** `job_id`, `asset_id`, `source_list`, `transcript_text`, `checklist_items`, `photo_uris`, `uncertainty_terms`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Maintenance report

- **Key:** `maintenance_report`
- **Tool:** `field_service_maintenance_report_codex`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Return one JSON object with job_report and summary. job_report must include job_id, asset_id, ordered steps, parts_used, time_minutes, issues, safety_flags, completed, signature, provenance, and assumptions. Preserve explicit part numbers and integer durations.
```

- **Schema:** `FIELD_SERVICE_MAINTENANCE_REPORT_OUTPUT_V1`
- **Required fields:** `job_report`, `summary`
- **Evidence policy:** `traceable_sources_required`

### Customer summary

- **Key:** `customer_summary`
- **Tool:** `field_service_maintenance_report`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Create a one-sentence customer summary plus JSON/PDF export checklist. Preserve part numbers and flag delivery-blocking evidence gaps. Return JSON only.
```

- **Schema:** `FIELD_SERVICE_CUSTOMER_SUMMARY_OUTPUT_V1`
- **Required fields:** `summary`, `attachments`, `validation_assertions`, `evidence_gaps`
- **Evidence policy:** `traceable_sources_required`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
