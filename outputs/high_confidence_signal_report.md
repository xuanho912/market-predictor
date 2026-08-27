# High Confidence Signal Report

Generated at: `2026-08-27T11:16:32.358738+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0019`, median `0.0012`, brier `0.1963`, calibration_gap `-0.0055`
- 5d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0028`, brier `0.3054`, calibration_gap `0.2445`
- 10d: hit_rate `0.3750`, avg `-0.0058`, median `-0.0073`, brier `0.3731`, calibration_gap `0.3695`
- 20d: hit_rate `0.6250`, avg `0.0059`, median `0.0166`, brier `0.2475`, calibration_gap `0.1195`
- 60d: hit_rate `0.6250`, avg `0.0168`, median `0.0314`, brier `0.2424`, calibration_gap `0.1195`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0024`, median `0.0029`, brier `0.1927`, calibration_gap `-0.0168`
- 5d: hit_rate `0.4375`, avg `-0.0050`, median `-0.0079`, brier `0.3300`, calibration_gap `0.2957`
- 10d: hit_rate `0.3750`, avg `-0.0055`, median `-0.0104`, brier `0.3636`, calibration_gap `0.3582`
- 20d: hit_rate `0.5625`, avg `-0.0043`, median `0.0097`, brier `0.2727`, calibration_gap `0.1707`
- 60d: hit_rate `0.6875`, avg `0.0172`, median `0.0314`, brier `0.2146`, calibration_gap `0.0457`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5750`, avg `0.0028`, median `0.0023`, brier `0.2555`, calibration_gap `0.1043`
- 5d: hit_rate `0.4750`, avg `0.0019`, median `-0.0030`, brier `0.2916`, calibration_gap `0.2043`
- 10d: hit_rate `0.6250`, avg `0.0127`, median `0.0159`, brier `0.2329`, calibration_gap `0.0543`
- 20d: hit_rate `0.7000`, avg `0.0210`, median `0.0260`, brier `0.2058`, calibration_gap `-0.0207`
- 60d: hit_rate `0.7750`, avg `0.0553`, median `0.0597`, brier `0.1900`, calibration_gap `-0.0957`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0057`, median `0.0108`, brier `0.2329`, calibration_gap `0.0214`
- 5d: hit_rate `0.4375`, avg `0.0034`, median `-0.0059`, brier `0.2882`, calibration_gap `0.2089`
- 10d: hit_rate `0.5000`, avg `0.0105`, median `0.0011`, brier `0.2707`, calibration_gap `0.1464`
- 20d: hit_rate `0.6250`, avg `0.0208`, median `0.0125`, brier `0.2356`, calibration_gap `0.0214`
- 60d: hit_rate `0.8750`, avg `0.0877`, median `0.0786`, brier `0.1629`, calibration_gap `-0.2286`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
