# Stock Prediction Report

Generated at: `2026-06-15T13:43:10.577519+00:00`
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
- current_price: `28.82`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `23.0%`
- secondary: `stock_bounce` / `20.5%`
- risk: `stock_downside_continuation` / `23.0%`
- stock_confluence_score: `0` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `72.98`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `32.83`
- primary_invalidation_level: `27.48`
- risk_scenario_activation_level: `27.48`
- trend_repair_confirmation_level: `32.83`
- breakout_level: `32.83`
- breakdown_level: `27.48`
- nearest_support: `28.19`
- nearest_resistance: `29.75`
- bounce_target_zone: `{"conservative": 29.28, "base": 29.28, "extended": 33.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.44, "critical_warning": 27.48, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### KC

- company_name: `Kingsoft Cloud`
- status: `available`
- current_price: `11.30`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.7%`
- secondary: `stock_bounce` / `23.6%`
- risk: `stock_downside_continuation` / `29.7%`
- stock_confluence_score: `0` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `59.4`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `15.25`
- primary_invalidation_level: `10.47`
- risk_scenario_activation_level: `10.47`
- trend_repair_confirmation_level: `15.25`
- breakout_level: `15.25`
- breakdown_level: `10.47`
- nearest_support: `10.76`
- nearest_resistance: `12.10`
- bounce_target_zone: `{"conservative": 11.7, "base": 11.7, "extended": 15.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.97, "critical_warning": 10.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### NVDA

- company_name: `NVIDIA`
- status: `available`
- current_price: `209.43`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `20.6%`
- secondary: `stock_failed_bounce` / `20.4%`
- risk: `stock_downside_continuation` / `20.6%`
- stock_confluence_score: `8.0` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.73`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `202.78`
- nearest_resistance: `219.40`
- bounce_target_zone: `{"conservative": 214.41, "base": 214.41, "extended": 238.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.44, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla`
- status: `available`
- current_price: `411.54`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `20.6%`
- secondary: `stock_bounce` / `18.9%`
- risk: `stock_failed_bounce` / `20.6%`
- stock_confluence_score: `0` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.79`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `397.30`
- nearest_resistance: `432.90`
- bounce_target_zone: `{"conservative": 422.22, "base": 422.22, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 403.53, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
