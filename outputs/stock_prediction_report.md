# Stock Prediction Report

Generated at: `2026-11-05T20:01:30.064435+00:00`
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
- current_price: `183.92`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `30.1%`
- secondary: `stock_failed_bounce` / `27.1%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `40.1` / `weak`
- stock_alpha_score_v1: `35.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.9%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `48.03`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `233.92`
- primary_invalidation_level: `179.07`
- risk_scenario_activation_level: `175.72`
- trend_repair_confirmation_level: `233.92`
- breakout_level: `233.92`
- breakdown_level: `175.72`
- nearest_support: `181.55`
- nearest_resistance: `192.87`
- bounce_target_zone: `{"conservative": 188.39, "base": 188.39, "extended": 239.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 180.56, "critical_warning": 179.07, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `343.88`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.0%`
- secondary: `stock_downside_continuation` / `21.3%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `30.14` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.9%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.33`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `414.23`
- primary_invalidation_level: `332.42`
- risk_scenario_activation_level: `324.49`
- trend_repair_confirmation_level: `414.23`
- breakout_level: `414.23`
- breakdown_level: `324.49`
- nearest_support: `338.15`
- nearest_resistance: `365.02`
- bounce_target_zone: `{"conservative": 354.45, "base": 354.45, "extended": 428.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 335.94, "critical_warning": 332.42, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `4.49`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.7%`
- secondary: `stock_failed_bounce` / `24.2%`
- risk: `stock_event_risk` / `12.2%`
- stock_confluence_score: `42.73` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `8.6%`
- 60d_expected_return: `-5.9%`
- risk_reward_ratio: `0.25`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `94.37`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `7.42`
- primary_invalidation_level: `4.21`
- risk_scenario_activation_level: `4.02`
- trend_repair_confirmation_level: `7.42`
- breakout_level: `7.42`
- breakdown_level: `4.02`
- nearest_support: `4.28`
- nearest_resistance: `5.00`
- bounce_target_zone: `{"conservative": 4.74, "base": 4.74, "extended": 7.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 4.29, "critical_warning": 4.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `240.12`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `26.8%`
- secondary: `stock_failed_bounce` / `26.4%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `27.72` / `weak`
- stock_alpha_score_v1: `22.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.1%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `45.71`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `301.77`
- primary_invalidation_level: `231.30`
- risk_scenario_activation_level: `226.73`
- trend_repair_confirmation_level: `301.77`
- breakout_level: `301.77`
- breakdown_level: `226.73`
- nearest_support: `231.30`
- nearest_resistance: `254.73`
- bounce_target_zone: `{"conservative": 247.42, "base": 247.42, "extended": 311.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 234.64, "critical_warning": 231.3, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
