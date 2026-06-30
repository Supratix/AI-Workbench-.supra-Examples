# Field Service Maintenance Report

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../field_service_maintenance_report.supra`](../field_service_maintenance_report.supra)
- **Workbench-Titel:** Field Service Maintenance Report Desk
- **Paket-Key:** `field_service_maintenance_report`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 4
- **Workflows:** 1

## Zweck

Wandelt Technikernotizen oder Transkripte in einen nachvollziehbaren Wartungsbericht mit Kunden-Zusammenfassung um.

## Starter-Eingabe

### Field Service Maintenance Report Starter

- **Anfrage:** Fügen Sie ein Technikertranskript, eine Audio-URI, eine Checkliste, Fotoverweise und Auftragsmetadaten ein.
- **Quelltyp:** `field_service_context`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

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

### Field Service Maintenance Report Workflow

Wandelt Technikernotizen oder Transkripte in einen nachvollziehbaren Wartungsbericht mit Kunden-Zusammenfassung um.

| # | Schritt              | ID                     | Backlog |
| - | -------------------- | ---------------------- | ------- |
| 1 | Service intake       | `service_intake`       | ja      |
| 2 | Transcribed evidence | `transcribed_evidence` | nein    |
| 3 | Maintenance report   | `maintenance_report`   | nein    |
| 4 | Customer summary     | `customer_summary`     | nein    |

## Spalten und Tools

| # | Key                    | Titel                | Kategorie  | Tool                                        | Prüfung | Pflichtausgabe                                                                                                                              |
| - | ---------------------- | -------------------- | ---------- | ------------------------------------------- | ------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| 1 | `service_intake`       | Service intake       | `manual`   | `user_input`                                | nein    | -                                                                                                                                           |
| 2 | `transcribed_evidence` | Transcribed evidence | `ai_tool`  | `field_service_maintenance_report_evidence` | ja      | `job_id`<br>`asset_id`<br>`source_list`<br>`transcript_text`<br>`checklist_items`<br>`photo_uris`<br>`uncertainty_terms`<br>`evidence_gaps` |
| 3 | `maintenance_report`   | Maintenance report   | `ai_tool`  | `field_service_maintenance_report_codex`    | ja      | `job_report`<br>`summary`                                                                                                                   |
| 4 | `customer_summary`     | Customer summary     | `shortcut` | `field_service_maintenance_report`          | ja      | `summary`<br>`attachments`<br>`validation_assertions`<br>`evidence_gaps`                                                                    |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Service intake

- **Key:** `service_intake`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### Transcribed evidence

- **Key:** `transcribed_evidence`
- **Tool:** `field_service_maintenance_report_evidence`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Extract job_id, asset_id, sources, transcript text, checklist items, photo URIs, uncertainty terms, and evidence gaps. Preserve part numbers. Return JSON only.
```

- **Schema:** `FIELD_SERVICE_EVIDENCE_OUTPUT_V1`
- **Pflichtfelder:** `job_id`, `asset_id`, `source_list`, `transcript_text`, `checklist_items`, `photo_uris`, `uncertainty_terms`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Maintenance report

- **Key:** `maintenance_report`
- **Tool:** `field_service_maintenance_report_codex`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Return one JSON object with job_report and summary. job_report must include job_id, asset_id, ordered steps, parts_used, time_minutes, issues, safety_flags, completed, signature, provenance, and assumptions. Preserve explicit part numbers and integer durations.
```

- **Schema:** `FIELD_SERVICE_MAINTENANCE_REPORT_OUTPUT_V1`
- **Pflichtfelder:** `job_report`, `summary`
- **Evidenzregel:** `traceable_sources_required`

### Customer summary

- **Key:** `customer_summary`
- **Tool:** `field_service_maintenance_report`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Create a one-sentence customer summary plus JSON/PDF export checklist. Preserve part numbers and flag delivery-blocking evidence gaps. Return JSON only.
```

- **Schema:** `FIELD_SERVICE_CUSTOMER_SUMMARY_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `attachments`, `validation_assertions`, `evidence_gaps`
- **Evidenzregel:** `traceable_sources_required`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
