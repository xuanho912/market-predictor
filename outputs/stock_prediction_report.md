# Stock Prediction Report

Generated at: `2026-07-28T14:41:10.490156+00:00`
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
- current_price: `195.92`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `42.73` / `weak`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `64.4%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.95`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `190.99`
- risk_scenario_activation_level: `187.58`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `187.58`
- nearest_support: `191.14`
- nearest_resistance: `205.01`
- bounce_target_zone: `{"conservative": 200.47, "base": 200.47, "extended": 220.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 192.51, "critical_warning": 190.99, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `302.45`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.6%`
- secondary: `stock_failed_bounce` / `26.3%`
- risk: `stock_event_risk` / `11.4%`
- stock_confluence_score: `35.52` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.6%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `61.21`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `291.96`
- risk_scenario_activation_level: `284.70`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `284.70`
- nearest_support: `300.69`
- nearest_resistance: `321.81`
- bounce_target_zone: `{"conservative": 312.13, "base": 312.13, "extended": 445.77, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 295.19, "critical_warning": 291.96, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.97`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.7%`
- secondary: `stock_failed_bounce` / `22.1%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `28.85` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.2%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `57.14`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `7.46`
- nearest_resistance: `8.72`
- bounce_target_zone: `{"conservative": 8.34, "base": 8.34, "extended": 11.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.68, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.37`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `22.6%`
- risk: `stock_event_risk` / `10.7%`
- stock_confluence_score: `33.31` / `weak`
- stock_alpha_score_v1: `26.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.9%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.57`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `228.63`
- nearest_support: `252.46`
- nearest_resistance: `269.73`
- bounce_target_zone: `{"conservative": 264.55, "base": 264.55, "extended": 286.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.48, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
