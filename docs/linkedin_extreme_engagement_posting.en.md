# LinkedIn Extreme Engagement Posting

This documentation is generated from the `.supra` package content. Internal column titles, tool identifiers, prompts, and required fields are kept as source data.

## Package Overview

- **Source package:** [`../linkedin_extreme_engagement_posting.supra`](../linkedin_extreme_engagement_posting.supra)
- **Workbench title:** LinkedIn Extreme Engagement Posting Desk
- **Package key:** `linkedin_extreme_engagement_posting`
- **Module:** `linkedin_extreme_engagement_posting`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Export / import version:** `1.0.0` / `1.0.0`
- **Columns:** 9
- **Workflows:** 1
- **Commerce:** `free_of_use`, usage unit `cloud_credits`

## Purpose

Create a high-engagement LinkedIn post package with hooks, post copy, risk checks, and engagement follow-up.

## Starter Intake

### LinkedIn Extreme Engagement Posting starter

- **Request:** Paste the source context for LinkedIn Extreme Engagement Posting.
- **Source type:** `content_goal`

**Starter payload:**

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "linkedin_extreme_engagement_posting",
  "focus": "audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks",
  "intake": "Topic: Why most SME AI pilots fail after the demo. Audience: owners and operators. Position: start with measurable workflow pain, not tools. Constraint: provocative but respectful.",
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

### LinkedIn Extreme Engagement Posting workflow

Create a high-engagement LinkedIn post package with hooks, post copy, risk checks, and engagement follow-up.

| # | Step                   | ID                | Backlog | Auto finished | Auto close |
| - | ---------------------- | ----------------- | ------- | ------------- | ---------- |
| 1 | Content goal           | `content_goal`    | yes     | no            | no         |
| 2 | Audience signal map    | `audience_signal` | no      | no            | no         |
| 3 | Trend scan             | `trend_scan`      | no      | no            | no         |
| 4 | Hook bank              | `hook_bank`       | no      | no            | no         |
| 5 | Post draft             | `post_draft`      | no      | no            | no         |
| 6 | Engagement plan        | `engagement_plan` | no      | no            | no         |
| 7 | Tone and risk check    | `risk_check`      | no      | no            | no         |
| 8 | Publishing plan        | `publishing_plan` | no      | no            | no         |
| 9 | Final LinkedIn package | `execution_brief` | no      | no            | no         |

## Columns and Tools

| # | Key               | Title                  | Category   | Tool                                                  | Inputs                                                                                                                                       | Execution       | Review | Required output                                                                        |
| - | ----------------- | ---------------------- | ---------- | ----------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | --------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `content_goal`    | Content goal           | `manual`   | `user_input`                                          | -                                                                                                                                            | `disabled`      | no     | -                                                                                      |
| 2 | `audience_signal` | Audience signal map    | `ai_tool`  | `linkedin_extreme_engagement_posting_audience_signal` | `content_goal`                                                                                                                               | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `trend_scan`      | Trend scan             | `ai_tool`  | `linkedin_extreme_engagement_posting_trend_scan`      | `content_goal`<br>`audience_signal`                                                                                                          | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 4 | `hook_bank`       | Hook bank              | `ai_tool`  | `linkedin_extreme_engagement_posting_hook_bank`       | `content_goal`<br>`audience_signal`<br>`trend_scan`                                                                                          | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 5 | `post_draft`      | Post draft             | `ai_tool`  | `linkedin_extreme_engagement_posting_post_draft`      | `content_goal`<br>`audience_signal`<br>`trend_scan`<br>`hook_bank`                                                                           | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 6 | `engagement_plan` | Engagement plan        | `ai_tool`  | `linkedin_extreme_engagement_posting_engagement_plan` | `content_goal`<br>`audience_signal`<br>`trend_scan`<br>`hook_bank`<br>`post_draft`                                                           | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 7 | `risk_check`      | Tone and risk check    | `ai_tool`  | `linkedin_extreme_engagement_posting_risk_check`      | `content_goal`<br>`audience_signal`<br>`trend_scan`<br>`hook_bank`<br>`post_draft`<br>`engagement_plan`                                      | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 8 | `publishing_plan` | Publishing plan        | `ai_tool`  | `linkedin_extreme_engagement_posting_publishing_plan` | `content_goal`<br>`audience_signal`<br>`trend_scan`<br>`hook_bank`<br>`post_draft`<br>`engagement_plan`<br>`risk_check`                      | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`metrics`<br>`risks`<br>`evidence_gaps`        |
| 9 | `execution_brief` | Final LinkedIn package | `shortcut` | `linkedin_extreme_engagement_posting`                 | `content_goal`<br>`audience_signal`<br>`trend_scan`<br>`hook_bank`<br>`post_draft`<br>`engagement_plan`<br>`risk_check`<br>`publishing_plan` | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt and Contract Reference

### Content goal

- **Key:** `content_goal`
- **Tool category:** `manual`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no; label=Manual intake

No prompt is stored for this column; it calls the configured shortcut/tool directly.

### Audience signal map

- **Key:** `audience_signal`
- **Tool category:** `ai_tool`
- **Tool:** `linkedin_extreme_engagement_posting_audience_signal`
- **Inputs:** `content_goal`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Audience signal map

**Prompt:**

```text
Use the available inputs to produce audience signal map for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize audience pain and urgency. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Trend scan

- **Key:** `trend_scan`
- **Tool category:** `ai_tool`
- **Tool:** `linkedin_extreme_engagement_posting_trend_scan`
- **Inputs:** `content_goal`, `audience_signal`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Trend scan

**Prompt:**

```text
Use the available inputs to produce trend scan for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize relevant zeitgeist without unsupported claims. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Hook bank

- **Key:** `hook_bank`
- **Tool category:** `ai_tool`
- **Tool:** `linkedin_extreme_engagement_posting_hook_bank`
- **Inputs:** `content_goal`, `audience_signal`, `trend_scan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Hook bank

**Prompt:**

```text
Use the available inputs to produce hook bank for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize clear, punchy hooks. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Post draft

- **Key:** `post_draft`
- **Tool category:** `ai_tool`
- **Tool:** `linkedin_extreme_engagement_posting_post_draft`
- **Inputs:** `content_goal`, `audience_signal`, `trend_scan`, `hook_bank`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Post draft

**Prompt:**

```text
Use the available inputs to produce post draft for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize post structure and point of view. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Engagement plan

- **Key:** `engagement_plan`
- **Tool category:** `ai_tool`
- **Tool:** `linkedin_extreme_engagement_posting_engagement_plan`
- **Inputs:** `content_goal`, `audience_signal`, `trend_scan`, `hook_bank`, `post_draft`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Engagement plan

**Prompt:**

```text
Use the available inputs to produce engagement plan for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize comments, follow-up prompts, and reply angles. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Tone and risk check

- **Key:** `risk_check`
- **Tool category:** `ai_tool`
- **Tool:** `linkedin_extreme_engagement_posting_risk_check`
- **Inputs:** `content_goal`, `audience_signal`, `trend_scan`, `hook_bank`, `post_draft`, `engagement_plan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Tone and risk check

**Prompt:**

```text
Use the available inputs to produce tone and risk check for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize claims, tone, and reputational risk. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Publishing plan

- **Key:** `publishing_plan`
- **Tool category:** `ai_tool`
- **Tool:** `linkedin_extreme_engagement_posting_publishing_plan`
- **Inputs:** `content_goal`, `audience_signal`, `trend_scan`, `hook_bank`, `post_draft`, `engagement_plan`, `risk_check`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Publishing plan

**Prompt:**

```text
Use the available inputs to produce publishing plan for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize timing, owner actions, and variants. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `metrics`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Final LinkedIn package

- **Key:** `execution_brief`
- **Tool category:** `shortcut`
- **Tool:** `linkedin_extreme_engagement_posting`
- **Inputs:** `content_goal`, `audience_signal`, `trend_scan`, `hook_bank`, `post_draft`, `engagement_plan`, `risk_check`, `publishing_plan`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Final LinkedIn package

**Prompt:**

```text
Use the available inputs to produce final linkedin package for audience pain, point of view, hooks, post structure, comments, engagement prompts, and publishing risks. Emphasize ready-to-use post package. Separate facts from assumptions, identify evidence gaps, keep recommendations actionable, and return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

## Governance Notes

- Manual columns collect user or file input and do not execute prompts.
- Executable AI and shortcut columns are configured for manual review when the package marks `requires_review`.
- Output contracts define expected JSON shape, required fields, quality gates, and evidence policies for downstream checks.
