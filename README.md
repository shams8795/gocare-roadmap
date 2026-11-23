# GoCare Roadmap

Requirements analysis for the GoCare AI roadmap (agents and recommendation system), plus the current integration status and action plan.

Original analysis by Shams Abdelhalim. Status review and action plan added 21 Nov 2026.

## Start here

| Page | Source |
|---|---|
| Action Plan: what to work on next | [`docs/action-plan.md`](docs/action-plan.md) |
| Integration Status: what is live today | [`docs/integration-status.md`](docs/integration-status.md) |
| Review Notes: review of the four reports | [`docs/review-notes.md`](docs/review-notes.md) |
| Final Decisions: features ranked by business impact | [`docs/final-decisions.md`](docs/final-decisions.md) |
| Team Requests: catalog and admin-panel problems | [`docs/team-requests.md`](docs/team-requests.md) |

## Endpoint sheet

- [`docs/data/endpoints-reviewed.csv`](docs/data/endpoints-reviewed.csv): reviewed status, code check, next action, owner. **Source of truth.**
- [`docs/data/endpoints-original.csv`](docs/data/endpoints-original.csv): the original testing sheet, unchanged.
- [`docs/data/gocare-endpoints-review.xlsx`](docs/data/gocare-endpoints-review.xlsx): Excel version with Summary (live counts), Reviewed (status dropdown, Owner and Target date to fill), Legend, and Original sheets.

To update: edit `endpoints-reviewed.csv`, then run `python scripts/build_status.py`. It rebuilds the Integration Status page and the Excel file.

## Build the site

```bash
pip install -r requirements.txt
zensical serve        # preview at http://localhost:8000
zensical build        # output in site/
```

Pushing to `main` deploys the site with GitHub Pages (`.github/workflows/pages.yml`). Turn it on once under **Settings → Pages → Source: GitHub Actions**.

## Layout

```
docs/                 markdown pages (one file per feature under recommendation/ and agents/)
docs/data/            endpoint sheet (CSV + Excel)
scripts/              build_status.py
mkdocs.yml            site config and navigation
```

The markdown in `docs/` was rebuilt from the originally published HTML, and gives the same text and page structure on all 53 original pages.
