# Stock Prediction Report

Generated at: `2026-09-02T16:38:26.710956+00:00`
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
- current_price: `227.13`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.8%`
- secondary: `stock_downside_continuation` / `18.6%`
- risk: `stock_event_risk` / `14.9%`
- stock_confluence_score: `51.74` / `mixed`
- stock_alpha_score_v1: `53.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `63.2%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.54`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `25.85`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `207.25`
- risk_scenario_activation_level: `207.25`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `207.25`
- nearest_support: `221.39`
- nearest_resistance: `230.47`
- bounce_target_zone: `{"conservative": 231.43, "base": 231.43, "extended": 236.21, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 223.9, "critical_warning": 207.25, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `352.70`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.2%`
- secondary: `stock_downside_continuation` / `18.8%`
- risk: `stock_event_risk` / `15.1%`
- stock_confluence_score: `42.61` / `weak`
- stock_alpha_score_v1: `2.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `47.7%`
- 60d_expected_return: `-0.8%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.28`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `368.92`
- primary_invalidation_level: `315.52`
- risk_scenario_activation_level: `315.52`
- trend_repair_confirmation_level: `368.92`
- breakout_level: `368.92`
- breakdown_level: `315.52`
- nearest_support: `342.04`
- nearest_resistance: `368.69`
- bounce_target_zone: `{"conservative": 360.69, "base": 360.69, "extended": 379.58, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 346.7, "critical_warning": 315.52, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.24`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `13.6%`
- stock_confluence_score: `30.08` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `42.1%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `35.58`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.53`
- risk_scenario_activation_level: `8.53`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.53`
- nearest_support: `8.73`
- nearest_resistance: `10.01`
- bounce_target_zone: `{"conservative": 9.63, "base": 9.63, "extended": 10.77, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.96, "critical_warning": 8.53, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `282.30`
- market_context: `market_headwind`
- primary: `stock_failed_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `19.8%`
- risk: `stock_event_risk` / `11.6%`
- stock_confluence_score: `43.4` / `weak`
- stock_alpha_score_v1: `45.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `61.0%`
- 60d_expected_return: `-0.5%`
- risk_reward_ratio: `0.59`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `29.61`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `275.31`
- nearest_resistance: `287.00`
- bounce_target_zone: `{"conservative": 287.53, "base": 287.53, "extended": 293.99, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 278.37, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
