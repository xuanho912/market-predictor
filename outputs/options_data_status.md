# Options / Volatility Structure Status

Generated at: `2026-07-01T23:55:16.914552+00:00`

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

- VIX: `16.59000015258789`
- VIX9D: `13.140000343322754`
- VIX3M: `19.15999984741211`
- VIX6M: `21.6299991607666`
- VVIX: `89.04000091552734`
- SKEW: `154.82000732421875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.84`
- panic_release_score: `0.6214`
- tail_risk_score: `0.3929`
- option_stress_score: `0.236`
- failed_bounce_options_risk: `0.2584`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-01 | 154.82000732421875 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-01 | 16.59000015258789 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-01 | 19.15999984741211 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-01 | 21.6299991607666 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-01 | 13.140000343322754 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-01 | 89.04000091552734 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
