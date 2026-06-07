# MINT Study Planning

This documentation is generated from the `.supra` package content.

## Package Overview

- **Source package:** [`../mint_study_planning.supra`](../mint_study_planning.supra)
- **Workbench title:** MINT Study Planning Desk
- **Package key:** `mint_study_planning`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 4
- **Workflows:** 1

## Purpose

Generate structured MINT/STEM study plans from learner goals, baseline skills, schedule, constraints, milestones, resources, and assessments.

## Starter Intake

### MINT Study Planning starter

- **Request:** Paste the learner profile, learning goals, dates, weekly hours, and constraints for MINT Study Planning.
- **Source type:** `learner_context`

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

### MINT Study Planning workflow

Generate structured MINT/STEM study plans from learner goals, baseline skills, schedule, constraints, milestones, resources, and assessments.

| # | Step                 | ID                     | Backlog |
| - | -------------------- | ---------------------- | ------- |
| 1 | Learner context      | `learner_context`      | yes     |
| 2 | Curriculum blueprint | `curriculum_blueprint` | no      |
| 3 | Weekly study plan    | `weekly_study_plan`    | no      |
| 4 | Validation pack      | `validation_pack`      | no      |

## Columns and Tools

| # | Key                    | Title                | Category   | Tool                            | Review | Required output                                                                                         |
| - | ---------------------- | -------------------- | ---------- | ------------------------------- | ------ | ------------------------------------------------------------------------------------------------------- |
| 1 | `learner_context`      | Learner context      | `manual`   | `user_input`                    | no     | -                                                                                                       |
| 2 | `curriculum_blueprint` | Curriculum blueprint | `ai_tool`  | `mint_study_planning_blueprint` | yes    | `summary`<br>`learner_profile`<br>`learning_goals`<br>`constraints`<br>`assumptions`<br>`evidence_gaps` |
| 3 | `weekly_study_plan`    | Weekly study plan    | `ai_tool`  | `mint_study_planning_weeks`     | yes    | `summary`<br>`meta`<br>`week_by_week`<br>`milestones`<br>`resources`<br>`evidence_gaps`                 |
| 4 | `validation_pack`      | Validation pack      | `shortcut` | `mint_study_planning`           | yes    | `study_plan`<br>`one_pager`                                                                             |

## Prompt and Contract Reference

### Learner context

- **Key:** `learner_context`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Curriculum blueprint

- **Key:** `curriculum_blueprint`
- **Tool:** `mint_study_planning_blueprint`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Analyze the MINT study-planning intake. Extract learner role, baseline skills, weekly availability, preferred modalities, learning goals, start date, duration, equipment, budget or accreditation constraints, safety considerations, assumptions, and evidence gaps. Normalize these into a curriculum blueprint that is practical for a semester-style plan. Do not invent facts. Return JSON only.
```

- **Schema:** `MINT_STUDYPLAN_BLUEPRINT_OUTPUT_V1`
- **Required fields:** `summary`, `learner_profile`, `learning_goals`, `constraints`, `assumptions`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Weekly study plan

- **Key:** `weekly_study_plan`
- **Tool:** `mint_study_planning_weeks`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Using the learner context and curriculum blueprint, build a week-by-week MINT study plan. Include meta{plan_id,start_date,duration_weeks,target_role}, week_by_week entries with integer time_est_h, milestones with pass_criteria, assessments with criteria, and resources with resource_uri. Keep resource recommendations pragmatic, label low-cost alternatives when budget is constrained, and mark assumptions or evidence gaps. Return JSON only.
```

- **Schema:** `MINT_STUDYPLAN_WEEKLY_OUTPUT_V1`
- **Required fields:** `summary`, `meta`, `week_by_week`, `milestones`, `resources`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Validation pack

- **Key:** `validation_pack`
- **Tool:** `mint_study_planning`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Produce the final MINT Study Planning output. Return exactly a JSON object with study_plan and one_pager. study_plan must include meta{plan_id,start_date,duration_weeks,target_role}, week_by_week[], milestones[] with pass_criteria, assessments[], and resources[] with resource_uri. The one_pager must be concise enough for a grant annex or pilot syllabus summary. Keep recommendations evidence-based, pragmatic, and reviewable.
```

- **Schema:** `MINT_STUDYPLAN_FINAL_OUTPUT_V1`
- **Required fields:** `study_plan`, `one_pager`
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
