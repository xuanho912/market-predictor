# Options / Volatility Structure Status

Generated at: `2026-07-31T14:38:18.440686+00:00`

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

- VIX: `18.18000030517578`
- VIX9D: `16.350000381469727`
- VIX3M: `20.149999618530273`
- VIX6M: `22.139999389648438`
- VVIX: `96.62999725341797`
- SKEW: `139.89999389648438`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5829`
- panic_release_score: `0.3758`
- tail_risk_score: `0.255`
- option_stress_score: `0.2941`
- failed_bounce_options_risk: `0.2628`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-30 | 139.89999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-31 | 18.18000030517578 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-31 | 20.149999618530273 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-31 | 22.139999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-31 | 16.350000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-31 | 96.62999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
