# Stock Prediction Report

Generated at: `2026-07-01T23:55:41.101955+00:00`
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
- current_price: `197.58`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.7%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `36.35` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.0%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.33`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `41.79`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.82`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `222.82`
- breakout_level: `222.82`
- breakdown_level: `189.80`
- nearest_support: `192.60`
- nearest_resistance: `205.05`
- bounce_target_zone: `{"conservative": 201.32, "base": 201.32, "extended": 227.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 194.78, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `425.30`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.0%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `15.8%`
- stock_confluence_score: `43.03` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.5%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.29`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `433.60`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `433.60`
- breakout_level: `433.60`
- breakdown_level: `368.60`
- nearest_support: `411.44`
- nearest_resistance: `433.60`
- bounce_target_zone: `{"conservative": 435.69, "base": 435.69, "extended": 447.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 417.51, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.15`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.7%`
- secondary: `stock_failed_bounce` / `19.4%`
- risk: `stock_event_risk` / `12.8%`
- stock_confluence_score: `38.19` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `14.1%`
- 60d_expected_return: `-3.8%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.17`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `13.52`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `9.12`
- trend_repair_confirmation_level: `13.52`
- breakout_level: `13.52`
- breakdown_level: `9.12`
- nearest_support: `9.45`
- nearest_resistance: `11.20`
- bounce_target_zone: `{"conservative": 10.68, "base": 10.68, "extended": 14.22, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.75, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `236.50`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.9%`
- secondary: `stock_failed_bounce` / `27.3%`
- risk: `stock_event_risk` / `9.5%`
- stock_confluence_score: `26.21` / `weak`
- stock_alpha_score_v1: `27.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.9%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `72.16`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.65`
- risk_scenario_activation_level: `225.16`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `225.16`
- nearest_support: `228.65`
- nearest_resistance: `248.87`
- bounce_target_zone: `{"conservative": 242.68, "base": 242.68, "extended": 291.01, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 231.86, "critical_warning": 228.65, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
