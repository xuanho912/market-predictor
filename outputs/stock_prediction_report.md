# Stock Prediction Report

Generated at: `2026-06-16T00:16:24.050186+00:00`
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
- current_price: `28.68`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `27.9%`
- secondary: `stock_failed_bounce` / `24.0%`
- risk: `stock_downside_continuation` / `27.9%`
- stock_confluence_score: `15.28` / `weak`
- strongest_alert: `Relative Weakness Alert` / `HIGH_CONVICTION` / `77.47`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `32.83`
- primary_invalidation_level: `27.48`
- risk_scenario_activation_level: `27.48`
- trend_repair_confirmation_level: `32.83`
- breakout_level: `32.83`
- breakdown_level: `27.48`
- nearest_support: `28.06`
- nearest_resistance: `29.62`
- bounce_target_zone: `{"conservative": 29.15, "base": 29.15, "extended": 33.45, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.31, "critical_warning": 27.48, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### KC

- company_name: `Kingsoft Cloud Holdings Ltd`
- status: `available`
- current_price: `11.34`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `34.1%`
- secondary: `stock_failed_bounce` / `18.1%`
- risk: `stock_downside_continuation` / `34.1%`
- stock_confluence_score: `25.67` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WARNING` / `61.5`
- historical_analog_support: `weak` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `15.25`
- primary_invalidation_level: `10.47`
- risk_scenario_activation_level: `10.47`
- trend_repair_confirmation_level: `15.25`
- breakout_level: `15.25`
- breakdown_level: `10.47`
- nearest_support: `10.80`
- nearest_resistance: `12.15`
- bounce_target_zone: `{"conservative": 11.74, "base": 11.74, "extended": 15.79, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 11.02, "critical_warning": 10.47, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### NVDA

- company_name: `NVIDIA Corp`
- status: `available`
- current_price: `212.45`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.6%`
- secondary: `stock_downside_continuation` / `25.1%`
- risk: `stock_failed_bounce` / `25.6%`
- stock_confluence_score: `21.65` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `40.03`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `232.28`
- primary_invalidation_level: `199.34`
- risk_scenario_activation_level: `199.34`
- trend_repair_confirmation_level: `232.28`
- breakout_level: `232.28`
- breakdown_level: `199.34`
- nearest_support: `205.71`
- nearest_resistance: `222.57`
- bounce_target_zone: `{"conservative": 217.51, "base": 217.51, "extended": 239.02, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 208.66, "critical_warning": 199.34, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### TSLA

- company_name: `Tesla Inc`
- status: `available`
- current_price: `411.15`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.5%`
- secondary: `stock_downside_continuation` / `23.1%`
- risk: `stock_failed_bounce` / `25.5%`
- stock_confluence_score: `18.68` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WATCH` / `46.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `445.60`
- primary_invalidation_level: `380.15`
- risk_scenario_activation_level: `380.15`
- trend_repair_confirmation_level: `445.60`
- breakout_level: `445.60`
- breakdown_level: `380.15`
- nearest_support: `396.91`
- nearest_resistance: `432.51`
- bounce_target_zone: `{"conservative": 421.83, "base": 421.83, "extended": 459.84, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 403.14, "critical_warning": 380.15, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AMD

- company_name: `Advanced Micro Devices Inc`
- status: `available`
- current_price: `547.26`
- market_context: `risk_off_pressure`
- primary: `stock_trend_repair` / `27.4%`
- secondary: `stock_failed_bounce` / `20.4%`
- risk: `stock_failed_bounce` / `20.4%`
- stock_confluence_score: `46.57` / `mixed`
- strongest_alert: `Relative Strength Alert` / `WARNING` / `67.5`
- historical_analog_support: `supportive` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `563.27`
- primary_invalidation_level: `393.36`
- risk_scenario_activation_level: `393.36`
- trend_repair_confirmation_level: `589.95`
- breakout_level: `563.27`
- breakdown_level: `393.36`
- nearest_support: `518.79`
- nearest_resistance: `558.37`
- bounce_target_zone: `{"conservative": 568.61, "base": 589.95, "extended": 589.95, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 531.25, "critical_warning": 393.36, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### AAPL

- company_name: `Apple Inc`
- status: `available`
- current_price: `296.42`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `26.6%`
- secondary: `stock_downside_continuation` / `22.4%`
- risk: `stock_failed_bounce` / `26.6%`
- stock_confluence_score: `19.57` / `weak`
- strongest_alert: `Stock Failed Bounce Risk` / `NO_ALERT` / `31.3`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `317.40`
- primary_invalidation_level: `287.38`
- risk_scenario_activation_level: `287.38`
- trend_repair_confirmation_level: `317.40`
- breakout_level: `317.40`
- breakdown_level: `287.38`
- nearest_support: `290.20`
- nearest_resistance: `305.74`
- bounce_target_zone: `{"conservative": 301.08, "base": 301.08, "extended": 323.62, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 292.92, "critical_warning": 287.38, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### MSFT

- company_name: `Microsoft Corp`
- status: `available`
- current_price: `399.76`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `25.9%`
- secondary: `stock_downside_continuation` / `24.6%`
- risk: `stock_failed_bounce` / `25.9%`
- stock_confluence_score: `14.89` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `62.06`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `466.32`
- primary_invalidation_level: `382.27`
- risk_scenario_activation_level: `382.27`
- trend_repair_confirmation_level: `466.32`
- breakout_level: `466.32`
- breakdown_level: `382.27`
- nearest_support: `388.99`
- nearest_resistance: `415.91`
- bounce_target_zone: `{"conservative": 407.84, "base": 407.84, "extended": 477.09, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 393.7, "critical_warning": 382.27, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### META

- company_name: `Meta Platforms Inc`
- status: `available`
- current_price: `593.48`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `25.3%`
- secondary: `stock_failed_bounce` / `25.2%`
- risk: `stock_downside_continuation` / `25.3%`
- stock_confluence_score: `19.07` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `63.78`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `643.00`
- primary_invalidation_level: `557.01`
- risk_scenario_activation_level: `557.01`
- trend_repair_confirmation_level: `643.00`
- breakout_level: `643.00`
- breakdown_level: `557.01`
- nearest_support: `575.65`
- nearest_resistance: `620.22`
- bounce_target_zone: `{"conservative": 606.85, "base": 606.85, "extended": 660.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 582.77, "critical_warning": 557.01, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### BABA

- company_name: `Alibaba Group Holding Ltd`
- status: `available`
- current_price: `112.55`
- market_context: `risk_off_pressure`
- primary: `stock_downside_continuation` / `28.6%`
- secondary: `stock_failed_bounce` / `23.3%`
- risk: `stock_downside_continuation` / `28.6%`
- stock_confluence_score: `16.34` / `weak`
- strongest_alert: `Stock Breakdown Warning` / `WATCH` / `41.51`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `136.78`
- primary_invalidation_level: `109.66`
- risk_scenario_activation_level: `108.36`
- trend_repair_confirmation_level: `136.78`
- breakout_level: `136.78`
- breakdown_level: `108.36`
- nearest_support: `109.66`
- nearest_resistance: `117.12`
- bounce_target_zone: `{"conservative": 114.84, "base": 114.84, "extended": 139.83, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 110.72, "critical_warning": 108.54, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### PLTR

- company_name: `Palantir Technologies Inc`
- status: `available`
- current_price: `134.71`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `24.2%`
- secondary: `stock_downside_continuation` / `21.2%`
- risk: `stock_failed_bounce` / `24.2%`
- stock_confluence_score: `17.38` / `weak`
- strongest_alert: `Relative Weakness Alert` / `WARNING` / `68.75`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `163.70`
- primary_invalidation_level: `126.65`
- risk_scenario_activation_level: `126.24`
- trend_repair_confirmation_level: `163.70`
- breakout_level: `163.70`
- breakdown_level: `126.24`
- nearest_support: `128.55`
- nearest_resistance: `143.95`
- bounce_target_zone: `{"conservative": 139.33, "base": 139.33, "extended": 169.86, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 131.24, "critical_warning": 126.65, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`

### SMCI

- company_name: `Super Micro Computer Inc`
- status: `available`
- current_price: `30.85`
- market_context: `risk_off_pressure`
- primary: `stock_failed_bounce` / `32.6%`
- secondary: `stock_downside_continuation` / `17.8%`
- risk: `stock_failed_bounce` / `32.6%`
- stock_confluence_score: `23.35` / `weak`
- strongest_alert: `Liquidity / Gap Risk Alert` / `HIGH_CONVICTION` / `74.09`
- historical_analog_support: `conflicting` / samples `10`
- validation_status: `not_yet_validated`

- primary_confirmation_level: `51.40`
- primary_invalidation_level: `27.88`
- risk_scenario_activation_level: `25.82`
- trend_repair_confirmation_level: `51.40`
- breakout_level: `51.40`
- breakdown_level: `25.82`
- nearest_support: `28.61`
- nearest_resistance: `36.34`
- bounce_target_zone: `{"conservative": 33.6, "base": 33.6, "extended": 55.06, "source": "scenario_path + atr + recent_resistance", "meaning": "概率反抽情景参考区间，不是目标价承诺。", "not_trading_instruction": true}`
- failed_bounce_warning_zone: `{"first_warning": 28.79, "critical_warning": 26.73, "source": "risk_path + atr + recent_support", "meaning": "跌入该区间说明失败反抽风险上升。", "not_trading_instruction": true}`
