# Stock Prediction Report

Generated at: `2026-10-26T18:44:23.455096+00:00`
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
- current_price: `216.05`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `41.21` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.4%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.85`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `210.18`
- risk_scenario_activation_level: `209.29`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `209.29`
- nearest_support: `211.14`
- nearest_resistance: `223.42`
- bounce_target_zone: `{"conservative": 219.74, "base": 219.74, "extended": 248.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 213.29, "critical_warning": 210.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `394.64`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.3%`
- secondary: `stock_failed_bounce` / `22.7%`
- risk: `stock_downside_continuation` / `16.3%`
- stock_confluence_score: `52.12` / `mixed`
- stock_alpha_score_v1: `23.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.2%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.74`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `60.24`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `400.55`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `410.40`
- breakout_level: `400.55`
- breakdown_level: `345.88`
- nearest_support: `384.12`
- nearest_resistance: `397.27`
- bounce_target_zone: `{"conservative": 402.52, "base": 410.4, "extended": 410.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 388.33, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.29`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `37.5%`
- secondary: `stock_failed_bounce` / `19.3%`
- risk: `stock_event_risk` / `10.7%`
- stock_confluence_score: `39.91` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `12.3%`
- 60d_expected_return: `-4.3%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `85.7`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `5.00`
- risk_scenario_activation_level: `4.80`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `4.80`
- nearest_support: `5.20`
- nearest_resistance: `5.82`
- bounce_target_zone: `{"conservative": 5.55, "base": 5.55, "extended": 8.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.09, "critical_warning": 5.0, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `252.96`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `24.5%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `29.73` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.9%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.79`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `244.31`
- risk_scenario_activation_level: `238.31`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `238.31`
- nearest_support: `247.20`
- nearest_resistance: `268.94`
- bounce_target_zone: `{"conservative": 260.95, "base": 260.95, "extended": 320.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 246.97, "critical_warning": 244.31, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
