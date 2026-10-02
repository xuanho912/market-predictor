# Stock Prediction Report

Generated at: `2026-10-02T01:53:04.572637+00:00`
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
- current_price: `230.86`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `46.68` / `mixed`
- stock_alpha_score_v1: `42.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.6%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.21`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `226.61`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 234.05, "base": 234.05, "extended": 239.01, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 228.47, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `354.11`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `29.5%`
- secondary: `stock_downside_continuation` / `20.6%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `39.25` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.9%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `36.45`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `342.27`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `342.27`
- nearest_support: `345.88`
- nearest_resistance: `367.03`
- bounce_target_zone: `{"conservative": 360.57, "base": 360.57, "extended": 395.44, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 349.27, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.79`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `30.0%`
- secondary: `stock_failed_bounce` / `23.9%`
- risk: `stock_event_risk` / `10.6%`
- stock_confluence_score: `24.54` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.3%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `47.49`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.45`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.21`
- nearest_support: `7.75`
- nearest_resistance: `8.43`
- bounce_target_zone: `{"conservative": 8.11, "base": 8.11, "extended": 11.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.55, "critical_warning": 7.45, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `258.92`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `26.5%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `35.51` / `weak`
- stock_alpha_score_v1: `18.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.9%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `247.20`
- nearest_support: `250.70`
- nearest_resistance: `271.26`
- bounce_target_zone: `{"conservative": 265.09, "base": 265.09, "extended": 314.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 254.29, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
