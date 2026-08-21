# Breadth Data Status

Generated at: 2026-08-21T04:23:32.230649+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 38.74
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 42.0
- equal_weight_vs_cap_weight_20d: 0.002264
- small_cap_vs_large_cap_20d: -0.013978

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-19
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5299 / 0.5948 / 0.716
- advancers / decliners / A-D ratio: 284 / 217 / 1.3088
- new highs/lows 20d: 83 / 36
- new highs/lows 52w: 20 / 0
- improvement / deterioration / confirmation / conflict / quality: 52.16 / 82.24 / 58.98 / 62.5 / 100.0
- internal_resonance: surface_only / score 38.57 / SPY 指数表面强但内部没充分跟上：confirmation 59，conflict 62，RSP/SPY 0.23%，IWM/SPY -1.40%。

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
- internal_resonance: surface_only / score 7.48 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.23%，IWM/SPY -1.40%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-19
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6667 / 0.6667 / 0.7667
- advancers / decliners / A-D ratio: 19 / 11 / 1.7273
- new highs/lows 20d: 8 / 4
- new highs/lows 52w: 4 / 0
- improvement / deterioration / confirmation / conflict / quality: 63.96 / 54.51 / 69.69 / 41.43 / 100.0
- internal_resonance: surface_only / score 47.63 / DIA 指数表面强但内部没充分跟上：confirmation 70，conflict 41，RSP/SPY 0.23%，IWM/SPY -1.40%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-20
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
- improvement / deterioration / confirmation / conflict / quality: 40.71 / 50.82 / 46.53 / 47.11 / 64
- internal_resonance: surface_only / score 30.03 / IWM 指数表面强但内部没充分跟上：confirmation 47，conflict 47，RSP/SPY 0.23%，IWM/SPY -1.40%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
