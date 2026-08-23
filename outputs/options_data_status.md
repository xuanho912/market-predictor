# Options / Volatility Structure Status

Generated at: `2026-08-23T13:04:22.988700+00:00`

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

- VIX: `15.130000114440918`
- VIX9D: `16.850000381469727`
- VIX3M: `20.540000915527344`
- VIX6M: `22.280000686645508`
- VVIX: `86.2699966430664`
- SKEW: `143.89999389648438`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8`
- panic_release_score: `0.5456`
- tail_risk_score: `0.2378`
- option_stress_score: `0.2381`
- failed_bounce_options_risk: `0.2612`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-21 | 143.89999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-21 | 15.130000114440918 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-17 | 20.540000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-17 | 22.280000686645508 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-17 | 16.850000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-21 | 86.2699966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
