# High Confidence Signal Report

Generated at: `2026-11-06T07:58:50.429943+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0074`, median `0.0144`, brier `0.1960`, calibration_gap `0.0532`
- 5d: hit_rate `0.7500`, avg `0.0145`, median `0.0175`, brier `0.1806`, calibration_gap `0.0532`
- 10d: hit_rate `0.7500`, avg `0.0123`, median `0.0388`, brier `0.1960`, calibration_gap `0.0532`
- 20d: hit_rate `0.7500`, avg `-0.0190`, median `0.0427`, brier `0.1960`, calibration_gap `0.0532`
- 60d: hit_rate `0.7500`, avg `0.0498`, median `0.0727`, brier `0.1960`, calibration_gap `0.0532`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0042`, median `0.0118`, brier `0.2588`, calibration_gap `0.1592`
- 5d: hit_rate `0.6875`, avg `0.0096`, median `0.0139`, brier `0.2193`, calibration_gap `0.0967`
- 10d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0006`, brier `0.3230`, calibration_gap `0.2842`
- 20d: hit_rate `0.6250`, avg `-0.0284`, median `0.0290`, brier `0.2588`, calibration_gap `0.1592`
- 60d: hit_rate `0.7500`, avg `0.0396`, median `0.0719`, brier `0.1912`, calibration_gap `0.0342`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6000`, avg `0.0078`, median `0.0114`, brier `0.2688`, calibration_gap `0.1710`
- 5d: hit_rate `0.6000`, avg `0.0097`, median `0.0139`, brier `0.2633`, calibration_gap `0.1710`
- 10d: hit_rate `0.5500`, avg `0.0120`, median `0.0207`, brier `0.2955`, calibration_gap `0.2210`
- 20d: hit_rate `0.6500`, avg `0.0036`, median `0.0290`, brier `0.2442`, calibration_gap `0.1210`
- 60d: hit_rate `0.9000`, avg `0.0638`, median `0.0710`, brier `0.1160`, calibration_gap `-0.1290`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0049`, median `0.0036`, brier `0.2359`, calibration_gap `-0.0121`
- 5d: hit_rate `0.5625`, avg `0.0093`, median `0.0045`, brier `0.2493`, calibration_gap `0.0504`
- 10d: hit_rate `0.6250`, avg `0.0009`, median `0.0156`, brier `0.2341`, calibration_gap `-0.0121`
- 20d: hit_rate `0.6875`, avg `0.0206`, median `0.0231`, brier `0.2205`, calibration_gap `-0.0746`
- 60d: hit_rate `0.6875`, avg `0.0364`, median `0.0433`, brier `0.2178`, calibration_gap `-0.0746`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
