# Options / Volatility Structure Status

Generated at: `2026-10-15T17:04:42.743447+00:00`

## Summary

- options_available: `True`
- options_partial: `False`
- options_missing: `False`
- options_stale: `False`
- options_source: `market_data_cache/yahoo/stooq`
- vix_term_available: `True`
- vvix_available: `True`
- skew_available: `True`
- put_call_available: `False`
- gamma_available: `False`
- options_quality_score: `92`

## Market Snapshot

- VIX: `16.829999923706055`
- VIX9D: `14.6899995803833`
- VIX3M: `18.700000762939453`
- VIX6M: `20.459999084472656`
- VVIX: `93.44999694824219`
- SKEW: `157.3000030517578`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.5229`
- option_stress_score: `0.4394`
- failed_bounce_options_risk: `0.4317`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-14 | 157.3000030517578 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-15 | 16.829999923706055 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-15 | 18.700000762939453 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-15 | 20.459999084472656 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-15 | 14.6899995803833 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-15 | 93.44999694824219 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
