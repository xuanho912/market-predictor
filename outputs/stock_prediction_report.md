# Stock Prediction Report

Generated at: `2026-07-21T14:26:10.463126+00:00`
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
- current_price: `205.02`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.3%`
- secondary: `stock_downside_continuation` / `20.1%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `46.28` / `mixed`
- stock_alpha_score_v1: `46.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.7%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.16`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.81`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.81`
- breakout_level: `213.81`
- breakdown_level: `189.80`
- nearest_support: `199.21`
- nearest_resistance: `213.73`
- bounce_target_zone: `{"conservative": 209.38, "base": 209.38, "extended": 219.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 201.75, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `382.75`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.0%`
- secondary: `stock_downside_continuation` / `21.7%`
- risk: `stock_event_risk` / `17.6%`
- stock_confluence_score: `30.76` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.1%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.8`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `363.98`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `363.98`
- nearest_support: `369.10`
- nearest_resistance: `403.23`
- bounce_target_zone: `{"conservative": 392.99, "base": 392.99, "extended": 446.51, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 375.07, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.42`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `33.2%`
- secondary: `stock_failed_bounce` / `19.3%`
- risk: `stock_event_risk` / `11.8%`
- stock_confluence_score: `30.34` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.8%`
- 60d_expected_return: `-3.4%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `55.49`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.82`
- primary_invalidation_level: `7.21`
- risk_scenario_activation_level: `7.21`
- trend_repair_confirmation_level: `11.82`
- breakout_level: `11.82`
- breakdown_level: `7.21`
- nearest_support: `7.89`
- nearest_resistance: `9.22`
- bounce_target_zone: `{"conservative": 8.82, "base": 8.82, "extended": 12.35, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.12, "critical_warning": 7.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `258.24`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.0%`
- secondary: `stock_failed_bounce` / `26.1%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `27.59` / `weak`
- stock_alpha_score_v1: `22.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `41.8%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.29`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.52`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `275.81`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `275.81`
- breakout_level: `275.81`
- breakdown_level: `228.63`
- nearest_support: `251.37`
- nearest_resistance: `268.55`
- bounce_target_zone: `{"conservative": 263.4, "base": 263.4, "extended": 282.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 254.37, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
