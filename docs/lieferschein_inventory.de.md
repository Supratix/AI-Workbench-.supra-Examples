# Lieferschein → Lagerbestand (Internal Products)

Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt.

## Paketüberblick

- **Quellpaket:** [`../lieferschein_inventory.supra`](../lieferschein_inventory.supra)
- **Workbench-Titel:** Lieferschein → Lagerbestand (Internal Products) Desk
- **Paket-Key:** `lieferschein_inventory`
- **Anbieter:** SupraTix
- **Schemaversion:** `1`
- **Spalten:** 3
- **Workflows:** 0

## Zweck

Ordnet Lieferscheinpositionen internen Produkten zu, markiert unsichere Treffer und erstellt einen prüfbaren Bestandsaktualisierungsvorschlag für Lagerteams.

## Starter-Eingabe

### Lieferschein → Lagerbestand (Internal Products) Starter

- **Anfrage:** Fügen Sie den Quellkontext für Lieferschein → Lagerbestand (Internal Products) ein.
- **Quelltyp:** `delivery_note`

_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._

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

_Es ist kein Workflow konfiguriert._

## Spalten und Tools

| # | Key               | Titel                 | Kategorie  | Tool                                     | Prüfung | Pflichtausgabe                                                                         |
| - | ----------------- | --------------------- | ---------- | ---------------------------------------- | ------- | -------------------------------------------------------------------------------------- |
| 1 | `delivery_note`   | Delivery note         | `manual`   | `user_input`                             | nein    | -                                                                                      |
| 2 | `product_mapping` | Product mapping       | `ai_tool`  | `lieferschein_inventory_product_mapping` | ja      | `summary`<br>`signals`<br>`constraints`<br>`assumptions`<br>`risks`<br>`evidence_gaps` |
| 3 | `stock_update`    | Stock update proposal | `shortcut` | `lieferschein_inventory`                 | ja      | `summary`<br>`decision`<br>`actions`<br>`risks`<br>`evidence_gaps`                     |

## Prompt- und Vertragsreferenz

_Prompts werden als Originalauszüge aus dem Paket angezeigt._

### Delivery note

- **Key:** `delivery_note`
- **Tool:** `user_input`
- **Ausführung:** execute_prompt=nein; mode=`disabled`; requires_review=nein

### Product mapping

- **Key:** `product_mapping`
- **Tool:** `lieferschein_inventory_product_mapping`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Map delivery-note lines to internal products, quantities, and exceptions. Mark unknown or ambiguous product matches for human review. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_WORKBENCH_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `signals`, `constraints`, `assumptions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

### Stock update proposal

- **Key:** `stock_update`
- **Tool:** `lieferschein_inventory`
- **Ausführung:** execute_prompt=ja; mode=`manual_review`; requires_review=ja

```text
Create a reviewable inventory update proposal from the delivery note and product mapping. Do not post stock changes automatically; include exceptions and evidence gaps. Return JSON only.
```

- **Schema:** `DISRUPTIVE_SME_SHORTCUT_OUTPUT_V1`
- **Pflichtfelder:** `summary`, `decision`, `actions`, `risks`, `evidence_gaps`
- **Evidenzregel:** `no_invented_facts`

## Governance-Hinweise

- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.
- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.
- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.
