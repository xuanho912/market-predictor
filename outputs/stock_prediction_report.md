# Stock Prediction Report

Generated at: `2026-11-11T19:38:58.505971+00:00`
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
- current_price: `175.35`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.5%`
- secondary: `stock_failed_bounce` / `26.1%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `34.58` / `weak`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.8%`
- 60d_expected_return: `-2.7%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `69.62`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `165.89`
- risk_scenario_activation_level: `165.29`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `165.29`
- nearest_support: `168.03`
- nearest_resistance: `186.32`
- bounce_target_zone: `{"conservative": 180.83, "base": 180.83, "extended": 229.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 171.23, "critical_warning": 165.89, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `392.20`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.7%`
- secondary: `stock_trend_repair` / `19.7%`
- risk: `stock_downside_continuation` / `17.0%`
- stock_confluence_score: `44.31` / `weak`
- stock_alpha_score_v1: `13.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.8%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `51.16`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `377.53`
- nearest_resistance: `414.21`
- bounce_target_zone: `{"conservative": 403.21, "base": 403.21, "extended": 428.9, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 383.39, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.23`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.2%`
- secondary: `stock_failed_bounce` / `19.7%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `35.83` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.3%`
- 60d_expected_return: `-3.8%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `68.15`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.20`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `6.20`
- breakout_level: `6.20`
- breakdown_level: `4.28`
- nearest_support: `4.85`
- nearest_resistance: `5.80`
- bounce_target_zone: `{"conservative": 5.52, "base": 5.52, "extended": 6.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.02, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `275.52`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `16.4%`
- stock_confluence_score: `36.46` / `weak`
- stock_alpha_score_v1: `24.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.4%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.29`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `281.38`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `277.66`
- breakout_level: `281.38`
- breakdown_level: `231.30`
- nearest_support: `265.11`
- nearest_resistance: `277.66`
- bounce_target_zone: `{"conservative": 283.33, "base": 283.33, "extended": 288.07, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 269.67, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
