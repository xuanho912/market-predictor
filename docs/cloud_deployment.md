# Cloud Deployment

Goal: open one mobile-friendly URL and see Alpha v1 status, live signals, `SPY` / `QQQ` / `IWM` / `DIA` bounce probabilities, distance to threshold, historical analogs, and the forward validation report.

Alpha v1 stays frozen:

- signal: `bounce_probability_top_decile_v1`
- threshold: `0.32534311`
- status: `RESEARCH ALPHA CANDIDATE`
- no synthetic live signals
- no threshold tuning
- no use of `down_probability` or `crash_probability` as trade triggers

## Backend On Render

The repository includes `render.yaml`. Deploy it as a Render Blueprint from the GitHub repository:

1. Open Render and create a new Blueprint.
2. Select `https://github.com/xuanho912/market-predictor`.
3. Confirm the service `market-predictor-backend`.
4. Keep the persistent disk mounted at `/var/data`.
5. Deploy.

The backend uses these important production paths:

- `PREDICTION_DB_PATH=/var/data/market_predictor.sqlite`
- `PREDICTION_STORE_PATH=/var/data/predictions`
- `MARKET_DATA_CACHE_DIR=/var/data/market_data_cache`
- `ALPHA_OUTPUT_DIR=/var/data/outputs`

The FastAPI service runs APScheduler. Every weekday at `FORWARD_TRACKER_UTC_HOUR:FORWARD_TRACKER_UTC_MINUTE`, it runs the same forward-only observation as:

```powershell
python -m backend.app.services.validation.forward_alpha_tracker
```

The default is `22:30 UTC`. Adjust the two environment variables after deployment if a different post-close time is needed.

Important production note: the backend service must be on an always-on plan for the in-process scheduler to run reliably. If the service is asleep, a scheduled job cannot execute.

## Frontend On Vercel

The repository includes `frontend/vercel.json`. Deploy only the `frontend` directory:

1. Import `https://github.com/xuanho912/market-predictor` into Vercel.
2. Set the project root directory to `frontend`.
3. Set environment variable:

```text
NEXT_PUBLIC_API_BASE_URL=https://<YOUR_RENDER_BACKEND_URL>
```

4. Deploy.

Open the Vercel URL on mobile. The home page shows the Alpha v1 block and Historical Analogs block.

## Backend URLs

Replace `<BACKEND_URL>` with the Render URL:

- `<BACKEND_URL>/api/health`
- `<BACKEND_URL>/api/alpha/v1/status`
- `<BACKEND_URL>/api/alpha/v1/latest`
- `<BACKEND_URL>/api/alpha/v1/signals`
- `<BACKEND_URL>/api/alpha/v1/report`
- `<BACKEND_URL>/api/analogs/latest?symbol=SPY`
- `<BACKEND_URL>/api/analogs/alpha-v1?symbol=SPY`
- `<BACKEND_URL>/api/analogs/similar-days?symbol=SPY&top_k=20`

## What Codex Cannot Do Without Authorization

Codex can commit and push deployable configuration, but creating the actual Render and Vercel public URLs requires the owner's platform authorization in the browser. Do not share passwords or tokens in chat.

After the backend URL exists, set `NEXT_PUBLIC_API_BASE_URL` in Vercel and redeploy the frontend.
