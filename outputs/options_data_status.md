# Options / Volatility Structure Status

Generated at: `2026-11-11T19:38:36.508645+00:00`

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

- VIX: `17.6200008392334`
- VIX9D: `16.290000915527344`
- VIX3M: `19.530000686645508`
- VIX6M: `21.280000686645508`
- VVIX: `92.45999908447266`
- SKEW: `151.1199951171875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5086`
- panic_release_score: `0.2711`
- tail_risk_score: `0.4656`
- option_stress_score: `0.4674`
- failed_bounce_options_risk: `0.4255`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-10 | 151.1199951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-11 | 17.6200008392334 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-11 | 19.530000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-11 | 21.280000686645508 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-11 | 16.290000915527344 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-11 | 92.45999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
