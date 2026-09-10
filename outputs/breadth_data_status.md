# Breadth Data Status

Generated at: 2026-09-10T00:42:20.771671+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 20.85
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 24.0
- equal_weight_vs_cap_weight_20d: -0.016824
- small_cap_vs_large_cap_20d: -0.023797

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-08
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2684 / 0.4235 / 0.6008
- advancers / decliners / A-D ratio: 146 / 356 / 0.4101
- new highs/lows 20d: 18 / 128
- new highs/lows 52w: 5 / 13
- improvement / deterioration / confirmation / conflict / quality: 13.8 / 100.0 / 29.94 / 85.0 / 100.0
- internal_resonance: surface_only / score 16.14 / SPY 指数表面强但内部没充分跟上：confirmation 30，conflict 85，RSP/SPY -1.68%，IWM/SPY -2.38%。

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
- internal_resonance: surface_only / score 4.29 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -1.68%，IWM/SPY -2.38%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-08
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3333 / 0.4667 / 0.6667
- advancers / decliners / A-D ratio: 6 / 24 / 0.25
- new highs/lows 20d: 0 / 5
- new highs/lows 52w: 0 / 1
- improvement / deterioration / confirmation / conflict / quality: 32.68 / 99.85 / 43.54 / 75.89 / 100.0
- internal_resonance: surface_only / score 22.28 / DIA 指数表面强但内部没充分跟上：confirmation 44，conflict 76，RSP/SPY -1.68%，IWM/SPY -2.38%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-09
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
- improvement / deterioration / confirmation / conflict / quality: 38.7 / 68.12 / 45.03 / 60.09 / 64
- internal_resonance: surface_only / score 24.14 / IWM 指数表面强但内部没充分跟上：confirmation 45，conflict 60，RSP/SPY -1.68%，IWM/SPY -2.38%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
