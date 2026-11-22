# Breadth Data Status

Generated at: 2026-11-22T19:43:43.087352+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 36.71
- resonance_state: weak
- label: no_internal_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 6.0
- equal_weight_vs_cap_weight_20d: 0.050295
- small_cap_vs_large_cap_20d: 0.022909

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-20
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2048 / 0.4323 / 0.464
- advancers / decliners / A-D ratio: 127 / 373 / 0.3405
- new highs/lows 20d: 2 / 190
- new highs/lows 52w: 0 / 23
- improvement / deterioration / confirmation / conflict / quality: 24.33 / 100.0 / 37.52 / 76.0 / 100.0
- internal_resonance: weak / score 32.55 / SPY 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### QQQ

- status: missing
- source: wikipedia-nasdaq100
- latest_date: None
- true_breadth: False
- proxy: False
- constituents used / expected: 0 / 6
- coverage_ratio: 0.0
- stale_constituents: False
- stale_price_data: True
- percent_above_20d / 50d / 200d: None / None / None
- advancers / decliners / A-D ratio: 0 / 0 / 0.0
- new highs/lows 20d: 0 / 0
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 8.67 / 70.67 / 9.39 / 69.07 / 4.0
- internal_resonance: weak / score 19.01 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-20
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2667 / 0.4667 / 0.5667
- advancers / decliners / A-D ratio: 12 / 18 / 0.6667
- new highs/lows 20d: 0 / 11
- new highs/lows 52w: 0 / 3
- improvement / deterioration / confirmation / conflict / quality: 30.22 / 100.0 / 41.76 / 76.0 / 100.0
- internal_resonance: weak / score 35.66 / DIA 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-20
- true_breadth: False
- proxy: True
- constituents used / expected: None / None
- coverage_ratio: None
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: None / None / None
- advancers / decliners / A-D ratio: None / None / None
- new highs/lows 20d: None / None
- new highs/lows 52w: None / None
- improvement / deterioration / confirmation / conflict / quality: 48.22 / 58.19 / 52.16 / 52.64 / 64
- internal_resonance: weak / score 41.91 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
