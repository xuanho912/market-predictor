# Options / Volatility Structure Status

Generated at: `2026-09-22T08:49:51.637631+00:00`

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
- VIX9D: `13.140000343322754`
- VIX3M: `18.079999923706055`
- VIX6M: `20.15999984741211`
- VVIX: `85.7699966430664`
- SKEW: `142.19000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.9303`
- panic_release_score: `0.6868`
- tail_risk_score: `0.1771`
- option_stress_score: `0.0682`
- failed_bounce_options_risk: `0.1229`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-21 | 142.19000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-22 | 14.930000305175781 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-21 | 18.079999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-21 | 20.15999984741211 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-21 | 13.140000343322754 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-21 | 85.7699966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
