# Stock Prediction Report

Generated at: `2026-10-27T02:01:54.940413+00:00`
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
- current_price: `216.00`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `42.57` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.23`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `210.18`
- risk_scenario_activation_level: `209.24`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `209.24`
- nearest_support: `211.09`
- nearest_resistance: `223.37`
- bounce_target_zone: `{"conservative": 219.69, "base": 219.69, "extended": 248.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 213.24, "critical_warning": 210.18, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `391.62`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.8%`
- secondary: `stock_trend_repair` / `22.8%`
- risk: `stock_downside_continuation` / `16.4%`
- stock_confluence_score: `52.58` / `mixed`
- stock_alpha_score_v1: `25.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.3%`
- 60d_expected_return: `0.0%`
- risk_reward_ratio: `0.73`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `57.36`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `397.54`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `397.27`
- breakout_level: `397.54`
- breakdown_level: `345.88`
- nearest_support: `381.10`
- nearest_resistance: `397.27`
- bounce_target_zone: `{"conservative": 399.51, "base": 399.51, "extended": 407.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 385.3, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.27`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `37.5%`
- secondary: `stock_failed_bounce` / `19.4%`
- risk: `stock_event_risk` / `10.7%`
- stock_confluence_score: `40.95` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `12.2%`
- 60d_expected_return: `-4.5%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `86.16`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.37`
- primary_invalidation_level: `4.98`
- risk_scenario_activation_level: `4.78`
- trend_repair_confirmation_level: `8.37`
- breakout_level: `8.37`
- breakdown_level: `4.78`
- nearest_support: `5.20`
- nearest_resistance: `5.80`
- bounce_target_zone: `{"conservative": 5.53, "base": 5.53, "extended": 8.72, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.07, "critical_warning": 4.98, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `252.48`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `24.6%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `27.99` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.8%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.67`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `243.83`
- risk_scenario_activation_level: `237.83`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `237.83`
- nearest_support: `247.20`
- nearest_resistance: `268.46`
- bounce_target_zone: `{"conservative": 260.47, "base": 260.47, "extended": 320.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 246.49, "critical_warning": 243.83, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
