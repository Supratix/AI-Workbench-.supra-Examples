# Lieferschein → Lagerbestand (Internal Products)

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt. Interne Spaltentitel, Tool-IDs, Prompts und Pflichtfelder bleiben als Quelldaten erhalten.

## Paketüberblick

- **Quellpaket:** [`../lieferschein_inventory.supra`](../lieferschein_inventory.supra)
- **Workbench-Titel:** Lieferschein → Lagerbestand (Internal Products) Desk
- **Paket-Key:** `lieferschein_inventory`
- **Modul:** `lieferschein_inventory`
- **Anbieter:** SupraTix
- **Schema-Version:** `1`
- **Export-/Import-Version:** `1.0.0` / `1.0.0`
- **Columns:** 3
- **Workflows:** 0
- **Commerce:** `free_of_use`, usage unit `cloud_credits`

## Zweck

Map delivery-note lines to internal products and create a reviewable stock update proposal.

## Starter-Eingabe

### Lieferschein → Lagerbestand (Internal Products) starter

- **Request:** Paste the source context for Lieferschein → Lagerbestand (Internal Products).
- **Source type:** `delivery_note`

**Starter-Payload:**

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

_No workflow is configured; the package exposes reviewable columns only._

## Spalten und Tools

| # | Key               | Title                 | Category   | Tool                                     | Inputs                               | Execution       | Review | Required output                                                                        |
| - | ----------------- | --------------------- | ---------- | ---------------------------------------- | ------------------------------------ | --------------- | ------ | -------------------------------------------------------------------------------------- |
| 1 | `delivery_note`   | Delivery note         | `manual`   | `user_input`                             | -                                    | `disabled`      | no     | -                                                                                      |
| 2 | `product_mapping` | Product mapping       | `ai_tool`  | `lieferschein_inventory_product_mapping` | `delivery_note`                      | `manual_review` | yes    | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `stock_update`    | Stock update proposal | `shortcut` | `lieferschein_inventory`                 | `delivery_note`<br>`product_mapping` | `manual_review` | yes    | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

### Delivery note

- **Key:** `delivery_note`
- **Tool category:** `manual`
- **Tool:** `user_input`
- **Execution:** execute_prompt=no; mode=`disabled`; requires_review=no; label=Manual intake

No prompt is stored for this column; it calls the configured shortcut/tool directly.

### Product mapping

- **Key:** `product_mapping`
- **Tool category:** `ai_tool`
- **Tool:** `lieferschein_inventory_product_mapping`
- **Inputs:** `delivery_note`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Map products

**Prompt:**

```text
Map delivery-note lines to internal products, quantities, and exceptions. Mark unknown or ambiguous product matches for human review. Return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Quality gate:** Return JSON only. Separate facts from assumptions, identify missing evidence, and recommend concrete next actions.
- **Evidence policy:** `no_invented_facts`

### Stock update proposal

- **Key:** `stock_update`
- **Tool category:** `shortcut`
- **Tool:** `lieferschein_inventory`
- **Inputs:** `delivery_note`, `product_mapping`
- **Execution:** execute_prompt=yes; mode=`manual_review`; requires_review=yes; label=Draft stock update

**Prompt:**

```text
Create a reviewable inventory update proposal from the delivery note and product mapping. Do not post stock changes automatically; include exceptions and evidence gaps. Return JSON only.
```

**Output contract:**

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Content type:** `application/json`
- **Expects JSON:** yes
- **Required fields:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Quality gate:** Return a reviewable proposal with no automatic inventory mutation.
- **Evidence policy:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare KI- und Shortcut-Spalten sind auf manuelle Prüfung gesetzt, wenn das Paket `requires_review` markiert.
- Output Contracts definieren erwartete JSON-Strukturen, Pflichtfelder, Quality Gates und Evidence Policies für nachgelagerte Prüfungen.
