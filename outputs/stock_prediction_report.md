# Stock Prediction Report

Generated at: `2026-08-05T00:14:48.413774+00:00`
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
- current_price: `211.94`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `50.38` / `mixed`
- stock_alpha_score_v1: `54.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `64.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.79`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `215.43`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `215.43`
- breakdown_level: `190.01`
- nearest_support: `205.74`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 216.59, "base": 216.59, "extended": 220.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.45, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `327.35`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `29.8%`
- secondary: `stock_failed_bounce` / `20.9%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `40.54` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.4%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `45.63`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `413.16`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `413.16`
- breakout_level: `413.16`
- breakdown_level: `297.38`
- nearest_support: `314.70`
- nearest_resistance: `346.33`
- bounce_target_zone: `{"conservative": 336.84, "base": 336.84, "extended": 425.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 320.23, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.49`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `22.6%`
- risk: `stock_event_risk` / `17.3%`
- stock_confluence_score: `38.52` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.4%`
- 60d_expected_return: `-3.1%`
- risk_reward_ratio: `0.38`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `33.63`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.81`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `9.71`
- breakout_level: `9.81`
- breakdown_level: `7.21`
- nearest_support: `8.92`
- nearest_resistance: `9.71`
- bounce_target_zone: `{"conservative": 9.92, "base": 9.92, "extended": 10.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.17, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `267.25`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `42.77` / `weak`
- stock_alpha_score_v1: `37.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.7%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.62`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.45`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `259.31`
- nearest_resistance: `279.16`
- bounce_target_zone: `{"conservative": 273.2, "base": 273.2, "extended": 287.54, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 262.78, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
