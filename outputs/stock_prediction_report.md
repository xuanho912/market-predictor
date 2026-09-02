# Stock Prediction Report

Generated at: `2026-09-02T00:37:49.756501+00:00`
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
- current_price: `217.44`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `45.84` / `mixed`
- stock_alpha_score_v1: `45.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.1%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.25`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `207.25`
- nearest_support: `212.10`
- nearest_resistance: `225.45`
- bounce_target_zone: `{"conservative": 221.44, "base": 221.44, "extended": 235.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.44, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `356.09`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `18.5%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `45.54` / `mixed`
- stock_alpha_score_v1: `10.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.0%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.25`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `368.92`
- primary_invalidation_level: `315.52`
- risk_scenario_activation_level: `315.52`
- trend_repair_confirmation_level: `368.92`
- breakout_level: `368.92`
- breakdown_level: `315.52`
- nearest_support: `345.10`
- nearest_resistance: `368.92`
- bounce_target_zone: `{"conservative": 364.33, "base": 364.33, "extended": 379.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 349.91, "critical_warning": 315.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.21`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `22.5%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `31.28` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `37.2%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.49`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.48`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.48`
- nearest_support: `8.68`
- nearest_resistance: `10.01`
- bounce_target_zone: `{"conservative": 9.61, "base": 9.61, "extended": 10.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.91, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `280.31`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `20.1%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `47.0` / `mixed`
- stock_alpha_score_v1: `39.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.5%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.7`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `273.40`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 285.5, "base": 285.5, "extended": 293.91, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 276.42, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
