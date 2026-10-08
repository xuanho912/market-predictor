# Options / Volatility Structure Status

Generated at: `2026-10-08T10:57:47.106961+00:00`

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

- VIX: `15.949999809265137`
- VIX9D: `11.779999732971191`
- VIX3M: `17.719999313354492`
- VIX6M: `19.860000610351562`
- VVIX: `83.18000030517578`
- SKEW: `141.83999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7623`
- panic_release_score: `0.511`
- tail_risk_score: `0.1552`
- option_stress_score: `0.1351`
- failed_bounce_options_risk: `0.1553`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-07 | 141.83999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-08 | 15.949999809265137 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-07 | 17.719999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-07 | 19.860000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-07 | 11.779999732971191 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-07 | 83.18000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
