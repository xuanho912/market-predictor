# Breadth Data Status

Generated at: 2026-06-22T15:54:48.939170+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Market Internal Resonance

- resonance_score: 44.39
- resonance_state: surface_only
- label: index_surface_strength
- aligned_symbols: none
- surface_only_symbols: SPY, QQQ
- sector_score: 46.0
- equal_weight_vs_cap_weight_20d: 0.023031
- small_cap_vs_large_cap_20d: 0.051664

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-06-18
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.508 / 0.5359 / 0.5808
- advancers / decliners / A-D ratio: 74 / 428 / 0.1729
- new highs/lows 20d: 32 / 82
- new highs/lows 52w: 18 / 25
- improvement / deterioration / confirmation / conflict / quality: 27.53 / 87.93 / 40.78 / 75.83 / 100.0
- internal_resonance: surface_only / score 31.14 / SPY 指数表面强但内部没充分跟上：confirmation 41，conflict 76，RSP/SPY 2.30%，IWM/SPY 5.17%。

### QQQ

- status: available
- source: wikipedia-nasdaq100
- latest_date: 2026-06-17
- true_breadth: True
- proxy: False
- constituents used / expected: 101 / 101
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.3366 / 0.4653 / 0.5644
- advancers / decliners / A-D ratio: 19 / 81 / 0.2346
- new highs/lows 20d: 5 / 21
- new highs/lows 52w: 4 / 7
- improvement / deterioration / confirmation / conflict / quality: 30.81 / 95.46 / 42.55 / 81.55 / 100.0
- internal_resonance: surface_only / score 27.77 / QQQ 指数表面强但内部没充分跟上：confirmation 43，conflict 82，RSP/SPY 2.30%，IWM/SPY 5.17%。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-06-17
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5333 / 0.6 / 0.7333
- advancers / decliners / A-D ratio: 4 / 26 / 0.1538
- new highs/lows 20d: 3 / 4
- new highs/lows 52w: 2 / 1
- improvement / deterioration / confirmation / conflict / quality: 85.2 / 49.76 / 85.36 / 37.81 / 100.0
- internal_resonance: mixed / score 64.3 / DIA 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-06-22
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
- improvement / deterioration / confirmation / conflict / quality: 76.39 / 15.76 / 73.29 / 20.82 / 64
- internal_resonance: mixed / score 54.37 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
