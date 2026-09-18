# Stock Prediction Report

Generated at: `2026-09-18T16:27:50.509228+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `CEG`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `219.39`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `43.72` / `weak`
- stock_alpha_score_v1: `41.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.0%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.51`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `214.75`
- nearest_resistance: `226.36`
- bounce_target_zone: `{"conservative": 222.87, "base": 222.87, "extended": 239.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 216.78, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `362.30`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `15.6%`
- stock_confluence_score: `42.67` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.5%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `342.53`
- risk_scenario_activation_level: `342.53`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `342.53`
- nearest_support: `350.93`
- nearest_resistance: `379.35`
- bounce_target_zone: `{"conservative": 370.83, "base": 370.83, "extended": 395.41, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 355.91, "critical_warning": 342.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.29`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.5%`
- secondary: `stock_failed_bounce` / `23.5%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `28.41` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.2%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.14`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.82`
- risk_scenario_activation_level: `7.49`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.49`
- nearest_support: `8.05`
- nearest_resistance: `9.16`
- bounce_target_zone: `{"conservative": 8.73, "base": 8.73, "extended": 11.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.96, "critical_warning": 7.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `256.47`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.7%`
- secondary: `stock_downside_continuation` / `24.9%`
- risk: `stock_event_risk` / `10.2%`
- stock_confluence_score: `31.34` / `weak`
- stock_alpha_score_v1: `26.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.0%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.85`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `249.53`
- risk_scenario_activation_level: `244.73`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `244.73`
- nearest_support: `254.71`
- nearest_resistance: `269.28`
- bounce_target_zone: `{"conservative": 262.87, "base": 262.87, "extended": 314.34, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 251.67, "critical_warning": 249.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
