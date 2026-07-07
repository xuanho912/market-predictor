# Stock Prediction Report

Generated at: `2026-07-07T21:51:11.940264+00:00`
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
- current_price: `196.93`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `25.2%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `37.87` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.1%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.16`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `191.88`
- nearest_resistance: `204.51`
- bounce_target_zone: `{"conservative": 200.72, "base": 200.72, "extended": 219.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 194.09, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `402.90`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.4%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `16.1%`
- stock_confluence_score: `43.14` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.9%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.24`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `386.64`
- nearest_resistance: `427.29`
- bounce_target_zone: `{"conservative": 415.1, "base": 415.1, "extended": 449.12, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 393.75, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.96`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `24.1%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `36.31` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.1%`
- 60d_expected_return: `-3.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `53.56`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.39`
- risk_scenario_activation_level: `7.99`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.99`
- nearest_support: `8.64`
- nearest_resistance: `10.02`
- bounce_target_zone: `{"conservative": 9.49, "base": 9.49, "extended": 12.56, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.56, "critical_warning": 8.39, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `239.71`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.6%`
- secondary: `stock_failed_bounce` / `27.0%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `26.36` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.4%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `56.24`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.56`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.56`
- nearest_support: `231.60`
- nearest_resistance: `251.87`
- bounce_target_zone: `{"conservative": 245.79, "base": 245.79, "extended": 290.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 235.15, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
