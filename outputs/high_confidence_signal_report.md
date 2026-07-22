# High Confidence Signal Report

Generated at: `2026-07-22T22:39:04.070466+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0058`, median `0.0007`, brier `0.2550`, calibration_gap `0.1324`
- 5d: hit_rate `0.5000`, avg `-0.0098`, median `-0.0029`, brier `0.3155`, calibration_gap `0.2574`
- 10d: hit_rate `0.2500`, avg `-0.0036`, median `-0.0127`, brier `0.4465`, calibration_gap `0.5074`
- 20d: hit_rate `0.6250`, avg `0.0108`, median `0.0205`, brier `0.2515`, calibration_gap `0.1324`
- 60d: hit_rate `0.7500`, avg `0.0378`, median `0.0519`, brier `0.1846`, calibration_gap `0.0074`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0035`, median `0.0007`, brier `0.2503`, calibration_gap `0.1226`
- 5d: hit_rate `0.5000`, avg `-0.0063`, median `-0.0009`, brier `0.3115`, calibration_gap `0.2476`
- 10d: hit_rate `0.2500`, avg `-0.0071`, median `-0.0156`, brier `0.4348`, calibration_gap `0.4976`
- 20d: hit_rate `0.5625`, avg `0.0025`, median `0.0002`, brier `0.2784`, calibration_gap `0.1851`
- 60d: hit_rate `0.6875`, avg `0.0311`, median `0.0519`, brier `0.2147`, calibration_gap `0.0601`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.4000`, avg `-0.0093`, median `-0.0097`, brier `0.3462`, calibration_gap `0.3242`
- 5d: hit_rate `0.4500`, avg `-0.0112`, median `-0.0102`, brier `0.3275`, calibration_gap `0.2742`
- 10d: hit_rate `0.3500`, avg `-0.0023`, median `-0.0074`, brier `0.3729`, calibration_gap `0.3742`
- 20d: hit_rate `0.7000`, avg `0.0157`, median `0.0209`, brier `0.2126`, calibration_gap `0.0242`
- 60d: hit_rate `0.7500`, avg `0.0422`, median `0.0548`, brier `0.1899`, calibration_gap `-0.0258`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0052`, median `-0.0047`, brier `0.3114`, calibration_gap `0.2551`
- 5d: hit_rate `0.2500`, avg `-0.0110`, median `-0.0109`, brier `0.3839`, calibration_gap `0.4426`
- 10d: hit_rate `0.4375`, avg `-0.0048`, median `-0.0091`, brier `0.3115`, calibration_gap `0.2551`
- 20d: hit_rate `0.6250`, avg `0.0019`, median `0.0114`, brier `0.2375`, calibration_gap `0.0676`
- 60d: hit_rate `0.5000`, avg `-0.0191`, median `0.0009`, brier `0.2885`, calibration_gap `0.1926`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
