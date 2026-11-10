# Options / Volatility Structure Status

Generated at: `2026-11-10T19:46:52.599815+00:00`

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

- VIX: `19.989999771118164`
- VIX9D: `19.18000030517578`
- VIX3M: `21.049999237060547`
- VIX6M: `22.31999969482422`
- VVIX: `99.1500015258789`
- SKEW: `150.33999633789062`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6767`
- panic_release_score: `0.5667`
- tail_risk_score: `0.5535`
- option_stress_score: `0.4192`
- failed_bounce_options_risk: `0.3912`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-09 | 150.33999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-10 | 19.989999771118164 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-10 | 21.049999237060547 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-10 | 22.31999969482422 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-10 | 19.18000030517578 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-10 | 99.1500015258789 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
