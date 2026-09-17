# Breadth Data Status

Generated at: 2026-09-17T17:02:46.138066+00:00

Provider available: True
True breadth available: False
True breadth symbols: SPY, DIA
Proxy-only symbols: IWM
Average breadth quality score: 67.0
Stale data: True

## Market Internal Resonance

- resonance_score: 21.1
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ, DIA, IWM
- sector_score: 28.0
- equal_weight_vs_cap_weight_20d: -0.02933
- small_cap_vs_large_cap_20d: -0.040608

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-09-14
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.2445 / 0.3797 / 0.5569
- advancers / decliners / A-D ratio: 262 / 241 / 1.0871
- new highs/lows 20d: 36 / 96
- new highs/lows 52w: 7 / 11
- improvement / deterioration / confirmation / conflict / quality: 12.75 / 100.0 / 29.18 / 85.0 / 100.0
- internal_resonance: surface_only / score 15.81 / SPY 指数表面强但内部没充分跟上：confirmation 29，conflict 85，RSP/SPY -2.93%，IWM/SPY -4.06%。

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
- internal_resonance: surface_only / score 3.56 / QQQ 指数表面强但内部没充分跟上：confirmation 9，conflict 69，RSP/SPY -2.93%，IWM/SPY -4.06%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-09-14
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.4 / 0.4 / 0.6667
- advancers / decliners / A-D ratio: 20 / 10 / 2.0
- new highs/lows 20d: 4 / 4
- new highs/lows 52w: 0 / 0
- improvement / deterioration / confirmation / conflict / quality: 43.13 / 100.0 / 51.06 / 76.0 / 100.0
- internal_resonance: surface_only / score 27.08 / DIA 指数表面强但内部没充分跟上：confirmation 51，conflict 76，RSP/SPY -2.93%，IWM/SPY -4.06%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-09-17
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
- improvement / deterioration / confirmation / conflict / quality: 29.85 / 78.49 / 38.39 / 67.86 / 64
- internal_resonance: surface_only / score 20.42 / IWM 指数表面强但内部没充分跟上：confirmation 38，conflict 68，RSP/SPY -2.93%，IWM/SPY -4.06%。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
