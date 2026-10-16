# Stock Prediction Report

Generated at: `2026-10-16T22:56:46.052403+00:00`
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
- current_price: `214.13`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `21.0%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `41.13` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.0%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.52`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `210.39`
- risk_scenario_activation_level: `207.79`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `207.79`
- nearest_support: `212.85`
- nearest_resistance: `221.04`
- bounce_target_zone: `{"conservative": 217.59, "base": 217.59, "extended": 247.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 211.54, "critical_warning": 210.39, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `354.72`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.5%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `16.7%`
- stock_confluence_score: `37.41` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.8%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.86`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `342.78`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `342.78`
- nearest_support: `346.03`
- nearest_resistance: `367.75`
- bounce_target_zone: `{"conservative": 361.23, "base": 361.23, "extended": 397.25, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 349.83, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.83`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.1%`
- secondary: `stock_failed_bounce` / `23.9%`
- risk: `stock_event_risk` / `10.4%`
- stock_confluence_score: `40.05` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.2%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `79.18`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.02`
- primary_invalidation_level: `5.44`
- risk_scenario_activation_level: `5.29`
- trend_repair_confirmation_level: `9.02`
- breakout_level: `9.02`
- breakdown_level: `5.29`
- nearest_support: `5.44`
- nearest_resistance: `6.41`
- bounce_target_zone: `{"conservative": 6.12, "base": 6.12, "extended": 9.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.61, "critical_warning": 5.44, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `271.37`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `43.38` / `weak`
- stock_alpha_score_v1: `34.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.7%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.43`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `258.01`
- nearest_resistance: `291.41`
- bounce_target_zone: `{"conservative": 281.39, "base": 281.39, "extended": 323.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 263.86, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
