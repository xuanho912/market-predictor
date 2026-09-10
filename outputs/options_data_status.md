# Options / Volatility Structure Status

Generated at: `2026-09-10T16:27:16.001480+00:00`

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

- VIX: `17.649999618530273`
- VIX9D: `17.459999084472656`
- VIX3M: `19.520000457763672`
- VIX6M: `21.09000015258789`
- VVIX: `99.55999755859375`
- SKEW: `149.25`
- term_structure_state: `contango`
- volatility_reversal_score: `0.51`
- panic_release_score: `0.28`
- tail_risk_score: `0.5382`
- option_stress_score: `0.4921`
- failed_bounce_options_risk: `0.5116`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-09 | 149.25 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-10 | 17.649999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-10 | 19.520000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-10 | 21.09000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-10 | 17.459999084472656 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-10 | 99.55999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
