# Options / Volatility Structure Status

Generated at: `2026-06-16T09:58:47.193843+00:00`

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

- VIX: `16.1299991607666`
- VIX9D: `17.260000228881836`
- VIX3M: `20.510000228881836`
- VIX6M: `22.59000015258789`
- VVIX: `87.58000183105469`
- SKEW: `142.60000610351562`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.1818`
- option_stress_score: `0.1248`
- failed_bounce_options_risk: `0.1621`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-12 | 142.60000610351562 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-16 | 16.1299991607666 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-12 | 20.510000228881836 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-12 | 22.59000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-12 | 17.260000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-15 | 87.58000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
