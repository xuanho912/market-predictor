# Stock Prediction Report

Generated at: `2026-06-15T14:29:14.990584+00:00`
Model version: `stock_baseline_v1`

This module extends the dashboard to watchlist stocks. It is not a trading system and does not produce execution instructions.

## Summary

- supported_symbols: `11`
- watchlist_size: `11`
- strongest_stock_symbol: `KC`
- stock_data_quality_score: `100.0`
- validation_status: `not_yet_validated`
- missing_high_value_data: `['fundamentals', 'earnings', 'company_news', 'single_stock_options']`

## Symbols

### JD

- company_name: `JD.com Inc`
- status: `available`
- current_price: `28.78`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `24.1%`
- risk: `stock_downside_continuation` / `27.8%`
- stock_confluence_score: `14.44` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `74.02`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `32.83`
- primary_invalidation_level: `27.48`
- risk_scenario_activation_level: `27.48`
- trend_repair_confirmation_level: `32.83`
- breakout_level: `32.83`
- breakdown_level: `27.48`
- nearest_support: `28.16`
- nearest_resistance: `29.72`
- bounce_target_zone: `{"conservative": 29.25, "base": 29.25, "extended": 33.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.41, "critical_warning": 27.48, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### KC

- company_name: `Kingsoft Cloud Holdings Ltd`
- status: `available`
- current_price: `11.27`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.2%`
- secondary: `stock_failed_bounce` / `18.3%`
- risk: `stock_downside_continuation` / `34.2%`
- stock_confluence_score: `21.86` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `62.45`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `15.25`
- primary_invalidation_level: `10.47`
- risk_scenario_activation_level: `10.47`
- trend_repair_confirmation_level: `15.25`
- breakout_level: `15.25`
- breakdown_level: `10.47`
- nearest_support: `10.73`
- nearest_resistance: `12.07`
- bounce_target_zone: `{"conservative": 11.67, "base": 11.67, "extended": 15.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.94, "critical_warning": 10.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `209.16`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.5%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_downside_continuation` / `25.5%`
- stock_confluence_score: `17.81` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.85`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `202.51`
- nearest_resistance: `219.13`
- bounce_target_zone: `{"conservative": 214.14, "base": 214.14, "extended": 238.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.17, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `411.62`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `23.1%`
- risk: `stock_failed_bounce` / `25.5%`
- stock_confluence_score: `15.13` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `44.26`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `397.38`
- nearest_resistance: `432.98`
- bounce_target_zone: `{"conservative": 422.3, "base": 422.3, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 403.61, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AMD

- company_name: `Advanced Micro Devices Inc`
- status: `available`
- current_price: `551.03`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `27.6%`
- secondary: `stock_failed_bounce` / `20.4%`
- risk: `stock_failed_bounce` / `20.4%`
- stock_confluence_score: `42.66` / `weak`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `567.04`
- primary_invalidation_level: `393.36`
- risk_scenario_activation_level: `393.36`
- trend_repair_confirmation_level: `593.74`
- breakout_level: `567.04`
- breakdown_level: `393.36`
- nearest_support: `522.56`
- nearest_resistance: `558.37`
- bounce_target_zone: `{"conservative": 572.38, "base": 593.74, "extended": 593.74, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 535.01, "critical_warning": 393.36, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AAPL

- company_name: `Apple Inc`
- status: `available`
- current_price: `295.69`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `22.5%`
- risk: `stock_failed_bounce` / `26.7%`
- stock_confluence_score: `16.5` / `weak`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.87`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `317.40`
- primary_invalidation_level: `287.38`
- risk_scenario_activation_level: `287.26`
- trend_repair_confirmation_level: `317.40`
- breakout_level: `317.40`
- breakdown_level: `287.26`
- nearest_support: `289.56`
- nearest_resistance: `304.89`
- bounce_target_zone: `{"conservative": 300.29, "base": 300.29, "extended": 323.53, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 292.24, "critical_warning": 287.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### MSFT

- company_name: `Microsoft Corp`
- status: `available`
- current_price: `397.97`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `24.8%`
- risk: `stock_failed_bounce` / `25.9%`
- stock_confluence_score: `12.82` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `61.9`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `466.32`
- primary_invalidation_level: `382.27`
- risk_scenario_activation_level: `382.27`
- trend_repair_confirmation_level: `466.32`
- breakout_level: `466.32`
- breakdown_level: `382.27`
- nearest_support: `387.32`
- nearest_resistance: `413.94`
- bounce_target_zone: `{"conservative": 405.96, "base": 405.96, "extended": 476.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 391.98, "critical_warning": 382.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### META

- company_name: `Meta Platforms Inc`
- status: `available`
- current_price: `590.91`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.6%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_downside_continuation` / `25.6%`
- stock_confluence_score: `16.75` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `63.55`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `643.00`
- primary_invalidation_level: `557.01`
- risk_scenario_activation_level: `557.01`
- trend_repair_confirmation_level: `643.00`
- breakout_level: `643.00`
- breakdown_level: `557.01`
- nearest_support: `573.51`
- nearest_resistance: `617.01`
- bounce_target_zone: `{"conservative": 603.96, "base": 603.96, "extended": 660.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 580.47, "critical_warning": 557.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### BABA

- company_name: `Alibaba Group Holding Ltd`
- status: `available`
- current_price: `113.18`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.5%`
- secondary: `stock_failed_bounce` / `23.2%`
- risk: `stock_downside_continuation` / `28.5%`
- stock_confluence_score: `14.73` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.55`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `136.78`
- primary_invalidation_level: `109.66`
- risk_scenario_activation_level: `109.00`
- trend_repair_confirmation_level: `136.78`
- breakout_level: `136.78`
- breakdown_level: `109.00`
- nearest_support: `110.14`
- nearest_resistance: `117.75`
- bounce_target_zone: `{"conservative": 115.47, "base": 115.47, "extended": 139.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 111.36, "critical_warning": 109.19, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### PLTR

- company_name: `Palantir Technologies Inc`
- status: `available`
- current_price: `132.21`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.7%`
- secondary: `stock_downside_continuation` / `22.1%`
- risk: `stock_failed_bounce` / `24.7%`
- stock_confluence_score: `13.87` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `74.4`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `163.70`
- primary_invalidation_level: `126.65`
- risk_scenario_activation_level: `123.94`
- trend_repair_confirmation_level: `163.70`
- breakout_level: `163.70`
- breakdown_level: `123.94`
- nearest_support: `126.65`
- nearest_resistance: `141.23`
- bounce_target_zone: `{"conservative": 136.72, "base": 136.72, "extended": 169.71, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 128.83, "critical_warning": 125.44, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMCI

- company_name: `Super Micro Computer Inc`
- status: `available`
- current_price: `31.36`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `32.5%`
- secondary: `stock_downside_continuation` / `17.3%`
- risk: `stock_failed_bounce` / `32.5%`
- stock_confluence_score: `25.38` / `weak`
- strongest_alert: `Liquidity / Gap Risk Alert` / `HIGH_CONVICTION` / `72.65`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `51.40`
- primary_invalidation_level: `28.39`
- risk_scenario_activation_level: `26.33`
- trend_repair_confirmation_level: `51.40`
- breakout_level: `51.40`
- breakdown_level: `26.33`
- nearest_support: `28.61`
- nearest_resistance: `36.85`
- bounce_target_zone: `{"conservative": 34.11, "base": 34.11, "extended": 55.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 29.3, "critical_warning": 27.24, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
