# Breadth Data Status

Generated at: 2026-07-21T04:35:25.454997+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 49.9
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 36.0
- equal_weight_vs_cap_weight_20d: 0.017943
- small_cap_vs_large_cap_20d: -0.004869

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-17
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5805 / 0.6347 / 0.662
- advancers / decliners / A-D ratio: 147 / 356 / 0.4129
- new highs/lows 20d: 58 / 48
- new highs/lows 52w: 32 / 4
- improvement / deterioration / confirmation / conflict / quality: 50.9 / 50.91 / 60.58 / 38.69 / 100.0
- internal_resonance: mixed / score 54.56 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: weak / score 19.85 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-17
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6 / 0.5667 / 0.6333
- advancers / decliners / A-D ratio: 7 / 23 / 0.3043
- new highs/lows 20d: 3 / 1
- new highs/lows 52w: 2 / 0
- improvement / deterioration / confirmation / conflict / quality: 48.75 / 66.93 / 57.75 / 50.86 / 100.0
- internal_resonance: mixed / score 51.49 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-20
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
- improvement / deterioration / confirmation / conflict / quality: 50.53 / 54.72 / 53.9 / 50.04 / 64
- internal_resonance: weak / score 43.64 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
