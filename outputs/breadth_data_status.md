# Breadth Data Status

Generated at: 2026-06-23T05:16:57.320913+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Market Internal Resonance

- resonance_score: 36.51
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA
- sector_score: 46.0
- equal_weight_vs_cap_weight_20d: 0.021688
- small_cap_vs_large_cap_20d: 0.053293

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-06-22
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.506 / 0.5438 / 0.5749
- advancers / decliners / A-D ratio: 267 / 235 / 1.1362
- new highs/lows 20d: 72 / 86
- new highs/lows 52w: 38 / 35
- improvement / deterioration / confirmation / conflict / quality: 28.05 / 100.0 / 40.2 / 85.0 / 100.0
- internal_resonance: surface_only / score 31.26 / SPY 指数表面强但内部没充分跟上：confirmation 40，conflict 85，RSP/SPY 2.17%，IWM/SPY 5.33%。

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
- improvement / deterioration / confirmation / conflict / quality: 19.43 / 100.0 / 33.99 / 85.0 / 100.0
- internal_resonance: surface_only / score 26.95 / QQQ 指数表面强但内部没充分跟上：confirmation 34，conflict 85，RSP/SPY 2.17%，IWM/SPY 5.33%。

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
- internal_resonance: surface_only / score 33.34 / DIA 指数表面强但内部没充分跟上：confirmation 42，conflict 81，RSP/SPY 2.17%，IWM/SPY 5.33%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-06-22
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
- improvement / deterioration / confirmation / conflict / quality: 77.02 / 14.8 / 73.76 / 20.1 / 64
- internal_resonance: mixed / score 54.48 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
