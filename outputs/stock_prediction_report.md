# Stock Prediction Report

Generated at: `2026-10-23T17:12:20.135957+00:00`
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
- current_price: `211.73`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.9%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `39.82` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.0%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `36.93`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `207.84`
- risk_scenario_activation_level: `205.15`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `205.15`
- nearest_support: `210.18`
- nearest_resistance: `218.90`
- bounce_target_zone: `{"conservative": 215.31, "base": 215.31, "extended": 248.15, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 209.03, "critical_warning": 207.84, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `371.45`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `17.7%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `38.18` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.4%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.47`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.86`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.86`
- breakout_level: `388.86`
- breakdown_level: `345.88`
- nearest_support: `362.09`
- nearest_resistance: `385.49`
- bounce_target_zone: `{"conservative": 378.47, "base": 378.47, "extended": 398.22, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.19, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.39`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `36.4%`
- secondary: `stock_failed_bounce` / `20.1%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `38.65` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `11.0%`
- 60d_expected_return: `-4.7%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Stock Breakdown Warning` / `HIGH_CONVICTION` / `84.11`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.08`
- risk_scenario_activation_level: `4.87`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `4.87`
- nearest_support: `5.20`
- nearest_resistance: `5.95`
- bounce_target_zone: `{"conservative": 5.67, "base": 5.67, "extended": 8.75, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.17, "critical_warning": 5.08, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `253.91`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `24.3%`
- risk: `stock_event_risk` / `11.8%`
- stock_confluence_score: `29.35` / `weak`
- stock_alpha_score_v1: `26.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.7%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.53`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `243.60`
- risk_scenario_activation_level: `236.46`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `236.46`
- nearest_support: `247.20`
- nearest_resistance: `272.95`
- bounce_target_zone: `{"conservative": 263.43, "base": 263.43, "extended": 322.49, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 246.77, "critical_warning": 243.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
