# Import-Bewertung SupraWorx v3.0

Dieses Dokument hält fest, wie sich die Pakete dieses Repositories beim Import in SupraWorx v3.0 (`mint/workbench`, AI Workbench) verhalten. Grundlage ist ein Lauf der produktiven Importer-Codepfade gegen jedes Paket. Die Ergebnisse bilden die Basis für die SupraWorx-Kompatibilitätsschicht in `scripts/validate_supra.py`.

Bewerteter Code (SupraWorx v3.0, `mint/`):

| Komponente | Datei | Rolle |
| --- | --- | --- |
| Strikter Payload-Validator | `workbench/config_security.py` → `parse_workbench_example()` | Wird vom Datei-Upload **und** von der lokalen Vorlagen-Galerie verwendet. Lehnt unbekannte Felder ab (`reject_unknown=True`). |
| Upload-View | `workbench/views.py` → `ai_workbench_supra_file_import()` | Entschlüsselt, validiert und prüft anschließend das Shortcut-Gate `_validate_uploaded_supra_shortcut_references()`. |
| Vorlagen-Galerie | `workbench/views.py` → `_iter_local_workbench_supra_templates()` | Listet `*.supra`-Dateien in `workbench/examples/` (flach, keine Unterordner); Dateien, die die Validierung nicht bestehen, werden stillschweigend übersprungen. |
| Workbench-Aufbau | `workbench/views.py` → `_apply_workbench_node_to_timeline()` | Legt je Spalte ein `AutomationSettings`-Objekt an; Shortcut-Spalten werden über `_ensure_imported_shared_shortcut()` gebunden. |
| Verwaltete SME-Shortcuts | `shortcuts/services/sme_shortcuts.py` | Registry der Shortcut-IDs; jede ID ist in `shortcuts/tasks.py::SHORTCUT_TASKS` an `sme_shortcut_task` gebunden. |
| Katalog-Test | `workbench/test_supra_catalog.py` | Prüft, dass jedes mitgelieferte Beispiel `parse_workbench_example` besteht, und prüft die Anzahl der Dateien (derzeit `63`). |

## Vorgehen

1. `parse_workbench_example()` und seine Abhängigkeiten (`config_security.py`, `rules.py`, `constants.py`, `supra_package.py`, `shortcuts/services/ocr.py`, `sme_shortcuts.py`) wurden unverändert gegen jede `.supra`-Datei ausgeführt; Django-/ORM-Importe wurden gestubbt (für die Validierung ist keine Datenbank nötig).
2. Das Shortcut-Gate des Uploads wurde nachgestellt: Eine `shortcut`-Spalte wird nur akzeptiert, wenn ihr `tool` ein verwalteter SME-Shortcut (`get_sme_shortcut_definition()`), der generische `gpt`-Prompt-Shortcut oder ein vertrauenswürdiger Upload-Shortcut ist. Aktive geteilte Shortcuts, die nur in einer konkreten Mandanten-Datenbank existieren, lassen sich offline nicht prüfen und gelten als nicht registriert.
3. Nach den unten beschriebenen Korrekturen wurde der Lauf wiederholt.

## Ergebnisse

| Stufe | Vorher | Nachher |
| --- | --- | --- |
| Pakete | 47 | 147 (47 bestehende + 100 neue SME-Pakete) |
| Bestehen `parse_workbench_example()` (strikter Validator) | **0 / 47** | **147 / 147** |
| Bestehen das Shortcut-Gate des Datei-Uploads | 0 / 47 | **145 / 147** (2 dokumentierte Ausnahmen) |
| Nach Installation in der lokalen Galerie sichtbar | 0 / 47 | 147 / 147 |

### Befund 1 – `metadata.github_example` blockierte jedes Paket (behoben)

Jedes Paket enthielt ein Objekt `metadata.github_example`. Die Metadaten-Allowlist des Importers (`WORKBENCH_EXAMPLE_ALLOWED_METADATA`) kennt dieses Feld nicht, daher warf `_canonicalize_workbench_metadata()` für alle 47 Pakete *„metadata enthält unbekannte Felder."*. Folgen: Der Datei-Upload lieferte HTTP 400, die Galerie übersprang die Dateien stillschweigend (die bereits in `workbench/examples/` liegenden Kopien hatten das Feld manuell entfernt bekommen, weshalb sie dort funktionierten).

Korrektur: `scripts/fix_supraworx_compat.py` entfernt `github_example` und ergänzt stattdessen das erlaubte `metadata.source_attribution` (`text`, `url`). Der Validator erzwingt jetzt die Importer-Allowlists für Root, Metadaten, `source_attribution`, `commerce` und Starter-Zeilen, sodass dieser Fehler nicht wieder auftreten kann.

### Befund 2 – Erweiterungsmetadaten in `workforce_intelligence_platform` (behoben)

`metadata.deployment`, `metadata.integrations` und `metadata.supraagents` sind ebenfalls nicht erlaubt. Der Importer akzeptiert fünf freie Erweiterungsobjekte (`scoring`, `account_universe`, `process`, `governance`, `operating_cadence`, je max. 64 KiB). Die drei Blöcke wurden verlustfrei nach `metadata.process.{deployment,integrations,supraagents}` verschoben.

### Befund 3 – nicht registrierte Shortcut-IDs werden beim Upload abgelehnt (durch Registrierung behoben)

Die Upload-View lehnt ein Paket ab, dessen `shortcut`-Spalte auf einen Shortcut verweist, der weder verwaltet noch als aktiver geteilter Shortcut auf der Instanz vorhanden ist („*Die .supra-Datei verweist auf den nicht freigegebenen Shortcut …*"). Nur 35 der 47 Pakete nutzten eine registrierte ID. Die 100 neuen Pakete bringen 100 neue IDs mit (`sme_thirteen_week_cash_forecast`, …).

Korrektur: Die IDs werden als verwaltete SME-Shortcuts registriert. `scripts/render_sme_shortcut_specs.py` erzeugt die Einträge für `_DISRUPTIVE_SME_SHORTCUT_SPECS` in `mint/shortcuts/services/sme_shortcuts.py` aus `scripts/data/sme_use_cases.json` plus `scripts/data/sme_registry_extras.json` (die 10 Alt-IDs, die reine LLM-Briefings sind: `sme_esg_sustainability_copilot`, `linkedin_extreme_engagement_posting`, `aevalley_grant_tender_url_condenser`, `kmu_tender_factory`, `mint_study_planning`, die vier `data_analytics_*`-Pakete und `field_service_maintenance_report`). Da `SHORTCUT_TASKS` in `shortcuts/tasks.py` jede Definition automatisch auf `sme_shortcut_task` abbildet, ist **keine Änderung an `tasks.py` nötig** – die Registrierung allein macht den Shortcut importier- und ausführbar. Der Block ist durch Marker-Kommentare begrenzt und kann idempotent neu erzeugt werden:

```bash
python3 scripts/render_sme_shortcut_specs.py . --apply ../supraworxv30/mint/shortcuts/services/sme_shortcuts.py
python3 scripts/render_sme_shortcut_specs.py . --registry   # aktualisiert scripts/data/supraworx_managed_shortcuts.json
```

Nach dem Patch enthält die Registry 146 verwaltete SME-Shortcut-Definitionen (36 bestehende + 110 generierte), alle mit eindeutigen IDs.

Dokumentierte Ausnahmen (der Validator gibt eine Warnung aus, der Upload wird abgelehnt, die Galerie-Installation funktioniert):

| Paket | Shortcut | Warum nicht registriert |
| --- | --- | --- |
| `lieferschein_inventory` | `lieferschein_inventory` | Benötigt die internen Produkt-Tasks (Lieferschein-Extraktor / Bestands-Updater), kein LLM-Briefing. |
| `workforce_intelligence_platform` | `workforce_intelligence_action_receipts` | Benötigt einen eigenen Action-Receipt-Task. |

### Befund 4 – das Installationsskript verunreinigte `workbench/examples/` (behoben)

`scripts/install_to_supraworx_examples.sh` synchronisierte per `rsync` das gesamte Repository und kopierte damit README, Docs, Schemas und Skripte in den Beispielordner. Die Galerie liest nur `*.supra` auf oberster Ebene, und `test_supra_catalog.py` prüft eine exakte Dateianzahl. Das Skript kopiert jetzt ausschließlich `packages/**/*.supra` (flach, optional je Domäne) und gibt die resultierende Anzahl aus, damit die Test-Assertion bewusst angepasst werden kann.

### Befund 5 – Grenzwerte, die man kennen sollte (keine Verstöße)

| Grenze | Wert | Status im Repository |
| --- | --- | --- |
| Payload-Größe | 1 MiB | Größtes Paket 97 KB |
| Spalten je Workbench | 64 | Max. 17 |
| Länge der Beschreibung | 2000 Zeichen | OK |
| Starter-Zeilen / Starter-Text | 200 Zeilen / 4000 Zeichen | Längster Starter-Text < 1500 Zeichen |
| `json_schema` im Output-Vertrag | 12 KiB | OK |
| Erweiterungsobjekte | 64 KiB | OK |
| Spalten-`key` | keine Segmente mit Punkten (`test_supra_rejects_dotted_semantic_key_segments`) | OK |

Alle Grenzwerte werden jetzt von `scripts/validate_supra.py` geprüft.

### Beobachtungen (keine Änderung vorgenommen)

* `ai_tool`-Spalten nutzen paketspezifische Tool-Slugs wie `sme_x_signals`. Der Importer speichert den Slug unverändert (`_resolve_imported_ai_tool_slug()` schreibt nur OpenAI-artige Referenzen auf den OpenAI-Produkt-Slug um). Zur Laufzeit wird die Spalte über das im Mandanten konfigurierte GenAI-Tool ausgeführt; das entspricht dem Muster der 35 bereits in SupraWorx enthaltenen SME-Pakete, das Verhalten ist also unverändert.
* Prompts mit `output_contract.expects_json = true` werden automatisch im JSON-Modus ausgeführt, wobei der Vertrag an den Prompt angehängt wird (`_apply_declared_json_output_contract()`). Deshalb trägt jede ausführbare Spalte der generierten Pakete einen Vertrag.
* Nach einem erfolgreichen Upload stellt SupraWorx die automatische Ausführung der Starter-Zeilen in die Warteschlange (`_schedule_imported_workbench_execution()`); Spalten mit `requires_review = true` halten weiterhin zur Prüfung an.
* Der Ordner `workbench/examples/` in SupraWorx enthält heute 63 Dateien. Wer alle 147 Pakete dort installiert, muss die Anzahl in `test_supra_catalog.py` anpassen.

## Bewertung reproduzieren

Die Kompatibilitätsprüfungen sind Teil des normalen Validierungslaufs:

```bash
python3 scripts/validate_supra.py .          # Standard + Importer-Allowlists + Shortcut-Gate
python3 scripts/fix_supraworx_compat.py . --check
```

Um den produktiven Validator selbst auszuführen, aus einem SupraWorx-Checkout:

```bash
cd supraworxv30/mint
python -m pytest workbench/test_supra_catalog.py -k production_validation
```
