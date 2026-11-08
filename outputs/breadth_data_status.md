# Breadth Data Status

Generated at: 2026-11-08T17:57:58.681121+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 60.38
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 58.0
- equal_weight_vs_cap_weight_20d: 0.069718
- small_cap_vs_large_cap_20d: 0.036696

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-06
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6103 / 0.6215 / 0.566
- advancers / decliners / A-D ratio: 192 / 310 / 0.6194
- new highs/lows 20d: 46 / 58
- new highs/lows 52w: 10 / 4
- improvement / deterioration / confirmation / conflict / quality: 53.67 / 65.15 / 61.43 / 49.51 / 100.0
- internal_resonance: mixed / score 58.07 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: weak / score 25.46 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-06
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7 / 0.7333 / 0.6667
- advancers / decliners / A-D ratio: 15 / 15 / 1.0
- new highs/lows 20d: 7 / 4
- new highs/lows 52w: 2 / 0
- improvement / deterioration / confirmation / conflict / quality: 74.55 / 43.62 / 78.19 / 33.15 / 100.0
- internal_resonance: mixed / score 68.28 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-06
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
- improvement / deterioration / confirmation / conflict / quality: 70.33 / 40.04 / 68.75 / 39.03 / 64
- internal_resonance: mixed / score 54.8 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
