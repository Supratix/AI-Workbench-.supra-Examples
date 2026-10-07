# Golden output examples

This first golden-output slice covers two package families and all executable
output contracts in those packages:

- `sme_thirteen_week_cash_forecast`: signal map, decision plan, and execution brief.
- `field_service_maintenance_report`: normalized evidence, maintenance report,
  and customer summary.

Each JSON file in `golden_outputs/<package-key>/` is a reviewed reference
example validated against the output contract embedded in its `.supra`
package. The tests also remove a required field from each otherwise-valid
example and verify that the contract rejects it.

## Scope and evidence

These files are synthetic examples constructed only from the packages' synthetic
starter data. They are not actual measured runtime results, production outputs,
verified financial records, service records, or AI Workbench executions. No
additional facts are inferred as established.

Assumptions, missing evidence, uncertainty, and required human approvals are
called out in the outputs. The cash forecast examples do not calculate a
13-week balance because dated and reconciled cash-flow inputs are absent. The
field-service photo URL is a placeholder from the starter data; no image was
retrieved or inspected. Reports and customer-facing content remain drafts until
the responsible people verify the evidence and approve release.

To validate locally, install the test dependencies and run:

```sh
python -m pip install pytest jsonschema
python -m pytest -q tests
```
