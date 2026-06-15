# Options / Volatility Structure Status

Generated at: `2026-06-15T15:10:54.293804+00:00`

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

- VIX: `16.229999542236328`
- VIX9D: `15.300000190734863`
- VIX3M: `19.649999618530273`
- VIX6M: `22.030000686645508`
- VVIX: `90.54000091552734`
- SKEW: `142.60000610351562`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.2005`
- option_stress_score: `0.1256`
- failed_bounce_options_risk: `0.1592`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-06-12 | 142.60000610351562 | yahoo-chart | True | False |
| ^VIX | available | 2026-06-15 | 16.229999542236328 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-06-15 | 19.649999618530273 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-06-15 | 22.030000686645508 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-06-15 | 15.300000190734863 | yahoo-chart | True | False |
| ^VVIX | available | 2026-06-15 | 90.54000091552734 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
