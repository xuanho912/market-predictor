# Stock Prediction Report

Generated at: `2026-07-01T05:56:38.709445+00:00`
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
- current_price: `200.09`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.2%`
- secondary: `stock_failed_bounce` / `25.3%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `37.18` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.8%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `47.54`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `189.80`
- nearest_support: `195.02`
- nearest_resistance: `207.70`
- bounce_target_zone: `{"conservative": 203.9, "base": 203.9, "extended": 237.35, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 197.24, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `420.60`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.2%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `16.1%`
- stock_confluence_score: `43.02` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.4%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.84`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `433.60`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `433.60`
- breakout_level: `433.60`
- breakdown_level: `368.60`
- nearest_support: `406.62`
- nearest_resistance: `433.60`
- bounce_target_zone: `{"conservative": 431.09, "base": 431.09, "extended": 447.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 412.74, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.03`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.2%`
- secondary: `stock_failed_bounce` / `21.9%`
- risk: `stock_event_risk` / `12.4%`
- stock_confluence_score: `30.87` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `17.1%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.7`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.04`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `9.04`
- nearest_support: `9.31`
- nearest_resistance: `11.12`
- bounce_target_zone: `{"conservative": 10.57, "base": 10.57, "extended": 15.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.62, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `248.37`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.8%`
- secondary: `stock_downside_continuation` / `27.6%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `24.62` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.2%`
- 60d_expected_return: `-1.8%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `47.18`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `237.71`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `237.71`
- nearest_support: `240.62`
- nearest_resistance: `260.00`
- bounce_target_zone: `{"conservative": 254.19, "base": 254.19, "extended": 290.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 244.01, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
