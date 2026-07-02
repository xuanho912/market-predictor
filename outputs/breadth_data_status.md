# Breadth Data Status

Generated at: 2026-07-02T23:42:21.319430+00:00

Provider available: True
True breadth available: True
True breadth symbols: SPY, QQQ, DIA
Proxy-only symbols: IWM
Average breadth quality score: 91.0
Stale data: False

## Market Internal Resonance

- resonance_score: 62.12
- resonance_state: mixed
- label: partial_resonance
- aligned_symbols: none
- surface_only_symbols: DIA
- sector_score: 72.0
- equal_weight_vs_cap_weight_20d: 0.039591
- small_cap_vs_large_cap_20d: 0.046991

## Universe Status

### SPY

- status: available
- source: wikipedia-sp500
- latest_date: 2026-06-29
- true_breadth: True
- proxy: False
- constituents used / expected: 503 / 503
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.6454 / 0.6467 / 0.618
- advancers / decliners / A-D ratio: 229 / 273 / 0.8388
- new highs/lows 20d: 101 / 55
- new highs/lows 52w: 48 / 12
- improvement / deterioration / confirmation / conflict / quality: 100.0 / 32.27 / 97.42 / 24.52 / 100.0
- internal_resonance: mixed / score 78.55 / SPY 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### QQQ

- status: available
- source: wikipedia-nasdaq100
- latest_date: 2026-06-29
- true_breadth: True
- proxy: False
- constituents used / expected: 101 / 101
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.505 / 0.505 / 0.6139
- advancers / decliners / A-D ratio: 59 / 42 / 1.4048
- new highs/lows 20d: 16 / 10
- new highs/lows 52w: 10 / 2
- improvement / deterioration / confirmation / conflict / quality: 88.64 / 43.59 / 88.33 / 33.13 / 100.0
- internal_resonance: mixed / score 70.66 / QQQ 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

### DIA

- status: available
- source: static-dow30-list
- latest_date: 2026-06-29
- true_breadth: True
- proxy: False
- constituents used / expected: 30 / 30
- coverage_ratio: 1.0
- stale_constituents: False
- stale_price_data: False
- percent_above_20d / 50d / 200d: 0.5 / 0.5667 / 0.6333
- advancers / decliners / A-D ratio: 17 / 13 / 1.3077
- new highs/lows 20d: 7 / 2
- new highs/lows 52w: 3 / 0
- improvement / deterioration / confirmation / conflict / quality: 39.84 / 75.77 / 50.62 / 66.59 / 100.0
- internal_resonance: surface_only / score 42.18 / DIA 指数表面强但内部没充分跟上：confirmation 51，conflict 67，RSP/SPY 3.96%，IWM/SPY 4.70%。

### IWM

- status: proxy
- source: iwm-spy-relative-strength-proxy
- latest_date: 2026-07-02
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
- improvement / deterioration / confirmation / conflict / quality: 72.46 / 22.59 / 70.35 / 25.94 / 64
- internal_resonance: mixed / score 57.1 / IWM 内部信号分歧：成分股/行业有部分支持，但等权、小盘或新高新低没有完全确认。

## Notes

- IWM is explicitly proxy-only until a stable Russell 2000 constituent feed is added.
- Cached data may be used only when marked; stale breadth is not treated as fresh evidence.
- This report does not change Alpha v1 threshold or status.
