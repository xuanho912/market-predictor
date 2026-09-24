# Stock Prediction Report

Generated at: `2026-09-24T23:18:10.398721+00:00`
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
- current_price: `224.58`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `49.76` / `mixed`
- stock_alpha_score_v1: `50.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `60.6%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `26.53`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `208.93`
- risk_scenario_activation_level: `208.93`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `208.93`
- nearest_support: `220.26`
- nearest_resistance: `231.06`
- bounce_target_zone: `{"conservative": 227.82, "base": 227.82, "extended": 239.08, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 222.15, "critical_warning": 208.93, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `377.94`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `15.3%`
- stock_confluence_score: `44.22` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.1%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.15`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `386.70`
- primary_invalidation_level: `345.20`
- risk_scenario_activation_level: `345.20`
- trend_repair_confirmation_level: `386.70`
- breakout_level: `386.70`
- breakdown_level: `345.20`
- nearest_support: `368.64`
- nearest_resistance: `386.70`
- bounce_target_zone: `{"conservative": 384.92, "base": 384.92, "extended": 396.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 372.71, "critical_warning": 345.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.47`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.8%`
- secondary: `stock_downside_continuation` / `24.8%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `29.97` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `35.7%`
- 60d_expected_return: `-2.8%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Liquidity / Gap Risk Alert` / `NO_ALERT` / `31.77`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.37`
- primary_invalidation_level: `8.00`
- risk_scenario_activation_level: `7.67`
- trend_repair_confirmation_level: `11.37`
- breakout_level: `11.37`
- breakdown_level: `7.67`
- nearest_support: `8.05`
- nearest_resistance: `9.35`
- bounce_target_zone: `{"conservative": 8.91, "base": 8.91, "extended": 11.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.14, "critical_warning": 8.0, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `261.62`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.1%`
- secondary: `stock_failed_bounce` / `24.9%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `37.55` / `weak`
- stock_alpha_score_v1: `32.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.9%`
- 60d_expected_return: `-1.4%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `33.31`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `250.55`
- risk_scenario_activation_level: `250.37`
- trend_repair_confirmation_level: `305.80`
- breakout_level: `305.80`
- breakdown_level: `250.37`
- nearest_support: `253.44`
- nearest_resistance: `273.89`
- bounce_target_zone: `{"conservative": 267.75, "base": 267.75, "extended": 313.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 257.02, "critical_warning": 250.55, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
