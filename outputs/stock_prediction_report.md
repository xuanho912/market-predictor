# Stock Prediction Report

Generated at: `2026-07-14T14:17:04.495471+00:00`
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
- current_price: `204.59`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `19.6%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `41.02` / `weak`
- stock_alpha_score_v1: `40.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.6%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.57`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `199.27`
- nearest_resistance: `212.57`
- bounce_target_zone: `{"conservative": 208.58, "base": 208.58, "extended": 219.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 201.6, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `397.95`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.9%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `33.86` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.0%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `39.03`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `383.18`
- nearest_resistance: `420.11`
- bounce_target_zone: `{"conservative": 409.03, "base": 409.03, "extended": 447.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 389.64, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.44`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `29.9%`
- secondary: `stock_downside_continuation` / `25.0%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `36.95` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.0%`
- 60d_expected_return: `0.4%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `56.08`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.00`
- risk_scenario_activation_level: `7.70`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.70`
- nearest_support: `8.27`
- nearest_resistance: `9.25`
- bounce_target_zone: `{"conservative": 8.9, "base": 9.28, "extended": 12.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.14, "critical_warning": 8.0, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `264.10`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `23.9%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `39.02` / `weak`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.9%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.84`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `256.84`
- nearest_resistance: `274.99`
- bounce_target_zone: `{"conservative": 269.55, "base": 269.55, "extended": 290.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 260.01, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
