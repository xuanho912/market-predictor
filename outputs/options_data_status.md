# Options / Volatility Structure Status

Generated at: `2026-08-27T14:48:13.531172+00:00`

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

- VIX: `14.579999923706055`
- VIX9D: `12.119999885559082`
- VIX3M: `17.670000076293945`
- VIX6M: `20.479999542236328`
- VVIX: `83.44000244140625`
- SKEW: `142.9600067138672`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9893`
- panic_release_score: `0.6912`
- tail_risk_score: `0.1811`
- option_stress_score: `0.0525`
- failed_bounce_options_risk: `0.1151`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-26 | 142.9600067138672 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-27 | 14.579999923706055 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-27 | 17.670000076293945 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-27 | 20.479999542236328 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-27 | 12.119999885559082 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-27 | 83.44000244140625 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
