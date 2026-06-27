# Options / Volatility Structure Status

Generated at: `2026-06-27T05:06:03.827194+00:00`

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

- VIX: `18.40999984741211`
- VIX9D: `13.930000305175781`
- VIX3M: `19.56999969482422`
- VIX6M: `21.989999771118164`
- VVIX: `89.0199966430664`
- SKEW: `139.88999938964844`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5219`
- panic_release_score: `0.3544`
- tail_risk_score: `0.1344`
- option_stress_score: `0.3953`
- failed_bounce_options_risk: `0.3445`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-25 | 139.88999938964844 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-26 | 18.40999984741211 | local-cache-yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-18 | 19.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-18 | 21.989999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-18 | 13.930000305175781 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-26 | 89.0199966430664 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
