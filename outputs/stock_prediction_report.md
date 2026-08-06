# Stock Prediction Report

Generated at: `2026-08-06T06:16:37.817294+00:00`
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
- current_price: `219.22`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `17.6%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `56.52` / `mixed`
- stock_alpha_score_v1: `67.5` / `watchlist_candidate`
- 20d_outperformance_probability: `70.3%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.62`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.67`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `222.82`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `222.22`
- breakout_level: `222.82`
- breakdown_level: `190.01`
- nearest_support: `212.81`
- nearest_resistance: `222.22`
- bounce_target_zone: `{"conservative": 224.02, "base": 224.02, "extended": 228.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 215.62, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `321.55`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `29.8%`
- secondary: `stock_failed_bounce` / `20.8%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `41.7` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.6%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.34`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `47.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `413.16`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `413.16`
- breakout_level: `413.16`
- breakdown_level: `297.38`
- nearest_support: `309.06`
- nearest_resistance: `340.28`
- bounce_target_zone: `{"conservative": 330.92, "base": 330.92, "extended": 425.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 314.53, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.38`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `22.8%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `42.8` / `weak`
- stock_alpha_score_v1: `10.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.1%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `30.06`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `9.71`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `9.71`
- breakout_level: `9.71`
- breakdown_level: `7.21`
- nearest_support: `8.84`
- nearest_resistance: `9.71`
- bounce_target_zone: `{"conservative": 9.79, "base": 9.79, "extended": 10.25, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.07, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `265.12`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.1%`
- secondary: `stock_downside_continuation` / `17.9%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `42.69` / `weak`
- stock_alpha_score_v1: `36.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.5%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.53`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `279.60`
- primary_invalidation_level: `244.95`
- risk_scenario_activation_level: `244.95`
- trend_repair_confirmation_level: `279.60`
- breakout_level: `279.60`
- breakdown_level: `244.95`
- nearest_support: `257.07`
- nearest_resistance: `277.20`
- bounce_target_zone: `{"conservative": 271.16, "base": 271.16, "extended": 287.65, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 260.59, "critical_warning": 244.95, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
