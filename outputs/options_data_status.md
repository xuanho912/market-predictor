# Options / Volatility Structure Status

Generated at: `2026-11-05T03:28:39.377709+00:00`

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

- VIX: `16.610000610351562`
- VIX9D: `15.1899995803833`
- VIX3M: `18.799999237060547`
- VIX6M: `20.68000030517578`
- VVIX: `90.41000366210938`
- SKEW: `150.89999389648438`
- term_structure_state: `contango`
- volatility_reversal_score: `0.55`
- panic_release_score: `0.3729`
- tail_risk_score: `0.4206`
- option_stress_score: `0.2742`
- failed_bounce_options_risk: `0.285`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-04 | 150.89999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-04 | 16.610000610351562 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-04 | 18.799999237060547 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-04 | 20.68000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-04 | 15.1899995803833 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-04 | 90.41000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
