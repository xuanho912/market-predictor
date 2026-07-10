# Stock Prediction Report

Generated at: `2026-07-10T15:04:45.263515+00:00`
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
- current_price: `206.02`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `27.5%`
- secondary: `stock_downside_continuation` / `22.0%`
- risk: `stock_event_risk` / `14.2%`
- stock_confluence_score: `43.3` / `weak`
- stock_alpha_score_v1: `36.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `51.8%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.43`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `34.34`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `213.99`
- primary_invalidation_level: `189.80`
- risk_scenario_activation_level: `189.80`
- trend_repair_confirmation_level: `213.99`
- breakout_level: `213.99`
- breakdown_level: `189.80`
- nearest_support: `200.74`
- nearest_resistance: `213.94`
- bounce_target_zone: `{"conservative": 209.98, "base": 209.98, "extended": 219.27, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 203.05, "critical_warning": 189.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `406.64`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `18.7%`
- risk: `stock_event_risk` / `16.4%`
- stock_confluence_score: `40.6` / `weak`
- stock_alpha_score_v1: `7.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `43.2%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.52`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.07`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `432.86`
- primary_invalidation_level: `368.60`
- risk_scenario_activation_level: `368.60`
- trend_repair_confirmation_level: `432.86`
- breakout_level: `432.86`
- breakdown_level: `368.60`
- nearest_support: `390.53`
- nearest_resistance: `430.80`
- bounce_target_zone: `{"conservative": 418.72, "base": 418.72, "extended": 448.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 397.58, "critical_warning": 368.6, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `8.81`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `26.7%`
- secondary: `stock_failed_bounce` / `25.3%`
- risk: `stock_event_risk` / `11.9%`
- stock_confluence_score: `31.41` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `30.3%`
- 60d_expected_return: `-3.2%`
- risk_reward_ratio: `0.45`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `62.08`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `11.85`
- primary_invalidation_level: `8.33`
- risk_scenario_activation_level: `8.00`
- trend_repair_confirmation_level: `11.85`
- breakout_level: `11.85`
- breakdown_level: `8.00`
- nearest_support: `8.55`
- nearest_resistance: `9.69`
- bounce_target_zone: `{"conservative": 9.25, "base": 9.25, "extended": 12.44, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 8.48, "critical_warning": 8.33, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `251.54`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `25.0%`
- risk: `stock_event_risk` / `10.8%`
- stock_confluence_score: `34.63` / `weak`
- stock_alpha_score_v1: `26.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `48.8%`
- 60d_expected_return: `-1.2%`
- risk_reward_ratio: `0.32`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `32.94`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `282.77`
- primary_invalidation_level: `228.63`
- risk_scenario_activation_level: `228.63`
- trend_repair_confirmation_level: `282.77`
- breakout_level: `282.77`
- breakdown_level: `228.63`
- nearest_support: `244.27`
- nearest_resistance: `262.44`
- bounce_target_zone: `{"conservative": 256.99, "base": 256.99, "extended": 290.04, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 247.45, "critical_warning": 228.63, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
