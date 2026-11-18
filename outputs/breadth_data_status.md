# Breadth Data Status

Generated at: 2026-11-18T08:36:54.908581+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 53.81
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 26.0
- equal_weight_vs_cap_weight_20d: 0.047141
- small_cap_vs_large_cap_20d: 0.023201

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-16
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5686 / 0.6534 / 0.604
- advancers / decliners / A-D ratio: 158 / 342 / 0.462
- new highs/lows 20d: 54 / 27
- new highs/lows 52w: 28 / 7
- improvement / deterioration / confirmation / conflict / quality: 50.1 / 69.41 / 58.52 / 52.75 / 100.0
- internal_resonance: mixed / score 53.05 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: weak / score 21.08 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-16
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5667 / 0.7667 / 0.6333
- advancers / decliners / A-D ratio: 10 / 20 / 0.5
- new highs/lows 20d: 3 / 1
- new highs/lows 52w: 3 / 1
- improvement / deterioration / confirmation / conflict / quality: 72.08 / 47.74 / 76.08 / 36.28 / 100.0
- internal_resonance: mixed / score 61.42 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-17
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
- improvement / deterioration / confirmation / conflict / quality: 56.33 / 46.82 / 58.25 / 44.12 / 64
- internal_resonance: weak / score 46.97 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
