# High Confidence Signal Report

Generated at: `2026-10-08T07:30:15.654840+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0005`, median `0.0031`, brier `0.2676`, calibration_gap `0.1915`
- 5d: hit_rate `0.6250`, avg `-0.0013`, median `0.0056`, brier `0.2676`, calibration_gap `0.1915`
- 10d: hit_rate `0.5000`, avg `-0.0035`, median `-0.0047`, brier `0.3547`, calibration_gap `0.3165`
- 20d: hit_rate `0.7500`, avg `0.0196`, median `0.0173`, brier `0.1977`, calibration_gap `0.0665`
- 60d: hit_rate `1.0000`, avg `0.0443`, median `0.0415`, brier `0.0338`, calibration_gap `-0.1835`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0009`, brier `0.3370`, calibration_gap `0.3038`
- 5d: hit_rate `0.4375`, avg `-0.0077`, median `-0.0134`, brier `0.3731`, calibration_gap `0.3663`
- 10d: hit_rate `0.4375`, avg `-0.0152`, median `-0.0116`, brier `0.3801`, calibration_gap `0.3663`
- 20d: hit_rate `0.5625`, avg `-0.0022`, median `0.0009`, brier `0.3020`, calibration_gap `0.2413`
- 60d: hit_rate `0.9375`, avg `0.0530`, median `0.0571`, brier `0.0751`, calibration_gap `-0.1337`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5250`, avg `-0.0007`, median `0.0018`, brier `0.2907`, calibration_gap `0.1990`
- 5d: hit_rate `0.5250`, avg `-0.0047`, median `0.0012`, brier `0.2976`, calibration_gap `0.1990`
- 10d: hit_rate `0.5500`, avg `-0.0042`, median `0.0040`, brier `0.2871`, calibration_gap `0.1740`
- 20d: hit_rate `0.6250`, avg `0.0043`, median `0.0157`, brier `0.2490`, calibration_gap `0.0990`
- 60d: hit_rate `0.8500`, avg `0.0364`, median `0.0445`, brier `0.1370`, calibration_gap `-0.1260`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0010`, median `-0.0024`, brier `0.2905`, calibration_gap `0.2043`
- 5d: hit_rate `0.5000`, avg `-0.0048`, median `0.0002`, brier `0.2717`, calibration_gap `0.1418`
- 10d: hit_rate `0.5625`, avg `0.0015`, median `0.0074`, brier `0.2523`, calibration_gap `0.0793`
- 20d: hit_rate `0.5625`, avg `-0.0031`, median `0.0120`, brier `0.2474`, calibration_gap `0.0793`
- 60d: hit_rate `0.7500`, avg `0.0087`, median `0.0306`, brier `0.1944`, calibration_gap `-0.1082`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
