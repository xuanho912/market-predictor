# Options / Volatility Structure Status

Generated at: `2026-10-23T08:52:33.039933+00:00`

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

- VIX: `18.8799991607666`
- VIX9D: `18.860000610351562`
- VIX3M: `20.1200008392334`
- VIX6M: `21.65999984741211`
- VVIX: `107.94000244140625`
- SKEW: `152.38999938964844`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7136`
- panic_release_score: `0.5546`
- tail_risk_score: `0.6485`
- option_stress_score: `0.4273`
- failed_bounce_options_risk: `0.4147`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-22 | 152.38999938964844 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-23 | 18.8799991607666 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-22 | 20.1200008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-22 | 21.65999984741211 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-22 | 18.860000610351562 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-22 | 107.94000244140625 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
