# Stock Prediction Report

Generated at: `2026-07-13T22:34:41.622151+00:00`
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
- current_price: `203.53`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `22.3%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `43.46` / `weak`
- stock_alpha_score_v1: `40.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.3%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.41`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.2`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `198.01`
- nearest_resistance: `211.81`
- bounce_target_zone: `{"conservative": 207.67, "base": 207.67, "extended": 219.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 200.43, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `394.76`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.5%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `36.51` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.7%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.98`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `378.85`
- nearest_resistance: `418.63`
- bounce_target_zone: `{"conservative": 406.69, "base": 406.69, "extended": 448.77, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 385.81, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.35`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.1%`
- secondary: `stock_failed_bounce` / `24.2%`
- risk: `stock_event_risk` / `12.1%`
- stock_confluence_score: `35.0` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.0%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `60.41`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `7.87`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.54`
- nearest_support: `8.27`
- nearest_resistance: `9.23`
- bounce_target_zone: `{"conservative": 8.79, "base": 8.79, "extended": 12.44, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.02, "critical_warning": 7.87, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `257.57`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.1%`
- secondary: `stock_downside_continuation` / `24.5%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `38.01` / `weak`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.7%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.51`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `250.34`
- nearest_resistance: `268.41`
- bounce_target_zone: `{"conservative": 262.99, "base": 262.99, "extended": 290.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 253.51, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
