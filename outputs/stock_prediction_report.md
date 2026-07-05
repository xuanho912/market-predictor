# Stock Prediction Report

Generated at: `2026-07-05T14:58:43.056216+00:00`
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
- current_price: `194.83`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.1%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `39.44` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.8%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.04`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `221.60`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `187.86`
- trend_repair_confirmation_level: `221.60`
- breakout_level: `221.60`
- breakdown_level: `187.86`
- nearest_support: `189.80`
- nearest_resistance: `202.44`
- bounce_target_zone: `{"conservative": 198.63, "base": 198.63, "extended": 226.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 191.98, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `393.45`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `24.1%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `39.62` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.7%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.39`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `378.21`
- nearest_resistance: `416.31`
- bounce_target_zone: `{"conservative": 404.88, "base": 404.88, "extended": 448.1, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 384.88, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.76`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.4%`
- secondary: `stock_failed_bounce` / `20.6%`
- risk: `stock_event_risk` / `13.4%`
- stock_confluence_score: `37.07` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.9%`
- 60d_expected_return: `-3.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `44.42`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `12.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `8.75`
- trend_repair_confirmation_level: `12.30`
- breakout_level: `12.30`
- breakdown_level: `8.75`
- nearest_support: `9.12`
- nearest_resistance: `10.86`
- bounce_target_zone: `{"conservative": 10.31, "base": 10.31, "extended": 13.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.35, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `239.25`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.9%`
- secondary: `stock_failed_bounce` / `27.6%`
- risk: `stock_event_risk` / `9.8%`
- stock_confluence_score: `24.85` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.8%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `62.85`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `227.79`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `227.79`
- nearest_support: `230.91`
- nearest_resistance: `251.75`
- bounce_target_zone: `{"conservative": 245.5, "base": 245.5, "extended": 291.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 234.56, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
