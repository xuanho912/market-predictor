# Stock Prediction Report

Generated at: `2026-09-02T22:46:03.741342+00:00`
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
- current_price: `224.41`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `24.4%`
- secondary: `stock_downside_continuation` / `17.5%`
- risk: `stock_event_risk` / `14.1%`
- stock_confluence_score: `52.47` / `mixed`
- stock_alpha_score_v1: `61.0` / `wait_for_confirmation`
- 20d_outperformance_probability: `65.2%`
- 60d_expected_return: `-0.4%`
- risk_reward_ratio: `0.6`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.59`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `207.25`
- nearest_support: `218.67`
- nearest_resistance: `230.47`
- bounce_target_zone: `{"conservative": 228.71, "base": 228.71, "extended": 236.21, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 221.18, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `357.01`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.3%`
- risk: `stock_event_risk` / `15.0%`
- stock_confluence_score: `45.69` / `mixed`
- stock_alpha_score_v1: `11.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `52.3%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.16`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `368.92`
- primary_invalidation_level: `315.52`
- risk_scenario_activation_level: `315.52`
- trend_repair_confirmation_level: `368.92`
- breakout_level: `368.92`
- breakdown_level: `315.52`
- nearest_support: `346.35`
- nearest_resistance: `368.92`
- bounce_target_zone: `{"conservative": 365.0, "base": 365.0, "extended": 379.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 351.01, "critical_warning": 315.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.56`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.6%`
- secondary: `stock_downside_continuation` / `19.5%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `36.35` / `weak`
- stock_alpha_score_v1: `9.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.9%`
- 60d_expected_return: `-1.9%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.28`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.53`
- nearest_support: `9.04`
- nearest_resistance: `10.26`
- bounce_target_zone: `{"conservative": 9.95, "base": 9.95, "extended": 10.78, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.27, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `290.04`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `22.7%`
- secondary: `stock_trend_repair` / `21.6%`
- risk: `stock_downside_continuation` / `18.0%`
- stock_confluence_score: `48.82` / `mixed`
- stock_alpha_score_v1: `49.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `65.6%`
- 60d_expected_return: `-0.0%`
- risk_reward_ratio: `0.73`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `35.97`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `294.08`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `290.81`
- breakout_level: `294.08`
- breakdown_level: `260.67`
- nearest_support: `282.87`
- nearest_resistance: `290.81`
- bounce_target_zone: `{"conservative": 295.42, "base": 295.42, "extended": 297.98, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 285.74, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
