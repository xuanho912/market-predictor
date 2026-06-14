# market-predictor

`market-predictor` is a research-first market trend prediction engine. It is designed to estimate probabilities for broad-market trend, pullback, downside continuation, bounce, reversal, crash risk, and systemic crisis scenarios across multiple horizons and market regimes.

It is a Market Prediction Dashboard, not a Trading Bot. It does not connect to brokers, place orders, provide execution recommendations, or simulate order execution.

## Architecture

- `backend/`: data ingestion, point-in-time feature engineering, labeling, model training, walk-forward backtesting, probability calibration, prediction logging, risk scoring, and explanations.
- `frontend/`: mobile-first display layer for probabilities, regime summaries, risk drivers, and historical prediction quality.
- `docs/`: research framework, labels, data dictionary, modeling plan, validation plan, and risk scoring design.
- `.agents/skills/market-prediction-research/`: reusable Codex Skill for market prediction research tasks.

## MVP Scope

First-stage scope:

- symbols: `SPY`, `QQQ`, `IWM`, `DIA`
- automatic data refresh path, no CSV upload required
- automatic feature generation and labeling interfaces
- rules-based score models
- regime-aware model ensemble with bull, bear, panic, recovery, and high-volatility model slots
- Platt scaling, isotonic regression, and Brier-score probability calibration helpers
- walk-forward replay engine that saves horizon-level prediction logs
- feature importance analysis with permutation importance, SHAP status, ablation, instability, and leakage checks
- ML model entry points for `LogisticRegression`, `RandomForestClassifier`, `HistGradientBoostingClassifier`, and `CalibratedClassifierCV`
- walk-forward backtest summary
- SQLite persistence for prediction records
- APScheduler background refresh hook
- Next.js + React + TypeScript + Tailwind PWA dashboard

No broker integration, no order placement, no order simulation workflow, and no execution recommendations.

## Local Run

Backend:

```powershell
cd market-predictor\backend
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Frontend:

```powershell
cd market-predictor\frontend
npm install
npm run dev
```

Open the frontend at `http://localhost:3000`. The API defaults to `http://localhost:8000`.

Docker Compose:

```powershell
cd market-predictor
docker compose up --build
```

Then open `http://localhost:3000`. The backend API is available at `http://localhost:8000`.

No Docker:

```powershell
cd market-predictor
.\scripts\run_local_windows.ps1
```

This creates a backend virtual environment, installs backend requirements, installs frontend packages, starts FastAPI on `http://localhost:8000`, and starts the PWA on `http://localhost:3000`.

## Deployment

Use `docker-compose.yml` as the local deployment baseline:

1. Build the backend image from `backend/Dockerfile`.
2. Build the frontend image from `frontend/Dockerfile`.
3. Provide production values for the variables in `.env.example`.
4. Mount persistent storage or configure a database for prediction records, feature snapshots, labels, calibration tables, and model registry metadata.
5. Schedule data updates and model evaluation outside the frontend.

Free-first cloud deployment uses GitHub only:

- `.github/workflows/forward-alpha-v1.yml`: runs the frozen Alpha v1 forward tracker, commits updated `outputs/`, builds the static frontend, and deploys GitHub Pages.
- `scripts/export_static_alpha_v1.py`: exports committed tracker results to frontend-readable static JSON, including the Market Prediction Dashboard payload.
- `scripts/export_public_dashboard_bundle.py`: exports a sanitized static dashboard bundle for a public display repository without backend code, research scripts, Codex skills, `.env` files, source maps, or secret markers.
- `scripts/market_intelligence_v2.py`: adds data quality auditing, proxy feature snapshots, Market State Engine v2, model confidence scoring, horizon-specific analog support, and scenario weights.
- `frontend/next.config.js`: switches to static export when `GITHUB_PAGES=true`.
- `docs/cloud_deployment.md`: no-card, GitHub Pages deployment instructions.
- `docs/private_core_public_dashboard.md`: recommended private-code / public-results structure.

The recommended free path is GitHub Actions plus GitHub Pages. No Vercel, no Render, no payment information.

If the code repository stays public, the published URL after Pages is enabled:

```text
https://xuanho912.github.io/market-predictor/
```

If you want to protect the core work, use the recommended two-repository structure:

```text
private: xuanho912/market-predictor
public:  xuanho912/market-predictor-dashboard
```

The private repository runs the model and generates results. The public repository receives only the generated static dashboard. Configure these private-repo Actions variables:

```text
PUBLIC_DASHBOARD_REPO=xuanho912/market-predictor-dashboard
PUBLIC_DASHBOARD_BRANCH=main
PUBLIC_DASHBOARD_BASE_PATH=/market-predictor-dashboard
```

Configure this private-repo Actions secret:

```text
DASHBOARD_DEPLOY_TOKEN
```

Use a fine-grained token with `Contents: read/write` access only to the public dashboard repository. Keep `FINNHUB_API_KEY` as a secret. Do not put API keys in code, README files, frontend public JSON, or `NEXT_PUBLIC_*` variables.

Then the phone URL is normally:

```text
https://xuanho912.github.io/market-predictor-dashboard/
```

The static page reads the latest committed snapshots:

```text
frontend/public/alpha-v1-status.json
frontend/public/alpha-v1-analogs.json
frontend/public/market-overview.json
frontend/public/simulated-paths.json
frontend/public/prediction-dashboard.json
frontend/public/forecast-records.json
frontend/public/forecast-accuracy-scorecard.json
frontend/public/flow-status.json
```

Market Intelligence Engine v5 adds an immutable forecast accuracy ledger:

- `outputs/forecast_records.csv`: append/preserve daily forecast rows. Forecast fields are write-once by `forecast_id`; future runs may only backfill realized returns, best-matching scenario, primary-hit fields, and status.
- `frontend/public/forecast-records.json`: sanitized frontend-readable forecast ledger.
- `outputs/forecast_accuracy_scorecard.md` and `frontend/public/forecast-accuracy-scorecard.json`: horizon-specific accuracy tracking for primary scenario hit rate, primary-vs-secondary path accuracy, edge-status buckets, high-confidence buckets, and breadth/options/flow confirmation buckets.
- `frontend/public/flow-status.json` and `outputs/flow_data_status.md`: proxy-only flow / positioning status. This is not true fund flow unless a real feed is explicitly connected.

If a live backend is added later, set `NEXT_PUBLIC_API_BASE_URL` during the frontend build. This is optional and not required for the free Pages path.

## Update Data

Data updates must be point-in-time. Each provider record should include:

- observation date
- release timestamp
- revision timestamp, if applicable
- data vendor and symbol
- availability lag
- ingestion timestamp

Planned command:

```powershell
cd market-predictor\backend
python -m app.services.data_providers.pipeline --as-of 2026-06-13
```

Do not overwrite historical macro releases with revised values unless the revision is stored separately.

The API also exposes:

```powershell
Invoke-RestMethod -Method Post http://localhost:8000/api/admin/refresh-data
```

The local MVP starts APScheduler on API startup so users do not need to upload CSV files or manually run daily scripts.

The market data downloader uses this priority order:

1. `yfinance`
2. direct Yahoo chart API
3. Stooq
4. local cache from a prior real-data download
5. synthetic fallback for smoke tests only

Synthetic fallback data is never allowed to create Alpha v1 forecast signals.

## Train Models

Models must be trained separately by horizon and label family. Do not use a single model for all horizons. Regime must be identified before interpreting features or calibrating model probabilities.

Planned command:

```powershell
cd market-predictor\backend
python -m app.services.models.train --label crash_risk_60d --horizon 60d
```

Training must persist:

- feature definition version
- label definition version
- regime definition version
- train and validation windows
- model parameters
- calibration method
- probability outputs
- explanations

## API

Required MVP endpoints:

- `GET /api/health`
- `GET /api/markets`
- `GET /api/prediction/latest?symbol=SPY`
- `GET /api/prediction/history?symbol=SPY`
- `GET /api/prediction/horizon?symbol=SPY&horizon=5d`
- `GET /api/features/latest?symbol=SPY`
- `GET /api/explanations/latest?symbol=SPY`
- `GET /api/similar-days?symbol=SPY`
- `GET /api/backtest/summary?symbol=SPY`
- `GET /api/evaluation/report?symbol=SPY`
- `GET /api/alpha/v1/status`
- `GET /api/alpha/v1/latest`
- `GET /api/alpha/v1/signals`
- `GET /api/alpha/v1/report`
- `GET /api/analogs/latest?symbol=SPY`
- `GET /api/analogs/alpha-v1?symbol=SPY`
- `GET /api/analogs/similar-days?symbol=SPY&top_k=20`
- `POST /api/admin/refresh-data`
- `POST /api/admin/retrain`
- `POST /api/admin/run-backtest`

Prediction responses include market regime, horizon probabilities, expected return, confidence, pullback risk score, crisis risk score, bounce probability, bounce quality score, downside continuation probability, trend reversal probability, dead-cat bounce risk, top reasons, similar historical days, and current risk source breakdown.

The evaluation report includes overall prediction accuracy, by-regime accuracy, by-horizon accuracy, calibration quality, best and worst forecast signal types, and an expected forecast edge score. The score is diagnostic only; this project tracks forecast quality and scenario outcomes.

## Alpha v1 Forward Observation

Current frozen candidate:

- Signal: `bounce_probability_top_decile_v1`
- Version: `alpha_v1`
- Threshold: `0.32534311`
- Status: `RESEARCH ALPHA CANDIDATE`
- Validation mode: `forward_only`

Alpha v1 is not a confirmed alpha and must not be used as an execution recommendation. It is only a frozen forecast signal and bounce-scenario input until enough post-freeze observations mature with stable prediction accuracy. Do not change the threshold, add new features, retune the model, or reuse `alpha_v1` for a modified rule. Any future change must be versioned as `alpha_v2` or later.

Run the daily forward tracker from the repository root:

```powershell
cd market-predictor
python -m backend.app.services.validation.forward_alpha_tracker
```

On Windows, use:

```powershell
cd market-predictor
.\scripts\run_forward_tracker_windows.ps1
```

The tracker:

- refreshes the latest market data,
- generates current predictions for `SPY`, `QQQ`, `IWM`, and `DIA`,
- records a daily check even when there is no signal,
- appends triggered signals to `outputs/forward_alpha_v1_signals.csv`,
- keeps all signal rows marked `validation_period=forward_only`,
- backfills 3d/5d/10d/20d/60d realized returns when mature,
- updates `outputs/forward_alpha_v1_report.md`.

Query Alpha v1 status:

```powershell
Invoke-RestMethod http://localhost:8000/api/alpha/v1/status
Invoke-RestMethod http://localhost:8000/api/alpha/v1/latest
Invoke-RestMethod http://localhost:8000/api/alpha/v1/signals
Invoke-RestMethod http://localhost:8000/api/alpha/v1/report
```

The status API returns whether there is a forecast signal, the latest checked date, latest `bounce_probability` by symbol, distance to threshold, expected validation horizons, data source status, and the risk note. If there is no forecast signal, the next action is continued observation. If real data fails, the next action is no forecast signal because the real data source failed. If a forecast signal appears, the next action is scenario validation and forward return tracking.

To schedule the tracker after market close on Windows, see `docs/windows_daily_tracker_setup.md`.

Free cloud scheduling uses GitHub Actions:

```text
.github/workflows/forward-alpha-v1.yml
```

It runs automatically on weekdays at `22:37 UTC`, updates `outputs/forward_alpha_v1_*`, exports static frontend JSON, commits the changes back to the repository, builds the static frontend, and deploys GitHub Pages. This is the preferred no-card option because Render Free services can sleep and lose local filesystem writes.

The dashboard date is the latest real market data date, not the calendar date. On weekends and US market holidays it is normal for the dashboard to keep showing the prior market session until the next market-close workflow finishes. Manual `Run workflow` is only needed when you want an immediate refresh or deployment check.

## Market Intelligence Engine v2

The dashboard is no longer only an Alpha v1 observer. Each GitHub Actions run also exports:

```text
frontend/public/data_quality_report.json
frontend/public/high-confidence-signal-report.json
frontend/public/market-overview.json
frontend/public/simulated-paths.json
frontend/public/prediction-dashboard.json
outputs/high_confidence_signal_report.md
```

Current real data coverage:

- price: SPY / QQQ / IWM / DIA
- volatility: VIX level, 5d/20d change, percentile
- credit proxies: HYG / LQD relative strength, HYG drawdown
- rates and liquidity proxies: ^TNX, TLT, UUP
- market structure proxies: small cap vs large cap, growth vs SPY, DIA vs SPY

Explicitly not available unless real feeds are added:

- breadth: advance/decline, new highs/lows, percent above moving averages
- options: VVIX, put/call, skew, gamma, dealer positioning
- macro: economic release calendar and point-in-time revisions
- flow: ETF flow, fund flow, option flow

The page shows `data_completeness_score`, `model_confidence_score`, Market State Engine v2 probabilities, 3d/5d/10d/20d/60d horizon predictions, period-specific historical analog support, and scenario path weights. Missing data reduces confidence and is shown directly on the page.

## Market Intelligence Engine v3

V3 adds a higher-quality signal layer without changing Alpha v1:

- optional Finnhub provider via GitHub Actions Secret `FINNHUB_API_KEY` for quotes, candle fallback, market status, economic calendar, market news and news sentiment where available,
- additional market symbols for volatility term proxies, sector breadth proxies, high-beta/low-vol rotation, and equal-weight/cap-weight comparison,
- FRED downloader for HY OAS, IG OAS, 10Y, 2Y, 3M and real-yield proxy when available,
- explicit `available / proxy / fallback / missing / stale` source status in `data_quality_report.json`,
- `signal_agreement_score` with supporting and conflicting signals,
- four predictor outputs: bounce, downside continuation, trend reversal, risk expansion,
- `market_edge_status`: `NO_EDGE`, `WEAK_EDGE`, `MODERATE_EDGE`, `STRONG_EDGE`,
- explicit simulated path weights: `base_path_weight`, `bounce_path_weight`, `bearish_path_weight`, `analog_path_weight`,
- high-confidence signal report focused on top-confidence buckets instead of full-sample accuracy.

Proxy categories are clearly labeled. Breadth uses sector ETFs and RSP/SPY, not constituent-level breadth. Flow uses volume and rotation proxies, not real fund-flow data. Macro currently uses a deterministic event-calendar fallback, not a live economic calendar feed.

Simulated path weights are driven by bounce probability, failed-bounce risk, signal agreement, historical analog support, credit stability, volatility reversal, breadth support, and data completeness. If data completeness falls below the threshold, the path is marked `low_confidence_simulation`.

Finnhub responses are cached under `data/finnhub_cache` during GitHub Actions. The cache is ignored by git and the API key is never written to code, README, public JSON, logs, or frontend environment variables.

## Historical Analog Engine

The Historical Analog Engine is an explanation and auxiliary validation module, not a replacement for Alpha v1.

It answers:

- which historical dates had similar market structure,
- how those analogs performed after 3d/5d/10d/20d/60d,
- whether the frozen Alpha v1 bounce signal is historically supported or conflicting,
- what conditions are shared with historical analogs,
- what current risks differ from the analog set.

Similarity is computed across market structure, not only price:

- 20d/60d return
- drawdown depth
- RSI / oversold level
- VIX level and VIX changes
- credit proxy and HYG/LQD relative strength
- TLT, UUP, and 10-year yield proxy
- regime
- bounce probability
- volatility contribution
- market stress score
- liquidity proxy

The engine implements z-score normalized Euclidean distance, cosine similarity, and regime-filtered nearest neighbors. It never uses future returns to choose similar days; future returns are attached only after retrieval for conditional distribution and explanation.

Historical analogs are not proof of alpha. They must not be used to change the Alpha v1 threshold, retune the model, or upgrade Alpha v1 from `RESEARCH ALPHA CANDIDATE`.

## Validate Models

Validation must use walk-forward time splits. Random train/test splits are not allowed.

Planned command:

```powershell
cd market-predictor\backend
python -m app.services.backtesting.walk_forward --sample
```

Track at least:

- Brier score
- log loss
- calibration curve
- expected calibration error
- precision/recall by probability bucket
- regime-conditioned calibration
- hit rate by regime
- drawdown/crisis recall
- false alarm rate

The concrete engine is `backend/app/services/backtesting/walk_forward_engine.py`. It replays historical forecasts using only prior-window data, evaluates 1d/3d/5d/10d/20d/60d horizons, stores forecast rows in `predictions_log`, and reports regime breakdowns.

## Prediction Logging

SQLite stores two levels:

- `prediction_records`: complete JSON snapshots for API history.
- `predictions_log`: one row per timestamp, symbol, and horizon with up/down/sideways probabilities, bounce probability, crash probability, future realized return, and error metrics.

This log is the audit trail for proving whether the engine is learning or only producing attractive charts.

## Research Discipline

Start every prediction task by defining labels and horizons. Then decide which point-in-time features are allowed at each forecast timestamp. See `docs/labels.md`, `docs/data_dictionary.md`, and `.agents/skills/market-prediction-research/SKILL.md`.

## Push To GitHub

If the environment cannot create a remote GitHub repository directly, initialize and push manually:

```powershell
git init
git add .
git commit -m "Freeze alpha v1 bounce candidate and forward validation framework"
git branch -M main
git remote add origin <YOUR_GITHUB_REPO_URL>
git push -u origin main
```

Windows helper:

```powershell
cd market-predictor
.\scripts\setup_git_push_windows.ps1
```

If a remote already exists:

```powershell
git status
git add .
git commit -m "Freeze alpha v1 bounce candidate and forward validation framework"
git branch -M main
git push -u origin main
```
