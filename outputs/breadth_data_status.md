# Breadth Data Status

Generated at: 2026-09-27T17:01:28.720861+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 30.79
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 24.0
- equal_weight_vs_cap_weight_20d: -0.047016
- small_cap_vs_large_cap_20d: -0.059829

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-25
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2962 / 0.2744 / 0.4571
- advancers / decliners / A-D ratio: 320 / 180 / 1.7778
- new highs/lows 20d: 49 / 83
- new highs/lows 52w: 8 / 14
- improvement / deterioration / confirmation / conflict / quality: 76.64 / 69.78 / 77.6 / 53.03 / 100.0
- internal_resonance: surface_only / score 36.76 / SPY 指数表面强但内部没充分跟上：confirmation 78，conflict 53，RSP/SPY -4.70%，IWM/SPY -5.98%。

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
- internal_resonance: surface_only / score 1.79 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -4.70%，IWM/SPY -5.98%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-25
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4 / 0.4 / 0.6333
- advancers / decliners / A-D ratio: 18 / 11 / 1.6364
- new highs/lows 20d: 2 / 4
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 74.15 / 59.51 / 76.63 / 45.23 / 100.0
- internal_resonance: surface_only / score 40.38 / DIA 指数表面强但内部没充分跟上：confirmation 77，conflict 45，RSP/SPY -4.70%，IWM/SPY -5.98%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-25
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
- improvement / deterioration / confirmation / conflict / quality: 18.72 / 88.81 / 30.04 / 75.61 / 64
- internal_resonance: surface_only / score 15.24 / IWM 指数表面强但内部没充分跟上：confirmation 30，conflict 76，RSP/SPY -4.70%，IWM/SPY -5.98%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
