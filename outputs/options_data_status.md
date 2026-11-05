# Options / Volatility Structure Status

Generated at: `2026-11-05T20:01:02.846265+00:00`

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

- VIX: `24.6200008392334`
- VIX9D: `27.290000915527344`
- VIX3M: `23.6200008392334`
- VIX6M: `24.149999618530273`
- VVIX: `117.93000030517578`
- SKEW: `150.89999389648438`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1919`
- panic_release_score: `0.3819`
- tail_risk_score: `0.9145`
- option_stress_score: `0.9137`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-04 | 150.89999389648438 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-05 | 24.6200008392334 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-05 | 23.6200008392334 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-05 | 24.149999618530273 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-05 | 27.290000915527344 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-05 | 117.93000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
