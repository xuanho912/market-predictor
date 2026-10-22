# Options / Volatility Structure Status

Generated at: `2026-10-22T17:13:56.675825+00:00`

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

- VIX: `18.940000534057617`
- VIX9D: `18.510000228881836`
- VIX3M: `20.100000381469727`
- VIX6M: `21.6299991607666`
- VVIX: `104.29000091552734`
- SKEW: `150.36000061035156`
- term_structure_state: `contango`
- volatility_reversal_score: `0.5305`
- panic_release_score: `0.408`
- tail_risk_score: `0.6139`
- option_stress_score: `0.5566`
- failed_bounce_options_risk: `0.5409`

## Sources

| symbol | status | latest_date | latest_value | source | real_data | stale |
|---|---|---|---:|---|---:|---:|
| ^SKEW | available | 2026-10-21 | 150.36000061035156 | yahoo-chart | True | False |
| ^VIX | available | 2026-10-22 | 18.940000534057617 | yahoo-chart | True | False |
| ^VIX3M | available | 2026-10-22 | 20.100000381469727 | yahoo-chart | True | False |
| ^VIX6M | available | 2026-10-22 | 21.6299991607666 | yahoo-chart | True | False |
| ^VIX9D | available | 2026-10-22 | 18.510000228881836 | yahoo-chart | True | False |
| ^VVIX | available | 2026-10-22 | 104.29000091552734 | yahoo-chart | True | False |

## Guardrails

- If only VIX term data is available, options coverage is partial, not full.
- Missing put/call and gamma are explicit missing evidence; they are not inferred.
- Options structure can change path weights and risk, but it does not change Alpha v1.
