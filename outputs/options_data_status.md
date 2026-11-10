# Options / Volatility Structure Status

Generated at: `2026-11-10T11:47:52.601425+00:00`

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

- VIX: `20.030000686645508`
- VIX9D: `19.8799991607666`
- VIX3M: `20.850000381469727`
- VIX6M: `22.219999313354492`
- VVIX: `98.43000030517578`
- SKEW: `150.33999633789062`
- term_structure_state: `normal`
- volatility_reversal_score: `0.6705`
- panic_release_score: `0.5639`
- tail_risk_score: `0.5849`
- option_stress_score: `0.4691`
- failed_bounce_options_risk: `0.4625`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-09 | 150.33999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-10 | 20.030000686645508 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-09 | 20.850000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-09 | 22.219999313354492 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-09 | 19.8799991607666 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-09 | 98.43000030517578 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
