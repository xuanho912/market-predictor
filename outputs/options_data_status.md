# Options / Volatility Structure Status

Generated at: `2026-07-14T00:04:15.218631+00:00`

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

- VIX: `17.15999984741211`
- VIX9D: `15.130000114440918`
- VIX3M: `19.639999389648438`
- VIX6M: `21.690000534057617`
- VVIX: `95.27999877929688`
- SKEW: `145.69000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.7285`
- panic_release_score: `0.4725`
- tail_risk_score: `0.3648`
- option_stress_score: `0.3955`
- failed_bounce_options_risk: `0.3802`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-13 | 145.69000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-13 | 17.15999984741211 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-13 | 19.639999389648438 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-13 | 21.690000534057617 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-13 | 15.130000114440918 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-13 | 95.27999877929688 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
