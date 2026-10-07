# Options / Volatility Structure Status

Generated at: `2026-10-07T18:59:24.433126+00:00`

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

- VIX: `15.119999885559082`
- VIX9D: `11.819999694824219`
- VIX3M: `17.719999313354492`
- VIX6M: `19.860000610351562`
- VVIX: `84.25`
- SKEW: `141.2100067138672`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8373`
- panic_release_score: `0.588`
- tail_risk_score: `0.147`
- option_stress_score: `0.0767`
- failed_bounce_options_risk: `0.1216`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-06 | 141.2100067138672 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-07 | 15.119999885559082 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-07 | 17.719999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-07 | 19.860000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-07 | 11.819999694824219 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-07 | 84.25 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
