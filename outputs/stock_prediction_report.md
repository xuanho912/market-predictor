# Stock Prediction Report

Generated at: `2026-07-21T21:39:58.411779+00:00`
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
- current_price: `207.29`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `19.2%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `46.62` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.2%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.0`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.81`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.81`
- breakout_level: `213.81`
- breakdown_level: `189.80`
- nearest_support: `201.48`
- nearest_resistance: `213.81`
- bounce_target_zone: `{"conservative": 211.65, "base": 211.65, "extended": 219.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 204.02, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `378.93`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `24.1%`
- risk: `stock_event_risk` / `16.3%`
- stock_confluence_score: `31.27` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.0%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.81`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `367.78`
- risk_scenario_activation_level: `360.05`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `360.05`
- nearest_support: `368.60`
- nearest_resistance: `399.52`
- bounce_target_zone: `{"conservative": 389.23, "base": 389.23, "extended": 446.59, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 371.21, "critical_warning": 367.78, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.71`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.4%`
- secondary: `stock_failed_bounce` / `19.1%`
- risk: `stock_event_risk` / `12.3%`
- stock_confluence_score: `35.5` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `20.4%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.41`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `50.15`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.82`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `11.82`
- breakout_level: `11.82`
- breakdown_level: `7.21`
- nearest_support: `8.16`
- nearest_resistance: `9.53`
- bounce_target_zone: `{"conservative": 9.12, "base": 9.12, "extended": 12.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.4, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `262.22`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.3%`
- secondary: `stock_downside_continuation` / `24.5%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `30.42` / `weak`
- stock_alpha_score_v1: `17.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.7%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `38.54`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `275.81`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `275.81`
- breakout_level: `275.81`
- breakdown_level: `228.63`
- nearest_support: `255.19`
- nearest_resistance: `272.77`
- bounce_target_zone: `{"conservative": 267.49, "base": 267.49, "extended": 282.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 258.26, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
