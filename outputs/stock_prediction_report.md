# Stock Prediction Report

Generated at: `2026-07-14T23:40:43.397128+00:00`
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
- current_price: `211.80`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `19.3%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `50.05` / `mixed`
- stock_alpha_score_v1: `47.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.8%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.02`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.93`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `214.93`
- breakdown_level: `189.80`
- nearest_support: `206.24`
- nearest_resistance: `213.99`
- bounce_target_zone: `{"conservative": 215.97, "base": 215.97, "extended": 219.55, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.67, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `396.18`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `23.0%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `34.61` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.2%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.48`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `381.33`
- nearest_resistance: `418.46`
- bounce_target_zone: `{"conservative": 407.32, "base": 407.32, "extended": 447.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 387.82, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.60`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.0%`
- secondary: `stock_failed_bounce` / `21.0%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `38.74` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.1%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `55.88`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.16`
- risk_scenario_activation_level: `7.86`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.86`
- nearest_support: `8.27`
- nearest_resistance: `9.41`
- bounce_target_zone: `{"conservative": 9.0, "base": 9.0, "extended": 12.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.3, "critical_warning": 8.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `256.43`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `24.0%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `35.53` / `weak`
- stock_alpha_score_v1: `24.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.5%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `31.74`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `249.03`
- nearest_resistance: `267.53`
- bounce_target_zone: `{"conservative": 261.98, "base": 261.98, "extended": 290.17, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 252.27, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
