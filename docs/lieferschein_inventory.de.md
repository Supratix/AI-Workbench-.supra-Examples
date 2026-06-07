# Lieferschein → Lagerbestand (Internal Products)

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Source package:** [`../lieferschein_inventory.supra`](../lieferschein_inventory.supra)
- **Workbench title:** Lieferschein → Lagerbestand (Internal Products) Desk
- **Package key:** `lieferschein_inventory`
- **Vendor:** SupraTix
- **Schema version:** `1`
- **Columns:** 3
- **Workflows:** 0

## Zweck

Map delivery-note lines to internal products, flag ambiguous matches, and produce a reviewable stock update proposal for inventory teams.

## Starter-Eingabe

### Lieferschein → Lagerbestand (Internal Products) starter

- **Request:** Paste the source context for Lieferschein → Lagerbestand (Internal Products).
- **Source type:** `delivery_note`

```json
{
  "schema": "DISRUPTIVE_SME_INTAKE_V1",
  "use_case": "lieferschein_inventory",
  "focus": "delivery-note parsing, product matching, quantity reconciliation, exceptions, and inventory update readiness",
  "intake": "Lieferschein: Supplier ACME, DN-2026-0412, items: 12x M8 washer, 4x pump filter A, 1x unknown gasket. Warehouse: Köln. Constraint: review unknown products before stock update.",
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

_No workflow is configured._

## Spalten und Tools

| # | Key               | Title                 | Category   | Tool                                     | Review | Required output                                                                        |
| - | ----------------- | --------------------- | ---------- | ---------------------------------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `delivery_note`   | Delivery note         | `manual`   | `user_input`                             | no     | -                                                                                      |
| 2 | `product_mapping` | Product mapping       | `ai_tool`  | `lieferschein_inventory_product_mapping` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `stock_update`    | Stock update proposal | `shortcut` | `lieferschein_inventory`                 | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

### Delivery note

- **Key:** `delivery_note`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no

### Product mapping

- **Key:** `product_mapping`
- **Tool:** `lieferschein_inventory_product_mapping`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Map delivery-note lines to internal products, quantities, and exceptions. Mark unknown or ambiguous product matches for human review. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

### Stock update proposal

- **Key:** `stock_update`
- **Tool:** `lieferschein_inventory`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes

```text
Create a reviewable inventory update proposal from the delivery note and product mapping. Do not post stock changes automatically; include exceptions and evidence gaps. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidence policy:** `no_invented_facts`

## Governance-Hinweise

- Manual columns collect user or file input and do not execute prompts.
- Executable columns default to manual review where configured.
- Output contracts keep downstream checks predictable.
