# Options / Volatility Structure Status

Generated at: `2026-08-17T20:51:33.962795+00:00`

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

- VIX: `15.1899995803833`
- VIX9D: `12.390000343322754`
- VIX3M: `19.040000915527344`
- VIX6M: `21.329999923706055`
- VVIX: `93.91999816894531`
- SKEW: `138.36000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.845`
- panic_release_score: `0.5848`
- tail_risk_score: `0.2083`
- option_stress_score: `0.0967`
- failed_bounce_options_risk: `0.1448`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-14 | 138.36000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-17 | 15.1899995803833 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-17 | 19.040000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-17 | 21.329999923706055 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-17 | 12.390000343322754 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-17 | 93.91999816894531 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
