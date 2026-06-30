#!/usr/bin/env python3
"""Generate EN/DE docs and a manifest from .supra package files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


MANIFEST_SCHEMA = "SUPRA_EXAMPLES_MANIFEST_V1"
MANIFEST_TARGET = "AI Workbench .supra examples repository"
GERMAN_DESCRIPTIONS = {
    "aevalley_grant_tender_url_condenser": "Verdichtet Förder-, Ausschreibungs- und Projekt-URLs zu einem kompakten Evidenz-Briefing mit Fit, Angebotsreife, Finanzierungsrisiken und nächsten Validierungsschritten.",
    "data_analytics_experiment_launch_analyzer": "Wandelt Experiment- oder Launch-Notizen in eine entscheidungsreife Analytics-Prüfung mit Hypothesenchecks, Ergebnissignalen, Risiken und offenen Instrumentierungsbedarfen um.",
    "data_analytics_kpi_framework_designer": "Entwirft ein praxisnahes KPI-Framework, das Ziele mit Metrikdefinitionen, Verantwortlichen, Guardrails, Review-Rhythmus und reportingfähigen Hinweisen verbindet.",
    "data_analytics_kpi_operating_review": "Erstellt einen strukturierten KPI-Operating-Review mit Status, Risiken, Korrekturmaßnahmen, Verantwortlichen und Follow-up-Triggern für wiederkehrende Business-Reviews.",
    "data_analytics_market_opportunity_sizer": "Schätzt Markt- oder Chancenpotenziale mit transparenten Annahmen, Szenarien, Sensitivitätschecks, Evidenzlücken und Validierungsprioritäten.",
    "field_service_maintenance_report": "Wandelt Technikernotizen oder Transkripte in einen nachvollziehbaren Wartungsbericht mit Kunden-Zusammenfassung um.",
    "kmu_tender_factory": "Analysiert Ausschreibungs-PDFs und erstellt für KMU-Angebote einen kriterienbasierten Angebotsentwurf, eine Bewertungsmatrix, eine Compliance-Checkliste und ein Evidenzpaket.",
    "lieferschein_inventory": "Ordnet Lieferscheinpositionen internen Produkten zu, markiert unsichere Treffer und erstellt einen prüfbaren Bestandsaktualisierungsvorschlag für Lagerteams.",
    "linkedin_extreme_engagement_posting": "Erstellt ein LinkedIn-Publishing-Paket für hohe Interaktion mit Hooks, Post-Varianten, Positionierungsnotizen, Risikoprüfungen und Follow-up-Impulsen.",
    "mint_study_planning": "Erstellt strukturierte MINT/STEM-Lernpläne aus Lernzielen, Ausgangskompetenzen, Zeitplan, Einschränkungen, Meilensteinen, Ressourcen und Assessments.",
    "sme_ai_adoption_readiness_sprint": "Bewertet die KI-Einführungsreife eines KMU und übersetzt Einschränkungen, Datenqualität, Risiken und Teamkapazität in einen konkreten ersten Sprintplan.",
    "sme_cashflow_war_room": "Priorisiert Cashflow-Risiken aus Forderungen, Verbindlichkeiten und Zusagen und überführt sie in ein verantwortbares Recovery-Board mit Eskalationstriggern.",
    "sme_churn_rescue_desk": "Erkennt Abwanderungssignale aus Kundenkontext und erstellt einen praktikablen Rettungsplan mit Ursachen, Verantwortlichenaktionen und Review-Triggern.",
    "sme_compliance_evidence_pack": "Strukturiert Compliance-Fakten zu einem Evidenzpaket mit Pflichten, Nachweislücken, Verantwortlichen, Fristen und prüfbereiten Hinweisen.",
    "sme_customer_reply": "Entwirft eine professionelle Kundenantwort, die Ton, Fakten, Evidenzlücken, Zusagen und Follow-up-Prüfungen für sensible Servicesituationen ausbalanciert.",
    "sme_cyber_hygiene_action_board": "Überführt Cyber-Hygiene-Beobachtungen in ein priorisiertes Remediation-Board mit Risikostufe, verantwortlichen Personen, Fristen und Verifikationschecks.",
    "sme_data_cleanup_command_center": "Erstellt einen praxisnahen Datenbereinigungsplan mit Problemkategorien, Qualitätsregeln, Verantwortlichen, Validierungschecks und Umsetzungsreihenfolge.",
    "sme_deadstock_liquidator": "Erkennt Ladenhüterrisiken aus Bestandssignalen und übersetzt sie in einen Liquidationsplan mit Preisoptionen, Kanälen, Verantwortlichen und Review-Metriken.",
    "sme_downtime_triage": "Diagnostiziert Ausfallkontext und erstellt einen fokussierten Triageplan, der Sofortmaßnahmen, Root-Cause-Hypothesen, Prävention und Verantwortliche trennt.",
    "sme_energy_cost_anomaly_finder": "Erkennt Energiekostenanomalien, trennt wahrscheinliche Treiber von Annahmen und schlägt prüfbare Einspar- oder Untersuchungsmaßnahmen mit Ownership vor.",
    "sme_field_service_route_optimizer": "Wandelt Serviceaufträge, Techniker-Kapazitäten, Reiserestriktionen und Prioritätsregeln in ein Routenoptimierungs-Briefing für Außendienstteams um.",
    "sme_grant_funding_fit_radar": "Bewertet Förder-Fit-Signale und erstellt eine Shortlist mit Eignungshinweisen, Evidenzlücken, Fristen, Aufwandsschätzungen und nächsten Antragsschritten.",
    "sme_hiring_scorecard_kit": "Erstellt eine Rollen-Scorecard mit Erfolgszielen, Interview-Signalen, Entscheidungsrubrik, Evidenzfragen und Hiring-Risikohinweisen für KMU-Teams.",
    "sme_invoice_dispute_resolver": "Strukturiert Rechnungsstreit-Fakten zu einem Lösungsplan mit Anspruchszusammenfassung, Evidenzlücken, Verhandlungsoptionen, Verantwortlichen und Eskalationstriggern.",
    "sme_late_payment_collector": "Bereitet einen menschlichen, aber klaren Mahnplan mit Kundenkontext, Nachrichtenvorlagen, Eskalationspfad und Zahlungsrisikosignalen vor.",
    "sme_lead_qualifier": "Qualifiziert Leads anhand von Fit, Dringlichkeit, Budgetsignalen, Risikoflaggen und Next-Best-Action-Empfehlungen für praktische Vertriebsnacharbeit.",
    "sme_local_seo_content_engine": "Erstellt lokale SEO-Content-Briefings aus Geschäftskontext, Servicegebieten, Kundennachweisen, Suchintention und seitenbezogenen Handlungshinweisen.",
    "sme_margin_leak_detector": "Erkennt Margenverluste aus Preis-, Rabatt-, Kosten- und Liefersignalen und erstellt daraus einen praxisnahen Gewinnschutzplan.",
    "sme_meeting_summarizer": "Fasst Meetingnotizen zu Entscheidungen, Maßnahmen, Risiken, Verantwortlichen, Fälligkeiten, Evidenzlücken und Follow-up-Impulsen zusammen.",
    "sme_onboarding_micro_sop_factory": "Wandelt Onboarding-Kontext in kurze SOPs, rollenfertige Checklisten, Warnungen vor typischen Fehlern und Review-Impulse für neue Teammitglieder um.",
    "sme_pricing_power_simulator": "Bewertet Preissetzungsmacht anhand von Nachfrage-, Wettbewerbs-, Kosten- und Kundensignalen und schlägt Szenarien, Guardrails und Review-Trigger vor.",
    "sme_product_launch_kill_scale_gate": "Erstellt ein Kill/Scale-Gate für Produktlaunch-Entscheidungen mit Evidenzzusammenfassung, Konfidenzniveau, Risiken und nächsten Maßnahmen.",
    "sme_proposal_drafter": "Entwirft ein Angebotsbriefing mit Kundenzielen, Scope, Annahmen, Liefergegenständen, Ausschlüssen, Risiken und nächster Handlungssprache.",
    "sme_quote_to_cash_bottleneck": "Prüft den Quote-to-Cash-Prozess auf Übergabeengpässe, fehlende Daten, Aging-Risiken und verantwortbare Maßnahmen zum Schutz des Umsatzzeitpunkts.",
    "sme_review_reputation_responder": "Entwirft Review-Antworten und Reputationsmaßnahmen mit evidenzbewusstem Ton, Eskalationshinweisen, Servicesignalen und Follow-up-Prüfungen.",
    "sme_safety_incident_prevention": "Wandelt Sicherheitsvorfallnotizen in Präventionsmaßnahmen mit Root-Cause-Hypothesen, Verantwortlichen, Verifikationschecks und Review-Triggern um.",
    "sme_esg_sustainability_copilot": "Konsolidiert Nachhaltigkeitsnachweise zu einer ESG-Readiness-Scorecard mit Gap-Analyse und Maßnahmenplan.",
    "sme_shift_handover_risk_radar": "Erkennt Übergaberisiken und erstellt ein schichtbereites Minderungsbriefing mit Prioritätsthemen, Owner-Checks, offenen Fragen und Eskalationssignalen.",
    "sme_sop_builder": "Wandelt Prozesskontext in eine klare SOP mit Rollen, Inputs, Schritten, Qualitätschecks, Ausnahmen und Review-Rhythmus um.",
    "sme_subscription_retention_playbook": "Erstellt ein Retention-Playbook für Abos aus Kundensignalen, Verlängerungsrisiken, Interventionsmaßnahmen, Verantwortlichen und Review-Metriken.",
    "sme_tender_no_bid_gate": "Erstellt eine Bid/No-Bid-Empfehlung für Ausschreibungen mit Fit-Bewertung, Evidenzlücken, Lieferrisiken, Governance-Hinweisen und nächsten Maßnahmen.",
    "sme_training_skill_gap_matrix": "Ordnet Trainingsbedarfe in eine Skill-Gap-Matrix mit Rollenwirkung, priorisierten Lernmaßnahmen, Verantwortlichen und Fortschritts-Reviews ein.",
    "sme_upsell_signal_miner": "Findet Upsell-Signale im Account-Kontext und übersetzt sie in accountspezifische Angebote, Timing-Hinweise, Risikoflaggen und nächste Maßnahmen.",
    "sme_vendor_negotiation_brief": "Bereitet ein Lieferantenverhandlungsbriefing mit Hebelsignalen, Zielanfragen, Rückfalloptionen, Risikohinweisen und owner-fertigen Talking Points vor.",
    "sme_warranty_root_cause_radar": "Analysiert Garantieprobleme und schlägt Root-Cause-Hypothesen, Containment-Maßnahmen, Evidenzlücken, Kundenwirkung und Präventionschecks vor.",
    "sme_webshop_conversion_rescue": "Diagnostiziert Webshop-Conversion-Probleme und erstellt einen priorisierten Rettungsplan zu Funnel-Signalen, Reibungspunkten, Experimenten und Owner-Actions.",
    "workforce_intelligence_platform": "Bewahrt Expertenwissen, kartiert Kompetenzrisiken und orchestriert Lern-, Nachfolge- und Recruiting-Workflows mit erklärbaren KI-Belegen.",
}
GERMAN_STARTER_REQUESTS = {
    "Paste the learner profile, learning goals, dates, weekly hours, and constraints for MINT Study Planning.": "Fügen Sie das Lernendenprofil, die Lernziele, Termine, Wochenstunden und Einschränkungen für MINT Study Planning ein.",
    "Paste tender PDF text/OCR, evaluation criteria, company profile, and reference fragments.": "Fügen Sie Ausschreibungs-PDF-Text oder OCR, Bewertungskriterien, Unternehmensprofil und Referenzfragmente ein.",
    "Paste a technician transcript, audio URI, checklist, photo references, and job metadata.": "Fügen Sie ein Technikertranskript, eine Audio-URI, eine Checkliste, Fotoverweise und Auftragsmetadaten ein.",
    "Paste workforce, expert-knowledge, SpeakSphere, HRIS, LMS, ATS, project, and SOP context for analysis.": "Fügen Sie Workforce-, Expertenwissen-, SpeakSphere-, HRIS-, LMS-, ATS-, Projekt- und SOP-Kontext für die Analyse ein.",
}


def table(rows: list[list[str]]) -> str:
    widths = [max(len(str(row[i])) for row in rows) for i in range(len(rows[0]))]
    out = ["| " + " | ".join(str(rows[0][i]).ljust(widths[i]) for i in range(len(widths))) + " |"]
    out.append("| " + " | ".join("-" * widths[i] for i in range(len(widths))) + " |")
    for row in rows[1:]:
        out.append("| " + " | ".join(str(row[i]).ljust(widths[i]) for i in range(len(widths))) + " |")
    return "\n".join(out)


def localized_description(pkg: dict, lang: str) -> str:
    if lang == "de":
        return GERMAN_DESCRIPTIONS[pkg["key"]]
    return pkg.get("description", "")


def yn(value: bool, lang: str) -> str:
    if lang == "de":
        return "ja" if value else "nein"
    return "yes" if value else "no"


def localized_starter_request(pkg: dict, starter: dict, lang: str) -> str:
    request = starter.get("request", "")
    if lang == "de":
        if not request:
            return f"Fügen Sie den Quellkontext für {pkg['title']} ein."
        if request in GERMAN_STARTER_REQUESTS:
            return GERMAN_STARTER_REQUESTS[request]
        if request.startswith("Paste the source context for ") and request.endswith("."):
            name = request.removeprefix("Paste the source context for ").removesuffix(".")
            return f"Fügen Sie den Quellkontext für {name} ein."
    return request


def localized_title(value: str, lang: str) -> str:
    if lang != "de":
        return value
    if value.endswith(" starter"):
        return value.removesuffix(" starter") + " Starter"
    if value.endswith(" workflow"):
        return value.removesuffix(" workflow") + " Workflow"
    return value


def doc(pkg: dict, lang: str) -> str:
    de = lang == "de"
    labels = {
        "overview": "Paketüberblick" if de else "Package Overview",
        "purpose": "Zweck" if de else "Purpose",
        "starter": "Starter-Eingabe" if de else "Starter Intake",
        "workflow": "Workflow",
        "columns": "Spalten und Tools" if de else "Columns and Tools",
        "prompts": "Prompt- und Vertragsreferenz" if de else "Prompt and Contract Reference",
        "governance": "Governance-Hinweise" if de else "Governance Notes",
    }
    overview_labels = {
        "source": "Quellpaket" if de else "Source package",
        "workbench": "Workbench-Titel" if de else "Workbench title",
        "key": "Paket-Key" if de else "Package key",
        "vendor": "Anbieter" if de else "Vendor",
        "schema": "Schemaversion" if de else "Schema version",
        "columns": "Spalten" if de else "Columns",
        "workflows": "Workflows",
        "request": "Anfrage" if de else "Request",
        "source_type": "Quelltyp" if de else "Source type",
        "step": "Schritt" if de else "Step",
        "review": "Prüfung" if de else "Review",
        "required_output": "Pflichtausgabe" if de else "Required output",
        "execution": "Ausführung" if de else "Execution",
        "required_fields": "Pflichtfelder" if de else "Required fields",
        "evidence_policy": "Evidenzregel" if de else "Evidence policy",
    }
    lines = [f"# {pkg['title']}", ""]
    lines.append("Diese Dokumentation wird aus dem `.supra`-Paketinhalt erzeugt." if de else "This documentation is generated from the `.supra` package content.")
    lines += ["", f"## {labels['overview']}", ""]
    lines += [
        f"- **{overview_labels['source']}:** [`../{pkg['key']}.supra`](../{pkg['key']}.supra)",
        f"- **{overview_labels['workbench']}:** {pkg.get('workbench_title', '')}",
        f"- **{overview_labels['key']}:** `{pkg['key']}`",
        f"- **{overview_labels['vendor']}:** {pkg.get('metadata', {}).get('vendor', '')}",
        f"- **{overview_labels['schema']}:** `{pkg.get('schemaVersion', '')}`",
        f"- **{overview_labels['columns']}:** {len(pkg.get('columns', []))}",
        f"- **{overview_labels['workflows']}:** {len(pkg.get('workflows', []))}",
        "",
        f"## {labels['purpose']}",
        "",
        localized_description(pkg, lang),
        "",
        f"## {labels['starter']}",
        "",
    ]
    for starter in pkg.get("metadata", {}).get("starter_rows", []):
        lines += [f"### {localized_title(starter.get('title', 'Starter'), lang)}", "", f"- **{overview_labels['request']}:** {localized_starter_request(pkg, starter, lang)}", f"- **{overview_labels['source_type']}:** `{starter.get('source_type', '')}`", ""]
        if de:
            lines += ["_Der folgende JSON-Block bleibt ein Originalauszug aus dem Paket._", ""]
        lines += ["```json"]
        try:
            lines.append(json.dumps(json.loads(starter.get("text", "{}")), indent=2, ensure_ascii=False))
        except Exception:
            lines.append(starter.get("text", ""))
        lines += ["```", ""]
    lines += [f"## {labels['workflow']}", ""]
    if pkg.get("workflows"):
        for wf in pkg["workflows"]:
            workflow_description = localized_description(pkg, lang) if wf.get("description") == pkg.get("description") else wf.get("description", "")
            lines += [f"### {localized_title(wf.get('title', ''), lang)}", "", workflow_description, ""]
            rows = [["#", overview_labels["step"], "ID", "Backlog"]]
            for i, step in enumerate(wf.get("steps", []), 1):
                rows.append([str(i), step.get("title", ""), f"`{step.get('id', '')}`", yn(step.get("backlog"), lang)])
            lines += [table(rows), ""]
    else:
        lines += ["_Es ist kein Workflow konfiguriert._" if de else "_No workflow is configured._", ""]
    lines += [f"## {labels['columns']}", ""]
    rows = [["#", "Key", "Titel" if de else "Title", "Kategorie" if de else "Category", "Tool", overview_labels["review"], overview_labels["required_output"]]]
    for i, col in enumerate(pkg.get("columns", []), 1):
        pe = col.get("tooling", {}).get("prompt_execution", {})
        contract = col.get("tooling", {}).get("output_contract", {})
        rows.append([str(i), f"`{col.get('key', '')}`", col.get("title", ""), f"`{col.get('tool_category', '')}`", f"`{col.get('tool', '')}`", yn(pe.get("requires_review"), lang), "<br>".join(f"`{x}`" for x in contract.get("required_fields", [])) or "-"])
    lines += [table(rows), "", f"## {labels['prompts']}", ""]
    if de:
        lines += ["_Prompts werden als Originalauszüge aus dem Paket angezeigt._", ""]
    for col in pkg.get("columns", []):
        pe = col.get("tooling", {}).get("prompt_execution", {})
        contract = col.get("tooling", {}).get("output_contract")
        lines += [f"### {col.get('title', '')}", "", f"- **Key:** `{col.get('key', '')}`", f"- **Tool:** `{col.get('tool', '')}`", f"- **{overview_labels['execution']}:** execute_prompt={yn(pe.get('execute_prompt'), lang)}; mode=`{pe.get('mode', '-')}`; requires_review={yn(pe.get('requires_review'), lang)}", ""]
        if col.get("prompt"):
            lines += ["```text", col["prompt"], "```", ""]
        if contract:
            lines += [f"- **Schema:** `{contract.get('schema_version', '')}`", f"- **{overview_labels['required_fields']}:** {', '.join(f'`{x}`' for x in contract.get('required_fields', []))}", f"- **{overview_labels['evidence_policy']}:** `{contract.get('evidence_policy', '')}`", ""]
    governance = [
        "- Manuelle Spalten sammeln Nutzer- oder Dateieingaben und führen keine Prompts aus.",
        "- Ausführbare Spalten verwenden, sofern konfiguriert, standardmäßig eine manuelle Prüfung.",
        "- Output-Verträge halten nachgelagerte Prüfungen vorhersehbar.",
    ] if de else [
        "- Manual columns collect user or file input and do not execute prompts.",
        "- Executable columns default to manual review where configured.",
        "- Output contracts keep downstream checks predictable.",
    ]
    lines += [f"## {labels['governance']}", "", *governance, ""]
    return "\n".join(lines)


def manifest(packages: list[dict]) -> dict:
    return {
        "schema": MANIFEST_SCHEMA,
        "generated_for": MANIFEST_TARGET,
        "package_count": len(packages),
        "packages": [
            {
                "key": pkg["key"],
                "title": pkg["title"],
                "description": pkg.get("description", ""),
                "columns": len(pkg.get("columns", [])),
                "workflows": len(pkg.get("workflows", [])),
                "source": f"{pkg['key']}.supra",
                "docs": {
                    "en": f"docs/{pkg['key']}.en.md",
                    "de": f"docs/{pkg['key']}.de.md",
                },
            }
            for pkg in packages
        ],
    }


def docs_readme(packages: list[dict]) -> str:
    rows = [["Package", "Description", "Columns", "Workflows", "Deutsch", "English"]]
    for pkg in packages:
        rows.append([
            pkg["title"],
            pkg.get("description", ""),
            str(len(pkg.get("columns", []))),
            str(len(pkg.get("workflows", []))),
            f"[`{pkg['key']}.de.md`]({pkg['key']}.de.md)",
            f"[`{pkg['key']}.en.md`]({pkg['key']}.en.md)",
        ])
    return "\n".join([
        "# `.supra` Example Documentation",
        "",
        "Generated German and English Markdown documentation for every `.supra` package in this examples repository.",
        "Descriptions are read from the source package metadata so this catalog stays aligned with the importable examples.",
        "",
        "![Workflow pipeline](assets/supra-workflow-pipeline.svg)",
        "",
        table(rows),
        "",
        "## Diagrams",
        "",
        "- [Architecture](assets/supra-workbench-architecture.svg)",
        "- [Package anatomy](assets/supra-package-anatomy.svg)",
        "- [Workflow pipeline](assets/supra-workflow-pipeline.svg)",
        "- [Import/export flow](assets/supra-import-export-flow.svg)",
        "- [Governance loop](assets/supra-governance-loop.svg)",
        "",
        "## Standards",
        "",
        "- [The `.supra` v1 Standard](supra-v1-standard.md)",
        "- [`.supra` v1 Standard Fix Playbook](supra-v1-standard-fix.md)",
        "",
        "## Regeneration",
        "",
        "```bash",
        "python3 scripts/generate_docs.py .",
        "python3 scripts/render_assets.py .",
        "```",
        "",
    ])


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", nargs="?", default=".")
    parser.add_argument("--check", action="store_true", help="Fail if expected docs are missing")
    args = parser.parse_args()
    root = Path(args.root)
    docs = root / "docs"
    docs.mkdir(exist_ok=True)
    packages = [json.loads(path.read_text(encoding="utf-8")) for path in sorted(root.glob("*.supra"))]
    missing_de = [pkg["key"] for pkg in packages if pkg["key"] not in GERMAN_DESCRIPTIONS]
    if missing_de:
        raise SystemExit(f"Missing German descriptions for: {', '.join(missing_de)}")
    for pkg in packages:
        for lang in ["en", "de"]:
            target = docs / f"{pkg['key']}.{lang}.md"
            if args.check and not target.exists():
                raise SystemExit(f"Missing generated doc: {target}")
            if not args.check:
                target.write_text(doc(pkg, lang), encoding="utf-8")
    if args.check and not (docs / "README.md").exists():
        raise SystemExit("Missing docs/README.md")
    if args.check and not (root / "examples_manifest.json").exists():
        raise SystemExit("Missing examples_manifest.json")
    if not args.check:
        (docs / "README.md").write_text(docs_readme(packages), encoding="utf-8")
        (root / "examples_manifest.json").write_text(json.dumps(manifest(packages), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"Documentation {'checked' if args.check else 'generated'} for {len(packages)} packages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
