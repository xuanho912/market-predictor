# Stock Prediction Report

Generated at: `2026-07-06T14:44:32.246850+00:00`
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
- current_price: `196.60`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.7%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `33.93` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.6%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `41.26`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.87`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.64`
- trend_repair_confirmation_level: `214.87`
- breakout_level: `214.87`
- breakdown_level: `189.64`
- nearest_support: `191.53`
- nearest_resistance: `204.19`
- bounce_target_zone: `{"conservative": 200.39, "base": 200.39, "extended": 219.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 193.75, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `404.35`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `20.7%`
- risk: `stock_event_risk` / `16.1%`
- stock_confluence_score: `40.42` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.0%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.4`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `389.32`
- nearest_resistance: `426.89`
- bounce_target_zone: `{"conservative": 415.62, "base": 415.62, "extended": 447.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 395.89, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.81`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.7%`
- secondary: `stock_failed_bounce` / `21.1%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `36.12` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.4%`
- 60d_expected_return: `-3.7%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `42.29`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `12.24`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `8.81`
- trend_repair_confirmation_level: `12.24`
- breakout_level: `12.24`
- breakdown_level: `8.81`
- nearest_support: `9.12`
- nearest_resistance: `10.89`
- bounce_target_zone: `{"conservative": 10.35, "base": 10.35, "extended": 12.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.4, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `242.76`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.3%`
- secondary: `stock_failed_bounce` / `27.1%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `24.59` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.4%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `57.66`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `234.47`
- nearest_resistance: `255.18`
- bounce_target_zone: `{"conservative": 248.97, "base": 248.97, "extended": 291.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 238.09, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
