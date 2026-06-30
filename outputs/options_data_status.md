# Options / Volatility Structure Status

Generated at: `2026-06-30T23:47:54.422165+00:00`

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

- VIX: `16.450000762939453`
- VIX9D: `13.729999542236328`
- VIX3M: `19.0`
- VIX6M: `21.5`
- VVIX: `86.87000274658203`
- SKEW: `149.60000610351562`
- term_structure_state: `contango`
- volatility_reversal_score: `0.95`
- panic_release_score: `0.7643`
- tail_risk_score: `0.3113`
- option_stress_score: `0.187`
- failed_bounce_options_risk: `0.2151`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-30 | 149.60000610351562 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-30 | 16.450000762939453 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-30 | 19.0 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-30 | 21.5 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-30 | 13.729999542236328 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-30 | 86.87000274658203 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
