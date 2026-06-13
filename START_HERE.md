# START HERE

Current state:

- GitHub repo: `https://github.com/xuanho912/market-predictor`
- Alpha v1 signal: `bounce_probability_top_decile_v1`
- Alpha v1 threshold: `0.32534311`
- Alpha v1 status: `RESEARCH ALPHA CANDIDATE`
- Validation mode: `forward_only`

Do not use Alpha v1 for live trading. It is not a confirmed alpha.

## Free Cloud Path

Recommended no-card setup:

1. Enable GitHub Actions in the repo.
2. Run workflow `Forward Alpha v1 Observation` once.
3. Deploy the `frontend` directory to Vercel Free.
4. Do not set a backend URL unless you successfully deploy a free backend.

The frontend can read the latest committed static snapshots:

```text
frontend/public/alpha-v1-status.json
frontend/public/alpha-v1-analogs.json
```

Optional backend:

1. Try Render Free Web Service manually.
2. If Render asks for payment information, skip it.
3. If Render deploys successfully, set Vercel env:

```text
NEXT_PUBLIC_API_BASE_URL=https://<YOUR_RENDER_BACKEND_URL>
```

4. Redeploy Vercel.

Details are in `docs/cloud_deployment.md`.

## Daily Forward Observation

Free persistent daily observation is handled by GitHub Actions:

```text
.github/workflows/forward-alpha-v1.yml
```

Schedule:

```text
37 22 * * 1-5
```

Manual GitHub run:

1. Open `https://github.com/xuanho912/market-predictor/actions`.
2. Select `Forward Alpha v1 Observation`.
3. Click `Run workflow`.

Manual command from repo root:

```powershell
python -m backend.app.services.validation.forward_alpha_tracker
```

## API Checks

Backend:

- `/api/alpha/v1/status`
- `/api/alpha/v1/latest`
- `/api/alpha/v1/signals`
- `/api/alpha/v1/report`
- `/api/analogs/latest?symbol=SPY`
- `/api/analogs/alpha-v1?symbol=SPY`
- `/api/analogs/similar-days?symbol=SPY&top_k=20`

## Historical Analog Engine

Historical analogs are explanatory only. They answer what current conditions resemble historically and whether those analogs support or conflict with the frozen Alpha v1 bounce candidate.

They do not prove alpha, do not change the threshold, and do not upgrade Alpha v1 status.
