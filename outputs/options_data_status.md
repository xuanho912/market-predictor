# Options / Volatility Structure Status

Generated at: `2026-10-21T08:54:12.199943+00:00`

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

- VIX: `17.270000457763672`
- VIX9D: `16.270000457763672`
- VIX3M: `18.989999771118164`
- VIX6M: `20.739999771118164`
- VVIX: `97.1500015258789`
- SKEW: `160.39999389648438`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5048`
- panic_release_score: `0.33`
- tail_risk_score: `0.5729`
- option_stress_score: `0.4836`
- failed_bounce_options_risk: `0.4406`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-20 | 160.39999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-21 | 17.270000457763672 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-20 | 18.989999771118164 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-20 | 20.739999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-20 | 16.270000457763672 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-20 | 97.1500015258789 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
