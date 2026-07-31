# Options / Volatility Structure Status

Generated at: `2026-07-31T22:38:59.723107+00:00`

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

- VIX: `15.989999771118164`
- VIX9D: `13.050000190734863`
- VIX3M: `19.020000457763672`
- VIX6M: `21.34000015258789`
- VVIX: `91.63999938964844`
- SKEW: `141.22999572753906`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9477`
- panic_release_score: `0.71`
- tail_risk_score: `0.1856`
- option_stress_score: `0.1129`
- failed_bounce_options_risk: `0.1492`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-31 | 141.22999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-31 | 15.989999771118164 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-31 | 19.020000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-31 | 21.34000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-31 | 13.050000190734863 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-31 | 91.63999938964844 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
