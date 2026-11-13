# Options / Volatility Structure Status

Generated at: `2026-11-13T19:45:44.227836+00:00`

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

- VIX: `18.940000534057617`
- VIX9D: `17.280000686645508`
- VIX3M: `20.450000762939453`
- VIX6M: `21.920000076293945`
- VVIX: `102.68000030517578`
- SKEW: `150.16000366210938`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.8461`
- tail_risk_score: `0.5891`
- option_stress_score: `0.3803`
- failed_bounce_options_risk: `0.377`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-12 | 150.16000366210938 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-13 | 18.940000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-13 | 20.450000762939453 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-13 | 21.920000076293945 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-13 | 17.280000686645508 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-13 | 102.68000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
