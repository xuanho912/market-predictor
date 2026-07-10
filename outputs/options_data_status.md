# Options / Volatility Structure Status

Generated at: `2026-07-10T15:04:21.877978+00:00`

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

- VIX: `15.680000305175781`
- VIX9D: `12.539999961853027`
- VIX3M: `18.989999771118164`
- VIX6M: `21.350000381469727`
- VVIX: `88.94000244140625`
- SKEW: `144.6699981689453`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8783`
- panic_release_score: `0.78`
- tail_risk_score: `0.241`
- option_stress_score: `0.1085`
- failed_bounce_options_risk: `0.1579`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-09 | 144.6699981689453 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-10 | 15.680000305175781 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-10 | 18.989999771118164 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-10 | 21.350000381469727 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-10 | 12.539999961853027 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-10 | 88.94000244140625 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
