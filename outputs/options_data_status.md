# Options / Volatility Structure Status

Generated at: `2026-07-08T04:36:08.980101+00:00`

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

- VIX: `16.1299991607666`
- VIX9D: `12.369999885559082`
- VIX3M: `19.040000915527344`
- VIX6M: `21.5`
- VVIX: `87.9000015258789`
- SKEW: `145.74000549316406`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.2556`
- option_stress_score: `0.1408`
- failed_bounce_options_risk: `0.1786`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-07 | 145.74000549316406 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-07 | 16.1299991607666 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-02 | 19.040000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-02 | 21.5 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-02 | 12.369999885559082 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-07 | 87.9000015258789 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
