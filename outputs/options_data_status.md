# Options / Volatility Structure Status

Generated at: `2026-10-20T01:45:47.769423+00:00`

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

- VIX: `18.440000534057617`
- VIX9D: `17.93000030517578`
- VIX3M: `19.600000381469727`
- VIX6M: `21.1200008392334`
- VVIX: `106.93000030517578`
- SKEW: `161.86000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5229`
- panic_release_score: `0.3604`
- tail_risk_score: `0.6818`
- option_stress_score: `0.5615`
- failed_bounce_options_risk: `0.5759`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-19 | 161.86000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-19 | 18.440000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-19 | 19.600000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-19 | 21.1200008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-19 | 17.93000030517578 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-19 | 106.93000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
