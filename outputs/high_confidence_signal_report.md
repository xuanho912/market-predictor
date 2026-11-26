# High Confidence Signal Report

Generated at: `2026-11-26T21:35:41.170447+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0047`, median `-0.0028`, brier `0.3860`, calibration_gap `0.3949`
- 5d: hit_rate `0.3750`, avg `0.0037`, median `-0.0078`, brier `0.3871`, calibration_gap `0.3949`
- 10d: hit_rate `0.6250`, avg `0.0094`, median `0.0070`, brier `0.2559`, calibration_gap `0.1449`
- 20d: hit_rate `0.3750`, avg `0.0011`, median `-0.0094`, brier `0.3860`, calibration_gap `0.3949`
- 60d: hit_rate `0.7500`, avg `0.0471`, median `0.0694`, brier `0.1940`, calibration_gap `0.0199`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0011`, median `-0.0024`, brier `0.3510`, calibration_gap `0.3239`
- 5d: hit_rate `0.4375`, avg `0.0040`, median `-0.0031`, brier `0.3497`, calibration_gap `0.3239`
- 10d: hit_rate `0.5625`, avg `0.0009`, median `0.0060`, brier `0.2857`, calibration_gap `0.1989`
- 20d: hit_rate `0.5000`, avg `-0.0049`, median `0.0010`, brier `0.3192`, calibration_gap `0.2614`
- 60d: hit_rate `0.8125`, avg `0.0454`, median `0.0703`, brier `0.1593`, calibration_gap `-0.0511`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0042`, median `0.0072`, brier `0.2351`, calibration_gap `-0.0258`
- 5d: hit_rate `0.6250`, avg `-0.0044`, median `0.0048`, brier `0.2356`, calibration_gap `-0.0258`
- 10d: hit_rate `0.6250`, avg `0.0049`, median `0.0309`, brier `0.2351`, calibration_gap `-0.0258`
- 20d: hit_rate `0.4375`, avg `-0.0166`, median `-0.0056`, brier `0.2732`, calibration_gap `0.1617`
- 60d: hit_rate `0.6250`, avg `0.0471`, median `0.0533`, brier `0.2323`, calibration_gap `-0.0258`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
