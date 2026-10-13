# High Confidence Signal Report

Generated at: `2026-10-13T07:47:54.022395+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0017`, median `0.0051`, brier `0.1914`, calibration_gap `0.0233`
- 5d: hit_rate `0.7500`, avg `0.0043`, median `0.0068`, brier `0.1914`, calibration_gap `0.0233`
- 10d: hit_rate `0.5000`, avg `-0.0000`, median `-0.0047`, brier `0.3263`, calibration_gap `0.2733`
- 20d: hit_rate `0.8750`, avg `0.0250`, median `0.0240`, brier `0.1202`, calibration_gap `-0.1017`
- 60d: hit_rate `1.0000`, avg `0.0358`, median `0.0378`, brier `0.0514`, calibration_gap `-0.2267`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0076`, median `-0.0060`, brier `0.3807`, calibration_gap `0.3892`
- 5d: hit_rate `0.3750`, avg `-0.0115`, median `-0.0166`, brier `0.3807`, calibration_gap `0.3892`
- 10d: hit_rate `0.5000`, avg `-0.0123`, median `-0.0048`, brier `0.3197`, calibration_gap `0.2642`
- 20d: hit_rate `0.5625`, avg `0.0059`, median `0.0078`, brier `0.2823`, calibration_gap `0.2017`
- 60d: hit_rate `0.8125`, avg `0.0352`, median `0.0501`, brier `0.1534`, calibration_gap `-0.0483`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.3500`, avg `-0.0086`, median `-0.0060`, brier `0.3901`, calibration_gap `0.4093`
- 5d: hit_rate `0.4000`, avg `-0.0124`, median `-0.0166`, brier `0.3661`, calibration_gap `0.3593`
- 10d: hit_rate `0.4500`, avg `-0.0111`, median `-0.0071`, brier `0.3412`, calibration_gap `0.3093`
- 20d: hit_rate `0.6000`, avg `0.0088`, median `0.0095`, brier `0.2638`, calibration_gap `0.1593`
- 60d: hit_rate `0.7500`, avg `0.0306`, median `0.0434`, brier `0.1848`, calibration_gap `0.0093`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0075`, median `-0.0116`, brier `0.3149`, calibration_gap `0.2841`
- 5d: hit_rate `0.5000`, avg `-0.0057`, median `-0.0049`, brier `0.2763`, calibration_gap `0.1591`
- 10d: hit_rate `0.6250`, avg `0.0007`, median `0.0033`, brier `0.2356`, calibration_gap `0.0341`
- 20d: hit_rate `0.9375`, avg `0.0272`, median `0.0238`, brier `0.1359`, calibration_gap `-0.2784`
- 60d: hit_rate `0.8125`, avg `0.0841`, median `0.0748`, brier `0.1771`, calibration_gap `-0.1534`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
