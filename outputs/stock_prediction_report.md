# Stock Prediction Report

Generated at: `2026-09-09T16:42:31.689365+00:00`
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
- current_price: `224.07`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `47.77` / `mixed`
- stock_alpha_score_v1: `47.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.09`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `218.03`
- nearest_resistance: `233.14`
- bounce_target_zone: `{"conservative": 228.6, "base": 228.6, "extended": 240.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 220.67, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `369.26`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `15.4%`
- stock_confluence_score: `46.06` / `mixed`
- stock_alpha_score_v1: `16.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.6%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.99`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `323.64`
- risk_scenario_activation_level: `323.64`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `323.64`
- nearest_support: `357.06`
- nearest_resistance: `384.04`
- bounce_target_zone: `{"conservative": 378.41, "base": 378.41, "extended": 396.24, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 362.4, "critical_warning": 323.64, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.91`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.7%`
- secondary: `stock_trend_repair` / `20.8%`
- risk: `stock_downside_continuation` / `18.0%`
- stock_confluence_score: `46.31` / `mixed`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.1%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.67`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `43.89`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `8.53`
- nearest_support: `10.37`
- nearest_resistance: `11.37`
- bounce_target_zone: `{"conservative": 11.32, "base": 11.32, "extended": 11.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.58, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `295.89`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_downside_continuation` / `19.3%`
- risk: `stock_event_risk` / `11.2%`
- stock_confluence_score: `45.47` / `mixed`
- stock_alpha_score_v1: `54.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `65.5%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.63`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.28`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `264.82`
- risk_scenario_activation_level: `264.82`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `264.82`
- nearest_support: `288.63`
- nearest_resistance: `305.80`
- bounce_target_zone: `{"conservative": 301.33, "base": 301.33, "extended": 313.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 291.8, "critical_warning": 264.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
