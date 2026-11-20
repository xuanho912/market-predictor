# Breadth Data Status

Generated at: 2026-11-20T03:57:58.804669+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 42.66
- resonance_state: weak
- label: no_internal_resonance
- aligned_symbols: none
- surface_only_symbols: none
- sector_score: 0.0
- equal_weight_vs_cap_weight_20d: 0.032749
- small_cap_vs_large_cap_20d: 0.017949

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-11-17
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5467 / 0.6394 / 0.592
- advancers / decliners / A-D ratio: 146 / 355 / 0.4113
- new highs/lows 20d: 52 / 40
- new highs/lows 52w: 27 / 9
- improvement / deterioration / confirmation / conflict / quality: 47.73 / 88.96 / 55.25 / 67.61 / 100.0
- internal_resonance: weak / score 45.03 / SPY 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

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
- internal_resonance: weak / score 17.38 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-11-17
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5333 / 0.6333 / 0.6333
- advancers / decliners / A-D ratio: 8 / 22 / 0.3636
- new highs/lows 20d: 2 / 5
- new highs/lows 52w: 2 / 2
- improvement / deterioration / confirmation / conflict / quality: 45.16 / 100.0 / 52.52 / 76.0 / 100.0
- internal_resonance: weak / score 41.9 / DIA 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-11-19
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
- improvement / deterioration / confirmation / conflict / quality: 49.41 / 54.07 / 53.06 / 49.55 / 64
- internal_resonance: weak / score 41.06 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
