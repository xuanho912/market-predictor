# Options / Volatility Structure Status

Generated at: `2026-08-07T05:24:56.231984+00:00`

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

- VIX: `15.149999618530273`
- VIX9D: `16.850000381469727`
- VIX3M: `20.540000915527344`
- VIX6M: `22.280000686645508`
- VVIX: `88.72000122070312`
- SKEW: `134.72999572753906`
- term_structure_state: `contango`
- volatility_reversal_score: `0.8923`
- panic_release_score: `0.6503`
- tail_risk_score: `0.1095`
- option_stress_score: `0.0702`
- failed_bounce_options_risk: `0.1212`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-08-06 | 134.72999572753906 | yahoo-chart | True | False |
| ^VIX | available | 2026-08-06 | 15.149999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-17 | 20.540000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-17 | 22.280000686645508 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-17 | 16.850000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-08-06 | 88.72000122070312 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
