# High Confidence Signal Report

Generated at: `2026-08-03T23:57:10.879309+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0022`, median `0.0035`, brier `0.2552`, calibration_gap `0.1310`
- 5d: hit_rate `0.7500`, avg `0.0012`, median `0.0112`, brier `0.1908`, calibration_gap `0.0060`
- 10d: hit_rate `0.3750`, avg `0.0065`, median `-0.0097`, brier `0.3840`, calibration_gap `0.3810`
- 20d: hit_rate `0.6250`, avg `0.0165`, median `0.0246`, brier `0.2488`, calibration_gap `0.1310`
- 60d: hit_rate `0.5000`, avg `0.0106`, median `0.0045`, brier `0.3096`, calibration_gap `0.2560`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0078`, median `-0.0092`, brier `0.3691`, calibration_gap `0.3708`
- 5d: hit_rate `0.7500`, avg `-0.0012`, median `0.0023`, brier `0.1893`, calibration_gap `-0.0042`
- 10d: hit_rate `0.2500`, avg `-0.0041`, median `-0.0129`, brier `0.4335`, calibration_gap `0.4958`
- 20d: hit_rate `0.3750`, avg `-0.0105`, median `-0.0144`, brier `0.3652`, calibration_gap `0.3708`
- 60d: hit_rate `0.3125`, avg `-0.0214`, median `-0.0274`, brier `0.3956`, calibration_gap `0.4333`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5750`, avg `0.0044`, median `0.0061`, brier `0.2524`, calibration_gap `0.1194`
- 5d: hit_rate `0.6250`, avg `0.0058`, median `0.0087`, brier `0.2371`, calibration_gap `0.0694`
- 10d: hit_rate `0.6500`, avg `0.0122`, median `0.0195`, brier `0.2264`, calibration_gap `0.0444`
- 20d: hit_rate `0.7250`, avg `0.0169`, median `0.0309`, brier `0.1935`, calibration_gap `-0.0306`
- 60d: hit_rate `0.6500`, avg `0.0157`, median `0.0589`, brier `0.2272`, calibration_gap `0.0444`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0007`, median `-0.0031`, brier `0.3031`, calibration_gap `0.2403`
- 5d: hit_rate `0.6250`, avg `0.0011`, median `0.0043`, brier `0.2363`, calibration_gap `0.0528`
- 10d: hit_rate `0.5625`, avg `-0.0022`, median `0.0046`, brier `0.2583`, calibration_gap `0.1153`
- 20d: hit_rate `0.5000`, avg `-0.0105`, median `-0.0015`, brier `0.2794`, calibration_gap `0.1778`
- 60d: hit_rate `0.5000`, avg `-0.0192`, median `0.0027`, brier `0.2791`, calibration_gap `0.1778`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
