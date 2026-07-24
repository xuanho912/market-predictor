# Options / Volatility Structure Status

Generated at: `2026-07-24T22:40:23.371074+00:00`

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

- VIX: `18.579999923706055`
- VIX9D: `17.6200008392334`
- VIX3M: `20.510000228881836`
- VIX6M: `22.43000030517578`
- VVIX: `100.7300033569336`
- SKEW: `147.27999877929688`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5846`
- panic_release_score: `0.4009`
- tail_risk_score: `0.4999`
- option_stress_score: `0.3803`
- failed_bounce_options_risk: `0.3591`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-24 | 147.27999877929688 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-24 | 18.579999923706055 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-24 | 20.510000228881836 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-24 | 22.43000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-24 | 17.6200008392334 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-24 | 100.7300033569336 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
