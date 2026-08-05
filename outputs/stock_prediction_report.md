# Stock Prediction Report

Generated at: `2026-08-05T14:36:10.750655+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `TSLA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `220.52`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `52.34` / `mixed`
- stock_alpha_score_v1: `60.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `67.2%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.24`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `224.13`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `222.22`
- breakout_level: `224.13`
- breakdown_level: `190.01`
- nearest_support: `214.12`
- nearest_resistance: `222.22`
- bounce_target_zone: `{"conservative": 225.33, "base": 225.33, "extended": 228.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 216.92, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `324.83`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.4%`
- secondary: `stock_failed_bounce` / `21.0%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `39.87` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.5%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.35`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `45.76`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `413.16`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `413.16`
- breakout_level: `413.16`
- breakdown_level: `297.38`
- nearest_support: `312.35`
- nearest_resistance: `343.55`
- bounce_target_zone: `{"conservative": 334.19, "base": 334.19, "extended": 425.64, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 317.81, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.36`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `17.0%`
- stock_confluence_score: `38.69` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.4%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.03`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.71`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `9.71`
- breakout_level: `9.71`
- breakdown_level: `7.21`
- nearest_support: `8.82`
- nearest_resistance: `9.71`
- bounce_target_zone: `{"conservative": 9.77, "base": 9.77, "extended": 10.25, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.06, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `266.05`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `18.9%`
- risk: `stock_event_risk` / `15.7%`
- stock_confluence_score: `36.56` / `weak`
- stock_alpha_score_v1: `30.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.1%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.5`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `244.95`
- nearest_support: `258.13`
- nearest_resistance: `277.94`
- bounce_target_zone: `{"conservative": 271.99, "base": 271.99, "extended": 287.52, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 261.59, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
