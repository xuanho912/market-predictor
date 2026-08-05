# Breadth Data Status

Generated at: 2026-08-05T21:41:19.480013+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 46.09
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 68.0
- equal_weight_vs_cap_weight_20d: 0.002765
- small_cap_vs_large_cap_20d: -0.011288

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
- internal_resonance: surface_only / score 44.6 / SPY 指数表面强但内部没充分跟上：confirmation 59，conflict 34，RSP/SPY 0.28%，IWM/SPY -1.13%。

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
- internal_resonance: surface_only / score 10.46 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.28%，IWM/SPY -1.13%。

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
- internal_resonance: surface_only / score 57.63 / DIA 指数表面强但内部没充分跟上：confirmation 96，conflict 27，RSP/SPY 0.28%，IWM/SPY -1.13%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-08-05
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
- improvement / deterioration / confirmation / conflict / quality: 56.25 / 49.16 / 58.19 / 45.87 / 64
- internal_resonance: surface_only / score 36.03 / IWM 指数表面强但内部没充分跟上：confirmation 58，conflict 46，RSP/SPY 0.28%，IWM/SPY -1.13%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
