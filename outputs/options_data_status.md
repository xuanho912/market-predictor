# Options / Volatility Structure Status

Generated at: `2026-11-11T07:47:49.828477+00:00`

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

- VIX: `19.459999084472656`
- VIX9D: `18.540000915527344`
- VIX3M: `20.639999389648438`
- VIX6M: `21.989999771118164`
- VVIX: `96.62999725341797`
- SKEW: `151.1199951171875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7602`
- panic_release_score: `0.6126`
- tail_risk_score: `0.526`
- option_stress_score: `0.3936`
- failed_bounce_options_risk: `0.3717`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-10 | 151.1199951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-10 | 19.459999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-10 | 20.639999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-10 | 21.989999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-10 | 18.540000915527344 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-10 | 96.62999725341797 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
