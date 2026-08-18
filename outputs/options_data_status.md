# Options / Volatility Structure Status

Generated at: `2026-08-18T23:11:04.223445+00:00`

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

- VIX: `15.84000015258789`
- VIX9D: `13.59000015258789`
- VIX3M: `19.270000457763672`
- VIX6M: `21.3700008392334`
- VVIX: `92.87000274658203`
- SKEW: `143.60000610351562`
- term_structure_state: `contango`
- volatility_reversal_score: `0.621`
- panic_release_score: `0.4056`
- tail_risk_score: `0.2967`
- option_stress_score: `0.2979`
- failed_bounce_options_risk: `0.2872`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-18 | 143.60000610351562 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-18 | 15.84000015258789 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-18 | 19.270000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-18 | 21.3700008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-18 | 13.59000015258789 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-18 | 92.87000274658203 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
