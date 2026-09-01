# Stock Prediction Report

Generated at: `2026-09-01T01:49:18.461047+00:00`
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
- current_price: `220.78`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `18.4%`
- risk: `stock_event_risk` / `14.8%`
- stock_confluence_score: `52.18` / `mixed`
- stock_alpha_score_v1: `55.5` / `wait_for_confirmation`
- 20d_outperformance_probability: `63.8%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.45`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `207.25`
- nearest_support: `215.33`
- nearest_resistance: `228.95`
- bounce_target_zone: `{"conservative": 224.87, "base": 224.87, "extended": 235.92, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 217.72, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `367.95`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.0%`
- secondary: `stock_trend_repair` / `18.6%`
- risk: `stock_downside_continuation` / `17.2%`
- stock_confluence_score: `51.67` / `mixed`
- stock_alpha_score_v1: `23.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `56.9%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `24.29`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `374.03`
- primary_invalidation_level: `315.52`
- risk_scenario_activation_level: `315.52`
- trend_repair_confirmation_level: `368.92`
- breakout_level: `374.03`
- breakdown_level: `315.52`
- nearest_support: `357.14`
- nearest_resistance: `368.92`
- bounce_target_zone: `{"conservative": 376.05, "base": 376.05, "extended": 379.73, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 361.47, "critical_warning": 315.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.27`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.7%`
- secondary: `stock_downside_continuation` / `21.8%`
- risk: `stock_event_risk` / `14.0%`
- stock_confluence_score: `35.03` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.9%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.49`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.92`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.53`
- nearest_support: `8.74`
- nearest_resistance: `10.07`
- bounce_target_zone: `{"conservative": 9.67, "base": 9.67, "extended": 10.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.97, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `274.77`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `20.1%`
- risk: `stock_event_risk` / `11.5%`
- stock_confluence_score: `43.56` / `weak`
- stock_alpha_score_v1: `35.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.3%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.5`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.69`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `268.49`
- nearest_resistance: `284.19`
- bounce_target_zone: `{"conservative": 279.48, "base": 279.48, "extended": 293.28, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 271.24, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
