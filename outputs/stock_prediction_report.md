# Stock Prediction Report

Generated at: `2026-10-23T08:52:56.035263+00:00`
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
- current_price: `212.21`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `43.54` / `weak`
- stock_alpha_score_v1: `40.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `53.5%`
- 60d_expected_return: `-0.9%`
- risk_reward_ratio: `0.51`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `27.2`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `243.37`
- primary_invalidation_level: `208.21`
- risk_scenario_activation_level: `205.44`
- trend_repair_confirmation_level: `243.37`
- breakout_level: `243.37`
- breakdown_level: `205.44`
- nearest_support: `211.26`
- nearest_resistance: `219.60`
- bounce_target_zone: `{"conservative": 215.9, "base": 215.9, "extended": 248.29, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 209.44, "critical_warning": 208.21, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `374.58`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.6%`
- secondary: `stock_downside_continuation` / `18.2%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `38.19` / `weak`
- stock_alpha_score_v1: `5.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.2%`
- 60d_expected_return: `-0.6%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Relative Strength Alert` / `NO_ALERT` / `29.23`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `388.86`
- primary_invalidation_level: `345.88`
- risk_scenario_activation_level: `345.88`
- trend_repair_confirmation_level: `388.86`
- breakout_level: `388.86`
- breakdown_level: `345.88`
- nearest_support: `364.95`
- nearest_resistance: `388.86`
- bounce_target_zone: `{"conservative": 381.8, "base": 381.8, "extended": 398.49, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 369.17, "critical_warning": 345.88, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `5.38`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `35.9%`
- secondary: `stock_failed_bounce` / `21.6%`
- risk: `stock_event_risk` / `12.7%`
- stock_confluence_score: `40.86` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `10.2%`
- 60d_expected_return: `-5.0%`
- risk_reward_ratio: `0.28`
- strongest_alert: `Stock Breakdown Warning` / `EXTREME` / `85.18`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `8.68`
- primary_invalidation_level: `5.07`
- risk_scenario_activation_level: `4.86`
- trend_repair_confirmation_level: `8.68`
- breakout_level: `8.68`
- breakdown_level: `4.86`
- nearest_support: `5.23`
- nearest_resistance: `5.95`
- bounce_target_zone: `{"conservative": 5.66, "base": 5.66, "extended": 9.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 5.17, "critical_warning": 5.07, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `255.21`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.6%`
- secondary: `stock_downside_continuation` / `22.3%`
- risk: `stock_event_risk` / `14.5%`
- stock_confluence_score: `30.07` / `weak`
- stock_alpha_score_v1: `21.0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `44.8%`
- 60d_expected_return: `-2.4%`
- risk_reward_ratio: `0.47`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `30.76`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `309.80`
- primary_invalidation_level: `244.70`
- risk_scenario_activation_level: `237.43`
- trend_repair_confirmation_level: `309.80`
- breakout_level: `309.80`
- breakdown_level: `237.43`
- nearest_support: `247.20`
- nearest_resistance: `274.61`
- bounce_target_zone: `{"conservative": 264.91, "base": 264.91, "extended": 322.73, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 247.94, "critical_warning": 244.7, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
