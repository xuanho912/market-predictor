# Options / Volatility Structure Status

Generated at: `2026-11-19T20:40:46.142639+00:00`

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

- VIX: `27.989999771118164`
- VIX9D: `28.219999313354492`
- VIX3M: `26.719999313354492`
- VIX6M: `26.610000610351562`
- VVIX: `127.30999755859375`
- SKEW: `142.83999633789062`
- term_structure_state: `stress`
- volatility_reversal_score: `0.1981`
- panic_release_score: `0.4206`
- tail_risk_score: `0.7555`
- option_stress_score: `0.8649`
- failed_bounce_options_risk: `1.0`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-11-18 | 142.83999633789062 | yahoo-chart | True | False |
| ^VIX | available | 2026-11-19 | 27.989999771118164 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-11-19 | 26.719999313354492 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-11-19 | 26.610000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-11-19 | 28.219999313354492 | yahoo-chart | True | False |
| ^VVIX | available | 2026-11-19 | 127.30999755859375 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
