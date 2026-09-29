# Stock Prediction Report

Generated at: `2026-09-29T02:35:19.582030+00:00`
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
- current_price: `228.86`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `17.7%`
- risk: `stock_event_risk` / `13.5%`
- stock_confluence_score: `50.89` / `mixed`
- stock_alpha_score_v1: `56.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `62.3%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.64`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.77`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `224.72`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 231.96, "base": 231.96, "extended": 238.9, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 226.53, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `357.45`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `29.3%`
- secondary: `stock_downside_continuation` / `20.6%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `44.69` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.1%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.37`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.83`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `347.15`
- risk_scenario_activation_level: `345.17`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.17`
- nearest_support: `348.52`
- nearest_resistance: `370.85`
- bounce_target_zone: `{"conservative": 364.15, "base": 364.15, "extended": 395.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 352.43, "critical_warning": 347.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.91`
- market_context: `market_headwind`
- primary: `stock_downside_continuation` / `28.1%`
- secondary: `stock_failed_bounce` / `24.9%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `29.9` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.4%`
- 60d_expected_return: `-3.3%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `46.26`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.49`
- risk_scenario_activation_level: `7.19`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.19`
- nearest_support: `7.89`
- nearest_resistance: `8.69`
- bounce_target_zone: `{"conservative": 8.3, "base": 8.3, "extended": 11.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.62, "critical_warning": 7.49, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `260.43`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `24.1%`
- secondary: `stock_failed_bounce` / `23.8%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `37.84` / `weak`
- stock_alpha_score_v1: `30.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.7%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.13`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `253.43`
- nearest_resistance: `270.92`
- bounce_target_zone: `{"conservative": 265.68, "base": 265.68, "extended": 312.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 256.5, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
