# Stock Prediction Report

Generated at: `2026-11-06T07:59:01.960739+00:00`
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
- current_price: `181.60`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `31.8%`
- secondary: `stock_failed_bounce` / `26.7%`
- risk: `stock_event_risk` / `8.6%`
- stock_confluence_score: `39.05` / `weak`
- stock_alpha_score_v1: `38.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.2%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `50.9`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `233.92`
- primary_invalidation_level: `176.75`
- risk_scenario_activation_level: `173.39`
- trend_repair_confirmation_level: `233.92`
- breakout_level: `233.92`
- breakdown_level: `173.39`
- nearest_support: `181.46`
- nearest_resistance: `190.55`
- bounce_target_zone: `{"conservative": 186.08, "base": 186.08, "extended": 239.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 178.24, "critical_warning": 176.75, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `343.69`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.3%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `10.5%`
- stock_confluence_score: `30.84` / `weak`
- stock_alpha_score_v1: `8.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.5%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.26`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `332.23`
- risk_scenario_activation_level: `324.30`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `324.30`
- nearest_support: `338.15`
- nearest_resistance: `364.84`
- bounce_target_zone: `{"conservative": 354.27, "base": 354.27, "extended": 428.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 335.76, "critical_warning": 332.23, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.37`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `37.2%`
- secondary: `stock_failed_bounce` / `24.3%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `42.69` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `7.7%`
- 60d_expected_return: `-6.2%`
- risk_reward_ratio: `0.25`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `98.0`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.42`
- primary_invalidation_level: `4.09`
- risk_scenario_activation_level: `3.90`
- trend_repair_confirmation_level: `7.42`
- breakout_level: `7.42`
- breakdown_level: `3.90`
- nearest_support: `4.28`
- nearest_resistance: `4.88`
- bounce_target_zone: `{"conservative": 4.63, "base": 4.63, "extended": 7.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.18, "critical_warning": 4.09, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `239.65`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `28.1%`
- secondary: `stock_failed_bounce` / `25.9%`
- risk: `stock_event_risk` / `12.5%`
- stock_confluence_score: `27.38` / `weak`
- stock_alpha_score_v1: `28.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.7%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.46`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `301.77`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `226.26`
- trend_repair_confirmation_level: `301.77`
- breakout_level: `301.77`
- breakdown_level: `226.26`
- nearest_support: `231.30`
- nearest_resistance: `254.26`
- bounce_target_zone: `{"conservative": 246.95, "base": 246.95, "extended": 311.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 234.17, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
