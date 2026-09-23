# Options / Volatility Structure Status

Generated at: `2026-09-23T17:02:54.442007+00:00`

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

- VIX: `14.930000305175781`
- VIX9D: `13.210000038146973`
- VIX3M: `17.969999313354492`
- VIX6M: `19.979999542236328`
- VVIX: `86.37000274658203`
- SKEW: `142.19000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9303`
- panic_release_score: `0.6868`
- tail_risk_score: `0.1877`
- option_stress_score: `0.0714`
- failed_bounce_options_risk: `0.1268`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-21 | 142.19000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-23 | 14.930000305175781 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-23 | 17.969999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-23 | 19.979999542236328 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-23 | 13.210000038146973 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-23 | 86.37000274658203 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
