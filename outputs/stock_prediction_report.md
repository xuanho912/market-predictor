# Stock Prediction Report

Generated at: `2026-07-24T21:35:59.447423+00:00`
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
- current_price: `206.84`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `49.54` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `67.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.65`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `214.39`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `214.39`
- breakout_level: `214.39`
- breakdown_level: `189.80`
- nearest_support: `200.76`
- nearest_resistance: `214.39`
- bounce_target_zone: `{"conservative": 211.4, "base": 211.4, "extended": 220.47, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 203.42, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `313.03`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.9%`
- secondary: `stock_failed_bounce` / `27.6%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `36.17` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `28.3%`
- 60d_expected_return: `-2.6%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `64.7`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `302.12`
- risk_scenario_activation_level: `294.57`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `294.57`
- nearest_support: `306.51`
- nearest_resistance: `333.17`
- bounce_target_zone: `{"conservative": 323.1, "base": 323.1, "extended": 446.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 305.48, "critical_warning": 302.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.09`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.3%`
- secondary: `stock_failed_bounce` / `19.0%`
- risk: `stock_event_risk` / `12.2%`
- stock_confluence_score: `34.85` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `24.3%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `57.38`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.87`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `10.87`
- breakout_level: `10.87`
- breakdown_level: `7.21`
- nearest_support: `7.58`
- nearest_resistance: `8.86`
- bounce_target_zone: `{"conservative": 8.47, "base": 8.47, "extended": 11.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.8, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.35`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.4%`
- secondary: `stock_downside_continuation` / `23.2%`
- risk: `stock_event_risk` / `11.0%`
- stock_confluence_score: `43.79` / `weak`
- stock_alpha_score_v1: `31.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.8%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.71`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `228.63`
- nearest_support: `267.79`
- nearest_resistance: `279.60`
- bounce_target_zone: `{"conservative": 279.27, "base": 279.27, "extended": 286.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 270.66, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
