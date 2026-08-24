# Stock Prediction Report

Generated at: `2026-08-24T23:33:04.730348+00:00`
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
- current_price: `208.48`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.9%`
- secondary: `stock_event_risk` / `16.8%`
- risk: `stock_downside_continuation` / `16.7%`
- stock_confluence_score: `50.63` / `mixed`
- stock_alpha_score_v1: `55.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `62.0%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.65`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `227.92`
- primary_invalidation_level: `190.01`
- risk_scenario_activation_level: `190.01`
- trend_repair_confirmation_level: `227.92`
- breakout_level: `227.92`
- breakdown_level: `190.01`
- nearest_support: `203.78`
- nearest_resistance: `215.54`
- bounce_target_zone: `{"conservative": 212.01, "base": 212.01, "extended": 232.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.66, "critical_warning": 190.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `348.95`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `23.9%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `43.59` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `49.2%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.41`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.71`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `366.50`
- primary_invalidation_level: `297.38`
- risk_scenario_activation_level: `297.38`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `366.50`
- breakdown_level: `297.38`
- nearest_support: `339.39`
- nearest_resistance: `363.29`
- bounce_target_zone: `{"conservative": 356.12, "base": 356.12, "extended": 376.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 343.57, "critical_warning": 297.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.05`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `22.3%`
- risk: `stock_event_risk` / `13.4%`
- stock_confluence_score: `39.46` / `weak`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.0%`
- 60d_expected_return: `-2.2%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `27.79`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.14`
- primary_invalidation_level: `7.54`
- risk_scenario_activation_level: `7.54`
- trend_repair_confirmation_level: `10.14`
- breakout_level: `10.14`
- breakdown_level: `7.54`
- nearest_support: `8.54`
- nearest_resistance: `9.81`
- bounce_target_zone: `{"conservative": 9.43, "base": 9.43, "extended": 10.64, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.76, "critical_warning": 7.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `273.43`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.5%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `11.1%`
- stock_confluence_score: `38.85` / `weak`
- stock_alpha_score_v1: `35.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.4%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.36`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `256.16`
- risk_scenario_activation_level: `256.16`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `256.16`
- nearest_support: `265.77`
- nearest_resistance: `284.91`
- bounce_target_zone: `{"conservative": 279.17, "base": 279.17, "extended": 294.66, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 269.12, "critical_warning": 256.16, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
