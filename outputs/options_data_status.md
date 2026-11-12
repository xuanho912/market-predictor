# Options / Volatility Structure Status

Generated at: `2026-11-12T19:57:04.931032+00:00`

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

- VIX: `18.670000076293945`
- VIX9D: `17.520000457763672`
- VIX3M: `20.020000457763672`
- VIX6M: `21.700000762939453`
- VVIX: `98.12000274658203`
- SKEW: `149.08999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9743`
- panic_release_score: `0.8193`
- tail_risk_score: `0.5125`
- option_stress_score: `0.3486`
- failed_bounce_options_risk: `0.3442`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-11 | 149.08999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-12 | 18.670000076293945 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-12 | 20.020000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-12 | 21.700000762939453 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-12 | 17.520000457763672 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-12 | 98.12000274658203 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
