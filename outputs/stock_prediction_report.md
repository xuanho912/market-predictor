# Stock Prediction Report

Generated at: `2026-09-09T06:02:53.994703+00:00`
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
- current_price: `225.73`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `50.48` / `mixed`
- stock_alpha_score_v1: `53.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.44`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `234.76`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `234.76`
- breakout_level: `234.76`
- breakdown_level: `207.25`
- nearest_support: `219.49`
- nearest_resistance: `234.76`
- bounce_target_zone: `{"conservative": 230.41, "base": 230.41, "extended": 241.0, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 222.22, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `368.16`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `23.8%`
- secondary: `stock_trend_repair` / `17.7%`
- risk: `stock_downside_continuation` / `17.1%`
- stock_confluence_score: `48.05` / `mixed`
- stock_alpha_score_v1: `22.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.1%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.18`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `384.04`
- primary_invalidation_level: `323.64`
- risk_scenario_activation_level: `323.64`
- trend_repair_confirmation_level: `384.04`
- breakout_level: `384.04`
- breakdown_level: `323.64`
- nearest_support: `355.52`
- nearest_resistance: `384.04`
- bounce_target_zone: `{"conservative": 377.64, "base": 377.64, "extended": 396.68, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 360.58, "critical_warning": 323.64, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `11.18`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `25.9%`
- secondary: `stock_failed_bounce` / `21.3%`
- risk: `stock_downside_continuation` / `15.3%`
- stock_confluence_score: `52.42` / `mixed`
- stock_alpha_score_v1: `17.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.8%`
- 60d_expected_return: `0.5%`
- risk_reward_ratio: `0.78`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.49`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `12.02`
- breakout_level: `11.49`
- breakdown_level: `8.53`
- nearest_support: `10.62`
- nearest_resistance: `11.37`
- bounce_target_zone: `{"conservative": 11.6, "base": 12.02, "extended": 12.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.84, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `299.05`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `23.2%`
- secondary: `stock_failed_bounce` / `22.3%`
- risk: `stock_downside_continuation` / `17.7%`
- stock_confluence_score: `55.02` / `mixed`
- stock_alpha_score_v1: `63.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `72.4%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.76`
- strongest_alert: `Relative Strength Alert` / `WATCH` / `47.02`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `305.80`
- primary_invalidation_level: `264.82`
- risk_scenario_activation_level: `264.82`
- trend_repair_confirmation_level: `310.10`
- breakout_level: `305.80`
- breakdown_level: `264.82`
- nearest_support: `291.68`
- nearest_resistance: `305.80`
- bounce_target_zone: `{"conservative": 304.57, "base": 310.1, "extended": 313.17, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 294.63, "critical_warning": 264.82, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
