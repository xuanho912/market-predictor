# Options / Volatility Structure Status

Generated at: `2026-06-22T15:54:50.105436+00:00`

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

- VIX: `17.440000534057617`
- VIX9D: `16.610000610351562`
- VIX3M: `19.889999389648438`
- VIX6M: `22.329999923706055`
- VVIX: `92.19999694824219`
- SKEW: `146.72000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.55`
- panic_release_score: `0.3143`
- tail_risk_score: `0.3276`
- option_stress_score: `0.3055`
- failed_bounce_options_risk: `0.2836`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-18 | 146.72000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-22 | 17.440000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-22 | 19.889999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-22 | 22.329999923706055 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-22 | 16.610000610351562 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-22 | 92.19999694824219 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
