# Stock Prediction Report

Generated at: `2026-10-07T01:54:25.046888+00:00`
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
- current_price: `239.24`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.5%`
- secondary: `stock_downside_continuation` / `19.0%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `52.22` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.4%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.98`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `208.93`
- nearest_support: `234.95`
- nearest_resistance: `243.37`
- bounce_target_zone: `{"conservative": 242.46, "base": 242.46, "extended": 247.66, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 236.82, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `380.68`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `28.2%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `14.4%`
- stock_confluence_score: `43.44` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `38.3%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.44`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.83`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.83`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `386.83`
- breakout_level: `386.83`
- breakdown_level: `345.88`
- nearest_support: `371.34`
- nearest_resistance: `386.83`
- bounce_target_zone: `{"conservative": 387.68, "base": 387.68, "extended": 396.17, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 375.43, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.02`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `32.1%`
- secondary: `stock_failed_bounce` / `21.0%`
- risk: `stock_event_risk` / `12.9%`
- stock_confluence_score: `32.25` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `19.0%`
- 60d_expected_return: `-2.9%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `68.11`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.26`
- primary_invalidation_level: `7.61`
- risk_scenario_activation_level: `7.45`
- trend_repair_confirmation_level: `11.26`
- breakout_level: `11.26`
- breakdown_level: `7.45`
- nearest_support: `7.61`
- nearest_resistance: `8.64`
- bounce_target_zone: `{"conservative": 8.33, "base": 8.33, "extended": 11.67, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 7.79, "critical_warning": 7.61, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `300.40`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.3%`
- secondary: `stock_downside_continuation` / `17.5%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `59.62` / `mixed`
- stock_alpha_score_v1: `49.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.6%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.55`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `247.20`
- risk_scenario_activation_level: `247.20`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `247.20`
- nearest_support: `290.10`
- nearest_resistance: `309.80`
- bounce_target_zone: `{"conservative": 308.12, "base": 308.12, "extended": 320.1, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 294.61, "critical_warning": 247.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
