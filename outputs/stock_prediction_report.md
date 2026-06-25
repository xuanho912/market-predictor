# Stock Prediction Report

Generated at: `2026-06-25T23:56:31.874162+00:00`
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
- market_context: `market_tailwind`
- primary: `stock_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_failed_bounce` / `16.9%`
- stock_confluence_score: `44.65` / `weak`
- stock_alpha_score_v1: `43.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `50.5%`
- 60d_expected_return: `-0.0%`
- risk_reward_ratio: `0.65`
- strongest_alert: `Relative Weakness Alert` / `NO_ALERT` / `31.81`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `190.91`
- risk_scenario_activation_level: `187.57`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `187.57`
- nearest_support: `192.13`
- nearest_resistance: `204.65`
- bounce_target_zone: `{"conservative": 200.8, "base": 205.04, "extended": 238.22, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 192.4, "critical_warning": 189.05, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `375.12`
- market_context: `market_tailwind`
- primary: `stock_bounce` / `25.1%`
- secondary: `stock_downside_continuation` / `23.4%`
- risk: `stock_failed_bounce` / `16.3%`
- stock_confluence_score: `35.77` / `weak`
- stock_alpha_score_v1: `0` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `27.6%`
- 60d_expected_return: `-0.3%`
- risk_reward_ratio: `0.75`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `70.24`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `443.96`
- primary_invalidation_level: `362.81`
- risk_scenario_activation_level: `354.28`
- trend_repair_confirmation_level: `443.96`
- breakout_level: `443.96`
- breakdown_level: `354.28`
- nearest_support: `371.22`
- nearest_resistance: `397.86`
- bounce_target_zone: `{"conservative": 388.0, "base": 398.8, "extended": 459.12, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 366.59, "critical_warning": 358.07, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMR

- company_name: `Nuscale Power Corp`
- status: `available`
- current_price: `10.07`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.9%`
- secondary: `stock_failed_bounce` / `20.3%`
- risk: `stock_event_risk` / `13.7%`
- stock_confluence_score: `27.53` / `weak`
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
- market_context: `market_tailwind`
- primary: `stock_bounce` / `25.0%`
- secondary: `stock_downside_continuation` / `22.9%`
- risk: `stock_failed_bounce` / `14.2%`
- stock_confluence_score: `36.91` / `weak`
- stock_alpha_score_v1: `29.5` / `weak_or_no_alpha_edge`
- 20d_outperformance_probability: `46.0%`
- 60d_expected_return: `0.1%`
- risk_reward_ratio: `0.62`
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
- bounce_target_zone: `{"conservative": 274.98, "base": 280.24, "extended": 298.3, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 264.53, "critical_warning": 240.51, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
