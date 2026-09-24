# Breadth Data Status

Generated at: 2026-09-24T23:17:43.187131+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 19.3
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 28.0
- equal_weight_vs_cap_weight_20d: -0.053337
- small_cap_vs_large_cap_20d: -0.059209

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-23
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2545 / 0.3022 / 0.495
- advancers / decliners / A-D ratio: 270 / 230 / 1.1739
- new highs/lows 20d: 34 / 127
- new highs/lows 52w: 7 / 25
- improvement / deterioration / confirmation / conflict / quality: 43.93 / 82.13 / 53.06 / 62.42 / 100.0
- internal_resonance: surface_only / score 23.36 / SPY 指数表面强但内部没充分跟上：confirmation 53，conflict 62，RSP/SPY -5.33%，IWM/SPY -5.92%。

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
- internal_resonance: surface_only / score 1.94 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -5.33%，IWM/SPY -5.92%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-22
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2 / 0.4 / 0.6667
- advancers / decliners / A-D ratio: 15 / 14 / 1.0714
- new highs/lows 20d: 2 / 5
- new highs/lows 52w: 0 / 1
- improvement / deterioration / confirmation / conflict / quality: 31.66 / 100.0 / 42.8 / 76.0 / 100.0
- internal_resonance: surface_only / score 19.47 / DIA 指数表面强但内部没充分跟上：confirmation 43，conflict 76，RSP/SPY -5.33%，IWM/SPY -5.92%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-24
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
- improvement / deterioration / confirmation / conflict / quality: 16.37 / 88.13 / 28.28 / 75.09 / 64
- internal_resonance: surface_only / score 15.07 / IWM 指数表面强但内部没充分跟上：confirmation 28，conflict 75，RSP/SPY -5.33%，IWM/SPY -5.92%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
