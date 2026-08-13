# Breadth Data Status

Generated at: 2026-08-13T23:29:02.104855+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 65.06
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: DIA
- surface_only_symbols: QQQ
- sector_score: 88.0
- equal_weight_vs_cap_weight_20d: -0.000514
- small_cap_vs_large_cap_20d: -0.009419

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-10
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6302 / 0.6514 / 0.708
- advancers / decliners / A-D ratio: 230 / 270 / 0.8519
- new highs/lows 20d: 98 / 48
- new highs/lows 52w: 22 / 4
- improvement / deterioration / confirmation / conflict / quality: 74.19 / 36.32 / 78.51 / 27.6 / 100.0
- internal_resonance: mixed / score 68.06 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

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
- internal_resonance: surface_only / score 12.58 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -0.05%，IWM/SPY -0.94%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-10
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7333 / 0.7 / 0.7333
- advancers / decliners / A-D ratio: 13 / 17 / 0.7647
- new highs/lows 20d: 5 / 0
- new highs/lows 52w: 2 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 25.37 / 97.97 / 19.28 / 100.0
- internal_resonance: aligned / score 77.64 / DIA 内部共振：成分股 20d 上方比例 73%，行业参与 80%，confirmation 98 高于 conflict 19。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-13
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
- improvement / deterioration / confirmation / conflict / quality: 51.01 / 47.08 / 54.26 / 44.31 / 64
- internal_resonance: weak / score 49.48 / IWM 暂无内部共振：成分股参与度、行业参与或等权/小盘代理不足。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
