# Free Cloud Deployment With GitHub Pages

Goal: no Vercel, no Render, no payment information, and still keep Alpha v1 in daily `forward_only` forecast validation.

Alpha v1 stays frozen:

- signal: `bounce_probability_top_decile_v1`
- threshold: `0.32534311`
- status: `RESEARCH ALPHA CANDIDATE`
- no synthetic forecast signals
- no threshold tuning
- no use of `down_probability` or `crash_probability` as order triggers or execution recommendations

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

## Privacy-First Free Architecture

If you do not want the core code to be public, use two repositories:

```text
private core:      xuanho912/market-predictor
public dashboard: xuanho912/market-predictor-dashboard
```

The private core repository keeps:

- backend code,
- model logic,
- feature engineering,
- validation scripts,
- Codex Skill files,
- research documents,
- GitHub Actions secrets.

The public dashboard repository receives only:

- generated HTML/CSS/JS static dashboard files,
- generated JSON prediction snapshots,
- a `dashboard_manifest.json` saying this is public static output only.

It does not receive `backend/`, `scripts/`, `.agents/`, `.github/`, `.env`, data caches, model files, or API keys.

Private core repository settings:

```text
Settings -> Secrets and variables -> Actions
```

Secrets:

```text
FINNHUB_API_KEY
DASHBOARD_DEPLOY_TOKEN
```

Use a fine-grained `DASHBOARD_DEPLOY_TOKEN` with access only to `xuanho912/market-predictor-dashboard` and only `Contents: read/write`.

Variables:

```text
PUBLIC_DASHBOARD_REPO=xuanho912/market-predictor-dashboard
PUBLIC_DASHBOARD_BRANCH=main
PUBLIC_DASHBOARD_BASE_PATH=/market-predictor-dashboard
```

Public dashboard repository Pages setting:

```text
Build and deployment -> Source -> Deploy from a branch
Branch -> main
Folder -> / (root)
```

Public URL:

```text
https://xuanho912.github.io/market-predictor-dashboard/
```

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
frontend/public/high-confidence-signal-report.json
frontend/public/market-overview.json
frontend/public/simulated-paths.json
frontend/public/prediction-dashboard.json
outputs/high_confidence_signal_report.md
```

5. Builds the frontend with:

```bash
GITHUB_PAGES=true npm run build
```

6. Exports and safety-scans a public-only dashboard bundle:

```bash
python scripts/export_public_dashboard_bundle.py --source frontend/out --dest outputs/public_dashboard_site
```

7. If `PUBLIC_DASHBOARD_REPO` is configured, publishes only `outputs/public_dashboard_site` to the public dashboard repository.

8. If the core repository is public, deploys `frontend/out` to the same repository's GitHub Pages.

If the core repository is private, same-repo Pages deployment is skipped. The public dashboard repository remains the free display path.

Schedule:

```yaml
cron: "37 22 * * 1-5"
```

This is UTC and intentionally not at minute `0`, reducing the chance of high-load schedule delays.

The public dashboard shows the latest real market data day, not the current calendar day. If today is a weekend or US market holiday, the latest date should remain the previous market session. The workflow still re-fetches data on every run; stale or failed data must be marked as `stale_data` or `data_source_failed`, never silently reused as fresh.

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
- Market Intelligence Engine v3 with signal agreement score, edge status and four predictor outputs.
- Model Confidence Score and confidence limits.
- SPY / QQQ / IWM / DIA market cards.
- Current state, forecast signal status, bounce probability, downside risk, and trend reversal probability.
- 3d / 5d / 10d / 20d / 60d horizon predictions.
- Past price plus simulated future paths.
- Base, bounce, bearish, and historical analog scenarios.
- Historical analog dates and invalidation conditions.
- Latest committed forward-only observation snapshot.

The page explicitly marks unavailable or proxy data categories. Breadth and flow are proxy-based until real feeds are connected; macro/event risk is a fallback calendar approximation. These improve situational awareness but do not confirm alpha.

No backend is required for this free path.

## What Is Protected

The privacy-first setup protects:

- core source code,
- model and feature logic,
- validation workflow internals,
- Codex Skill and research framework,
- API keys and deployment tokens.

It cannot protect what is intentionally displayed on the public dashboard. Anyone who can open the public URL can view the visible prediction results and chart data.

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

Do not use any backend deployment that requires synthetic forecast signals, threshold changes, or Alpha v1 rule changes.

Alpha v1 remains `RESEARCH ALPHA CANDIDATE`.
