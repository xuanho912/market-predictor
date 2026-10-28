# Options / Volatility Structure Status

Generated at: `2026-10-28T18:23:35.093973+00:00`

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

- VIX: `17.290000915527344`
- VIX9D: `16.43000030517578`
- VIX3M: `19.309999465942383`
- VIX6M: `21.260000228881836`
- VVIX: `97.05000305175781`
- SKEW: `149.22000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5043`
- panic_release_score: `0.33`
- tail_risk_score: `0.5084`
- option_stress_score: `0.463`
- failed_bounce_options_risk: `0.4216`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-27 | 149.22000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-28 | 17.290000915527344 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-28 | 19.309999465942383 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-28 | 21.260000228881836 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-28 | 16.43000030517578 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-28 | 97.05000305175781 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
