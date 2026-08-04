# Stock Prediction Report

Generated at: `2026-08-04T14:42:29.604403+00:00`
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
- current_price: `209.94`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `47.59` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.6%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.9`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `190.01`
- nearest_support: `203.79`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 214.55, "base": 214.55, "extended": 220.54, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 206.48, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `323.37`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `30.3%`
- secondary: `stock_failed_bounce` / `20.7%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `38.84` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.5%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `47.73`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `413.16`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `413.16`
- breakout_level: `413.16`
- breakdown_level: `297.38`
- nearest_support: `310.87`
- nearest_resistance: `342.12`
- bounce_target_zone: `{"conservative": 332.75, "base": 332.75, "extended": 425.66, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 316.34, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.33`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `23.2%`
- risk: `stock_event_risk` / `17.3%`
- stock_confluence_score: `35.3` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.7%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `36.75`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.64`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `9.54`
- breakout_level: `9.64`
- breakdown_level: `7.21`
- nearest_support: `8.77`
- nearest_resistance: `9.54`
- bounce_target_zone: `{"conservative": 9.75, "base": 9.75, "extended": 10.1, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.02, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `266.33`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `36.64` / `weak`
- stock_alpha_score_v1: `33.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.4%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.7`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `236.56`
- risk_scenario_activation_level: `236.56`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `236.56`
- nearest_support: `258.40`
- nearest_resistance: `278.24`
- bounce_target_zone: `{"conservative": 272.29, "base": 272.29, "extended": 287.54, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 261.87, "critical_warning": 236.56, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
