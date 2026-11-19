# Options / Volatility Structure Status

Generated at: `2026-11-19T04:07:07.895802+00:00`

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

- VIX: `24.559999465942383`
- VIX9D: `23.950000762939453`
- VIX3M: `24.290000915527344`
- VIX6M: `24.75`
- VVIX: `118.37000274658203`
- SKEW: `142.83999633789062`
- term_structure_state: `backwardation`
- volatility_reversal_score: `0.191`
- panic_release_score: `0.376`
- tail_risk_score: `0.6711`
- option_stress_score: `0.7689`
- failed_bounce_options_risk: `0.9159`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-18 | 142.83999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-18 | 24.559999465942383 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-18 | 24.290000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-18 | 24.75 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-18 | 23.950000762939453 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-18 | 118.37000274658203 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
