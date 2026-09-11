# Stock Prediction Report

Generated at: `2026-09-11T16:31:58.013046+00:00`
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
- current_price: `219.10`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.5%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `14.7%`
- stock_confluence_score: `43.56` / `weak`
- stock_alpha_score_v1: `39.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.4%`
- 60d_expected_return: `-1.1%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.88`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `212.96`
- nearest_resistance: `228.31`
- bounce_target_zone: `{"conservative": 223.71, "base": 223.71, "extended": 240.9, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 215.64, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `365.05`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `18.0%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `48.17` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.3%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `28.65`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `331.12`
- risk_scenario_activation_level: `331.12`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `331.12`
- nearest_support: `353.63`
- nearest_resistance: `382.17`
- bounce_target_zone: `{"conservative": 373.61, "base": 373.61, "extended": 395.46, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 358.62, "critical_warning": 331.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.85`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `27.0%`
- secondary: `stock_downside_continuation` / `23.2%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `29.5` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `33.5%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Liquidity / Gap Risk Alert` / `WATCH` / `38.8`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.36`
- risk_scenario_activation_level: `8.02`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `8.02`
- nearest_support: `8.53`
- nearest_resistance: `9.75`
- bounce_target_zone: `{"conservative": 9.3, "base": 9.3, "extended": 11.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.51, "critical_warning": 8.36, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `286.72`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `19.6%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `40.19` / `weak`
- stock_alpha_score_v1: `43.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `58.8%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.91`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `264.82`
- risk_scenario_activation_level: `264.82`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `264.82`
- nearest_support: `279.41`
- nearest_resistance: `297.69`
- bounce_target_zone: `{"conservative": 292.2, "base": 292.2, "extended": 313.11, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 282.61, "critical_warning": 264.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
