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
3. Enable GitHub Pages with Source set to `GitHub Actions`.
4. Open the GitHub Pages URL.

URL after deployment:

```text
https://xuanho912.github.io/market-predictor/
```

GitHub Pages setting:

```text
https://github.com/xuanho912/market-predictor/settings/pages
```

Set `Build and deployment -> Source -> GitHub Actions`.

Details are in `docs/cloud_deployment.md`.

## Dashboard Output

The GitHub Pages site is a Chinese Market Prediction Dashboard. It shows:

- SPY / QQQ / IWM / DIA market cards.
- Current state, live signal, bounce probability, downside risk, and trend reversal probability.
- Past price plus simulated future paths.
- Base, bounce, bearish, and historical analog scenarios.
- Historical analog dates and invalidation conditions.

Daily workflow outputs:

```text
frontend/public/market-overview.json
frontend/public/simulated-paths.json
frontend/public/prediction-dashboard.json
```

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
