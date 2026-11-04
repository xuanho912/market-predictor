# Options / Volatility Structure Status

Generated at: `2026-11-04T19:49:58.538877+00:00`

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

- VIX: `16.81999969482422`
- VIX9D: `15.630000114440918`
- VIX3M: `18.940000534057617`
- VIX6M: `20.809999465942383`
- VVIX: `90.95999908447266`
- SKEW: `150.00999450683594`
- term_structure_state: `contango`
- volatility_reversal_score: `0.515`
- panic_release_score: `0.3429`
- tail_risk_score: `0.4225`
- option_stress_score: `0.2867`
- failed_bounce_options_risk: `0.2922`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-03 | 150.00999450683594 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-04 | 16.81999969482422 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-04 | 18.940000534057617 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-04 | 20.809999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-04 | 15.630000114440918 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-04 | 90.95999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
