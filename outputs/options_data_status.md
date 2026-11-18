# Options / Volatility Structure Status

Generated at: `2026-11-18T03:57:11.171705+00:00`

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

- VIX: `25.459999084472656`
- VIX9D: `26.700000762939453`
- VIX3M: `24.979999542236328`
- VIX6M: `25.3700008392334`
- VVIX: `121.27999877929688`
- SKEW: `145.11000061035156`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1933`
- panic_release_score: `0.3908`
- tail_risk_score: `0.8018`
- option_stress_score: `0.8695`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-17 | 145.11000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-17 | 25.459999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-17 | 24.979999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-17 | 25.3700008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-17 | 26.700000762939453 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-17 | 121.27999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
