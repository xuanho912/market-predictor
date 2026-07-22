# Options / Volatility Structure Status

Generated at: `2026-07-22T14:24:48.573818+00:00`

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

- VIX: `16.8799991607666`
- VIX9D: `15.460000038146973`
- VIX3M: `19.56999969482422`
- VIX6M: `21.65999984741211`
- VVIX: `96.66999816894531`
- SKEW: `151.66000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `0.761`
- panic_release_score: `0.4931`
- tail_risk_score: `0.4797`
- option_stress_score: `0.4139`
- failed_bounce_options_risk: `0.4038`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-21 | 151.66000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-22 | 16.8799991607666 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-22 | 19.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-22 | 21.65999984741211 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-22 | 15.460000038146973 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-22 | 96.66999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
