# Stock Prediction Report

Generated at: `2026-09-03T16:28:30.268390+00:00`
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
- current_price: `227.06`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `50.82` / `mixed`
- stock_alpha_score_v1: `53.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.4`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `207.25`
- nearest_support: `221.22`
- nearest_resistance: `230.47`
- bounce_target_zone: `{"conservative": 231.43, "base": 231.43, "extended": 236.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 223.78, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `382.50`
- market_context: `market_headwind`
- primary: `stock_trend_repair` / `22.9%`
- secondary: `stock_failed_bounce` / `22.7%`
- risk: `stock_downside_continuation` / `16.3%`
- stock_confluence_score: `49.43` / `mixed`
- stock_alpha_score_v1: `20.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.5%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.73`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `38.37`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.85`
- primary_invalidation_level: `321.25`
- risk_scenario_activation_level: `321.25`
- trend_repair_confirmation_level: `399.44`
- breakout_level: `388.85`
- breakdown_level: `321.25`
- nearest_support: `371.21`
- nearest_resistance: `384.04`
- bounce_target_zone: `{"conservative": 390.97, "base": 399.44, "extended": 399.44, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 375.73, "critical_warning": 321.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.81`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `19.9%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `37.0` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.5%`
- 60d_expected_return: `-1.7%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.46`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.53`
- nearest_support: `9.30`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 10.19, "base": 10.19, "extended": 10.76, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.53, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `286.37`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_trend_repair` / `19.4%`
- risk: `stock_downside_continuation` / `19.1%`
- stock_confluence_score: `45.59` / `mixed`
- stock_alpha_score_v1: `48.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `64.5%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `29.43`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `296.62`
- primary_invalidation_level: `261.37`
- risk_scenario_activation_level: `261.37`
- trend_repair_confirmation_level: `296.62`
- breakout_level: `296.62`
- breakdown_level: `261.37`
- nearest_support: `279.04`
- nearest_resistance: `296.62`
- bounce_target_zone: `{"conservative": 291.87, "base": 291.87, "extended": 303.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 281.97, "critical_warning": 261.37, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
