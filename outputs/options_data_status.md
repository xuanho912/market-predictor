# Options / Volatility Structure Status

Generated at: `2026-09-03T01:07:26.930567+00:00`

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

- VIX: `15.199999809265137`
- VIX9D: `12.569999694824219`
- VIX3M: `17.729999542236328`
- VIX6M: `20.360000610351562`
- VVIX: `86.25`
- SKEW: `144.1199951171875`
- term_structure_state: `contango`
- volatility_reversal_score: `0.6717`
- panic_release_score: `0.447`
- tail_risk_score: `0.2383`
- option_stress_score: `0.1182`
- failed_bounce_options_risk: `0.1627`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-09-02 | 144.1199951171875 | yahoo-chart | True | False |
| ^VIX | available | 2026-09-02 | 15.199999809265137 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-09-02 | 17.729999542236328 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-09-02 | 20.360000610351562 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-09-02 | 12.569999694824219 | yahoo-chart | True | False |
| ^VVIX | available | 2026-09-02 | 86.25 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
