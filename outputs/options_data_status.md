# Options / Volatility Structure Status

Generated at: `2026-07-14T14:16:43.590620+00:00`

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

- VIX: `16.399999618530273`
- VIX9D: `13.869999885559082`
- VIX3M: `19.280000686645508`
- VIX6M: `21.440000534057617`
- VVIX: `93.1500015258789`
- SKEW: `145.69000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.628`
- panic_release_score: `0.41`
- tail_risk_score: `0.3302`
- option_stress_score: `0.3443`
- failed_bounce_options_risk: `0.3122`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-13 | 145.69000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-14 | 16.399999618530273 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-14 | 19.280000686645508 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-14 | 21.440000534057617 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-14 | 13.869999885559082 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-14 | 93.1500015258789 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
