# Stock Prediction Report

Generated at: `2026-08-28T15:41:56.865509+00:00`
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
- current_price: `222.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `18.1%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `53.16` / `mixed`
- stock_alpha_score_v1: `53.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `64.3%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.32`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `196.85`
- risk_scenario_activation_level: `196.85`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `196.85`
- nearest_support: `217.57`
- nearest_resistance: `230.47`
- bounce_target_zone: `{"conservative": 226.61, "base": 226.61, "extended": 235.64, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 219.83, "critical_warning": 196.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `350.29`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `36.63` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.4%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.6`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `366.50`
- primary_invalidation_level: `310.43`
- risk_scenario_activation_level: `310.43`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `366.50`
- breakdown_level: `310.43`
- nearest_support: `340.61`
- nearest_resistance: `364.81`
- bounce_target_zone: `{"conservative": 357.55, "base": 357.55, "extended": 376.18, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 344.85, "critical_warning": 310.43, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.44`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `37.17` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.7%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.84`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.29`
- risk_scenario_activation_level: `8.29`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.29`
- nearest_support: `8.89`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 9.85, "base": 9.85, "extended": 10.8, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.13, "critical_warning": 8.29, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `280.73`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `20.2%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `40.2` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `55.5%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.57`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.81`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `274.36`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 285.51, "base": 285.51, "extended": 293.37, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 277.15, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
