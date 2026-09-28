# Options / Volatility Structure Status

Generated at: `2026-09-28T19:43:05.438881+00:00`

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

- VIX: `15.989999771118164`
- VIX9D: `14.319999694824219`
- VIX3M: `18.170000076293945`
- VIX6M: `20.219999313354492`
- VVIX: `90.83000183105469`
- SKEW: `144.91000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.326`
- option_stress_score: `0.3219`
- failed_bounce_options_risk: `0.3202`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-25 | 144.91000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-28 | 15.989999771118164 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-28 | 18.170000076293945 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-28 | 20.219999313354492 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-28 | 14.319999694824219 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-28 | 90.83000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
