# Stock Prediction Report

Generated at: `2026-06-16T13:42:06.963104+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `209.21`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `24.6%`
- risk: `stock_failed_bounce` / `26.5%`
- stock_confluence_score: `33.98` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `50.77`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `202.53`
- nearest_resistance: `219.22`
- bounce_target_zone: `{"conservative": 214.21, "base": 214.21, "extended": 238.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.45, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `407.30`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_failed_bounce` / `26.9%`
- stock_confluence_score: `27.88` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `54.86`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `393.22`
- nearest_resistance: `428.42`
- bounce_target_zone: `{"conservative": 417.86, "base": 417.86, "extended": 459.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 399.38, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.78`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.8%`
- secondary: `stock_downside_continuation` / `21.7%`
- risk: `stock_failed_bounce` / `22.8%`
- stock_confluence_score: `29.73` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `53.73`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.12`
- nearest_support: `9.86`
- nearest_resistance: `12.18`
- bounce_target_zone: `{"conservative": 11.48, "base": 11.48, "extended": 15.23, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.26, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `269.59`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `23.8%`
- risk: `stock_failed_bounce` / `25.4%`
- stock_confluence_score: `37.99` / `weak`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.63`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `310.45`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `310.45`
- breakout_level: `310.45`
- breakdown_level: `240.51`
- nearest_support: `261.39`
- nearest_resistance: `281.90`
- bounce_target_zone: `{"conservative": 275.74, "base": 275.74, "extended": 318.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 264.98, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
