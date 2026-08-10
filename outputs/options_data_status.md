# Options / Volatility Structure Status

Generated at: `2026-08-10T23:24:15.410760+00:00`

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

- VIX: `15.460000038146973`
- VIX9D: `12.770000457763672`
- VIX3M: `18.979999542236328`
- VIX6M: `21.139999389648438`
- VVIX: `92.51000213623047`
- SKEW: `137.1300048828125`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7367`
- panic_release_score: `0.4934`
- tail_risk_score: `0.1642`
- option_stress_score: `0.1065`
- failed_bounce_options_risk: `0.1414`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-10 | 137.1300048828125 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-10 | 15.460000038146973 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-10 | 18.979999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-10 | 21.139999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-10 | 12.770000457763672 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-10 | 92.51000213623047 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
