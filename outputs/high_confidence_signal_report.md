# High Confidence Signal Report

Generated at: `2026-10-23T01:16:45.157022+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0008`, median `0.0028`, brier `0.2940`, calibration_gap `0.1883`
- 5d: hit_rate `0.6250`, avg `-0.0017`, median `0.0015`, brier `0.2476`, calibration_gap `0.0633`
- 10d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0092`, brier `0.2919`, calibration_gap `0.1883`
- 20d: hit_rate `0.3750`, avg `-0.0101`, median `-0.0224`, brier `0.3356`, calibration_gap `0.3133`
- 60d: hit_rate `0.8750`, avg `0.0637`, median `0.0674`, brier `0.1548`, calibration_gap `-0.1867`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0013`, median `-0.0028`, brier `0.3080`, calibration_gap `0.2403`
- 5d: hit_rate `0.5000`, avg `-0.0016`, median `-0.0071`, brier `0.2848`, calibration_gap `0.1778`
- 10d: hit_rate `0.4375`, avg `-0.0091`, median `-0.0280`, brier `0.3070`, calibration_gap `0.2403`
- 20d: hit_rate `0.3750`, avg `-0.0163`, median `-0.0291`, brier `0.3288`, calibration_gap `0.3028`
- 60d: hit_rate `0.8125`, avg `0.0530`, median `0.0565`, brier `0.1762`, calibration_gap `-0.1347`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0095`, median `0.0092`, brier `0.2364`, calibration_gap `-0.0517`
- 5d: hit_rate `0.7500`, avg `0.0102`, median `0.0181`, brier `0.2182`, calibration_gap `-0.1767`
- 10d: hit_rate `0.6875`, avg `0.0229`, median `0.0343`, brier `0.2280`, calibration_gap `-0.1142`
- 20d: hit_rate `0.8125`, avg `0.0249`, median `0.0211`, brier `0.2076`, calibration_gap `-0.2392`
- 60d: hit_rate `0.9375`, avg `0.1058`, median `0.1087`, brier `0.1896`, calibration_gap `-0.3642`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
