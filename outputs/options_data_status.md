# Options / Volatility Structure Status

Generated at: `2026-08-03T23:57:02.425616+00:00`

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

- VIX: `15.859999656677246`
- VIX9D: `13.279999732971191`
- VIX3M: `18.93000030517578`
- VIX6M: `21.200000762939453`
- VVIX: `90.80999755859375`
- SKEW: `139.9600067138672`
- term_structure_state: `contango`
- volatility_reversal_score: `0.95`
- panic_release_score: `0.7314`
- tail_risk_score: `0.161`
- option_stress_score: `0.1021`
- failed_bounce_options_risk: `0.1384`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-03 | 139.9600067138672 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-03 | 15.859999656677246 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-03 | 18.93000030517578 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-03 | 21.200000762939453 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-03 | 13.279999732971191 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-03 | 90.80999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
