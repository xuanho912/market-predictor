# Stock Prediction Report

Generated at: `2026-08-29T04:11:17.837107+00:00`
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
- current_price: `217.55`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.3%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `48.41` / `mixed`
- stock_alpha_score_v1: `53.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `62.8%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.58`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.17`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `230.47`
- primary_invalidation_level: `196.85`
- risk_scenario_activation_level: `196.85`
- trend_repair_confirmation_level: `230.47`
- breakout_level: `230.47`
- breakdown_level: `196.85`
- nearest_support: `212.05`
- nearest_resistance: `225.80`
- bounce_target_zone: `{"conservative": 221.68, "base": 221.68, "extended": 235.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 214.46, "critical_warning": 196.85, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `348.75`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.1%`
- secondary: `stock_downside_continuation` / `19.1%`
- risk: `stock_event_risk` / `14.6%`
- stock_confluence_score: `35.75` / `weak`
- stock_alpha_score_v1: `5.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.58`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `366.50`
- primary_invalidation_level: `310.43`
- risk_scenario_activation_level: `310.43`
- trend_repair_confirmation_level: `366.50`
- breakout_level: `366.50`
- breakdown_level: `310.43`
- nearest_support: `338.81`
- nearest_resistance: `363.67`
- bounce_target_zone: `{"conservative": 356.21, "base": 356.21, "extended": 376.44, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 343.16, "critical_warning": 310.43, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `9.29`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `21.3%`
- risk: `stock_event_risk` / `13.9%`
- stock_confluence_score: `34.37` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.0%`
- 60d_expected_return: `-2.1%`
- risk_reward_ratio: `0.53`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.33`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `10.26`
- primary_invalidation_level: `8.29`
- risk_scenario_activation_level: `8.29`
- trend_repair_confirmation_level: `10.26`
- breakout_level: `10.26`
- breakdown_level: `8.29`
- nearest_support: `8.73`
- nearest_resistance: `10.13`
- bounce_target_zone: `{"conservative": 9.71, "base": 9.71, "extended": 10.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.97, "critical_warning": 8.29, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `276.75`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `20.3%`
- risk: `stock_event_risk` / `11.7%`
- stock_confluence_score: `38.66` / `weak`
- stock_alpha_score_v1: `37.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `54.7%`
- 60d_expected_return: `-0.7%`
- risk_reward_ratio: `0.56`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.52`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `287.00`
- primary_invalidation_level: `260.67`
- risk_scenario_activation_level: `260.67`
- trend_repair_confirmation_level: `287.00`
- breakout_level: `287.00`
- breakdown_level: `260.67`
- nearest_support: `270.21`
- nearest_resistance: `286.57`
- bounce_target_zone: `{"conservative": 281.66, "base": 281.66, "extended": 293.54, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 273.07, "critical_warning": 260.67, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
