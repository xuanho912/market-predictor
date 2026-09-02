# Breadth Data Status

Generated at: 2026-09-02T05:53:29.814711+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 31.22
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 20.0
- equal_weight_vs_cap_weight_20d: 0.000394
- small_cap_vs_large_cap_20d: -0.024542

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-08-31
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4235 / 0.5288 / 0.6846
- advancers / decliners / A-D ratio: 228 / 274 / 0.8321
- new highs/lows 20d: 32 / 71
- new highs/lows 52w: 6 / 2
- improvement / deterioration / confirmation / conflict / quality: 53.35 / 85.53 / 59.57 / 65.0 / 100.0
- internal_resonance: surface_only / score 31.42 / SPY 指数表面强但内部没充分跟上：confirmation 60，conflict 65，RSP/SPY 0.04%，IWM/SPY -2.45%。

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
- internal_resonance: surface_only / score 4.6 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 0.04%，IWM/SPY -2.45%。

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
- improvement / deterioration / confirmation / conflict / quality: 72.6 / 68.09 / 74.83 / 51.75 / 100.0
- internal_resonance: surface_only / score 38.72 / DIA 指数表面强但内部没充分跟上：confirmation 75，conflict 52，RSP/SPY 0.04%，IWM/SPY -2.45%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-01
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
- improvement / deterioration / confirmation / conflict / quality: 34.25 / 69.05 / 41.68 / 60.79 / 64
- internal_resonance: surface_only / score 23.52 / IWM 指数表面强但内部没充分跟上：confirmation 42，conflict 61，RSP/SPY 0.04%，IWM/SPY -2.45%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
