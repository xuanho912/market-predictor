# Options / Volatility Structure Status

Generated at: `2026-09-03T16:28:10.557575+00:00`

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

- VIX: `14.609999656677246`
- VIX9D: `12.109999656677246`
- VIX3M: `17.579999923706055`
- VIX6M: `19.889999389648438`
- VVIX: `85.06999969482422`
- SKEW: `144.1199951171875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.554`
- panic_release_score: `0.3637`
- tail_risk_score: `0.2263`
- option_stress_score: `0.22`
- failed_bounce_options_risk: `0.2188`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-02 | 144.1199951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-03 | 14.609999656677246 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-03 | 17.579999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-03 | 19.889999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-03 | 12.109999656677246 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-03 | 85.06999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
