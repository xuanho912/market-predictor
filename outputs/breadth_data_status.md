# Breadth Data Status

Generated at: 2026-11-26T02:58:21.260122+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 65.49
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: SPY, DIA
- surface_only_symbols: none
- sector_score: 42.0
- equal_weight_vs_cap_weight_20d: 0.064232
- small_cap_vs_large_cap_20d: 0.027851

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-25
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4533 / 0.5876 / 0.546
- advancers / decliners / A-D ratio: 392 / 108 / 3.6296
- new highs/lows 20d: 61 / 10
- new highs/lows 52w: 25 / 2
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 48.76 / 96.1 / 37.06 / 100.0
- internal_resonance: aligned / score 71.48 / SPY 内部共振：成分股 20d 上方比例 45%，行业参与 30%，confirmation 96 高于 conflict 37。

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
- internal_resonance: weak / score 23.38 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-25
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5 / 0.5667 / 0.5333
- advancers / decliners / A-D ratio: 24 / 6 / 4.0
- new highs/lows 20d: 4 / 0
- new highs/lows 52w: 2 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 59.2 / 95.26 / 44.99 / 100.0
- internal_resonance: aligned / score 73.63 / DIA 内部共振：成分股 20d 上方比例 50%，行业参与 30%，confirmation 95 高于 conflict 45。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-25
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
- improvement / deterioration / confirmation / conflict / quality: 70.15 / 49.9 / 68.61 / 46.42 / 64
- internal_resonance: mixed / score 51.35 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
