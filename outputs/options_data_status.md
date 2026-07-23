# Options / Volatility Structure Status

Generated at: `2026-07-23T00:12:14.742360+00:00`

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

- VIX: `16.639999389648438`
- VIX9D: `14.880000114440918`
- VIX3M: `19.540000915527344`
- VIX6M: `21.68000030517578`
- VVIX: `95.55000305175781`
- SKEW: `150.19000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.785`
- panic_release_score: `0.5081`
- tail_risk_score: `0.4438`
- option_stress_score: `0.3877`
- failed_bounce_options_risk: `0.3762`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-22 | 150.19000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-22 | 16.639999389648438 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-22 | 19.540000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-22 | 21.68000030517578 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-22 | 14.880000114440918 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-22 | 95.55000305175781 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
