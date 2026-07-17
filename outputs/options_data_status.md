# Options / Volatility Structure Status

Generated at: `2026-07-17T14:06:13.568408+00:00`

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

- VIX: `18.799999237060547`
- VIX9D: `17.440000534057617`
- VIX3M: `20.639999389648438`
- VIX6M: `22.40999984741211`
- VVIX: `105.5`
- SKEW: `145.72000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5257`
- panic_release_score: `0.3782`
- tail_risk_score: `0.5229`
- option_stress_score: `0.5196`
- failed_bounce_options_risk: `0.5346`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-16 | 145.72000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-17 | 18.799999237060547 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-17 | 20.639999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-17 | 22.40999984741211 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-17 | 17.440000534057617 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-17 | 105.5 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
