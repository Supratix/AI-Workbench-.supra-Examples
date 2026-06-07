# AI Workbench `.supra` Examples

![AI Workbench .supra Examples](docs/assets/social-preview.png)

A ready-to-publish GitHub repository for SupraTix AI Workbench `.supra` example packages. The repository is designed to be copied into:

```text
/Users/tobiasgoecke/supraworxv30/mint/workbench/examples
```

It contains example `.supra` packages, generated bilingual package documentation, JSON schemas, validation scripts, governance notes, and reusable image assets for a polished public or private GitHub presentation.

## What is included

- **43 `.supra` packages** at the repository root.
- **English and German generated documentation** under [`docs/`](docs/README.md).
- **Schema contracts** under [`schemas/`](schemas/) for package-level validation and output-contract checks.
- **Local validation scripts** under [`scripts/`](scripts/).
- **GitHub Actions workflow** to validate examples on every pull request.
- **Image assets** for the README, docs, social preview, architecture, workflow, package anatomy, import/export, and governance diagrams.

## Fast start

```bash
# 1) Copy or unzip this repository into your examples folder
cd /Users/tobiasgoecke/supraworxv30/mint/workbench/examples

# 2) Validate every .supra package
python3 scripts/validate_supra.py .

# 3) Regenerate docs after edits
python3 scripts/generate_docs.py .

# 4) Optional: regenerate image assets
python3 scripts/render_assets.py .
```

## Repository layout

```text
.
├── *.supra                         # AI Workbench example packages
├── README.md                       # GitHub landing page
├── examples_manifest.json          # Machine-readable package catalog
├── docs/
│   ├── README.md                   # Package index
│   ├── *.en.md / *.de.md           # Generated package docs
│   └── assets/                     # SVG and PNG diagrams
├── schemas/                        # JSON schemas and contract notes
├── scripts/                        # Validation, docs, and asset generators
├── tests/                          # Lightweight pytest compatibility tests
└── .github/                        # CI, issue templates, PR template
```

## Package catalog

| Package                                         | Columns | Workflows | Docs                                                                                                                    |
| ----------------------------------------------- | ------- | --------- | ----------------------------------------------------------------------------------------------------------------------- |
| AE Valley Grant/Tender/Project URL Condenser    | 17      | 1         | [EN](docs/aevalley_grant_tender_url_condenser.en.md) · [DE](docs/aevalley_grant_tender_url_condenser.de.md)             |
| Data Analytics Experiment And Launch Analyzer   | 4       | 1         | [EN](docs/data_analytics_experiment_launch_analyzer.en.md) · [DE](docs/data_analytics_experiment_launch_analyzer.de.md) |
| Data Analytics KPI Framework Designer           | 4       | 1         | [EN](docs/data_analytics_kpi_framework_designer.en.md) · [DE](docs/data_analytics_kpi_framework_designer.de.md)         |
| Data Analytics KPI Operating Review             | 4       | 1         | [EN](docs/data_analytics_kpi_operating_review.en.md) · [DE](docs/data_analytics_kpi_operating_review.de.md)             |
| Data Analytics Market And Opportunity Sizer     | 4       | 1         | [EN](docs/data_analytics_market_opportunity_sizer.en.md) · [DE](docs/data_analytics_market_opportunity_sizer.de.md)     |
| Lieferschein → Lagerbestand (Internal Products) | 3       | 0         | [EN](docs/lieferschein_inventory.en.md) · [DE](docs/lieferschein_inventory.de.md)                                       |
| LinkedIn Extreme Engagement Posting             | 9       | 1         | [EN](docs/linkedin_extreme_engagement_posting.en.md) · [DE](docs/linkedin_extreme_engagement_posting.de.md)             |
| SME AI Adoption Readiness Sprint                | 4       | 1         | [EN](docs/sme_ai_adoption_readiness_sprint.en.md) · [DE](docs/sme_ai_adoption_readiness_sprint.de.md)                   |
| SME Cashflow War Room                           | 4       | 1         | [EN](docs/sme_cashflow_war_room.en.md) · [DE](docs/sme_cashflow_war_room.de.md)                                         |
| SME Churn Rescue Desk                           | 4       | 1         | [EN](docs/sme_churn_rescue_desk.en.md) · [DE](docs/sme_churn_rescue_desk.de.md)                                         |
| SME Compliance Evidence Pack                    | 4       | 1         | [EN](docs/sme_compliance_evidence_pack.en.md) · [DE](docs/sme_compliance_evidence_pack.de.md)                           |
| SME Customer Reply                              | 4       | 1         | [EN](docs/sme_customer_reply.en.md) · [DE](docs/sme_customer_reply.de.md)                                               |
| SME Cyber Hygiene Action Board                  | 4       | 1         | [EN](docs/sme_cyber_hygiene_action_board.en.md) · [DE](docs/sme_cyber_hygiene_action_board.de.md)                       |
| SME Data Cleanup Command Center                 | 4       | 1         | [EN](docs/sme_data_cleanup_command_center.en.md) · [DE](docs/sme_data_cleanup_command_center.de.md)                     |
| SME Deadstock Liquidator                        | 4       | 1         | [EN](docs/sme_deadstock_liquidator.en.md) · [DE](docs/sme_deadstock_liquidator.de.md)                                   |
| SME Downtime Triage                             | 4       | 1         | [EN](docs/sme_downtime_triage.en.md) · [DE](docs/sme_downtime_triage.de.md)                                             |
| SME Energy Cost Anomaly Finder                  | 4       | 1         | [EN](docs/sme_energy_cost_anomaly_finder.en.md) · [DE](docs/sme_energy_cost_anomaly_finder.de.md)                       |
| SME Field Service Route Optimizer               | 4       | 1         | [EN](docs/sme_field_service_route_optimizer.en.md) · [DE](docs/sme_field_service_route_optimizer.de.md)                 |
| SME Grant Funding Fit Radar                     | 4       | 1         | [EN](docs/sme_grant_funding_fit_radar.en.md) · [DE](docs/sme_grant_funding_fit_radar.de.md)                             |
| SME Hiring Scorecard Kit                        | 4       | 1         | [EN](docs/sme_hiring_scorecard_kit.en.md) · [DE](docs/sme_hiring_scorecard_kit.de.md)                                   |
| SME Invoice Dispute Resolver                    | 4       | 1         | [EN](docs/sme_invoice_dispute_resolver.en.md) · [DE](docs/sme_invoice_dispute_resolver.de.md)                           |
| SME Late Payment Collector                      | 4       | 1         | [EN](docs/sme_late_payment_collector.en.md) · [DE](docs/sme_late_payment_collector.de.md)                               |
| SME Lead Qualifier                              | 4       | 1         | [EN](docs/sme_lead_qualifier.en.md) · [DE](docs/sme_lead_qualifier.de.md)                                               |
| SME Local SEO Content Engine                    | 4       | 1         | [EN](docs/sme_local_seo_content_engine.en.md) · [DE](docs/sme_local_seo_content_engine.de.md)                           |
| SME Margin Leak Detector                        | 4       | 1         | [EN](docs/sme_margin_leak_detector.en.md) · [DE](docs/sme_margin_leak_detector.de.md)                                   |
| SME Meeting Summarizer                          | 4       | 1         | [EN](docs/sme_meeting_summarizer.en.md) · [DE](docs/sme_meeting_summarizer.de.md)                                       |
| SME Onboarding Micro-SOP Factory                | 4       | 1         | [EN](docs/sme_onboarding_micro_sop_factory.en.md) · [DE](docs/sme_onboarding_micro_sop_factory.de.md)                   |
| SME Pricing Power Simulator                     | 4       | 1         | [EN](docs/sme_pricing_power_simulator.en.md) · [DE](docs/sme_pricing_power_simulator.de.md)                             |
| SME Product Launch Kill/Scale Gate              | 4       | 1         | [EN](docs/sme_product_launch_kill_scale_gate.en.md) · [DE](docs/sme_product_launch_kill_scale_gate.de.md)               |
| SME Proposal Drafter                            | 4       | 1         | [EN](docs/sme_proposal_drafter.en.md) · [DE](docs/sme_proposal_drafter.de.md)                                           |
| SME Quote-to-Cash Bottleneck Scanner            | 4       | 1         | [EN](docs/sme_quote_to_cash_bottleneck.en.md) · [DE](docs/sme_quote_to_cash_bottleneck.de.md)                           |
| SME Review Reputation Responder                 | 4       | 1         | [EN](docs/sme_review_reputation_responder.en.md) · [DE](docs/sme_review_reputation_responder.de.md)                     |
| SME Safety Incident Prevention Loop             | 4       | 1         | [EN](docs/sme_safety_incident_prevention.en.md) · [DE](docs/sme_safety_incident_prevention.de.md)                       |
| SME Shift Handover Risk Radar                   | 4       | 1         | [EN](docs/sme_shift_handover_risk_radar.en.md) · [DE](docs/sme_shift_handover_risk_radar.de.md)                         |
| SME SOP Builder                                 | 4       | 1         | [EN](docs/sme_sop_builder.en.md) · [DE](docs/sme_sop_builder.de.md)                                                     |
| SME Subscription Retention Playbook             | 4       | 1         | [EN](docs/sme_subscription_retention_playbook.en.md) · [DE](docs/sme_subscription_retention_playbook.de.md)             |
| SME Tender No-Bid Gate                          | 4       | 1         | [EN](docs/sme_tender_no_bid_gate.en.md) · [DE](docs/sme_tender_no_bid_gate.de.md)                                       |
| SME Training Skill Gap Matrix                   | 4       | 1         | [EN](docs/sme_training_skill_gap_matrix.en.md) · [DE](docs/sme_training_skill_gap_matrix.de.md)                         |
| SME Upsell Signal Miner                         | 4       | 1         | [EN](docs/sme_upsell_signal_miner.en.md) · [DE](docs/sme_upsell_signal_miner.de.md)                                     |
| SME Vendor Negotiation Brief                    | 4       | 1         | [EN](docs/sme_vendor_negotiation_brief.en.md) · [DE](docs/sme_vendor_negotiation_brief.de.md)                           |
| SME Warranty Root Cause Radar                   | 4       | 1         | [EN](docs/sme_warranty_root_cause_radar.en.md) · [DE](docs/sme_warranty_root_cause_radar.de.md)                         |
| SME Webshop Conversion Rescue                   | 4       | 1         | [EN](docs/sme_webshop_conversion_rescue.en.md) · [DE](docs/sme_webshop_conversion_rescue.de.md)                         |
| VUCA Support Report Builder                     | 15      | 1         | [EN](docs/vuca_support_report_builder.en.md) · [DE](docs/vuca_support_report_builder.de.md)                             |

## `.supra` package conventions

Each package is JSON with a `.supra` extension. The key sections are:

1. `metadata` — vendor, version, starter rows, commerce metadata, and GitHub-example notes.
2. `columns` — manual, AI-tool, and shortcut columns with prompt execution settings.
3. `workflows` — ordered workbench steps when the package is workflow-enabled.
4. `main_workbench` — a portable workbench definition that mirrors the package columns and workflows.
5. `tooling.output_contract` — expected JSON shape, required fields, quality gate, and evidence policy.

## Import flow

![Import flow](docs/assets/supra-import-export-flow.svg)

1. Validate package JSON locally.
2. Review generated docs and output contracts.
3. Import the `.supra` file into AI Workbench.
4. Run starter rows in manual-review mode.
5. Capture improvements as a pull request.

## Governance baseline

The examples intentionally default to human-reviewable execution. Prompts ask the model to separate facts from assumptions, mark evidence gaps, and avoid invented facts. Finance, legal, safety, and compliance-sensitive recommendations are marked for responsible human review.

## Publishing checklist

- [ ] Confirm package titles and descriptions.
- [ ] Run `python3 scripts/validate_supra.py .`.
- [ ] Run `python3 scripts/generate_docs.py .` and commit changed docs.
- [ ] Review diagrams in `docs/assets/`.
- [ ] Decide whether this repository should use `LICENSE.template` or a project-specific license.
- [ ] Create the GitHub repository and push.

## Copy into your local Supraworx tree

```bash
rsync -av --exclude .git ./ /Users/tobiasgoecke/supraworxv30/mint/workbench/examples/
cd /Users/tobiasgoecke/supraworxv30/mint/workbench/examples
python3 scripts/validate_supra.py .
```

## Maintainer notes

This repository is intentionally dependency-light. The validation script uses the Python standard library only. PNG asset regeneration uses Pillow when available and falls back to SVG-only output if Pillow is not installed.
