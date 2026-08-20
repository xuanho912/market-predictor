# Options / Volatility Structure Status

Generated at: `2026-08-20T21:58:08.569941+00:00`

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

- VIX: `16.010000228881836`
- VIX9D: `14.390000343322754`
- VIX3M: `19.059999465942383`
- VIX6M: `21.25`
- VVIX: `89.86000061035156`
- SKEW: `143.22999572753906`
- term_structure_state: `contango`
- volatility_reversal_score: `0.764`
- panic_release_score: `0.495`
- tail_risk_score: `0.241`
- option_stress_score: `0.2799`
- failed_bounce_options_risk: `0.2866`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-20 | 143.22999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-20 | 16.010000228881836 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-20 | 19.059999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-20 | 21.25 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-20 | 14.390000343322754 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-20 | 89.86000061035156 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
