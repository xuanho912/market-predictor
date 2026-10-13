# Breadth Data Status

Generated at: 2026-10-13T19:20:59.693056+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 49.63
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 86.0
- equal_weight_vs_cap_weight_20d: -0.029685
- small_cap_vs_large_cap_20d: -0.056022

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-12
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5359 / 0.3426 / 0.47
- advancers / decliners / A-D ratio: 306 / 196 / 1.5612
- new highs/lows 20d: 60 / 31
- new highs/lows 52w: 12 / 6
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 40.75 / 96.74 / 30.97 / 100.0
- internal_resonance: surface_only / score 63.2 / SPY 指数表面强但内部没充分跟上：confirmation 97，conflict 31，RSP/SPY -2.97%，IWM/SPY -5.60%。

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
- internal_resonance: surface_only / score 9.39 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -2.97%，IWM/SPY -5.60%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-12
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4333 / 0.4667 / 0.5667
- advancers / decliners / A-D ratio: 22 / 8 / 2.75
- new highs/lows 20d: 4 / 1
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 35.06 / 97.2 / 26.65 / 100.0
- internal_resonance: surface_only / score 61.15 / DIA 指数表面强但内部没充分跟上：confirmation 97，conflict 27，RSP/SPY -2.97%，IWM/SPY -5.60%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-13
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
- improvement / deterioration / confirmation / conflict / quality: 21.22 / 79.52 / 31.91 / 68.64 / 64
- internal_resonance: surface_only / score 24.55 / IWM 指数表面强但内部没充分跟上：confirmation 32，conflict 69，RSP/SPY -2.97%，IWM/SPY -5.60%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
