# Stock Prediction Report

Generated at: `2026-09-01T16:43:31.906521+00:00`
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
- current_price: `219.20`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `50.49` / `mixed`
- stock_alpha_score_v1: `55.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `64.7%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.49`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `207.25`
- nearest_support: `213.86`
- nearest_resistance: `227.21`
- bounce_target_zone: `{"conservative": 223.2, "base": 223.2, "extended": 235.81, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 216.2, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `357.21`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `15.2%`
- stock_confluence_score: `44.33` / `weak`
- stock_alpha_score_v1: `8.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.4%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.86`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `368.92`
- primary_invalidation_level: `315.52`
- risk_scenario_activation_level: `315.52`
- trend_repair_confirmation_level: `368.92`
- breakout_level: `368.92`
- breakdown_level: `315.52`
- nearest_support: `346.25`
- nearest_resistance: `368.92`
- bounce_target_zone: `{"conservative": 365.44, "base": 365.44, "extended": 379.88, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 351.05, "critical_warning": 315.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.16`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.3%`
- secondary: `stock_downside_continuation` / `22.7%`
- risk: `stock_event_risk` / `13.3%`
- stock_confluence_score: `25.7` / `weak`
- stock_alpha_score_v1: `1.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.8%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.61`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.43`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.43`
- nearest_support: `8.63`
- nearest_resistance: `9.96`
- bounce_target_zone: `{"conservative": 9.56, "base": 9.56, "extended": 10.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.87, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `278.60`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `42.86` / `weak`
- stock_alpha_score_v1: `45.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.4%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.72`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `271.82`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 283.69, "base": 283.69, "extended": 293.78, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 274.79, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
