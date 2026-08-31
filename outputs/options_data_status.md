# Options / Volatility Structure Status

Generated at: `2026-08-31T19:10:48.079624+00:00`

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

- VIX: `15.119999885559082`
- VIX9D: `12.649999618530273`
- VIX3M: `17.649999618530273`
- VIX6M: `20.299999237060547`
- VVIX: `87.58999633789062`
- SKEW: `149.77000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5887`
- panic_release_score: `0.3858`
- tail_risk_score: `0.351`
- option_stress_score: `0.1517`
- failed_bounce_options_risk: `0.2036`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-28 | 149.77000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-31 | 15.119999885559082 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-31 | 17.649999618530273 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-31 | 20.299999237060547 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-31 | 12.649999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-31 | 87.58999633789062 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
