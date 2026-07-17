# Stock Prediction Report

Generated at: `2026-07-17T14:06:34.908909+00:00`
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
- current_price: `203.73`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `19.4%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `43.61` / `weak`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.2%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.34`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `197.85`
- nearest_resistance: `212.55`
- bounce_target_zone: `{"conservative": 208.14, "base": 208.14, "extended": 219.87, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 200.42, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `382.83`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `20.4%`
- risk: `stock_event_risk` / `17.7%`
- stock_confluence_score: `29.72` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.2%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.85`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `362.32`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `362.32`
- nearest_support: `368.60`
- nearest_resistance: `405.21`
- bounce_target_zone: `{"conservative": 394.02, "base": 394.02, "extended": 447.78, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 374.44, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.57`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.0%`
- secondary: `stock_failed_bounce` / `23.4%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `37.58` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `15.0%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `72.29`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `7.13`
- risk_scenario_activation_level: `6.83`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `6.83`
- nearest_support: `7.21`
- nearest_resistance: `8.37`
- bounce_target_zone: `{"conservative": 7.97, "base": 7.97, "extended": 12.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.27, "critical_warning": 7.13, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `250.22`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `25.9%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `27.73` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.6%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.09`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `242.83`
- nearest_resistance: `261.31`
- bounce_target_zone: `{"conservative": 255.76, "base": 255.76, "extended": 290.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 246.06, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
