# Stock Prediction Report

Generated at: `2026-06-15T13:55:30.626461+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `KC`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['fundamentals', 'earnings', 'company_news', 'single_stock_options']`

## Symbols

### JD

- company_name: `JD.com`
- status: `available`
- current_price: `28.83`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.7%`
- secondary: `stock_failed_bounce` / `24.2%`
- risk: `stock_downside_continuation` / `27.7%`
- stock_confluence_score: `0` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `73.71`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `32.83`
- primary_invalidation_level: `27.48`
- risk_scenario_activation_level: `27.48`
- trend_repair_confirmation_level: `32.83`
- breakout_level: `32.83`
- breakdown_level: `27.48`
- nearest_support: `28.21`
- nearest_resistance: `29.77`
- bounce_target_zone: `{"conservative": 29.3, "base": 29.3, "extended": 33.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.46, "critical_warning": 27.48, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### KC

- company_name: `Kingsoft Cloud`
- status: `available`
- current_price: `11.30`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.2%`
- secondary: `stock_failed_bounce` / `18.2%`
- risk: `stock_downside_continuation` / `34.2%`
- stock_confluence_score: `0` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `62.02`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `15.25`
- primary_invalidation_level: `10.47`
- risk_scenario_activation_level: `10.47`
- trend_repair_confirmation_level: `15.25`
- breakout_level: `15.25`
- breakdown_level: `10.47`
- nearest_support: `10.76`
- nearest_resistance: `12.11`
- bounce_target_zone: `{"conservative": 11.7, "base": 11.7, "extended": 15.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.98, "critical_warning": 10.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### NVDA

- company_name: `NVIDIA`
- status: `available`
- current_price: `209.13`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.5%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_downside_continuation` / `25.5%`
- stock_confluence_score: `2.0` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `45.31`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `202.48`
- nearest_resistance: `219.10`
- bounce_target_zone: `{"conservative": 214.11, "base": 214.11, "extended": 238.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.14, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla`
- status: `available`
- current_price: `412.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `22.9%`
- risk: `stock_failed_bounce` / `25.5%`
- stock_confluence_score: `0` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.52`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `398.45`
- nearest_resistance: `434.04`
- bounce_target_zone: `{"conservative": 423.36, "base": 423.36, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 404.68, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
