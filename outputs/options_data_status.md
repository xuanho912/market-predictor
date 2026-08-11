# Options / Volatility Structure Status

Generated at: `2026-08-11T23:27:34.329247+00:00`

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

- VIX: `15.279999732971191`
- VIX9D: `12.520000457763672`
- VIX3M: `18.90999984741211`
- VIX6M: `21.100000381469727`
- VVIX: `90.9000015258789`
- SKEW: `135.58999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8253`
- panic_release_score: `0.5805`
- tail_risk_score: `0.129`
- option_stress_score: `0.0745`
- failed_bounce_options_risk: `0.1168`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-11 | 135.58999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-11 | 15.279999732971191 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-11 | 18.90999984741211 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-11 | 21.100000381469727 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-11 | 12.520000457763672 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-11 | 90.9000015258789 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
