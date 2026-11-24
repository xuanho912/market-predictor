# Options / Volatility Structure Status

Generated at: `2026-11-24T14:17:35.619637+00:00`

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

- VIX: `29.56999969482422`
- VIX9D: `27.760000228881836`
- VIX3M: `25.5`
- VIX6M: `25.959999084472656`
- VVIX: `117.36000061035156`
- SKEW: `140.3699951171875`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1986`
- panic_release_score: `0.4236`
- tail_risk_score: `0.7078`
- option_stress_score: `0.8662`
- failed_bounce_options_risk: `0.9707`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-23 | 140.3699951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-24 | 29.56999969482422 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-23 | 25.5 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-23 | 25.959999084472656 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-23 | 27.760000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-23 | 117.36000061035156 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
