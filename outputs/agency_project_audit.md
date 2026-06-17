# Agency Project Audit

This audit applies an agency-style specialist review model to the current Market Prediction Dashboard.

## Executive Read

The project is no longer a simple dashboard. It has a real forecasting architecture: market scenarios, data quality gates, breadth, options/volatility, flow proxy, news/event intelligence, forecast records, model validation, stock prediction, and stock radar ranking.

The main risk is not lack of modules. The main risk is shallow evidence quality in stock-specific analysis and insufficient forward-validation samples.

## Specialist Findings

### Market Forecast Lead

Status: strong architecture, still not validated enough.

Strengths:

- primary / secondary / risk scenario structure exists
- key price levels exist
- stale-data gate exists
- forecast-only language is enforced

Gaps:

- forward completed samples are still the bottleneck
- path accuracy needs more realized records
- any new predictive logic must stay challenger-only

### Investment Researcher / Stock Thesis Analyst

Status: stock module exists, but stock-specific evidence needs depth.

Strengths:

- market -> sector -> stock hierarchy is defined
- top stock radar exists
- stock alpha score exists
- expected range and trigger levels exist

Gaps:

- fundamentals are still shallow or missing for many tickers
- earnings quality and revision data are not deep enough
- company-specific news needs better catalyst classification
- single-stock options and true flow are missing or proxy-only
- stock writeups should include thesis breakers, bull case, bear case, catalyst map, and downside path

Recommended next work:

- SEC/company facts provider as a challenger input
- earnings calendar and earnings-revision quality upgrade
- company news catalyst scoring upgrade
- stock-specific post-forecast error review

### Data Reliability Engineer

Status: much better than early versions, but freshness must stay first.

Strengths:

- data freshness status exists
- FRED raised data completeness
- breadth/internal resonance exists
- stale/proxy/missing labels are part of the design

Gaps:

- any GitHub Pages stale publication must be treated as blocking
- provider latest dates should remain visible
- stock-level data gaps must not silently collapse charts

Recommended next work:

- keep daily freshness gate as the first warning
- add per-stock data availability reasons when a stock chart is blank
- keep caches for resilience but always label stale data

### Model Validation Scientist

Status: governance is good; evidence is early.

Strengths:

- `baseline_v1` is frozen
- challenger framework exists
- model promotion rules exist
- historical replay is separated from forward validation
- ledger immutability is defined

Gaps:

- forward sample count remains too low for high precision or stable alpha claims
- stock radar needs its own validation scorecard
- confluence score must be validated, not just displayed

Recommended next work:

- accumulate forward samples
- compare high radar score versus ordinary watchlist
- compare primary path versus secondary path by horizon
- add error-attribution notes when predictions miss

### Scenario / Confluence Analyst

Status: core concept is right.

Strengths:

- multi-source confluence is now a central project rule
- price, volume, breadth, credit, volatility, flow, news, and analogs are treated as evidence groups

Gaps:

- stock confluence must avoid generic reasons
- missing stock-specific evidence should reduce confidence
- one headline or one technical pattern must not dominate

Recommended next work:

- evidence weight transparency for stock radar candidates
- post-miss attribution: news underestimated, breadth conflict ignored, volatility shock, sector divergence, stale data, or price-structure failure

### Product Terminal Designer

Status: much closer to a terminal, but information discipline must stay strict.

Strengths:

- first-screen hierarchy has improved
- dashboard separates market first, stock second
- validation and data quality are no longer supposed to dominate the top

Gaps:

- stock radar should show candidate ranking before individual stock details
- blank charts must show a data reason, not an empty canvas
- long details should stay folded

Recommended next work:

- keep command center first
- keep data quality and model leaderboard folded
- put stock radar after market forecast

### Security / Secrets Reviewer

Status: key-handling rules are correct.

Strengths:

- API keys are expected in GitHub Secrets
- frontend must not call Finnhub/FRED directly
- public dashboard should show results only

Gaps:

- continue checking `frontend/public` for accidental key leakage
- avoid logging raw provider URLs with keys

## Priority Ranking

Highest priority:

1. Stock-specific evidence depth
2. Freshness and blank-chart diagnostics
3. Forecast miss attribution
4. Forward-validation sample accumulation
5. Challenger-only put/call, gamma, and true-flow inputs

Low priority:

- new UI decorations
- deployment platform changes
- new alpha names
- generic infrastructure refactors

Do not do:

- trading workflow
- buy/sell advice
- paper trading / PnL
- overwriting forecast history
- changing Alpha v1 threshold
- replacing `baseline_v1` without promotion gates

