# Breadth Data Status

Generated at: 2026-07-14T05:57:38.950267+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 72.53
Stale data: False

## Market Internal Resonance

- resonance_score: 53.07
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 52.0
- equal_weight_vs_cap_weight_20d: 0.005893
- small_cap_vs_large_cap_20d: -0.004894

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-13
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6195 / 0.6607 / 0.662
- advancers / decliners / A-D ratio: 284 / 219 / 1.2968
- new highs/lows 20d: 74 / 17
- new highs/lows 52w: 20 / 1
- improvement / deterioration / confirmation / conflict / quality: 60.3 / 51.07 / 67.33 / 38.81 / 100.0
- internal_resonance: mixed / score 60.16 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### QQQ

- status: missing
- source: wikipedia-nasdaq100
- latest_date: 2026-07-09
- true_breadth: False
- proxy: False
- constituents used / expected: 1 / 19
- coverage_ratio: 0.0526
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.0 / 0.0 / 0.0
- advancers / decliners / A-D ratio: 1 / 0 / 1.0
- new highs/lows 20d: 0 / 0
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 70.67 / 79.57 / 65.53 / 26.11
- internal_resonance: weak / score 30.77 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-13
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6 / 0.6333 / 0.6
- advancers / decliners / A-D ratio: 16 / 14 / 1.1429
- new highs/lows 20d: 3 / 0
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 59.75 / 80.73 / 64.56 / 61.35 / 100.0
- internal_resonance: mixed / score 54.49 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-13
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
- improvement / deterioration / confirmation / conflict / quality: 44.81 / 49.31 / 49.61 / 45.99 / 64
- internal_resonance: weak / score 44.56 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
