# Options / Volatility Structure Status

Generated at: `2026-07-09T15:37:07.856066+00:00`

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

- VIX: `16.290000915527344`
- VIX9D: `13.470000267028809`
- VIX3M: `19.1299991607666`
- VIX6M: `21.329999923706055`
- VVIX: `90.02999877929688`
- SKEW: `149.7899932861328`
- term_structure_state: `contango`
- volatility_reversal_score: `0.85`
- panic_release_score: `0.5966`
- tail_risk_score: `0.3429`
- option_stress_score: `0.1955`
- failed_bounce_options_risk: `0.2261`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-08 | 149.7899932861328 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-09 | 16.290000915527344 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-09 | 19.1299991607666 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-09 | 21.329999923706055 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-09 | 13.470000267028809 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-09 | 90.02999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
