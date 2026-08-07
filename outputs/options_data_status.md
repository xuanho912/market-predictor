# Options / Volatility Structure Status

Generated at: `2026-08-07T21:08:34.126023+00:00`

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

- VIX: `14.899999618530273`
- VIX9D: `11.960000038146973`
- VIX3M: `18.719999313354492`
- VIX6M: `21.020000457763672`
- VVIX: `90.41999816894531`
- SKEW: `134.72999572753906`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6947`
- panic_release_score: `0.4938`
- tail_risk_score: `0.1148`
- option_stress_score: `0.065`
- failed_bounce_options_risk: `0.1087`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-06 | 134.72999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-07 | 14.899999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-07 | 18.719999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-07 | 21.020000457763672 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-07 | 11.960000038146973 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-07 | 90.41999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
