# START HERE

Current state:

- GitHub repo: `https://github.com/xuanho912/market-predictor`
- Alpha v1 signal: `bounce_probability_top_decile_v1`
- Alpha v1 threshold: `0.32534311`
- Alpha v1 status: `RESEARCH ALPHA CANDIDATE`
- Validation mode: `forward_only`

Do not use Alpha v1 for live trading. It is not a confirmed alpha.

## Cloud Path

1. Deploy backend with `render.yaml` from the GitHub repo.
2. Copy the Render backend URL.
3. Deploy the `frontend` directory to Vercel.
4. Set Vercel env:

```text
NEXT_PUBLIC_API_BASE_URL=https://<YOUR_RENDER_BACKEND_URL>
```

5. Open the Vercel frontend URL on mobile.

Details are in `docs/cloud_deployment.md`.

## Daily Forward Observation

The backend schedules Alpha v1 forward-only observation on weekdays using APScheduler:

```text
FORWARD_TRACKER_UTC_HOUR=22
FORWARD_TRACKER_UTC_MINUTE=30
```

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
