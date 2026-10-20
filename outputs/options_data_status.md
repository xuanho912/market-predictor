# Options / Volatility Structure Status

Generated at: `2026-10-20T17:10:34.315408+00:00`

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

- VIX: `17.729999542236328`
- VIX9D: `17.040000915527344`
- VIX3M: `19.200000762939453`
- VIX6M: `20.940000534057617`
- VVIX: `98.81999969482422`
- SKEW: `161.86000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5129`
- panic_release_score: `0.2979`
- tail_risk_score: `0.6094`
- option_stress_score: `0.5193`
- failed_bounce_options_risk: `0.519`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-19 | 161.86000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-20 | 17.729999542236328 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-20 | 19.200000762939453 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-20 | 20.940000534057617 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-20 | 17.040000915527344 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-20 | 98.81999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
