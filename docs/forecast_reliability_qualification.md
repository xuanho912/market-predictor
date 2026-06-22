# Forecast Reliability Qualification

This project is not considered a dependable forecasting tool just because it can draw paths or produce probabilities.
It earns that status only after passing the gates below.

## Current Role

Until the gates pass, the dashboard is a market radar and forecast research terminal:

- It can summarize market state.
- It can rank probability paths.
- It can highlight confluence and conflicts.
- It can record forecasts and later compare them with actual outcomes.
- It must not claim high precision, stable alpha or validated forecasting ability.

## Minimum Qualification Gates

### 1. Fresh Data Gate

The dashboard must use the latest completed US market trading day.

Required:

- `data_freshness_status` is `fresh` or `market_closed`.
- `stale` and `provider_failed` block current-day forecast use.
- `market_open_unconfirmed` may be viewed as an intraday snapshot but cannot append a baseline forecast record.

### 2. Data Completeness Gate

Required:

- Data completeness >= 85/100.
- Missing sources must be visible.
- Proxy data must remain marked as proxy.
- No synthetic data may create a live forecast.

### 3. Forward Sample Gate

Required before the dashboard can be treated as dependable:

- 1d completed samples >= 20
- 3d completed samples >= 20
- 5d completed samples >= 20
- 10d completed samples >= 30
- 20d completed samples >= 50
- 60d completed samples >= 50 before making longer-horizon claims

Samples must come from immutable forward records, not rewritten historical replay.

### 4. Primary vs Secondary Gate

The primary scenario must beat the secondary scenario on completed forward samples.

Required:

- Primary closer-than-secondary rate >= 55% on at least two core horizons.
- Primary-vs-secondary spread positive after close-call samples are separated.
- The result cannot be driven by one symbol only.

### 5. Confidence Validation Gate

High confidence must mean better performance.

Required:

- Top confidence bucket outperforms ordinary samples.
- Signal confirmation top bucket outperforms low-confirmation samples.
- MODERATE_EDGE / STRONG_EDGE performs better than NO_EDGE.

If not, confidence must stay capped.

### 6. Deviation Learning Gate

Forecast errors must be reviewed and classified.

Required:

- Material deviations are tracked.
- Dominant error themes are identified.
- Repeated error themes enter challenger models, not baseline edits.
- Past forecast fields are never rewritten.

### 7. Model Promotion Gate

New logic must run as challenger/shadow first.

Required:

- Challenger forecasts are recorded separately.
- Challenger beats baseline on most core metrics.
- Historical replay alone never promotes a model.
- Forward evidence is mandatory.

## Trust Status Meanings

- `BLOCKED_STALE_DATA`: Do not use as today's forecast.
- `RESEARCH_ONLY_FORWARD_VALIDATION_NEEDED`: Useful as a radar, not yet dependable.
- `RESEARCH_ONLY_PATH_EDGE_UNPROVEN`: Samples exist, but primary path has not proven it beats secondary.
- `CONDITIONAL_DECISION_SUPPORT`: Can support market review, still not a trading signal.
- `VALIDATED_FORECAST_TOOL`: Passed the configured reliability gates; still probabilistic.

## Non-Negotiables

- Do not change Alpha v1 threshold.
- Do not overwrite historical forecast records.
- Do not use stale or synthetic data as current predictions.
- Do not call research candidates confirmed alpha.
- Do not add trading, entry, exit, stop, position sizing or PnL language.
