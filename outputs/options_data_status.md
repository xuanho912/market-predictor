# Options / Volatility Structure Status

Generated at: `2026-09-05T00:55:08.201361+00:00`

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

- VIX: `14.529999732971191`
- VIX9D: `11.970000267028809`
- VIX3M: `17.610000610351562`
- VIX6M: `19.889999389648438`
- VVIX: `84.41999816894531`
- SKEW: `151.5800018310547`
- term_structure_state: `contango`
- volatility_reversal_score: `0.537`
- panic_release_score: `0.3531`
- tail_risk_score: `0.3497`
- option_stress_score: `0.2581`
- failed_bounce_options_risk: `0.2644`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-04 | 151.5800018310547 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-04 | 14.529999732971191 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-04 | 17.610000610351562 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-04 | 19.889999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-04 | 11.970000267028809 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-04 | 84.41999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
