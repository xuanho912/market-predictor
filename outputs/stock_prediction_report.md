# Stock Prediction Report

Generated at: `2026-07-29T14:34:06.299599+00:00`
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
- current_price: `192.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `21.5%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `44.2` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.5%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.41`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.99`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `186.95`
- risk_scenario_activation_level: `183.45`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `183.45`
- nearest_support: `190.92`
- nearest_resistance: `201.33`
- bounce_target_zone: `{"conservative": 196.66, "base": 196.66, "extended": 220.61, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 188.5, "critical_warning": 186.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `304.10`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.9%`
- secondary: `stock_failed_bounce` / `25.8%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `35.35` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.2%`
- 60d_expected_return: `-2.6%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `59.9`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `294.01`
- risk_scenario_activation_level: `287.02`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `287.02`
- nearest_support: `300.69`
- nearest_resistance: `322.74`
- bounce_target_zone: `{"conservative": 313.42, "base": 313.42, "extended": 445.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 297.11, "critical_warning": 294.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.05`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.6%`
- secondary: `stock_failed_bounce` / `22.4%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `23.62` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `24.9%`
- 60d_expected_return: `-3.4%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `53.65`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `7.55`
- nearest_resistance: `8.79`
- bounce_target_zone: `{"conservative": 8.42, "base": 8.42, "extended": 11.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.77, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.37`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.1%`
- secondary: `stock_downside_continuation` / `20.0%`
- risk: `stock_event_risk` / `11.4%`
- stock_confluence_score: `43.04` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.7%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.48`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `228.63`
- nearest_support: `252.65`
- nearest_resistance: `269.45`
- bounce_target_zone: `{"conservative": 264.41, "base": 264.41, "extended": 286.32, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.59, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
