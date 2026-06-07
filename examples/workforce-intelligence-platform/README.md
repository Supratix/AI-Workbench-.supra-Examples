# SupraWorx Workforce Intelligence Platform

Reference example for knowledge preservation, competence graph management, learning path planning, expert digital twins, skill gap analysis, SpeakSphere ingestion, action receipts, explainable logs, multi-tenant APIs, background workers, and Kubernetes deployment.

## Scope

This example captures operational know-how from SpeakSphere transcripts and documents, stores tenant-scoped evidence, builds a competence graph, and produces auditable recommendations for training and knowledge capture.

All recommendations are advisory and require human review before any organizational action.

## Layout

```text
backend/     Django REST API, models, services, workers, migrations
frontend/    React dashboard widgets
database/    PostgreSQL schema and seed data
deploy/      Docker Compose and Kubernetes manifests
workbench/   Complete mint/workbench JSON templates
docs/        Architecture, API, and runbook notes
```

## Quick start

```bash
cd examples/workforce-intelligence-platform
cp .env.example .env
docker compose -f deploy/docker-compose.yaml up --build
```

API: `http://localhost:8000/api/`
Frontend: `http://localhost:5173`

## API headers

All tenant-scoped calls use `X-Tenant-ID`.

## Main endpoints

```http
GET  /api/experts/
GET  /api/experts/{id}/twin/
POST /api/speaksphere/webhook/
POST /api/capture-workflows/
POST /api/skill-gaps/recalculate/
POST /api/recommendations/learning-paths/
POST /api/graphrag/query/
GET  /api/action-receipts/
GET  /api/explainability-logs/
POST /api/talent-intake/support-analysis/
```

## Agents

The template includes `KnowledgeAgent`, `SkillAgent`, `TrainingAgent`, `TalentIntakeAgent`, `SuccessionAgent`, and `GovernanceAgent`.

## Production notes

Use SSO/OIDC, tenant isolation, encrypted object storage, explicit approvals, and audit exports before production use.