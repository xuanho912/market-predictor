# Options / Volatility Structure Status

Generated at: `2026-07-07T15:17:42.695027+00:00`

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

- VIX: `16.450000762939453`
- VIX9D: `13.890000343322754`
- VIX3M: `19.270000457763672`
- VIX6M: `21.559999465942383`
- VVIX: `90.11000061035156`
- SKEW: `145.3800048828125`
- term_structure_state: `contango`
- volatility_reversal_score: `1.0`
- panic_release_score: `0.78`
- tail_risk_score: `0.2718`
- option_stress_score: `0.1762`
- failed_bounce_options_risk: `0.2013`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-06 | 145.3800048828125 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-07 | 16.450000762939453 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-07 | 19.270000457763672 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-07 | 21.559999465942383 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-07 | 13.890000343322754 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-07 | 90.11000061035156 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
