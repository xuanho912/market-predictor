# Options / Volatility Structure Status

Generated at: `2026-08-03T15:20:29.066635+00:00`

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

- VIX: `15.720000267028809`
- VIX9D: `13.100000381469727`
- VIX3M: `18.84000015258789`
- VIX6M: `21.139999389648438`
- VVIX: `90.80000305175781`
- SKEW: `141.22999572753906`
- term_structure_state: `contango`
- volatility_reversal_score: `0.95`
- panic_release_score: `0.7514`
- tail_risk_score: `0.175`
- option_stress_score: `0.0928`
- failed_bounce_options_risk: `0.1361`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-31 | 141.22999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-03 | 15.720000267028809 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-03 | 18.84000015258789 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-03 | 21.139999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-03 | 13.100000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-03 | 90.80000305175781 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
