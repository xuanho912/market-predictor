# Options / Volatility Structure Status

Generated at: `2026-11-14T18:05:07.243313+00:00`

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

- VIX: `19.299999237060547`
- VIX9D: `17.81999969482422`
- VIX3M: `20.6200008392334`
- VIX6M: `22.030000686645508`
- VVIX: `101.52999877929688`
- SKEW: `147.13999938964844`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.858`
- tail_risk_score: `0.5296`
- option_stress_score: `0.3664`
- failed_bounce_options_risk: `0.3574`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-13 | 147.13999938964844 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-13 | 19.299999237060547 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-13 | 20.6200008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-13 | 22.030000686645508 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-13 | 17.81999969482422 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-13 | 101.52999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
