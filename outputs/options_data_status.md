# Options / Volatility Structure Status

Generated at: `2026-11-06T19:27:47.049056+00:00`

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

- VIX: `24.459999084472656`
- VIX9D: `26.299999237060547`
- VIX3M: `23.6200008392334`
- VIX6M: `24.06999969482422`
- VVIX: `119.06999969482422`
- SKEW: `149.3699951171875`
- term_structure_state: `stress`
- volatility_reversal_score: `0.191`
- panic_release_score: `0.376`
- tail_risk_score: `0.888`
- option_stress_score: `0.8972`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-05 | 149.3699951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-06 | 24.459999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-06 | 23.6200008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-06 | 24.06999969482422 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-06 | 26.299999237060547 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-06 | 119.06999969482422 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
