# Breadth Data Status

Generated at: 2026-09-01T22:41:35.610783+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 45.62
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 20.0
- equal_weight_vs_cap_weight_20d: 0.014592
- small_cap_vs_large_cap_20d: -0.006692

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-31
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4235 / 0.5288 / 0.6846
- advancers / decliners / A-D ratio: 228 / 274 / 0.8321
- new highs/lows 20d: 32 / 71
- new highs/lows 52w: 6 / 2
- improvement / deterioration / confirmation / conflict / quality: 53.35 / 85.53 / 59.57 / 65.0 / 100.0
- internal_resonance: weak / score 44.7 / SPY 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

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
- internal_resonance: weak / score 17.88 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-28
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4 / 0.5667 / 0.7
- advancers / decliners / A-D ratio: 17 / 13 / 1.3077
- new highs/lows 20d: 3 / 4
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 72.6 / 68.09 / 74.83 / 51.75 / 100.0
- internal_resonance: mixed / score 52.01 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-01
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
- improvement / deterioration / confirmation / conflict / quality: 44.08 / 57.45 / 49.06 / 52.08 / 64
- internal_resonance: weak / score 40.14 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
