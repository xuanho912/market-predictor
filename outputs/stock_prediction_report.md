# Stock Prediction Report

Generated at: `2026-11-19T20:41:08.959886+00:00`
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
- current_price: `147.23`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.5%`
- secondary: `stock_failed_bounce` / `22.2%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `42.69` / `weak`
- stock_alpha_score_v1: `23.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `29.5%`
- 60d_expected_return: `-4.2%`
- risk_reward_ratio: `0.36`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `73.24`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `219.99`
- primary_invalidation_level: `139.54`
- risk_scenario_activation_level: `134.21`
- trend_repair_confirmation_level: `219.99`
- breakout_level: `219.99`
- breakdown_level: `134.21`
- nearest_support: `146.67`
- nearest_resistance: `161.43`
- bounce_target_zone: `{"conservative": 154.33, "base": 154.33, "extended": 229.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 141.91, "critical_warning": 139.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `375.29`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `16.3%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `48.51` / `mixed`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.8%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `39.38`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `338.15`
- risk_scenario_activation_level: `338.15`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `338.15`
- nearest_support: `360.57`
- nearest_resistance: `397.37`
- bounce_target_zone: `{"conservative": 386.33, "base": 386.33, "extended": 428.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 367.01, "critical_warning": 338.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `3.82`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.1%`
- secondary: `stock_failed_bounce` / `23.7%`
- risk: `stock_event_risk` / `10.9%`
- stock_confluence_score: `44.85` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.2%`
- 60d_expected_return: `-7.2%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `95.37`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `6.11`
- primary_invalidation_level: `3.50`
- risk_scenario_activation_level: `3.27`
- trend_repair_confirmation_level: `6.11`
- breakout_level: `6.11`
- breakdown_level: `3.27`
- nearest_support: `3.71`
- nearest_resistance: `4.41`
- bounce_target_zone: `{"conservative": 4.11, "base": 4.11, "extended": 6.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 3.59, "critical_warning": 3.5, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `252.43`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `40.18` / `weak`
- stock_alpha_score_v1: `28.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.5%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.13`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `284.97`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `231.30`
- trend_repair_confirmation_level: `284.97`
- breakout_level: `284.97`
- breakdown_level: `231.30`
- nearest_support: `241.11`
- nearest_resistance: `269.41`
- bounce_target_zone: `{"conservative": 260.92, "base": 260.92, "extended": 296.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 246.06, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
