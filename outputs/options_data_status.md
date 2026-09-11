# Options / Volatility Structure Status

Generated at: `2026-09-11T22:42:24.074736+00:00`

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

- VIX: `15.84000015258789`
- VIX9D: `14.470000267028809`
- VIX3M: `18.600000381469727`
- VIX6M: `20.389999389648438`
- VVIX: `91.27999877929688`
- SKEW: `154.49000549316406`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.458`
- option_stress_score: `0.3513`
- failed_bounce_options_risk: `0.3676`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-11 | 154.49000549316406 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-11 | 15.84000015258789 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-11 | 18.600000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-11 | 20.389999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-11 | 14.470000267028809 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-11 | 91.27999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
