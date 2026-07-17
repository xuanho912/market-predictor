# High Confidence Signal Report

Generated at: `2026-07-17T14:06:23.265544+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0028`, median `0.0054`, brier `0.1880`, calibration_gap `-0.0408`
- 5d: hit_rate `0.6250`, avg `0.0028`, median `0.0039`, brier `0.2399`, calibration_gap `0.0842`
- 10d: hit_rate `0.3750`, avg `-0.0012`, median `-0.0052`, brier `0.3483`, calibration_gap `0.3342`
- 20d: hit_rate `0.7500`, avg `0.0168`, median `0.0205`, brier `0.1856`, calibration_gap `-0.0408`
- 60d: hit_rate `0.6250`, avg `0.0127`, median `0.0216`, brier `0.2461`, calibration_gap `0.0842`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0015`, median `0.0087`, brier `0.2141`, calibration_gap `0.0147`
- 5d: hit_rate `0.5625`, avg `-0.0009`, median `0.0019`, brier `0.2642`, calibration_gap `0.1397`
- 10d: hit_rate `0.4375`, avg `0.0056`, median `-0.0052`, brier `0.3186`, calibration_gap `0.2647`
- 20d: hit_rate `0.7500`, avg `0.0180`, median `0.0205`, brier `0.1884`, calibration_gap `-0.0478`
- 60d: hit_rate `0.6250`, avg `0.0263`, median `0.0396`, brier `0.2425`, calibration_gap `0.0772`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `-0.0023`, median `0.0020`, brier `0.2359`, calibration_gap `0.0619`
- 5d: hit_rate `0.5500`, avg `-0.0015`, median `0.0027`, brier `0.2661`, calibration_gap `0.1369`
- 10d: hit_rate `0.3250`, avg `-0.0038`, median `-0.0124`, brier `0.3517`, calibration_gap `0.3619`
- 20d: hit_rate `0.7250`, avg `0.0147`, median `0.0185`, brier `0.1990`, calibration_gap `-0.0381`
- 60d: hit_rate `0.7000`, avg `0.0399`, median `0.0650`, brier `0.2105`, calibration_gap `-0.0131`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0065`, median `-0.0058`, brier `0.3205`, calibration_gap `0.2929`
- 5d: hit_rate `0.4375`, avg `-0.0020`, median `-0.0019`, brier `0.2981`, calibration_gap `0.2304`
- 10d: hit_rate `0.5000`, avg `0.0050`, median `-0.0003`, brier `0.2784`, calibration_gap `0.1679`
- 20d: hit_rate `0.6875`, avg `0.0108`, median `0.0123`, brier `0.2161`, calibration_gap `-0.0196`
- 60d: hit_rate `0.5625`, avg `0.0362`, median `0.0405`, brier `0.2578`, calibration_gap `0.1054`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
