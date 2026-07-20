# Stock Prediction Report

Generated at: `2026-07-20T14:37:01.062885+00:00`
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
- current_price: `205.40`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `21.1%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `43.89` / `weak`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.0%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `40.08`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `199.61`
- nearest_resistance: `213.99`
- bounce_target_zone: `{"conservative": 209.75, "base": 209.75, "extended": 219.78, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 202.14, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `375.07`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `24.2%`
- risk: `stock_event_risk` / `16.2%`
- stock_confluence_score: `29.08` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.2%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.25`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `363.93`
- risk_scenario_activation_level: `356.22`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `356.22`
- nearest_support: `368.60`
- nearest_resistance: `395.63`
- bounce_target_zone: `{"conservative": 385.35, "base": 385.35, "extended": 446.57, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 367.36, "critical_warning": 363.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.68`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `36.1%`
- secondary: `stock_failed_bounce` / `20.0%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `39.28` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `10.8%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `71.01`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `6.94`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `6.94`
- nearest_support: `7.21`
- nearest_resistance: `8.47`
- bounce_target_zone: `{"conservative": 8.07, "base": 8.07, "extended": 12.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.38, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `253.28`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.4%`
- secondary: `stock_failed_bounce` / `25.9%`
- risk: `stock_event_risk` / `10.5%`
- stock_confluence_score: `28.95` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.3%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `45.1`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.74`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.74`
- breakout_level: `279.74`
- breakdown_level: `228.63`
- nearest_support: `246.05`
- nearest_resistance: `264.12`
- bounce_target_zone: `{"conservative": 258.7, "base": 258.7, "extended": 286.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 249.21, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
