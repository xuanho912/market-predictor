# Stock Prediction Report

Generated at: `2026-10-13T07:48:05.250965+00:00`
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
- current_price: `226.32`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `17.9%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `47.24` / `mixed`
- stock_alpha_score_v1: `42.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.7%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.63`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `211.16`
- risk_scenario_activation_level: `211.16`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `211.16`
- nearest_support: `222.11`
- nearest_resistance: `232.64`
- bounce_target_zone: `{"conservative": 229.48, "base": 229.48, "extended": 247.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 223.95, "critical_warning": 211.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `378.03`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_event_risk` / `18.4%`
- risk: `stock_downside_continuation` / `18.2%`
- stock_confluence_score: `45.79` / `mixed`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.1%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.25`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.56`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.56`
- breakout_level: `388.56`
- breakdown_level: `345.88`
- nearest_support: `369.35`
- nearest_resistance: `388.56`
- bounce_target_zone: `{"conservative": 384.54, "base": 384.54, "extended": 397.24, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.82, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `6.70`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.6%`
- secondary: `stock_failed_bounce` / `24.5%`
- risk: `stock_event_risk` / `9.9%`
- stock_confluence_score: `36.56` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `23.8%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.31`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `64.26`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.26`
- primary_invalidation_level: `6.41`
- risk_scenario_activation_level: `6.20`
- trend_repair_confirmation_level: `9.26`
- breakout_level: `9.26`
- breakdown_level: `6.20`
- nearest_support: `6.61`
- nearest_resistance: `7.24`
- bounce_target_zone: `{"conservative": 6.97, "base": 6.97, "extended": 9.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 6.5, "critical_warning": 6.41, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `293.89`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.3%`
- secondary: `stock_trend_repair` / `19.7%`
- risk: `stock_downside_continuation` / `18.5%`
- stock_confluence_score: `50.27` / `mixed`
- stock_alpha_score_v1: `55.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `67.1%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.66`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `32.19`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `282.00`
- nearest_resistance: `309.80`
- bounce_target_zone: `{"conservative": 302.8, "base": 302.8, "extended": 321.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 286.75, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
