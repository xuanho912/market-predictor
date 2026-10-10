# Breadth Data Status

Generated at: 2026-10-10T01:58:21.696511+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 32.34
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 68.0
- equal_weight_vs_cap_weight_20d: -0.027201
- small_cap_vs_large_cap_20d: -0.053126

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-07
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3486 / 0.2749 / 0.438
- advancers / decliners / A-D ratio: 323 / 179 / 1.8045
- new highs/lows 20d: 57 / 55
- new highs/lows 52w: 16 / 12
- improvement / deterioration / confirmation / conflict / quality: 47.58 / 52.57 / 58.05 / 39.96 / 100.0
- internal_resonance: surface_only / score 38.7 / SPY 指数表面强但内部没充分跟上：confirmation 58，conflict 40，RSP/SPY -2.72%，IWM/SPY -5.31%。

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
- internal_resonance: surface_only / score 7.6 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -2.72%，IWM/SPY -5.31%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-06
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3667 / 0.3 / 0.5667
- advancers / decliners / A-D ratio: 18 / 12 / 1.5
- new highs/lows 20d: 5 / 4
- new highs/lows 52w: 1 / 1
- improvement / deterioration / confirmation / conflict / quality: 44.32 / 71.65 / 54.17 / 54.46 / 100.0
- internal_resonance: surface_only / score 35.07 / DIA 指数表面强但内部没充分跟上：confirmation 54，conflict 54，RSP/SPY -2.72%，IWM/SPY -5.31%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-09
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
- improvement / deterioration / confirmation / conflict / quality: 24.22 / 79.86 / 34.16 / 68.9 / 64
- internal_resonance: surface_only / score 23.26 / IWM 指数表面强但内部没充分跟上：confirmation 34，conflict 69，RSP/SPY -2.72%，IWM/SPY -5.31%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
