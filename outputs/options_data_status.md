# Options / Volatility Structure Status

Generated at: `2026-11-20T20:25:08.568456+00:00`

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

- VIX: `35.189998626708984`
- VIX9D: `37.72999954223633`
- VIX3M: `30.670000076293945`
- VIX6M: `29.639999389648438`
- VVIX: `135.3699951171875`
- SKEW: `140.86000061035156`
- term_structure_state: `stress`
- volatility_reversal_score: `0.2`
- panic_release_score: `0.4325`
- tail_risk_score: `0.7407`
- option_stress_score: `0.879`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-19 | 140.86000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-20 | 35.189998626708984 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-20 | 30.670000076293945 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-20 | 29.639999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-20 | 37.72999954223633 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-20 | 135.3699951171875 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
