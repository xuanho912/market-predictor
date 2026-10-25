# Breadth Data Status

Generated at: 2026-10-25T16:24:01.177355+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 66.5
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: DIA
- surface_only_symbols: none
- sector_score: 80.0
- equal_weight_vs_cap_weight_20d: 0.040475
- small_cap_vs_large_cap_20d: -0.007306

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-23
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7131 / 0.5857 / 0.558
- advancers / decliners / A-D ratio: 154 / 348 / 0.4425
- new highs/lows 20d: 67 / 47
- new highs/lows 52w: 17 / 9
- improvement / deterioration / confirmation / conflict / quality: 93.32 / 47.03 / 91.42 / 35.75 / 100.0
- internal_resonance: mixed / score 69.88 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: weak / score 25.62 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-23
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.8333 / 0.6333 / 0.6667
- advancers / decliners / A-D ratio: 9 / 21 / 0.4286
- new highs/lows 20d: 6 / 2
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 37.91 / 96.97 / 28.81 / 100.0
- internal_resonance: aligned / score 79.09 / DIA 内部共振：成分股 20d 上方比例 83%，行业参与 80%，confirmation 97 高于 conflict 29。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-23
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
- improvement / deterioration / confirmation / conflict / quality: 59.64 / 58.44 / 60.73 / 52.83 / 64
- internal_resonance: mixed / score 50.54 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
