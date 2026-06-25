# Options / Volatility Structure Status

Generated at: `2026-06-25T23:56:17.150185+00:00`

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

- VIX: `18.889999389648438`
- VIX9D: `17.920000076293945`
- VIX3M: `20.329999923706055`
- VIX6M: `22.350000381469727`
- VVIX: `91.19000244140625`
- SKEW: `139.88999938964844`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5271`
- panic_release_score: `0.3871`
- tail_risk_score: `0.1675`
- option_stress_score: `0.4159`
- failed_bounce_options_risk: `0.3235`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-25 | 139.88999938964844 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-25 | 18.889999389648438 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-25 | 20.329999923706055 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-25 | 22.350000381469727 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-25 | 17.920000076293945 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-25 | 91.19000244140625 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
