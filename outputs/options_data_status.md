# Options / Volatility Structure Status

Generated at: `2026-11-17T20:58:22.586796+00:00`

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

- VIX: `25.719999313354492`
- VIX9D: `26.829999923706055`
- VIX3M: `25.100000381469727`
- VIX6M: `25.3700008392334`
- VVIX: `123.2300033569336`
- SKEW: `146.3300018310547`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1943`
- panic_release_score: `0.3968`
- tail_risk_score: `0.8373`
- option_stress_score: `0.8823`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-16 | 146.3300018310547 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-17 | 25.719999313354492 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-17 | 25.100000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-17 | 25.3700008392334 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-17 | 26.829999923706055 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-17 | 123.2300033569336 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
