# Stock Prediction Report

Generated at: `2026-09-29T18:07:55.330550+00:00`
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
- current_price: `228.19`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.3%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `14.3%`
- stock_confluence_score: `49.01` / `mixed`
- stock_alpha_score_v1: `52.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `59.4%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `223.92`
- nearest_resistance: `234.60`
- bounce_target_zone: `{"conservative": 231.4, "base": 231.4, "extended": 239.03, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 225.79, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `353.83`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `29.9%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `13.4%`
- stock_confluence_score: `30.9` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `34.9%`
- 60d_expected_return: `-1.3%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.62`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `346.68`
- risk_scenario_activation_level: `341.73`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `341.73`
- nearest_support: `349.92`
- nearest_resistance: `367.02`
- bounce_target_zone: `{"conservative": 360.43, "base": 360.43, "extended": 395.63, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 348.88, "critical_warning": 346.68, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `7.84`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.2%`
- secondary: `stock_failed_bounce` / `25.4%`
- risk: `stock_event_risk` / `11.4%`
- stock_confluence_score: `29.1` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.0%`
- 60d_expected_return: `-3.4%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `45.34`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `7.43`
- risk_scenario_activation_level: `7.14`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.14`
- nearest_support: `7.76`
- nearest_resistance: `8.62`
- bounce_target_zone: `{"conservative": 8.23, "base": 8.23, "extended": 11.89, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.55, "critical_warning": 7.43, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `264.71`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.9%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `38.29` / `weak`
- stock_alpha_score_v1: `25.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.4%`
- 60d_expected_return: `-1.0%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.63`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.55`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.55`
- nearest_support: `257.53`
- nearest_resistance: `275.50`
- bounce_target_zone: `{"conservative": 270.11, "base": 270.11, "extended": 312.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 260.67, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
