# Options / Volatility Structure Status

Generated at: `2026-09-02T01:01:03.464882+00:00`

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

- VIX: `16.34000015258789`
- VIX9D: `14.329999923706055`
- VIX3M: `18.329999923706055`
- VIX6M: `20.559999465942383`
- VVIX: `91.25`
- SKEW: `149.22999572753906`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.3967`
- option_stress_score: `0.3621`
- failed_bounce_options_risk: `0.3408`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-01 | 149.22999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-01 | 16.34000015258789 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-01 | 18.329999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-01 | 20.559999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-01 | 14.329999923706055 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-01 | 91.25 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
