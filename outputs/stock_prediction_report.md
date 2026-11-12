# Stock Prediction Report

Generated at: `2026-11-12T19:57:26.352604+00:00`
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
- current_price: `164.29`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.0%`
- secondary: `stock_failed_bounce` / `22.9%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `41.9` / `weak`
- stock_alpha_score_v1: `37.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.9%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `61.04`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.19`
- primary_invalidation_level: `148.80`
- risk_scenario_activation_level: `148.80`
- trend_repair_confirmation_level: `222.19`
- breakout_level: `222.19`
- breakdown_level: `148.80`
- nearest_support: `155.77`
- nearest_resistance: `177.09`
- bounce_target_zone: `{"conservative": 170.69, "base": 170.69, "extended": 230.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 159.5, "critical_warning": 148.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `390.34`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.7%`
- secondary: `stock_trend_repair` / `19.5%`
- risk: `stock_downside_continuation` / `17.0%`
- stock_confluence_score: `45.52` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.1%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `48.48`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `375.73`
- nearest_resistance: `412.26`
- bounce_target_zone: `{"conservative": 401.3, "base": 401.3, "extended": 428.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 381.57, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.00`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.3%`
- secondary: `stock_failed_bounce` / `18.6%`
- risk: `stock_event_risk` / `13.4%`
- stock_confluence_score: `41.24` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.9%`
- 60d_expected_return: `-4.8%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `74.17`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.20`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `6.20`
- breakout_level: `6.20`
- breakdown_level: `4.28`
- nearest_support: `4.61`
- nearest_resistance: `5.59`
- bounce_target_zone: `{"conservative": 5.29, "base": 5.29, "extended": 6.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.78, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `281.57`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `16.2%`
- stock_confluence_score: `47.24` / `mixed`
- stock_alpha_score_v1: `45.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.6%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.28`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.56`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `281.78`
- breakout_level: `287.56`
- breakdown_level: `231.30`
- nearest_support: `270.92`
- nearest_resistance: `281.78`
- bounce_target_zone: `{"conservative": 289.56, "base": 289.56, "extended": 292.43, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 275.58, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
