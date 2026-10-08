# Options / Volatility Structure Status

Generated at: `2026-10-08T18:54:03.329618+00:00`

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

- VIX: `15.710000038146973`
- VIX9D: `12.569999694824219`
- VIX3M: `18.229999542236328`
- VIX6M: `20.149999618530273`
- VVIX: `88.7699966430664`
- SKEW: `141.83999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8263`
- panic_release_score: `0.5603`
- tail_risk_score: `0.217`
- option_stress_score: `0.1296`
- failed_bounce_options_risk: `0.1647`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-07 | 141.83999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-08 | 15.710000038146973 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-08 | 18.229999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-08 | 20.149999618530273 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-08 | 12.569999694824219 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-08 | 88.7699966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
