# Stock Prediction Report

Generated at: `pending_real_data_generation`

Model version: `stock_baseline_v1`

The stock prediction module has been added as an extension to the Market Prediction Dashboard. It will generate watchlist stock forecasts during the next GitHub Actions run using real market data only.

## Guardrails

- The stock module does not modify `baseline_v1`.
- The stock module does not modify Alpha v1 or its frozen threshold `0.32534311`.
- The stock module is not a trading system and does not produce execution instructions.
- Synthetic stock data is blocked from live stock forecasts.
- Fundamentals, earnings, company news and single-stock options remain `missing` unless a real provider is connected.

## Current Status

- status: `pending_real_data_generation`
- watchlist source: `config/stock_watchlist.json`
- output JSON: `frontend/public/stock-prediction-dashboard.json`
- forecast ledger: `outputs/stock_forecast_records.csv`
- planned generated fields: stock scenario ranking, forecast price levels, stock confluence score, stock alerts, historical analogs, simulated paths, and not-yet-validated forecast records.
