# Contributing

Thanks for improving the AI Workbench `.supra` examples.

## Contribution flow

1. Create or edit a `.supra` package at the repository root.
2. Keep package keys lowercase and underscore-separated.
3. Add or update starter rows with realistic but non-sensitive sample data.
4. Run validation:

   ```bash
   python3 scripts/validate_supra.py .
   ```

5. Regenerate docs:

   ```bash
   python3 scripts/generate_docs.py .
   ```

6. Open a pull request with a short package summary, screenshots or diagrams if helpful, and any governance considerations.

## Review checklist

- No secrets, credentials, customer data, or private URLs.
- Prompts require facts, assumptions, evidence gaps, and reviewable actions.
- Output contracts include required fields and JSON expectations.
- Human review remains enabled for consequential outputs.
