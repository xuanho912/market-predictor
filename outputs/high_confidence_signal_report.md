# High Confidence Signal Report

Generated at: `2026-07-05T15:36:30.738398+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0112`, median `-0.0097`, brier `0.4044`, calibration_gap `0.4609`
- 5d: hit_rate `0.3750`, avg `-0.0095`, median `-0.0114`, brier `0.3535`, calibration_gap `0.3359`
- 10d: hit_rate `0.2500`, avg `-0.0083`, median `-0.0128`, brier `0.4023`, calibration_gap `0.4609`
- 20d: hit_rate `0.6250`, avg `0.0035`, median `0.0108`, brier `0.2364`, calibration_gap `0.0859`
- 60d: hit_rate `0.3750`, avg `-0.0184`, median `-0.0378`, brier `0.3398`, calibration_gap `0.3359`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0060`, median `-0.0022`, brier `0.3697`, calibration_gap `0.3899`
- 5d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0005`, brier `0.2967`, calibration_gap `0.2024`
- 10d: hit_rate `0.4375`, avg `0.0015`, median `-0.0010`, brier `0.3199`, calibration_gap `0.2649`
- 20d: hit_rate `0.6250`, avg `0.0078`, median `0.0126`, brier `0.2382`, calibration_gap `0.0774`
- 60d: hit_rate `0.4375`, avg `-0.0018`, median `-0.0282`, brier `0.3136`, calibration_gap `0.2649`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.3500`, avg `-0.0089`, median `-0.0101`, brier `0.3499`, calibration_gap `0.3456`
- 5d: hit_rate `0.3000`, avg `-0.0112`, median `-0.0106`, brier `0.3667`, calibration_gap `0.3956`
- 10d: hit_rate `0.2500`, avg `-0.0066`, median `-0.0069`, brier `0.3883`, calibration_gap `0.4456`
- 20d: hit_rate `0.7500`, avg `0.0155`, median `0.0209`, brier `0.1908`, calibration_gap `-0.0544`
- 60d: hit_rate `0.7000`, avg `0.0363`, median `0.0528`, brier `0.2113`, calibration_gap `-0.0044`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0046`, median `-0.0022`, brier `0.2692`, calibration_gap `0.1379`
- 5d: hit_rate `0.4375`, avg `-0.0014`, median `-0.0140`, brier `0.2858`, calibration_gap `0.2004`
- 10d: hit_rate `0.3125`, avg `-0.0040`, median `-0.0100`, brier `0.3204`, calibration_gap `0.3254`
- 20d: hit_rate `0.6875`, avg `0.0101`, median `0.0075`, brier `0.2177`, calibration_gap `-0.0496`
- 60d: hit_rate `0.4375`, avg `-0.0016`, median `-0.0097`, brier `0.2873`, calibration_gap `0.2004`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
