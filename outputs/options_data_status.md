# Options / Volatility Structure Status

Generated at: `2026-07-15T22:35:44.481870+00:00`

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

- VIX: `15.670000076293945`
- VIX9D: `12.0600004196167`
- VIX3M: `18.90999984741211`
- VIX6M: `21.229999542236328`
- VVIX: `91.8499984741211`
- SKEW: `148.50999450683594`
- term_structure_state: `contango`
- volatility_reversal_score: `0.758`
- panic_release_score: `0.5388`
- tail_risk_score: `0.3551`
- option_stress_score: `0.1681`
- failed_bounce_options_risk: `0.2135`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-15 | 148.50999450683594 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-15 | 15.670000076293945 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-15 | 18.90999984741211 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-15 | 21.229999542236328 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-15 | 12.0600004196167 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-15 | 91.8499984741211 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
