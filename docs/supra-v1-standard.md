# The `.supra` v1 Standard

`.supra` v1 is a portable JSON package standard for AI Workbench examples. A
package describes one reviewable workbench: its identity, starter intake,
columns, execution settings, workflow steps, output contracts, governance rules,
and importable workbench mirror.

The standard exists so an AI-assisted workflow can move safely between authors,
reviewers, repositories, and AI Workbench environments without losing meaning.
A valid `.supra` v1 package is not just JSON that parses. It is a complete,
ordered, evidence-aware description of how work enters the system, how AI tools
may act on it, what structured outputs are expected, and where human judgment
must remain in control.

## Design Promise

A `.supra` v1 package MUST be:

- **Portable:** it contains no machine-specific paths, private directories, or
  hidden assumptions about a local checkout.
- **Self-describing:** title, description, metadata, columns, workflows, and
  contracts make the package understandable without opening external systems.
- **Deterministically ordered:** columns and workflow steps express dependency
  order explicitly.
- **Review-first:** AI execution settings and output contracts preserve human
  review, especially for sensitive decisions.
- **Evidence-aware:** prompts and contracts require facts, assumptions, risks,
  and evidence gaps to stay visible.
- **Regenerable:** package docs and the manifest can be rebuilt from package
  content.
- **Importable:** `main_workbench` mirrors the package structure expected by AI
  Workbench.

## Normative Language

This document uses these terms intentionally:

- **MUST** means required for `.supra` v1 conformance.
- **SHOULD** means strongly recommended unless a package has a documented reason.
- **MAY** means optional.

The executable baseline in this repository is
[`scripts/validate_supra.py`](../scripts/validate_supra.py). The schemas in
[`schemas/`](../schemas/) are lightweight references for editor support and
future stricter validation.

## File Identity

A `.supra` v1 package MUST be stored as:

```text
<key>.supra
```

The file content MUST be a single JSON object. The top-level `key` MUST match
the filename stem exactly.

Valid keys use lowercase letters, numbers, and underscores:

```text
^[a-z0-9_]+$
```

`schemaVersion` MUST be the integer `1` for v1 packages.

## Top-Level Contract

Every `.supra` v1 package MUST include these top-level fields:

| Field | Required meaning |
| --- | --- |
| `key` | Stable package identifier and filename stem. |
| `title` | Human-readable package name. |
| `description` | Concise package purpose used in docs and manifests. |
| `workbench_title` | Human-readable workbench title for import/display. |
| `schemaVersion` | Integer version marker; `1` for this standard. |
| `metadata` | Package metadata, starter rows, commerce hints, and repository notes. |
| `columns` | Ordered workbench columns and tools. |
| `workflows` | Ordered workflow definitions, or an empty list. |
| `main_workbench` | Importable workbench mirror of columns and workflows. |

Top-level fields SHOULD stay concise. Long operational guidance belongs in
prompts, output contracts, generated docs, or standard documentation.

## Metadata Contract

`metadata` MUST be an object with at least:

| Field | Required meaning |
| --- | --- |
| `module_name` | Module/package name, normally equal to `key`. |
| `vendor` | Package vendor or maintainer. |
| `content_name` | Human-readable package content name. |
| `content_description` | Content description aligned with top-level `description`. |
| `export_version` | Version string for exported package content. |
| `import_version` | Version string expected during import. |
| `commerce` | Commerce and usage metadata. |

`metadata.starter_rows` SHOULD provide at least one realistic starter intake for
example packages. If `metadata.starter_rows[*].text` is present, it MUST be valid
JSON. Starter rows SHOULD make constraints, guardrails, and intended outputs
visible.

Starter rows MUST NOT contain private secrets, local paths, personal data that is
not intentionally synthetic, or environment-specific identifiers.

## Column Contract

`columns` MUST be a non-empty ordered list. Each column MUST be an object with:

| Field | Required meaning |
| --- | --- |
| `key` | Unique column identifier. |
| `title` | Human-readable column title. |
| `column_kind` | Workbench column kind. |
| `tool_category` | Tool class, such as `manual`, `ai_tool`, or `shortcut`. |
| `tool` | Tool identifier used by AI Workbench. |
| `tooling` | Prompt execution settings and, when executable, output contract. |

Column keys MUST be unique within the package. If a column has `input_from`, each
referenced key MUST already appear earlier in the `columns` list. This gives the
package a readable execution graph without requiring a separate dependency
resolver.

### Column Categories

Manual columns collect human or file input. A manual column SHOULD set prompt
execution to disabled and MUST NOT require an output contract.

AI-tool columns transform prior inputs with a prompt or tool execution. They MUST
define prompt execution settings and an output contract.

Shortcut columns produce a final or consolidated output. They MUST define prompt
execution settings and an output contract.

## Prompt Execution Contract

Every column MUST include `tooling.prompt_execution` with:

| Field | Required meaning |
| --- | --- |
| `execute_prompt` | Boolean execution switch. |
| `selected` | Boolean UI/default selection state. |
| `mode` | Execution mode, for example `disabled` or `manual_review`. |
| `requires_review` | Boolean review requirement. |
| `label` | Human-readable execution label. |

Executable columns SHOULD default to human review when the output can influence
business, financial, legal, safety, compliance, customer, hiring, or operational
decisions.

## Output Contract

Every non-manual column MUST include `tooling.output_contract`.

An output contract MUST include:

| Field | Required meaning |
| --- | --- |
| `schema_version` | Version identifier for the output contract. |
| `content_type` | Expected output media type, normally `application/json`. |
| `expects_json` | Boolean stating whether JSON is expected. |
| `required_fields` | Non-empty list of required top-level response fields. |
| `json_schema` | JSON Schema object for machine-checkable output shape. |
| `quality_gate` | Human-readable acceptance rule for the output. |
| `evidence_policy` | Evidence rule, such as `no_invented_facts`. |

Every field listed in `required_fields` MUST also appear in
`json_schema.required`. This prevents drift between the short human-readable
contract and the machine-readable schema.

Output contracts SHOULD require enough structure for downstream review. Common
fields include:

- `summary`
- `signals`
- `constraints`
- `assumptions`
- `decision`
- `actions`
- `metrics`
- `risks`
- `evidence_gaps`

The exact fields MAY vary by package domain, but evidence gaps and assumptions
SHOULD remain explicit whenever facts may be incomplete.

## Workflow Contract

`workflows` MUST be a list. Use an empty list when a package has no workflow.

Each workflow SHOULD include:

- `id`
- `title`
- `description`
- `workflow_pipe`
- `steps`

Each workflow step MUST reference an existing column key. Step positions MUST be
contiguous and zero-based:

```text
0, 1, 2, 3, ...
```

A typical reviewable workflow follows this pattern:

1. Capture source context.
2. Extract facts, signals, constraints, assumptions, risks, and evidence gaps.
3. Produce a decision plan or action plan.
4. Produce a final execution brief or consolidated artifact.

Workflows SHOULD make the intended human review path obvious. They SHOULD NOT
hide meaningful decision points inside a single opaque final step when upstream
evidence needs review.

## `main_workbench` Contract

`main_workbench` MUST be an object that mirrors the importable workbench.

At minimum:

- `main_workbench.columns` MUST contain the same number of columns as top-level
  `columns`.
- `main_workbench.workflows` SHOULD mirror top-level `workflows`.
- `main_workbench.description` SHOULD stay aligned with top-level
  `description`.

When a package is changed, authors MUST keep top-level content and
`main_workbench` synchronized. The package should not describe one workbench at
the top level and import a different one through `main_workbench`.

## Documentation Contract

Documentation is generated from package content:

```bash
python3 scripts/generate_docs.py .
```

The generated docs SHOULD include:

- package overview
- package purpose
- starter intake
- workflow steps
- column/tool table
- prompt excerpts
- output contract summary
- governance notes

German documentation SHOULD translate the documentation shell and package
purpose while preserving prompt and JSON blocks as source excerpts. If a new
package is added, the generator MUST have the German package description needed
to keep German docs from falling back to English prose.

The manifest, `examples_manifest.json`, MUST be regenerated with the docs.

## Lifecycle

A `.supra` v1 package moves through six states:

| State | Standard expectation |
| --- | --- |
| Author | Create or edit package JSON, keeping identity, columns, workflows, and contracts synchronized. |
| Validate | Run the local validator and fix structural errors. |
| Document | Regenerate docs and manifest from package content. |
| Review | Inspect prompts, starter rows, evidence policy, and generated docs. |
| Import | Import into AI Workbench from a portable path. |
| Improve | Capture fixes as package changes, then repeat validation and docs generation. |

No lifecycle state should require a private local directory, a user-specific
machine path, or hidden external state.

## Governance Model

`.supra` v1 is designed for AI-assisted work that remains accountable to people.
Packages SHOULD enforce these governance defaults:

- Facts, assumptions, risks, and evidence gaps remain separated.
- Prompts do not ask the model to invent missing facts.
- Outputs that affect people, money, safety, law, compliance, reputation, or
  operations remain reviewable by a responsible human.
- Starter data is synthetic, anonymized, or intentionally shareable.
- Package behavior is auditable from JSON, generated docs, and output contracts.

The standard values traceability over cleverness. A reviewer should be able to
answer: what data enters, what tool acts, what output is expected, what evidence
is missing, and who must review the result.

## Conformance Checklist

A package conforms to `.supra` v1 when all of the following are true:

- [ ] The file is named `<key>.supra`.
- [ ] The top-level JSON value is an object.
- [ ] `key` matches the filename stem.
- [ ] `schemaVersion` is integer `1`.
- [ ] All required top-level fields are present.
- [ ] `metadata` contains all required metadata fields.
- [ ] Starter row `text` values are valid JSON.
- [ ] `columns` is a non-empty ordered list.
- [ ] Column keys are unique.
- [ ] `input_from` references only earlier columns.
- [ ] Every column has `tooling.prompt_execution`.
- [ ] Manual columns do not require output contracts.
- [ ] Every executable column has `tooling.output_contract`.
- [ ] Output contract `required_fields` is non-empty.
- [ ] Output contract `required_fields` appears in `json_schema.required`.
- [ ] `workflows` is a list.
- [ ] Workflow steps reference existing columns.
- [ ] Workflow `step_position` values are contiguous from `0`.
- [ ] `main_workbench` is present and mirrors the package columns.
- [ ] Top-level descriptions, metadata descriptions, workflow descriptions, and
  `main_workbench` descriptions are synchronized where they represent the same
  package purpose.
- [ ] Generated docs and manifest are current.
- [ ] The package contains no private local paths or user-specific machine
  references.

## Repository Acceptance Gates

Run these commands from the repository root:

```bash
python3 scripts/validate_supra.py .
python3 scripts/generate_docs.py . --check
python3 -m py_compile scripts/validate_supra.py scripts/generate_docs.py
```

If pytest is installed, also run:

```bash
python3 -m pytest tests
```

If pytest is unavailable, the validator command remains the authoritative
structural gate, and the existing validation test can be run directly until the
test environment is available.

## Minimal Example

This abbreviated example shows the shape, not a full production-ready package:

```json
{
  "key": "example_decision_brief",
  "title": "Example Decision Brief",
  "description": "Turn source context into a reviewable decision brief.",
  "workbench_title": "Example Decision Brief Desk",
  "schemaVersion": 1,
  "metadata": {
    "module_name": "example_decision_brief",
    "vendor": "SupraTix",
    "content_name": "Example Decision Brief",
    "content_description": "Turn source context into a reviewable decision brief.",
    "export_version": "1.0.0",
    "import_version": "1.0.0",
    "starter_rows": [
      {
        "title": "Example starter",
        "source_type": "business_context",
        "request": "Paste the source context for Example Decision Brief.",
        "text": "{\"schema\":\"EXAMPLE_INTAKE_V1\",\"intake\":\"Example context\",\"guardrails\":[\"Do not invent facts.\"],\"target_outputs\":[\"decision_brief\"]}"
      }
    ],
    "commerce": {
      "business_model": "free_of_use",
      "product_typ": "workflows"
    }
  },
  "columns": [
    {
      "key": "business_context",
      "title": "Business context",
      "column_kind": "step",
      "tool_category": "manual",
      "tool": "user_input",
      "tooling": {
        "prompt_execution": {
          "execute_prompt": false,
          "selected": false,
          "mode": "disabled",
          "requires_review": false,
          "label": "Manual intake"
        }
      }
    }
  ],
  "workflows": [],
  "main_workbench": {
    "key": "example_decision_brief",
    "title": "Example Decision Brief",
    "description": "Turn source context into a reviewable decision brief.",
    "workbench_title": "Example Decision Brief Desk",
    "columns": [
      {
        "key": "business_context",
        "title": "Business context",
        "column_kind": "step",
        "tool_category": "manual",
        "tool": "user_input",
        "tooling": {
          "prompt_execution": {
            "execute_prompt": false,
            "selected": false,
            "mode": "disabled",
            "requires_review": false,
            "label": "Manual intake"
          }
        }
      }
    ],
    "workflows": []
  }
}
```

Real packages should include complete executable columns, output contracts, and a
`main_workbench.columns` mirror. The minimal example is intentionally compact so
authors can see the outer frame before adding domain-specific behavior.

## Anti-Patterns

Avoid these patterns:

- A filename that does not match `key`.
- English-only German docs caused by missing localized descriptions.
- Executable columns without output contracts.
- Output contracts whose `required_fields` and `json_schema.required` disagree.
- Workflow steps that reference missing columns.
- `input_from` dependencies that point forward.
- Top-level and `main_workbench` definitions drifting apart.
- Starter rows containing real secrets or private customer data.
- Local machine paths in packages, docs, scripts, or manifests.
- Prompts that invite ungrounded claims instead of evidence gaps.

## Versioning Notes

`.supra` v1 is intentionally conservative. A future version may add stricter
schema validation, richer localization, stronger `main_workbench` equivalence
checks, or machine-readable governance policies. Such changes should become a
new standard version when they would break existing valid v1 packages.

Within v1, maintainers SHOULD improve examples by tightening contracts,
clarifying descriptions, adding safer starter rows, and improving generated docs
without changing the core package shape.
