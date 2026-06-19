# Options / Volatility Structure Status

Generated at: `2026-06-19T00:14:21.238999+00:00`

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
- VIX9D: `13.930000305175781`
- VIX3M: `19.56999969482422`
- VIX6M: `21.989999771118164`
- VVIX: `88.43000030517578`
- SKEW: `146.72000122070312`
- term_structure_state: `contango`
- volatility_reversal_score: `0.986`
- panic_release_score: `0.78`
- tail_risk_score: `0.2733`
- option_stress_score: `0.169`
- failed_bounce_options_risk: `0.1976`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-18 | 146.72000122070312 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-18 | 16.399999618530273 | local-cache-yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-18 | 19.56999969482422 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-18 | 21.989999771118164 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-18 | 13.930000305175781 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-18 | 88.43000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
