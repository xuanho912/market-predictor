# Options / Volatility Structure Status

Generated at: `2026-11-20T02:33:54.115087+00:00`

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

- VIX: `28.440000534057617`
- VIX9D: `29.260000228881836`
- VIX3M: `27.030000686645508`
- VIX6M: `26.850000381469727`
- VVIX: `127.0999984741211`
- SKEW: `140.86000061035156`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1986`
- panic_release_score: `0.4236`
- tail_risk_score: `0.7205`
- option_stress_score: `0.8603`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-19 | 140.86000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-19 | 28.440000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-19 | 27.030000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-19 | 26.850000381469727 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-19 | 29.260000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-19 | 127.0999984741211 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
