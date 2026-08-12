# Options / Volatility Structure Status

Generated at: `2026-08-12T21:11:52.097763+00:00`

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

- VIX: `14.550000190734863`
- VIX9D: `11.09000015258789`
- VIX3M: `18.530000686645508`
- VIX6M: `20.81999969482422`
- VVIX: `88.5`
- SKEW: `135.58999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.822`
- panic_release_score: `0.58`
- tail_risk_score: `0.1003`
- option_stress_score: `0.0393`
- failed_bounce_options_risk: `0.0917`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-11 | 135.58999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-12 | 14.550000190734863 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-12 | 18.530000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-12 | 20.81999969482422 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-12 | 11.09000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-12 | 88.5 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
