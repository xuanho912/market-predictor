# Breadth Data Status

Generated at: 2026-08-07T21:08:23.101984+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 64.99
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: DIA
- surface_only_symbols: QQQ
- sector_score: 70.0
- equal_weight_vs_cap_weight_20d: 0.002765
- small_cap_vs_large_cap_20d: -0.005435

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-05
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6481 / 0.6667 / 0.702
- advancers / decliners / A-D ratio: 245 / 258 / 0.9496
- new highs/lows 20d: 97 / 38
- new highs/lows 52w: 30 / 5
- improvement / deterioration / confirmation / conflict / quality: 68.51 / 45.02 / 73.72 / 34.22 / 100.0
- internal_resonance: mixed / score 64.85 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: surface_only / score 10.89 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.28%，IWM/SPY -0.54%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-05
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7667 / 0.8 / 0.7667
- advancers / decliners / A-D ratio: 21 / 9 / 2.3333
- new highs/lows 20d: 8 / 0
- new highs/lows 52w: 2 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 16.22 / 98.7 / 12.33 / 100.0
- internal_resonance: aligned / score 81.2 / DIA 内部共振：成分股 20d 上方比例 77%，行业参与 70%，confirmation 99 高于 conflict 12。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-07
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
- improvement / deterioration / confirmation / conflict / quality: 57.49 / 47.47 / 59.12 / 44.6 / 64
- internal_resonance: weak / score 48.91 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
