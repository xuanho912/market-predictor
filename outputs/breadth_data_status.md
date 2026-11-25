# Breadth Data Status

Generated at: 2026-11-25T05:25:08.891518+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 40.19
- resonance_state: weak
- label: no_internal_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 20.0
- equal_weight_vs_cap_weight_20d: 0.049741
- small_cap_vs_large_cap_20d: 0.019566

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-23
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.1988 / 0.4343 / 0.462
- advancers / decliners / A-D ratio: 171 / 329 / 0.5198
- new highs/lows 20d: 4 / 174
- new highs/lows 52w: 0 / 20
- improvement / deterioration / confirmation / conflict / quality: 24.95 / 100.0 / 37.96 / 76.0 / 100.0
- internal_resonance: weak / score 34.27 / SPY 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

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
- internal_resonance: weak / score 20.4 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-23
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2333 / 0.5 / 0.5333
- advancers / decliners / A-D ratio: 19 / 11 / 1.7273
- new highs/lows 20d: 1 / 6
- new highs/lows 52w: 0 / 1
- improvement / deterioration / confirmation / conflict / quality: 34.92 / 100.0 / 45.14 / 76.0 / 100.0
- internal_resonance: weak / score 39.57 / DIA 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-24
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
- improvement / deterioration / confirmation / conflict / quality: 64.03 / 53.81 / 64.02 / 49.36 / 64
- internal_resonance: weak / score 46.74 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
