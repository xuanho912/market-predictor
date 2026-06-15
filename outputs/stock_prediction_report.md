# Stock Prediction Report

Generated at: `2026-06-15T14:41:21.102314+00:00`
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
- current_price: `28.77`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.8%`
- secondary: `stock_failed_bounce` / `24.1%`
- risk: `stock_downside_continuation` / `27.8%`
- stock_confluence_score: `14.47` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `73.7`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `32.83`
- primary_invalidation_level: `27.48`
- risk_scenario_activation_level: `27.48`
- trend_repair_confirmation_level: `32.83`
- breakout_level: `32.83`
- breakdown_level: `27.48`
- nearest_support: `28.15`
- nearest_resistance: `29.71`
- bounce_target_zone: `{"conservative": 29.24, "base": 29.24, "extended": 33.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.4, "critical_warning": 27.48, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### KC

- company_name: `Kingsoft Cloud Holdings Ltd`
- status: `available`
- current_price: `11.26`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.2%`
- secondary: `stock_failed_bounce` / `18.3%`
- risk: `stock_downside_continuation` / `34.2%`
- stock_confluence_score: `21.87` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `62.59`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `15.25`
- primary_invalidation_level: `10.47`
- risk_scenario_activation_level: `10.47`
- trend_repair_confirmation_level: `15.25`
- breakout_level: `15.25`
- breakdown_level: `10.47`
- nearest_support: `10.72`
- nearest_resistance: `12.06`
- bounce_target_zone: `{"conservative": 11.66, "base": 11.66, "extended": 15.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 10.93, "critical_warning": 10.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `209.49`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.5%`
- secondary: `stock_failed_bounce` / `25.3%`
- risk: `stock_downside_continuation` / `25.5%`
- stock_confluence_score: `18.11` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `43.7`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `202.84`
- nearest_resistance: `219.46`
- bounce_target_zone: `{"conservative": 214.47, "base": 214.47, "extended": 238.93, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 205.5, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `409.23`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.4%`
- secondary: `stock_downside_continuation` / `23.4%`
- risk: `stock_failed_bounce` / `25.4%`
- stock_confluence_score: `14.77` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `46.32`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `395.00`
- nearest_resistance: `430.59`
- bounce_target_zone: `{"conservative": 419.91, "base": 419.91, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 401.23, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AMD

- company_name: `Advanced Micro Devices Inc`
- status: `available`
- current_price: `546.63`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `27.4%`
- secondary: `stock_failed_bounce` / `20.4%`
- risk: `stock_failed_bounce` / `20.4%`
- stock_confluence_score: `42.83` / `weak`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `562.64`
- primary_invalidation_level: `393.36`
- risk_scenario_activation_level: `393.36`
- trend_repair_confirmation_level: `589.33`
- breakout_level: `562.64`
- breakdown_level: `393.36`
- nearest_support: `518.16`
- nearest_resistance: `558.37`
- bounce_target_zone: `{"conservative": 567.98, "base": 589.33, "extended": 589.33, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 530.62, "critical_warning": 393.36, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AAPL

- company_name: `Apple Inc`
- status: `available`
- current_price: `295.60`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.7%`
- secondary: `stock_downside_continuation` / `22.6%`
- risk: `stock_failed_bounce` / `26.7%`
- stock_confluence_score: `16.59` / `weak`
- strongest_alert: `Stock Failed Bounce Risk` / `WATCH` / `38.67`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `317.40`
- primary_invalidation_level: `287.38`
- risk_scenario_activation_level: `287.17`
- trend_repair_confirmation_level: `317.40`
- breakout_level: `317.40`
- breakdown_level: `287.17`
- nearest_support: `289.47`
- nearest_resistance: `304.80`
- bounce_target_zone: `{"conservative": 300.2, "base": 300.2, "extended": 323.53, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 292.15, "critical_warning": 287.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### MSFT

- company_name: `Microsoft Corp`
- status: `available`
- current_price: `397.89`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `24.8%`
- risk: `stock_failed_bounce` / `25.9%`
- stock_confluence_score: `12.9` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `61.52`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `466.32`
- primary_invalidation_level: `382.27`
- risk_scenario_activation_level: `382.27`
- trend_repair_confirmation_level: `466.32`
- breakout_level: `466.32`
- breakdown_level: `382.27`
- nearest_support: `387.24`
- nearest_resistance: `413.86`
- bounce_target_zone: `{"conservative": 405.88, "base": 405.88, "extended": 476.97, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 391.9, "critical_warning": 382.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### META

- company_name: `Meta Platforms Inc`
- status: `available`
- current_price: `593.10`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.3%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_downside_continuation` / `25.3%`
- stock_confluence_score: `17.21` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `61.54`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `643.00`
- primary_invalidation_level: `557.01`
- risk_scenario_activation_level: `557.01`
- trend_repair_confirmation_level: `643.00`
- breakout_level: `643.00`
- breakdown_level: `557.01`
- nearest_support: `575.70`
- nearest_resistance: `619.20`
- bounce_target_zone: `{"conservative": 606.15, "base": 606.15, "extended": 660.4, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 582.65, "critical_warning": 557.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### BABA

- company_name: `Alibaba Group Holding Ltd`
- status: `available`
- current_price: `113.03`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.5%`
- secondary: `stock_failed_bounce` / `23.3%`
- risk: `stock_downside_continuation` / `28.5%`
- stock_confluence_score: `14.74` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `40.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `136.78`
- primary_invalidation_level: `109.66`
- risk_scenario_activation_level: `108.84`
- trend_repair_confirmation_level: `136.78`
- breakout_level: `136.78`
- breakdown_level: `108.84`
- nearest_support: `109.99`
- nearest_resistance: `117.60`
- bounce_target_zone: `{"conservative": 115.31, "base": 115.31, "extended": 139.82, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 111.2, "critical_warning": 109.03, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### PLTR

- company_name: `Palantir Technologies Inc`
- status: `available`
- current_price: `133.31`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.5%`
- secondary: `stock_downside_continuation` / `21.6%`
- risk: `stock_failed_bounce` / `24.5%`
- stock_confluence_score: `13.17` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `70.56`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `163.70`
- primary_invalidation_level: `126.65`
- risk_scenario_activation_level: `124.96`
- trend_repair_confirmation_level: `163.70`
- breakout_level: `163.70`
- breakdown_level: `124.96`
- nearest_support: `127.24`
- nearest_resistance: `142.42`
- bounce_target_zone: `{"conservative": 137.87, "base": 137.87, "extended": 169.77, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 129.89, "critical_warning": 126.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMCI

- company_name: `Super Micro Computer Inc`
- status: `available`
- current_price: `31.32`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `32.5%`
- secondary: `stock_downside_continuation` / `17.3%`
- risk: `stock_failed_bounce` / `32.5%`
- stock_confluence_score: `25.41` / `weak`
- strongest_alert: `Liquidity / Gap Risk Alert` / `HIGH_CONVICTION` / `72.77`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `51.40`
- primary_invalidation_level: `28.35`
- risk_scenario_activation_level: `26.29`
- trend_repair_confirmation_level: `51.40`
- breakout_level: `51.40`
- breakdown_level: `26.29`
- nearest_support: `28.61`
- nearest_resistance: `36.81`
- bounce_target_zone: `{"conservative": 34.07, "base": 34.07, "extended": 55.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 29.26, "critical_warning": 27.2, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
