# Stock Prediction Report

Generated at: `2026-07-20T21:39:59.975713+00:00`
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
- current_price: `203.28`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `45.28` / `mixed`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.8%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.58`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `197.45`
- nearest_resistance: `212.02`
- bounce_target_zone: `{"conservative": 207.65, "base": 207.65, "extended": 219.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 200.0, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `369.57`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.2%`
- secondary: `stock_downside_continuation` / `24.7%`
- risk: `stock_event_risk` / `15.9%`
- stock_confluence_score: `29.77` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `36.6%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.83`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `358.23`
- risk_scenario_activation_level: `350.39`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `350.39`
- nearest_support: `368.60`
- nearest_resistance: `390.50`
- bounce_target_zone: `{"conservative": 380.03, "base": 380.03, "extended": 446.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 361.72, "critical_warning": 358.23, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.96`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.5%`
- secondary: `stock_failed_bounce` / `19.1%`
- risk: `stock_event_risk` / `11.3%`
- stock_confluence_score: `41.56` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `13.1%`
- 60d_expected_return: `-4.0%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `65.86`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `7.21`
- nearest_support: `7.42`
- nearest_resistance: `8.77`
- bounce_target_zone: `{"conservative": 8.37, "base": 8.37, "extended": 12.39, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.66, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `253.50`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.4%`
- secondary: `stock_failed_bounce` / `25.9%`
- risk: `stock_event_risk` / `10.5%`
- stock_confluence_score: `28.54` / `weak`
- stock_alpha_score_v1: `20.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `40.7%`
- 60d_expected_return: `-1.5%`
- risk_reward_ratio: `0.3`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `42.94`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.74`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `279.74`
- breakout_level: `279.74`
- breakdown_level: `228.63`
- nearest_support: `246.27`
- nearest_resistance: `264.34`
- bounce_target_zone: `{"conservative": 258.92, "base": 258.92, "extended": 286.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 249.43, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
