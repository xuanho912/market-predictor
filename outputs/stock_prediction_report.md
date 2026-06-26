# Stock Prediction Report

Generated at: `2026-06-26T05:41:15.592429+00:00`
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
- current_price: `195.74`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.8%`
- secondary: `stock_downside_continuation` / `25.6%`
- risk: `stock_event_risk` / `13.0%`
- stock_confluence_score: `35.87` / `weak`
- stock_alpha_score_v1: `34.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.9%`
- 60d_expected_return: `-1.6%`
- risk_reward_ratio: `0.4`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `32.22`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `190.91`
- risk_scenario_activation_level: `187.57`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `187.57`
- nearest_support: `192.13`
- nearest_resistance: `204.66`
- bounce_target_zone: `{"conservative": 200.2, "base": 200.2, "extended": 238.22, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 192.4, "critical_warning": 190.91, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `375.12`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.6%`
- secondary: `stock_failed_bounce` / `25.8%`
- risk: `stock_event_risk` / `13.2%`
- stock_confluence_score: `27.73` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.6%`
- 60d_expected_return: `-2.3%`
- risk_reward_ratio: `0.46`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `70.24`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `443.96`
- primary_invalidation_level: `362.80`
- risk_scenario_activation_level: `354.28`
- trend_repair_confirmation_level: `443.96`
- breakout_level: `443.96`
- breakdown_level: `354.28`
- nearest_support: `371.22`
- nearest_resistance: `397.86`
- bounce_target_zone: `{"conservative": 386.49, "base": 386.49, "extended": 459.12, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.59, "critical_warning": 362.8, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.07`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.9%`
- secondary: `stock_failed_bounce` / `20.3%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `27.71` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `22.4%`
- 60d_expected_return: `-3.5%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Liquidity / Gap Risk Alert` / `WATCH` / `44.17`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `14.30`
- primary_invalidation_level: `9.12`
- risk_scenario_activation_level: `8.91`
- trend_repair_confirmation_level: `14.30`
- breakout_level: `14.30`
- breakdown_level: `8.91`
- nearest_support: `9.22`
- nearest_resistance: `11.34`
- bounce_target_zone: `{"conservative": 10.7, "base": 10.7, "extended": 15.15, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 9.59, "critical_warning": 9.12, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### CEG

- company_name: `Constellation Energy Corp`
- status: `available`
- current_price: `268.69`
- market_context: `neutral`
- primary: `stock_downside_continuation` / `24.5%`
- secondary: `stock_bounce` / `20.0%`
- risk: `stock_failed_bounce` / `15.2%`
- stock_confluence_score: `32.94` / `weak`
- stock_alpha_score_v1: `27.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `45.2%`
- 60d_expected_return: `-0.2%`
- risk_reward_ratio: `0.55`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `51.49`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `290.90`
- primary_invalidation_level: `240.51`
- risk_scenario_activation_level: `240.51`
- trend_repair_confirmation_level: `290.90`
- breakout_level: `290.90`
- breakdown_level: `240.51`
- nearest_support: `261.29`
- nearest_resistance: `279.78`
- bounce_target_zone: `{"conservative": 274.24, "base": 274.24, "extended": 298.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 264.53, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
