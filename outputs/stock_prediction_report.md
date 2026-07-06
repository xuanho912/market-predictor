# Stock Prediction Report

Generated at: `2026-07-06T14:50:58.606704+00:00`
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
- current_price: `196.09`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `33.72` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.4%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `41.15`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.87`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.13`
- trend_repair_confirmation_level: `214.87`
- breakout_level: `214.87`
- breakdown_level: `189.13`
- nearest_support: `191.02`
- nearest_resistance: `203.68`
- bounce_target_zone: `{"conservative": 199.88, "base": 199.88, "extended": 219.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 193.24, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `404.30`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `20.7%`
- risk: `stock_event_risk` / `16.1%`
- stock_confluence_score: `40.43` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.0%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.31`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `389.27`
- nearest_resistance: `426.84`
- bounce_target_zone: `{"conservative": 415.57, "base": 415.57, "extended": 447.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 395.84, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.88`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.1%`
- secondary: `stock_failed_bounce` / `22.3%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `30.61` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.8%`
- 60d_expected_return: `-4.2%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `79.86`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `12.24`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `8.88`
- trend_repair_confirmation_level: `12.24`
- breakout_level: `12.24`
- breakdown_level: `8.88`
- nearest_support: `9.15`
- nearest_resistance: `10.96`
- bounce_target_zone: `{"conservative": 10.42, "base": 10.42, "extended": 12.96, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.47, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `243.46`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.2%`
- secondary: `stock_failed_bounce` / `27.1%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `24.82` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.6%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `56.72`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `235.17`
- nearest_resistance: `255.88`
- bounce_target_zone: `{"conservative": 249.67, "base": 249.67, "extended": 291.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 238.79, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
