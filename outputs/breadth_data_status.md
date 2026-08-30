# Breadth Data Status

Generated at: 2026-08-30T16:43:30.767997+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 29.78
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 38.0
- equal_weight_vs_cap_weight_20d: -0.003461
- small_cap_vs_large_cap_20d: -0.014253

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-28
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4254 / 0.5288 / 0.6846
- advancers / decliners / A-D ratio: 228 / 274 / 0.8321
- new highs/lows 20d: 32 / 71
- new highs/lows 52w: 6 / 2
- improvement / deterioration / confirmation / conflict / quality: 36.13 / 100.0 / 46.01 / 85.0 / 100.0
- internal_resonance: surface_only / score 26.76 / SPY 指数表面强但内部没充分跟上：confirmation 46，conflict 85，RSP/SPY -0.35%，IWM/SPY -1.43%。

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
- internal_resonance: surface_only / score 6.77 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -0.35%，IWM/SPY -1.43%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-08-28
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4 / 0.5667 / 0.7
- advancers / decliners / A-D ratio: 17 / 13 / 1.3077
- new highs/lows 20d: 3 / 4
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 54.6 / 86.09 / 60.43 / 74.43 / 100.0
- internal_resonance: surface_only / score 33.36 / DIA 指数表面强但内部没充分跟上：confirmation 60，conflict 74，RSP/SPY -0.35%，IWM/SPY -1.43%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-28
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
- improvement / deterioration / confirmation / conflict / quality: 40.88 / 51.8 / 46.66 / 47.85 / 64
- internal_resonance: surface_only / score 29.22 / IWM 指数表面强但内部没充分跟上：confirmation 47，conflict 48，RSP/SPY -0.35%，IWM/SPY -1.43%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
