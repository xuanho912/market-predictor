# Breadth Data Status

Generated at: 2026-08-03T23:56:56.345201+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 44.34
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 64.0
- equal_weight_vs_cap_weight_20d: 0.001309
- small_cap_vs_large_cap_20d: -0.017472

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-07-31
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5328 / 0.6208 / 0.662
- advancers / decliners / A-D ratio: 221 / 281 / 0.7865
- new highs/lows 20d: 27 / 50
- new highs/lows 52w: 3 / 4
- improvement / deterioration / confirmation / conflict / quality: 48.37 / 45.21 / 59.21 / 34.36 / 100.0
- internal_resonance: surface_only / score 43.87 / SPY 指数表面强但内部没充分跟上：confirmation 59，conflict 34，RSP/SPY 0.13%，IWM/SPY -1.75%。

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
- internal_resonance: surface_only / score 9.73 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.13%，IWM/SPY -1.75%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-07-31
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5 / 0.6 / 0.6667
- advancers / decliners / A-D ratio: 18 / 12 / 1.5
- new highs/lows 20d: 3 / 2
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 98.21 / 35.28 / 95.89 / 26.81 / 100.0
- internal_resonance: surface_only / score 56.9 / DIA 指数表面强但内部没充分跟上：confirmation 96，conflict 27，RSP/SPY 0.13%，IWM/SPY -1.75%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-03
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
- improvement / deterioration / confirmation / conflict / quality: 46.95 / 59.23 / 51.21 / 53.42 / 64
- internal_resonance: surface_only / score 32.26 / IWM 指数表面强但内部没充分跟上：confirmation 51，conflict 53，RSP/SPY 0.13%，IWM/SPY -1.75%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
