# Breadth Data Status

Generated at: 2026-10-20T01:23:41.669902+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 47.28
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 72.0
- equal_weight_vs_cap_weight_20d: 0.012461
- small_cap_vs_large_cap_20d: -0.040998

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-19
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6534 / 0.4343 / 0.498
- advancers / decliners / A-D ratio: 170 / 332 / 0.512
- new highs/lows 20d: 71 / 56
- new highs/lows 52w: 12 / 5
- improvement / deterioration / confirmation / conflict / quality: 94.62 / 58.6 / 91.44 / 44.54 / 100.0
- internal_resonance: surface_only / score 52.63 / SPY 指数表面强但内部没充分跟上：confirmation 91，conflict 45，RSP/SPY 1.25%，IWM/SPY -4.10%。

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
- internal_resonance: surface_only / score 10.27 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 1.25%，IWM/SPY -4.10%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-19
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6667 / 0.4333 / 0.6333
- advancers / decliners / A-D ratio: 13 / 17 / 0.7647
- new highs/lows 20d: 7 / 3
- new highs/lows 52w: 3 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 39.58 / 96.83 / 30.08 / 100.0
- internal_resonance: surface_only / score 61.76 / DIA 指数表面强但内部没充分跟上：confirmation 97，conflict 30，RSP/SPY 1.25%，IWM/SPY -4.10%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-19
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
- improvement / deterioration / confirmation / conflict / quality: 31.94 / 78.92 / 39.95 / 68.19 / 64
- internal_resonance: surface_only / score 27.44 / IWM 指数表面强但内部没充分跟上：confirmation 40，conflict 68，RSP/SPY 1.25%，IWM/SPY -4.10%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
