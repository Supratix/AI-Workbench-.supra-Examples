# MINT Study Planning

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../mint_study_planning.supra`](../mint_study_planning.supra)
- **Workbench-Titel:** MINT Study Planning Desk
- **Paket-Key:** `mint_study_planning`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 4
- **Workflows:** 1

## Zweck

Erstellt strukturierte MINT/STEM-Lernpläne aus Lernzielen, Ausgangskompetenzen, Zeitplan, Einschränkungen, Meilensteinen, Ressourcen und Assessments.

## Starter-Eingabe

### MINT Study Planning Starter

- **Anfrage:** Fügen Sie das Lernendenprofil, die Lernziele, Termine, Wochenstunden und Einschränkungen für MINT Study Planning ein.
- **Quelltyp:** `learner_context`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

```json
{
  "schema": "MINT_STUDYPLAN_INTAKE_V1",
  "use_case": "mint_study_planning",
  "plan_id": "MINT-EDU-2026-01",
  "learner_profile": {
    "role": "early-career lab technician",
    "baseline_skills": [
      "basic physics",
      "basic electronics"
    ],
    "weekly_hours": 6,
    "preferred_modalities": [
      "hands-on",
      "micro-lectures"
    ]
  },
  "learning_goals": [
    "understand sensors and transducers",
    "perform basic data acquisition and analysis"
  ],
  "start_date": "2026-09-01",
  "duration_weeks": 12,
  "constraints": {
    "budget": "low",
    "equipment": [
      "multimeter",
      "Raspberry Pi"
    ]
  },
  "guardrails": [
    "Do not invent learner facts.",
    "Mark assumptions and evidence gaps.",
    "Include measurable pass criteria for every milestone.",
    "Add low-cost alternatives when budget is constrained."
  ],
  "target_outputs": [
    "curriculum_blueprint",
    "weekly_study_plan",
    "validation_pack"
  ]
}
```

## Workflow

### MINT Study Planning Workflow

Erstellt strukturierte MINT/STEM-Lernpläne aus Lernzielen, Ausgangskompetenzen, Zeitplan, Einschränkungen, Meilensteinen, Ressourcen und Assessments.

| # | Schritt              | ID                     | Backlog |
| - | -------------------- | ---------------------- | ------- |
| 1 | Learner context      | `learner_context`      | ja      |
| 2 | Curriculum blueprint | `curriculum_blueprint` | nein    |
| 3 | Weekly study plan    | `weekly_study_plan`    | nein    |
| 4 | Validation pack      | `validation_pack`      | nein    |

## Spalten und Tools

| # | Key                    | Titel                | Kategorie  | Tool                            | Prüfung | Pflichtausgabe                                                                                          |
| - | ---------------------- | -------------------- | ---------- | ------------------------------- | ------- | ------------------------------------------------------------------------------------------------------- |
| 1 | `learner_context`      | Learner context      | `manual`   | `user_input`                    | nein    | -                                                                                                       |
| 2 | `curriculum_blueprint` | Curriculum blueprint | `ai_tool`  | `mint_study_planning_blueprint` | ja      | `summary`<br>`learner_profile`<br>`learning_goals`<br>`constraints`<br>`assumptions`<br>`evidence_gaps` |
| 3 | `weekly_study_plan`    | Weekly study plan    | `ai_tool`  | `mint_study_planning_weeks`     | ja      | `summary`<br>`meta`<br>`week_by_week`<br>`milestones`<br>`resources`<br>`evidence_gaps`                 |
| 4 | `validation_pack`      | Validation pack      | `shortcut` | `mint_study_planning`           | ja      | `study_plan`<br>`one_pager`                                                                             |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Learner context

- **Key:** `learner_context`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### Curriculum blueprint

- **Key:** `curriculum_blueprint`
- **Tool:** `mint_study_planning_blueprint`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Analyze the MINT study-planning intake. Extract learner role, baseline skills, weekly availability, preferred modalities, learning goals, start date, duration, equipment, budget or accreditation constraints, safety considerations, assumptions, and evidence gaps. Normalize these into a curriculum blueprint that is practical for a semester-style plan. Do not invent facts. Return JSON only.
```

- **Schema:** `MINT_STUDYPLAN_BLUEPRINT_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `learner_profile`, `learning_goals`, `constraints`, `assumptions`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Weekly study plan

- **Key:** `weekly_study_plan`
- **Tool:** `mint_study_planning_weeks`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Using the learner context and curriculum blueprint, build a week-by-week MINT study plan. Include meta{plan_id,start_date,duration_weeks,target_role}, week_by_week entries with integer time_est_h, milestones with pass_criteria, assessments with criteria, and resources with resource_uri. Keep resource recommendations pragmatic, label low-cost alternatives when budget is constrained, and mark assumptions or evidence gaps. Return JSON only.
```

- **Schema:** `MINT_STUDYPLAN_WEEKLY_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `meta`, `week_by_week`, `milestones`, `resources`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Validation pack

- **Key:** `validation_pack`
- **Tool:** `mint_study_planning`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Produce the final MINT Study Planning output. Return exactly a JSON object with study_plan and one_pager. study_plan must include meta{plan_id,start_date,duration_weeks,target_role}, week_by_week[], milestones[] with pass_criteria, assessments[], and resources[] with resource_uri. The one_pager must be concise enough for a grant annex or pilot syllabus summary. Keep recommendations evidence-based, pragmatic, and reviewable.
```

- **Schema:** `MINT_STUDYPLAN_FINAL_OUTPUT_V1`
- **Pflichtfelder:** `study_plan`, `one_pager`
- **Evidenzregel:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
