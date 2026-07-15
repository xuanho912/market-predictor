# Options / Volatility Structure Status

Generated at: `2026-07-15T14:12:42.198227+00:00`

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

- VIX: `16.09000015258789`
- VIX9D: `12.739999771118164`
- VIX3M: `19.15999984741211`
- VIX6M: `21.34000015258789`
- VVIX: `94.26000213623047`
- SKEW: `145.69000244140625`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6657`
- panic_release_score: `0.4351`
- tail_risk_score: `0.3483`
- option_stress_score: `0.2006`
- failed_bounce_options_risk: `0.23`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-13 | 145.69000244140625 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-15 | 16.09000015258789 | local-cache-yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-15 | 19.15999984741211 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-15 | 21.34000015258789 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-15 | 12.739999771118164 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-15 | 94.26000213623047 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
