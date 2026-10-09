# Options / Volatility Structure Status

Generated at: `2026-10-09T18:23:57.468195+00:00`

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

- VIX: `14.880000114440918`
- VIX9D: `11.100000381469727`
- VIX3M: `17.850000381469727`
- VIX6M: `19.950000762939453`
- VVIX: `86.08000183105469`
- SKEW: `149.19000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6677`
- panic_release_score: `0.4514`
- tail_risk_score: `0.3454`
- option_stress_score: `0.1384`
- failed_bounce_options_risk: `0.1952`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-08 | 149.19000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-09 | 14.880000114440918 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-09 | 17.850000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-09 | 19.950000762939453 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-09 | 11.100000381469727 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-09 | 86.08000183105469 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
