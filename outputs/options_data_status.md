# Options / Volatility Structure Status

Generated at: `2026-10-02T17:54:38.803599+00:00`

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

- VIX: `15.800000190734863`
- VIX9D: `12.930000305175781`
- VIX3M: `18.350000381469727`
- VIX6M: `20.399999618530273`
- VVIX: `89.29000091552734`
- SKEW: `142.77000427246094`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5`
- panic_release_score: `0.33`
- tail_risk_score: `0.2439`
- option_stress_score: `0.2845`
- failed_bounce_options_risk: `0.2785`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-01 | 142.77000427246094 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-02 | 15.800000190734863 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-02 | 18.350000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-02 | 20.399999618530273 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-02 | 12.930000305175781 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-02 | 89.29000091552734 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
