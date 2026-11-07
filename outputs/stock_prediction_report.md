# Stock Prediction Report

Generated at: `2026-11-07T02:44:56.705501+00:00`
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

- company_name: `NVIDIA Corporation`
- status: `available`
- current_price: `186.64`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.0%`
- secondary: `stock_failed_bounce` / `25.7%`
- risk: `stock_event_risk` / `11.8%`
- stock_confluence_score: `33.36` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.1%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `45.19`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `228.86`
- primary_invalidation_level: `181.43`
- risk_scenario_activation_level: `177.82`
- trend_repair_confirmation_level: `228.86`
- breakout_level: `228.86`
- breakdown_level: `177.82`
- nearest_support: `181.46`
- nearest_resistance: `196.26`
- bounce_target_zone: `{"conservative": 191.45, "base": 191.45, "extended": 235.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 183.03, "critical_warning": 181.43, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `358.22`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `20.1%`
- risk: `stock_event_risk` / `13.8%`
- stock_confluence_score: `35.62` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.0%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `30.69`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `343.83`
- nearest_resistance: `379.80`
- bounce_target_zone: `{"conservative": 369.01, "base": 369.01, "extended": 428.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 350.13, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.08`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.4%`
- secondary: `stock_failed_bounce` / `20.8%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `45.95` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `16.0%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `78.46`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.07`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `7.07`
- breakout_level: `7.07`
- breakdown_level: `4.28`
- nearest_support: `4.72`
- nearest_resistance: `5.62`
- bounce_target_zone: `{"conservative": 5.35, "base": 5.35, "extended": 7.43, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.88, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `249.95`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.0%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `30.69` / `weak`
- stock_alpha_score_v1: `22.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.5%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `37.42`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `301.77`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `301.77`
- breakout_level: `301.77`
- breakdown_level: `231.30`
- nearest_support: `240.34`
- nearest_resistance: `264.37`
- bounce_target_zone: `{"conservative": 257.16, "base": 257.16, "extended": 311.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 244.54, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
