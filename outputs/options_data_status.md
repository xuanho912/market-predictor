# Options / Volatility Structure Status

Generated at: `2026-07-29T00:09:18.602011+00:00`

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

- VIX: `18.209999084472656`
- VIX9D: `17.25`
- VIX3M: `19.860000610351562`
- VIX6M: `21.81999969482422`
- VVIX: `98.51000213623047`
- SKEW: `142.97999572753906`
- term_structure_state: `contango`
- volatility_reversal_score: `0.611`
- panic_release_score: `0.403`
- tail_risk_score: `0.3606`
- option_stress_score: `0.3269`
- failed_bounce_options_risk: `0.3019`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-28 | 142.97999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-28 | 18.209999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-28 | 19.860000610351562 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-28 | 21.81999969482422 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-28 | 17.25 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-28 | 98.51000213623047 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
