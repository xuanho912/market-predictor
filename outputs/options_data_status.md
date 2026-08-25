# Options / Volatility Structure Status

Generated at: `2026-08-25T04:23:49.685966+00:00`

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

- VIX: `15.850000381469727`
- VIX9D: `14.069999694824219`
- VIX3M: `18.559999465942383`
- VIX6M: `21.040000915527344`
- VVIX: `88.63999938964844`
- SKEW: `145.63999938964844`
- term_structure_state: `contango`
- volatility_reversal_score: `0.782`
- panic_release_score: `0.5062`
- tail_risk_score: `0.2829`
- option_stress_score: `0.2837`
- failed_bounce_options_risk: `0.2791`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-24 | 145.63999938964844 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-24 | 15.850000381469727 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-08-24 | 18.559999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-08-24 | 21.040000915527344 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-08-24 | 14.069999694824219 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-24 | 88.63999938964844 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
