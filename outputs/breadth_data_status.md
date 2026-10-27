# Breadth Data Status

Generated at: 2026-10-27T02:01:21.862477+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 51.62
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 84.0
- equal_weight_vs_cap_weight_20d: 0.03631
- small_cap_vs_large_cap_20d: -0.010507

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-10-26
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7072 / 0.5797 / 0.558
- advancers / decliners / A-D ratio: 153 / 349 / 0.4384
- new highs/lows 20d: 59 / 51
- new highs/lows 52w: 16 / 11
- improvement / deterioration / confirmation / conflict / quality: 93.98 / 47.74 / 91.84 / 36.28 / 100.0
- internal_resonance: surface_only / score 57.89 / SPY 指数表面强但内部没充分跟上：confirmation 92，conflict 36，RSP/SPY 3.63%，IWM/SPY -1.05%。

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
- internal_resonance: surface_only / score 13.76 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY 3.63%，IWM/SPY -1.05%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-10-26
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.7667 / 0.6333 / 0.7
- advancers / decliners / A-D ratio: 11 / 19 / 0.5789
- new highs/lows 20d: 3 / 2
- new highs/lows 52w: 1 / 0
- improvement / deterioration / confirmation / conflict / quality: 90.6 / 57.02 / 88.67 / 43.33 / 100.0
- internal_resonance: surface_only / score 58.36 / DIA 指数表面强但内部没充分跟上：confirmation 89，conflict 43，RSP/SPY 3.63%，IWM/SPY -1.05%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-10-26
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
- improvement / deterioration / confirmation / conflict / quality: 58.12 / 56.91 / 59.59 / 51.68 / 64
- internal_resonance: surface_only / score 38.61 / IWM 指数表面强但内部没充分跟上：confirmation 60，conflict 52，RSP/SPY 3.63%，IWM/SPY -1.05%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
