# Stock Prediction Report

Generated at: `2026-07-09T22:54:31.452432+00:00`
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
- current_price: `202.78`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `23.7%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `39.68` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.8%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.3`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `197.47`
- nearest_resistance: `210.74`
- bounce_target_zone: `{"conservative": 206.76, "base": 206.76, "extended": 219.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 199.79, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `406.55`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.8%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `16.1%`
- stock_confluence_score: `43.05` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.9%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.62`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `389.98`
- nearest_resistance: `431.40`
- bounce_target_zone: `{"conservative": 418.97, "base": 418.97, "extended": 449.43, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 397.23, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.03`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `30.6` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.8%`
- 60d_expected_return: `-3.8%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `66.03`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.50`
- risk_scenario_activation_level: `8.14`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `8.14`
- nearest_support: `8.55`
- nearest_resistance: `10.00`
- bounce_target_zone: `{"conservative": 9.52, "base": 9.52, "extended": 12.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.67, "critical_warning": 8.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `250.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.8%`
- secondary: `stock_downside_continuation` / `24.8%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `32.04` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.3%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `40.77`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `242.79`
- nearest_resistance: `262.67`
- bounce_target_zone: `{"conservative": 256.71, "base": 256.71, "extended": 290.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 246.27, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
