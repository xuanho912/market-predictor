# Options / Volatility Structure Status

Generated at: `2026-09-16T23:48:40.274794+00:00`

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

- VIX: `17.709999084472656`
- VIX9D: `17.399999618530273`
- VIX3M: `19.729999542236328`
- VIX6M: `21.030000686645508`
- VVIX: `95.41000366210938`
- SKEW: `145.9499969482422`
- term_structure_state: `contango`
- volatility_reversal_score: `0.51`
- panic_release_score: `0.28`
- tail_risk_score: `0.4256`
- option_stress_score: `0.4583`
- failed_bounce_options_risk: `0.4184`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-16 | 145.9499969482422 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-16 | 17.709999084472656 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-16 | 19.729999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-16 | 21.030000686645508 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-16 | 17.399999618530273 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-16 | 95.41000366210938 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
