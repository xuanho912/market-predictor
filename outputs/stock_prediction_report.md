# Stock Prediction Report

Generated at: `2026-09-16T06:07:26.419901+00:00`
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
- current_price: `212.17`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `21.0%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `41.53` / `weak`
- stock_alpha_score_v1: `32.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.2%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.69`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `203.88`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `203.88`
- nearest_support: `207.25`
- nearest_resistance: `221.21`
- bounce_target_zone: `{"conservative": 216.69, "base": 216.69, "extended": 240.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.78, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `356.58`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `47.53` / `mixed`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.0%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.07`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `331.12`
- risk_scenario_activation_level: `331.12`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `331.12`
- nearest_support: `345.39`
- nearest_resistance: `373.36`
- bounce_target_zone: `{"conservative": 364.97, "base": 364.97, "extended": 395.23, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 350.29, "critical_warning": 331.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.43`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `31.6%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `38.43` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.4%`
- 60d_expected_return: `-3.6%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `41.41`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.96`
- risk_scenario_activation_level: `7.63`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.63`
- nearest_support: `8.23`
- nearest_resistance: `9.30`
- bounce_target_zone: `{"conservative": 8.87, "base": 8.87, "extended": 11.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.1, "critical_warning": 7.96, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `259.89`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `30.2%`
- secondary: `stock_downside_continuation` / `24.4%`
- risk: `stock_event_risk` / `10.0%`
- stock_confluence_score: `31.94` / `weak`
- stock_alpha_score_v1: `25.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.5%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.96`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `253.20`
- risk_scenario_activation_level: `248.57`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `248.57`
- nearest_support: `259.61`
- nearest_resistance: `272.24`
- bounce_target_zone: `{"conservative": 266.07, "base": 266.07, "extended": 314.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 255.26, "critical_warning": 253.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
