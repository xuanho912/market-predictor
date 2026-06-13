# Free Cloud Deployment

Goal: avoid payment information, avoid charges, and still keep Alpha v1 in daily `forward_only` observation.

Alpha v1 stays frozen:

- signal: `bounce_probability_top_decile_v1`
- threshold: `0.32534311`
- status: `RESEARCH ALPHA CANDIDATE`
- no synthetic live signals
- no threshold tuning
- no use of `down_probability` or `crash_probability` as trade triggers

## Recommended Free Architecture

Use:

- Vercel Free for the mobile PWA frontend.
- GitHub Actions scheduled workflow for daily forward tracker.
- Git commits to persist `outputs/` and frontend static JSON snapshots.
- Optional Render Free Web Service only if you want live API endpoints.

This avoids Render paid instances, persistent disks, Render cron jobs, background workers, databases, and any paid always-on service.

## Why Not Render Blueprint With Disk

The previous Blueprint used:

- `plan: starter`
- a persistent disk mounted at `/var/data`

Those are not free-first settings. The current `render.yaml` has been changed to:

- `plan: free`
- no persistent disk
- no database
- no Render cron job
- no background worker
- temporary `/tmp/market-predictor/...` paths only

Render Free Web Services are optional and should not be relied on for persistence. Free instances can spin down when idle, and local filesystem writes can be lost after sleep, restart, or redeploy.

## Daily Tracker On GitHub Actions

The workflow is:

```text
.github/workflows/forward-alpha-v1.yml
```

It runs:

```bash
python -m backend.app.services.validation.forward_alpha_tracker
python scripts/export_static_alpha_v1.py
```

Then it commits changed files:

- `outputs/forward_alpha_v1_daily_checks.csv`
- `outputs/forward_alpha_v1_signals.csv`
- `outputs/forward_alpha_v1_report.md`
- `frontend/public/alpha-v1-status.json`
- `frontend/public/alpha-v1-analogs.json`

Schedule:

```yaml
cron: "37 22 * * 1-5"
```

This is UTC and intentionally not at minute `0`, reducing the chance of high-load schedule delays.

## Enable GitHub Actions

1. Open `https://github.com/xuanho912/market-predictor/actions`.
2. If GitHub asks, enable workflows for the repository.
3. Open `Forward Alpha v1 Observation`.
4. Click `Run workflow` once to verify.
5. Confirm the workflow commits updated `outputs/` and `frontend/public/*.json`.

No GitHub secrets are required. The workflow uses the repository `GITHUB_TOKEN` with `contents: write`.

## Deploy Frontend On Vercel Free

1. Open Vercel.
2. Import GitHub repo `xuanho912/market-predictor`.
3. Set Root Directory:

```text
frontend
```

4. Deploy as Next.js.
5. Do not set `NEXT_PUBLIC_API_BASE_URL` if you are not deploying a backend.

With no backend URL, the frontend falls back to:

```text
https://raw.githubusercontent.com/xuanho912/market-predictor/main/frontend/public/alpha-v1-status.json
https://raw.githubusercontent.com/xuanho912/market-predictor/main/frontend/public/alpha-v1-analogs.json
```

Optional environment variable:

```text
NEXT_PUBLIC_STATIC_DATA_BASE_URL=https://raw.githubusercontent.com/xuanho912/market-predictor/main/frontend/public
```

## Optional Render Free Backend

Only use this if Render allows you to create a Free Web Service without payment information.

Manual service setup:

1. Render Dashboard -> New -> Web Service.
2. Connect `https://github.com/xuanho912/market-predictor`.
3. Root Directory:

```text
backend
```

4. Runtime:

```text
Python
```

5. Build Command:

```bash
pip install -r requirements.txt
```

6. Start Command:

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

7. Instance Type:

```text
Free
```

8. Environment variables:

```text
PYTHON_VERSION=3.12.13
ENVIRONMENT=production
ALLOW_TRADING=false
PREDICTION_DB_PATH=/tmp/market-predictor/market_predictor.sqlite
PREDICTION_STORE_PATH=/tmp/market-predictor/predictions
FEATURE_STORE_PATH=/tmp/market-predictor/features
MODEL_REGISTRY_PATH=/tmp/market-predictor/models
MARKET_DATA_CACHE_DIR=/tmp/market-predictor/market_data_cache
ALPHA_OUTPUT_DIR=/tmp/market-predictor/outputs
```

If Render still requires payment information, skip Render entirely. The Vercel + GitHub Actions path remains the free path.

## Optional Vercel Env For Backend

If you do have a working Render backend, set this in Vercel and redeploy:

```text
NEXT_PUBLIC_API_BASE_URL=https://<YOUR_RENDER_BACKEND_URL>
```

If the backend sleeps or fails, the frontend still falls back to the GitHub static JSON snapshot.

## What Free Deployment Loses

Compared with paid always-on backend:

- no always-on backend guarantee,
- no persistent backend SQLite storage on Render Free,
- no reliable in-process APScheduler on a sleeping Render Free service,
- frontend may show the latest committed snapshot instead of freshly computed API results,
- GitHub Actions schedule can be delayed or skipped during platform load.

The core forward-only observation remains free because GitHub Actions runs the tracker and commits the resulting audit files.

## Quick Checks

After GitHub Actions runs:

- Open `outputs/forward_alpha_v1_report.md`.
- Open `frontend/public/alpha-v1-status.json`.
- Open `frontend/public/alpha-v1-analogs.json`.

After Vercel deploys:

- Open the Vercel URL on mobile.
- Confirm Alpha v1 status, live signal, symbol bounce probabilities, and Historical Analogs are visible.

Alpha v1 remains `RESEARCH ALPHA CANDIDATE`.
