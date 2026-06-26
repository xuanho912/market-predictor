# Breadth Data Status

Generated at: 2026-06-26T05:40:48.900565+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Market Internal Resonance

- resonance_score: 47.76
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: DIA
- sector_score: 62.0
- equal_weight_vs_cap_weight_20d: 0.042065
- small_cap_vs_large_cap_20d: 0.050944

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-06-24
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.509 / 0.5449 / 0.574
- advancers / decliners / A-D ratio: 266 / 235 / 1.1319
- new highs/lows 20d: 72 / 85
- new highs/lows 52w: 38 / 35
- improvement / deterioration / confirmation / conflict / quality: 46.18 / 100.0 / 53.25 / 76.0 / 100.0
- internal_resonance: mixed / score 50.65 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### QQQ

- status: available
- source: wikipedia-nasdaq100
- latest_date: 2026-06-22
- true_breadth: True
- proxy: False
- constituents used / expected: 101 / 101
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4059 / 0.4653 / 0.5743
- advancers / decliners / A-D ratio: 42 / 58 / 0.7241
- new highs/lows 20d: 14 / 30
- new highs/lows 52w: 10 / 12
- improvement / deterioration / confirmation / conflict / quality: 37.43 / 100.0 / 46.95 / 76.0 / 100.0
- internal_resonance: weak / score 46.27 / QQQ 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-06-22
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5333 / 0.6 / 0.6333
- advancers / decliners / A-D ratio: 14 / 15 / 0.9333
- new highs/lows 20d: 4 / 4
- new highs/lows 52w: 2 / 2
- improvement / deterioration / confirmation / conflict / quality: 30.09 / 95.16 / 42.05 / 81.32 / 100.0
- internal_resonance: surface_only / score 35.93 / DIA 指数表面强但内部没充分跟上：confirmation 42，conflict 81，RSP/SPY 4.21%，IWM/SPY 5.09%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-06-25
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
- improvement / deterioration / confirmation / conflict / quality: 83.19 / 22.27 / 78.39 / 25.7 / 64
- internal_resonance: mixed / score 58.18 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
