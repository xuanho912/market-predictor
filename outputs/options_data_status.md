# Options / Volatility Structure Status

Generated at: `2026-11-06T01:02:15.601637+00:00`

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

- VIX: `28.18000030517578`
- VIX9D: `32.65999984741211`
- VIX3M: `25.549999237060547`
- VIX6M: `25.290000915527344`
- VVIX: `134.99000549316406`
- SKEW: `149.3699951171875`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1986`
- panic_release_score: `0.4236`
- tail_risk_score: `0.9223`
- option_stress_score: `0.9305`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-05 | 149.3699951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-05 | 28.18000030517578 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-05 | 25.549999237060547 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-05 | 25.290000915527344 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-05 | 32.65999984741211 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-05 | 134.99000549316406 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
