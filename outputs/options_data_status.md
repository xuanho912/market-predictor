# Options / Volatility Structure Status

Generated at: `2026-07-07T05:10:38.370324+00:00`

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

- VIX: `15.569999694824219`
- VIX9D: `12.369999885559082`
- VIX3M: `19.040000915527344`
- VIX6M: `21.5`
- VVIX: `87.08999633789062`
- SKEW: `145.3800048828125`
- term_structure_state: `contango`
- volatility_reversal_score: `0.95`
- panic_release_score: `0.7357`
- tail_risk_score: `0.2417`
- option_stress_score: `0.1106`
- failed_bounce_options_risk: `0.1592`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-07-06 | 145.3800048828125 | yahoo-chart | True | False |
| ^VIX | available | 2026-07-06 | 15.569999694824219 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-07-02 | 19.040000915527344 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-07-02 | 21.5 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-07-02 | 12.369999885559082 | yahoo-chart | True | False |
| ^VVIX | available | 2026-07-06 | 87.08999633789062 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
