# Stock Prediction Report

Generated at: `2026-07-15T14:13:00.019040+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `SMR`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `211.56`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `19.3%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `46.82` / `mixed`
- stock_alpha_score_v1: `47.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.5%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.43`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.73`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `214.73`
- breakdown_level: `189.80`
- nearest_support: `205.93`
- nearest_resistance: `213.99`
- bounce_target_zone: `{"conservative": 215.78, "base": 215.78, "extended": 219.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.39, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `399.80`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `21.3%`
- risk: `stock_event_risk` / `17.5%`
- stock_confluence_score: `35.49` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.7%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.12`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `384.70`
- nearest_resistance: `422.46`
- bounce_target_zone: `{"conservative": 411.13, "base": 411.13, "extended": 447.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 391.31, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.65`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.2%`
- secondary: `stock_failed_bounce` / `19.4%`
- risk: `stock_event_risk` / `11.8%`
- stock_confluence_score: `31.6` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.2%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.41`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `55.37`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.24`
- risk_scenario_activation_level: `7.95`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.95`
- nearest_support: `8.27`
- nearest_resistance: `9.43`
- bounce_target_zone: `{"conservative": 9.04, "base": 9.04, "extended": 12.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.36, "critical_warning": 8.24, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `261.77`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `23.5%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `32.58` / `weak`
- stock_alpha_score_v1: `24.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.2%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.53`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `254.37`
- nearest_resistance: `272.88`
- bounce_target_zone: `{"conservative": 267.33, "base": 267.33, "extended": 290.17, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 257.61, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
