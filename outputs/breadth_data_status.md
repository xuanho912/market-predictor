# Breadth Data Status

Generated at: 2026-08-07T04:06:35.839903+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 51.69
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, IWM
- sector_score: 72.0
- equal_weight_vs_cap_weight_20d: 0.001378
- small_cap_vs_large_cap_20d: -0.019018

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
- internal_resonance: surface_only / score 52.52 / SPY 指数表面强但内部没充分跟上：confirmation 74，conflict 34，RSP/SPY 0.14%，IWM/SPY -1.90%。

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
- internal_resonance: surface_only / score 10.56 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.14%，IWM/SPY -1.90%。

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
- internal_resonance: mixed / score 68.87 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-06
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
- improvement / deterioration / confirmation / conflict / quality: 48.43 / 56.76 / 52.32 / 51.57 / 64
- internal_resonance: surface_only / score 33.69 / IWM 指数表面强但内部没充分跟上：confirmation 52，conflict 52，RSP/SPY 0.14%，IWM/SPY -1.90%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
