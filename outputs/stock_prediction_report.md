# Stock Prediction Report

Generated at: `2026-09-04T16:25:44.089863+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `4`
- watchlist_size: `4`
- strongest_stock_symbol: `NVDA`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['single_stock_options']`

## Symbols

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `230.79`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `54.93` / `mixed`
- stock_alpha_score_v1: `55.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `63.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.54`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `224.69`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 235.36, "base": 235.36, "extended": 240.86, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 227.36, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `351.63`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `43.84` / `weak`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.7%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `323.64`
- risk_scenario_activation_level: `323.64`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `323.64`
- nearest_support: `339.36`
- nearest_resistance: `370.03`
- bounce_target_zone: `{"conservative": 360.83, "base": 360.83, "extended": 396.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 344.73, "critical_warning": 323.64, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.55`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.6%`
- secondary: `stock_downside_continuation` / `21.3%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `30.25` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.9%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.48`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.56`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.53`
- nearest_support: `9.05`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 9.92, "base": 9.92, "extended": 10.75, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.27, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `294.97`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `23.8%`
- secondary: `stock_trend_repair` / `20.7%`
- risk: `stock_downside_continuation` / `18.9%`
- stock_confluence_score: `47.11` / `mixed`
- stock_alpha_score_v1: `48.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `64.9%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.66`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `39.38`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `299.16`
- primary_invalidation_level: `264.82`
- risk_scenario_activation_level: `264.82`
- trend_repair_confirmation_level: `296.62`
- breakout_level: `299.16`
- breakdown_level: `264.82`
- nearest_support: `287.53`
- nearest_resistance: `296.62`
- bounce_target_zone: `{"conservative": 300.55, "base": 300.55, "extended": 304.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 290.51, "critical_warning": 264.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
