# Options / Volatility Structure Status

Generated at: `2026-10-06T10:48:27.143518+00:00`

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

- VIX: `15.380000114440918`
- VIX9D: `12.850000381469727`
- VIX3M: `18.0`
- VIX6M: `20.06999969482422`
- VVIX: `85.45999908447266`
- SKEW: `143.0399932861328`
- term_structure_state: `contango`
- volatility_reversal_score: `0.644`
- panic_release_score: `0.4455`
- tail_risk_score: `0.2036`
- option_stress_score: `0.1206`
- failed_bounce_options_risk: `0.157`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-05 | 143.0399932861328 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-06 | 15.380000114440918 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-05 | 18.0 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-05 | 20.06999969482422 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-05 | 12.850000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-05 | 85.45999908447266 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
