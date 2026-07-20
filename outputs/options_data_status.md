# Options / Volatility Structure Status

Generated at: `2026-07-20T14:36:32.891697+00:00`

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

- VIX: `18.299999237060547`
- VIX9D: `17.479999542236328`
- VIX3M: `20.170000076293945`
- VIX6M: `22.09000015258789`
- VVIX: `100.94999694824219`
- SKEW: `147.27999877929688`
- term_structure_state: `contango`
- volatility_reversal_score: `0.52`
- panic_release_score: `0.3425`
- tail_risk_score: `0.5037`
- option_stress_score: `0.5022`
- failed_bounce_options_risk: `0.4554`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-17 | 147.27999877929688 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-20 | 18.299999237060547 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-20 | 20.170000076293945 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-20 | 22.09000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-20 | 17.479999542236328 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-20 | 100.94999694824219 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
