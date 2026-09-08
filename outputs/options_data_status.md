# Options / Volatility Structure Status

Generated at: `2026-09-08T22:49:44.508189+00:00`

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

- VIX: `15.720000267028809`
- VIX9D: `14.8100004196167`
- VIX3M: `18.389999389648438`
- VIX6M: `20.34000015258789`
- VVIX: `88.69000244140625`
- SKEW: `148.86000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6033`
- panic_release_score: `0.4186`
- tail_risk_score: `0.3625`
- option_stress_score: `0.1836`
- failed_bounce_options_risk: `0.2235`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-08 | 148.86000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-08 | 15.720000267028809 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-08 | 18.389999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-08 | 20.34000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-08 | 14.8100004196167 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-08 | 88.69000244140625 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
