# Options / Volatility Structure Status

Generated at: `2026-08-20T13:14:14.307243+00:00`

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

- VIX: `15.84000015258789`
- VIX9D: `12.65999984741211`
- VIX3M: `18.56999969482422`
- VIX6M: `22.280000686645508`
- VVIX: `86.52999877929688`
- SKEW: `142.92999267578125`
- term_structure_state: `contango`
- volatility_reversal_score: `0.781`
- panic_release_score: `0.5056`
- tail_risk_score: `0.1894`
- option_stress_score: `0.2595`
- failed_bounce_options_risk: `0.2609`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-19 | 142.92999267578125 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-20 | 15.84000015258789 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-19 | 18.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-17 | 22.280000686645508 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-19 | 12.65999984741211 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-19 | 86.52999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
