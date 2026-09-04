# Stock Prediction Report

Generated at: `2026-09-04T23:15:53.950704+00:00`
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
- current_price: `230.36`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `52.46` / `mixed`
- stock_alpha_score_v1: `55.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `62.9%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.54`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `224.26`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 234.93, "base": 234.93, "extended": 240.86, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 226.93, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `354.08`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `17.7%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `46.28` / `mixed`
- stock_alpha_score_v1: `12.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.7%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.62`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.43`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `323.64`
- risk_scenario_activation_level: `323.64`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `323.64`
- nearest_support: `341.81`
- nearest_resistance: `372.48`
- bounce_target_zone: `{"conservative": 363.28, "base": 363.28, "extended": 396.31, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 347.18, "critical_warning": 323.64, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.70`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.6%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `32.95` / `weak`
- stock_alpha_score_v1: `3.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `39.9%`
- 60d_expected_return: `-2.0%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.35`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.53`
- nearest_support: `9.20`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 10.07, "base": 10.07, "extended": 10.75, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.42, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `298.96`
- market_context: `market_headwind`
- primary: `stock_trend_repair` / `23.1%`
- secondary: `stock_failed_bounce` / `22.3%`
- risk: `stock_downside_continuation` / `17.7%`
- stock_confluence_score: `53.03` / `mixed`
- stock_alpha_score_v1: `61.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `71.5%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.75`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `45.9`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `303.28`
- primary_invalidation_level: `264.82`
- risk_scenario_activation_level: `264.82`
- trend_repair_confirmation_level: `310.48`
- breakout_level: `303.28`
- breakdown_level: `264.82`
- nearest_support: `291.28`
- nearest_resistance: `299.73`
- bounce_target_zone: `{"conservative": 304.72, "base": 310.48, "extended": 310.48, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 294.35, "critical_warning": 264.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
