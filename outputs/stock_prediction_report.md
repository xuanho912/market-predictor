# Stock Prediction Report

Generated at: `2026-10-08T00:33:02.280791+00:00`
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
- current_price: `237.47`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `47.24` / `mixed`
- stock_alpha_score_v1: `44.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.1%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.6`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `208.93`
- nearest_support: `233.36`
- nearest_resistance: `243.37`
- bounce_target_zone: `{"conservative": 240.56, "base": 240.56, "extended": 247.48, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 235.16, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `377.81`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.1%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `39.82` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.6%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `37.03`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `368.94`
- nearest_resistance: `386.83`
- bounce_target_zone: `{"conservative": 384.47, "base": 384.47, "extended": 395.7, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.82, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.67`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.3%`
- secondary: `stock_failed_bounce` / `21.0%`
- risk: `stock_event_risk` / `10.1%`
- stock_confluence_score: `29.09` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `18.3%`
- 60d_expected_return: `-3.0%`
- risk_reward_ratio: `0.39`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `78.19`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.69`
- primary_invalidation_level: `7.35`
- risk_scenario_activation_level: `7.13`
- trend_repair_confirmation_level: `10.69`
- breakout_level: `10.69`
- breakdown_level: `7.13`
- nearest_support: `7.39`
- nearest_resistance: `8.26`
- bounce_target_zone: `{"conservative": 7.97, "base": 7.97, "extended": 11.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.45, "critical_warning": 7.35, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `299.59`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `15.9%`
- stock_confluence_score: `51.02` / `mixed`
- stock_alpha_score_v1: `48.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `57.2%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.3`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `289.07`
- nearest_resistance: `309.80`
- bounce_target_zone: `{"conservative": 307.48, "base": 307.48, "extended": 320.32, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 293.67, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
