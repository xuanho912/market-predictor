# Options / Volatility Structure Status

Generated at: `2026-11-27T03:46:59.136690+00:00`

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

- VIX: `26.799999237060547`
- VIX9D: `29.610000610351562`
- VIX3M: `26.290000915527344`
- VIX6M: `26.889999389648438`
- VVIX: `115.37999725341797`
- SKEW: `142.05999755859375`
- term_structure_state: `stress`
- volatility_reversal_score: `0.4681`
- panic_release_score: `0.634`
- tail_risk_score: `0.7229`
- option_stress_score: `0.7157`
- failed_bounce_options_risk: `0.7846`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-25 | 142.05999755859375 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-26 | 26.799999237060547 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-25 | 26.290000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-25 | 26.889999389648438 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-25 | 29.610000610351562 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-25 | 115.37999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
