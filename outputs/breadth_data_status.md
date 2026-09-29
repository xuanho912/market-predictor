# Breadth Data Status

Generated at: 2026-09-29T10:09:29.662452+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 28.77
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 20.0
- equal_weight_vs_cap_weight_20d: -0.044756
- small_cap_vs_large_cap_20d: -0.048326

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-28
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2922 / 0.2624 / 0.4531
- advancers / decliners / A-D ratio: 303 / 198 / 1.5303
- new highs/lows 20d: 37 / 83
- new highs/lows 52w: 6 / 15
- improvement / deterioration / confirmation / conflict / quality: 67.05 / 70.86 / 70.61 / 53.85 / 100.0
- internal_resonance: surface_only / score 32.7 / SPY 指数表面强但内部没充分跟上：confirmation 71，conflict 54，RSP/SPY -4.48%，IWM/SPY -4.83%。

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
- internal_resonance: surface_only / score 1.71 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -4.48%，IWM/SPY -4.83%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-28
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4333 / 0.3667 / 0.6333
- advancers / decliners / A-D ratio: 18 / 12 / 1.5
- new highs/lows 20d: 0 / 4
- new highs/lows 52w: 0 / 1
- improvement / deterioration / confirmation / conflict / quality: 64.47 / 52.33 / 70.23 / 39.77 / 100.0
- internal_resonance: surface_only / score 37.34 / DIA 指数表面强但内部没充分跟上：confirmation 70，conflict 40，RSP/SPY -4.48%，IWM/SPY -4.83%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-28
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
- improvement / deterioration / confirmation / conflict / quality: 20.16 / 82.63 / 31.12 / 70.97 / 64
- internal_resonance: surface_only / score 16.26 / IWM 指数表面强但内部没充分跟上：confirmation 31，conflict 71，RSP/SPY -4.48%，IWM/SPY -4.83%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
