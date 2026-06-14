# START HERE

Current state:

- GitHub repo: `https://github.com/xuanho912/market-predictor`
- Alpha v1 signal: `bounce_probability_top_decile_v1`
- Alpha v1 threshold: `0.32534311`
- Alpha v1 status: `RESEARCH ALPHA CANDIDATE`
- Validation mode: `forward_only`

Do not use Alpha v1 for live trading. It is not a confirmed alpha.

## Free Cloud Path

Recommended no-card setup while the repo is public:

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

## Recommended Protected Setup

If you want code private and results visible, use this instead:

```text
private core repo:      xuanho912/market-predictor
public dashboard repo: xuanho912/market-predictor-dashboard
```

Private repo Actions secrets:

```text
FINNHUB_API_KEY
DASHBOARD_DEPLOY_TOKEN
```

Private repo Actions variables:

```text
PUBLIC_DASHBOARD_REPO=xuanho912/market-predictor-dashboard
PUBLIC_DASHBOARD_BRANCH=main
PUBLIC_DASHBOARD_BASE_PATH=/market-predictor-dashboard
```

Then the public phone URL is normally:

```text
https://xuanho912.github.io/market-predictor-dashboard/
```

The private repo keeps code, model logic, Skill files, and secrets. The public repo receives only the generated static dashboard. Details are in `docs/private_core_public_dashboard.md`.

## Dashboard Output

The GitHub Pages site is a Chinese Market Prediction Dashboard. It shows:

- SPY / QQQ / IWM / DIA market cards.
- Data Quality Panel with real-data status, stale/missing checks, fallback status, and completeness score.
- Market State Engine v2 probabilities: risk_on, risk_off, oversold_bounce, failed_bounce_risk, downside_continuation, sideways, recovery, panic, no_edge.
- Market Intelligence Engine v3 signal agreement score and edge status: NO_EDGE / WEAK_EDGE / MODERATE_EDGE / STRONG_EDGE.
- Four predictor stack: bounce, downside continuation, trend reversal, risk expansion.
- Model Confidence Score with reasons why confidence is limited.
- Current state, live signal, bounce probability, downside risk, and trend reversal probability.
- 3d / 5d / 10d / 20d / 60d horizon predictions.
- Past price plus simulated future paths.
- Price labels inside the prediction chart, including current price.
- Explicit path weights: base, bounce, bearish, and historical analog.
- Base, bounce, bearish, and historical analog scenarios.
- Historical analog dates and invalidation conditions.

Daily workflow outputs:

```text
frontend/public/data_quality_report.json
frontend/public/high-confidence-signal-report.json
frontend/public/market-overview.json
frontend/public/simulated-paths.json
frontend/public/prediction-dashboard.json
outputs/high_confidence_signal_report.md
```

Current v2 data reality:

- Available: SPY / QQQ / IWM / DIA, VIX, HYG, LQD, TLT, UUP, ^TNX, sector ETFs when public data is available.
- Optional Finnhub: quotes, candle fallback, market status, economic calendar, market news, news sentiment. It requires GitHub Actions Secret `FINNHUB_API_KEY`.
- Proxy only: breadth, flow, liquidity, market structure, credit if FRED OAS is unavailable.
- Fallback only: macro/event calendar.
- Still missing unless a real feed is added: put/call ratio, gamma exposure, true fund flow, constituent-level breadth.

## Daily Forward Observation

Free persistent daily observation is handled by GitHub Actions:

```text
.github/workflows/forward-alpha-v1.yml
```

Schedule:

```text
37 22 * * 1-5
```

This runs automatically after regular US market closes on weekdays. The dashboard shows the latest real trading date, so weekends and market holidays will usually keep showing the prior trading day until the next close completes. You only need a manual run when you want to force an immediate refresh.

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
