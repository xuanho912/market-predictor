# Options / Volatility Structure Status

Generated at: `2026-09-09T23:30:47.205531+00:00`

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

- VIX: `16.459999084472656`
- VIX9D: `15.59000015258789`
- VIX3M: `18.8700008392334`
- VIX6M: `20.6299991607666`
- VVIX: `94.5`
- SKEW: `149.25`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.4552`
- option_stress_score: `0.3962`
- failed_bounce_options_risk: `0.3905`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-09 | 149.25 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-09 | 16.459999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-09 | 18.8700008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-09 | 20.6299991607666 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-09 | 15.59000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-09 | 94.5 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
