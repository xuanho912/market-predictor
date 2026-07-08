# Stock Prediction Report

Generated at: `2026-07-08T14:43:53.843804+00:00`
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
- current_price: `196.89`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `25.6%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `36.9` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.5%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `41.34`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `191.86`
- nearest_resistance: `204.44`
- bounce_target_zone: `{"conservative": 200.66, "base": 200.66, "extended": 219.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 194.06, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `393.92`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.8%`
- secondary: `stock_downside_continuation` / `20.8%`
- risk: `stock_event_risk` / `15.5%`
- stock_confluence_score: `32.4` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.3%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.53`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `377.78`
- nearest_resistance: `418.13`
- bounce_target_zone: `{"conservative": 406.02, "base": 406.02, "extended": 449.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 384.84, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.81`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.1%`
- secondary: `stock_failed_bounce` / `23.4%`
- risk: `stock_event_risk` / `12.4%`
- stock_confluence_score: `31.19` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.1%`
- 60d_expected_return: `-3.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `55.88`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.27`
- risk_scenario_activation_level: `7.89`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.89`
- nearest_support: `8.64`
- nearest_resistance: `9.82`
- bounce_target_zone: `{"conservative": 9.32, "base": 9.32, "extended": 12.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.44, "critical_warning": 8.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `241.83`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.1%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `10.5%`
- stock_confluence_score: `26.2` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.1%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `46.94`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `233.93`
- nearest_resistance: `253.67`
- bounce_target_zone: `{"conservative": 247.75, "base": 247.75, "extended": 290.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 237.39, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
