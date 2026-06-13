# Free Cloud Deployment With GitHub Pages

Goal: no Vercel, no Render, no payment information, and still keep Alpha v1 in daily `forward_only` observation.

Alpha v1 stays frozen:

- signal: `bounce_probability_top_decile_v1`
- threshold: `0.32534311`
- status: `RESEARCH ALPHA CANDIDATE`
- no synthetic live signals
- no threshold tuning
- no use of `down_probability` or `crash_probability` as trade triggers

## Recommended Free Architecture

Use only GitHub:

- GitHub Actions runs the daily Alpha v1 forward tracker.
- GitHub Actions exports static JSON snapshots.
- GitHub Actions builds the Next.js frontend as a static export.
- GitHub Pages hosts the mobile page.

The public URL will be:

```text
https://xuanho912.github.io/market-predictor/
```

GitHub Pages is available for public repositories on GitHub Free. For private repositories, Pages availability depends on the account plan.

## Required GitHub Setting

Open:

```text
https://github.com/xuanho912/market-predictor/settings/pages
```

Set:

```text
Build and deployment -> Source -> GitHub Actions
```

Save if GitHub shows a save button.

## Daily Tracker And Page Deployment

Workflow:

```text
.github/workflows/forward-alpha-v1.yml
```

It does all of this in one run:

1. Installs backend dependencies.
2. Runs:

```bash
python -m app.services.validation.forward_alpha_tracker
```

3. Exports:

```bash
python scripts/export_static_alpha_v1.py
```

4. Commits updated observation files:

```text
outputs/forward_alpha_v1_daily_checks.csv
outputs/forward_alpha_v1_signals.csv
outputs/forward_alpha_v1_report.md
frontend/public/alpha-v1-status.json
frontend/public/alpha-v1-analogs.json
frontend/public/data_quality_report.json
frontend/public/market-overview.json
frontend/public/simulated-paths.json
frontend/public/prediction-dashboard.json
```

5. Builds the frontend with:

```bash
GITHUB_PAGES=true npm run build
```

6. Deploys `frontend/out` to GitHub Pages.

Schedule:

```yaml
cron: "37 22 * * 1-5"
```

This is UTC and intentionally not at minute `0`, reducing the chance of high-load schedule delays.

## Manual Run

Open:

```text
https://github.com/xuanho912/market-predictor/actions
```

Then:

1. Select `Forward Alpha v1 Observation`.
2. Click `Run workflow`.
3. Wait for success.
4. Open:

```text
https://xuanho912.github.io/market-predictor/
```

GitHub Pages can take a few minutes to publish after the first deployment.

## What The Page Shows

The GitHub Pages page shows:

- Market Prediction Dashboard in Chinese.
- Data Quality Panel and data completeness score.
- Market State Engine v2 with state probabilities and conflicts.
- Model Confidence Score and confidence limits.
- SPY / QQQ / IWM / DIA market cards.
- Current state, live signal, bounce probability, downside risk, and trend reversal probability.
- 3d / 5d / 10d / 20d / 60d horizon predictions.
- Past price plus simulated future paths.
- Base, bounce, bearish, and historical analog scenarios.
- Historical analog dates and invalidation conditions.
- Latest committed forward-only observation snapshot.

The page explicitly marks unavailable data categories. At the current stage, options, breadth, macro, and flow are not connected and must not be treated as real model inputs.

No backend is required for this free path.

## What Free GitHub Pages Loses

Compared with a paid always-on backend:

- no real-time API server,
- no live backend computation when you refresh the page,
- the page shows the latest GitHub Actions snapshot,
- scheduled workflow runs can be delayed by GitHub platform load,
- private repo GitHub Pages may require a paid GitHub plan.

For this project stage, that is acceptable because Alpha v1 is still only a `RESEARCH ALPHA CANDIDATE`.

## Optional Backend Later

If you later want live API calls, deploy a backend separately and set:

```text
NEXT_PUBLIC_API_BASE_URL=https://<BACKEND_URL>
```

Do not use any backend deployment that requires synthetic live signals, threshold changes, or Alpha v1 rule changes.

Alpha v1 remains `RESEARCH ALPHA CANDIDATE`.
