# Stock Prediction Report

Generated at: `2026-10-14T17:15:11.450172+00:00`
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
- current_price: `222.38`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `28.9%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `13.8%`
- stock_confluence_score: `46.96` / `mixed`
- stock_alpha_score_v1: `39.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.1%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.12`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `217.15`
- risk_scenario_activation_level: `216.30`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `216.30`
- nearest_support: `217.96`
- nearest_resistance: `229.01`
- bounce_target_zone: `{"conservative": 225.69, "base": 225.69, "extended": 247.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 219.89, "critical_warning": 217.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `367.10`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.7%`
- secondary: `stock_event_risk` / `17.8%`
- risk: `stock_downside_continuation` / `17.6%`
- stock_confluence_score: `45.69` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.1%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.14`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `358.37`
- nearest_resistance: `380.20`
- bounce_target_zone: `{"conservative": 373.65, "base": 373.65, "extended": 397.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 361.87, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.89`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.6%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `9.9%`
- stock_confluence_score: `37.65` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.3%`
- 60d_expected_return: `-4.2%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `79.57`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.26`
- primary_invalidation_level: `5.59`
- risk_scenario_activation_level: `5.38`
- trend_repair_confirmation_level: `9.26`
- breakout_level: `9.26`
- breakdown_level: `5.38`
- nearest_support: `5.85`
- nearest_resistance: `6.44`
- bounce_target_zone: `{"conservative": 6.16, "base": 6.16, "extended": 9.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.68, "critical_warning": 5.59, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `281.67`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `49.69` / `mixed`
- stock_alpha_score_v1: `47.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.0%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.5`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `268.84`
- nearest_resistance: `300.90`
- bounce_target_zone: `{"conservative": 291.28, "base": 291.28, "extended": 322.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 274.45, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
