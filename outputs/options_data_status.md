# Options / Volatility Structure Status

Generated at: `2026-08-29T03:57:00.575322+00:00`

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

- VIX: `14.430000305175781`
- VIX9D: `11.220000267028809`
- VIX3M: `17.479999542236328`
- VIX6M: `20.299999237060547`
- VVIX: `86.62999725341797`
- SKEW: `149.77000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7727`
- panic_release_score: `0.5275`
- tail_risk_score: `0.3404`
- option_stress_score: `0.1115`
- failed_bounce_options_risk: `0.1794`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-28 | 149.77000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-28 | 14.430000305175781 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-28 | 17.479999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-28 | 20.299999237060547 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-28 | 11.220000267028809 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-28 | 86.62999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
