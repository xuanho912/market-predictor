# Stock Prediction Report

Generated at: `2026-08-14T13:47:18.885641+00:00`
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
- current_price: `225.77`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `48.98` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.24`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `228.83`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.49`
- breakout_level: `228.83`
- breakdown_level: `190.01`
- nearest_support: `220.33`
- nearest_resistance: `227.49`
- bounce_target_zone: `{"conservative": 229.85, "base": 229.85, "extended": 232.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 222.71, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `346.65`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.2%`
- secondary: `stock_failed_bounce` / `25.5%`
- risk: `stock_event_risk` / `13.1%`
- stock_confluence_score: `33.58` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `26.5%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.24`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `68.53`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.61`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `386.61`
- breakout_level: `386.61`
- breakdown_level: `297.38`
- nearest_support: `338.10`
- nearest_resistance: `359.47`
- bounce_target_zone: `{"conservative": 353.06, "base": 353.06, "extended": 395.16, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 341.84, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.70`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.0%`
- secondary: `stock_failed_bounce` / `22.4%`
- risk: `stock_downside_continuation` / `17.2%`
- stock_confluence_score: `36.95` / `weak`
- stock_alpha_score_v1: `15.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.1%`
- 60d_expected_return: `-0.1%`
- risk_reward_ratio: `0.63`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.69`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.53`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `9.15`
- nearest_resistance: `10.14`
- bounce_target_zone: `{"conservative": 10.11, "base": 10.53, "extended": 10.69, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.37, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `282.12`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `19.4%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `42.75` / `weak`
- stock_alpha_score_v1: `45.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.7%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.61`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.65`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `251.33`
- risk_scenario_activation_level: `251.33`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `251.33`
- nearest_support: `273.74`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 288.41, "base": 288.41, "extended": 295.38, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 277.4, "critical_warning": 251.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
