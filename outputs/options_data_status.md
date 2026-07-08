# Options / Volatility Structure Status

Generated at: `2026-07-08T14:43:27.797876+00:00`

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

- VIX: `17.610000610351562`
- VIX9D: `15.899999618530273`
- VIX3M: `19.729999542236328`
- VIX6M: `21.809999465942383`
- VVIX: `92.31999969482422`
- SKEW: `145.74000549316406`
- term_structure_state: `contango`
- volatility_reversal_score: `0.642`
- panic_release_score: `0.3678`
- tail_risk_score: `0.3174`
- option_stress_score: `0.4196`
- failed_bounce_options_risk: `0.3733`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-07 | 145.74000549316406 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-08 | 17.610000610351562 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-08 | 19.729999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-08 | 21.809999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-08 | 15.899999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-08 | 92.31999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
