# Stock Prediction Report

Generated at: `2026-11-11T02:20:10.199822+00:00`
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
- current_price: `168.89`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.6%`
- secondary: `stock_failed_bounce` / `26.8%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `37.28` / `weak`
- stock_alpha_score_v1: `35.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.7%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `73.54`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `226.00`
- primary_invalidation_level: `162.85`
- risk_scenario_activation_level: `158.67`
- trend_repair_confirmation_level: `226.00`
- breakout_level: `226.00`
- breakdown_level: `158.67`
- nearest_support: `165.89`
- nearest_resistance: `180.04`
- bounce_target_zone: `{"conservative": 174.46, "base": 174.46, "extended": 233.43, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 164.71, "critical_warning": 162.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `379.78`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_trend_repair` / `16.6%`
- risk: `stock_downside_continuation` / `16.3%`
- stock_confluence_score: `44.89` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.0%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `47.06`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `365.13`
- nearest_resistance: `401.75`
- bounce_target_zone: `{"conservative": 390.76, "base": 390.76, "extended": 428.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 370.99, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.22`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.0%`
- secondary: `stock_failed_bounce` / `19.9%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `32.78` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `21.2%`
- 60d_expected_return: `-4.4%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `71.53`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.32`
- primary_invalidation_level: `4.28`
- risk_scenario_activation_level: `4.28`
- trend_repair_confirmation_level: `6.32`
- breakout_level: `6.32`
- breakdown_level: `4.28`
- nearest_support: `4.84`
- nearest_resistance: `5.79`
- bounce_target_zone: `{"conservative": 5.5, "base": 5.5, "extended": 6.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.01, "critical_warning": 4.28, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `267.76`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `25.8%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `34.67` / `weak`
- stock_alpha_score_v1: `21.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.7%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.42`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.94`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `294.50`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `294.50`
- breakout_level: `294.50`
- breakdown_level: `231.30`
- nearest_support: `256.87`
- nearest_resistance: `284.10`
- bounce_target_zone: `{"conservative": 275.93, "base": 275.93, "extended": 305.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 261.63, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
