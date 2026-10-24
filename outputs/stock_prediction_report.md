# Stock Prediction Report

Generated at: `2026-10-24T05:59:22.385767+00:00`
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
- current_price: `210.96`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `23.0%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `41.38` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.7%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.53`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `207.07`
- risk_scenario_activation_level: `204.38`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `204.38`
- nearest_support: `210.18`
- nearest_resistance: `218.13`
- bounce_target_zone: `{"conservative": 214.55, "base": 214.55, "extended": 248.15, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.27, "critical_warning": 207.07, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `372.22`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.4%`
- secondary: `stock_downside_continuation` / `17.5%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `40.93` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.7%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `30.7`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.86`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.86`
- breakout_level: `388.86`
- breakdown_level: `345.88`
- nearest_support: `362.86`
- nearest_resistance: `386.26`
- bounce_target_zone: `{"conservative": 379.24, "base": 379.24, "extended": 398.22, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.95, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.38`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `37.9%`
- secondary: `stock_failed_bounce` / `19.3%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `39.96` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `10.9%`
- 60d_expected_return: `-4.8%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `85.17`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.07`
- risk_scenario_activation_level: `4.86`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `4.86`
- nearest_support: `5.20`
- nearest_resistance: `5.95`
- bounce_target_zone: `{"conservative": 5.66, "base": 5.66, "extended": 8.75, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.17, "critical_warning": 5.07, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `253.45`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `24.4%`
- risk: `stock_event_risk` / `11.8%`
- stock_confluence_score: `28.15` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.4%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.05`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `243.13`
- risk_scenario_activation_level: `235.99`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `235.99`
- nearest_support: `247.20`
- nearest_resistance: `272.49`
- bounce_target_zone: `{"conservative": 262.97, "base": 262.97, "extended": 322.5, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 246.31, "critical_warning": 243.13, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
