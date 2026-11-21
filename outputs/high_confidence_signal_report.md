# High Confidence Signal Report

Generated at: `2026-11-21T11:47:54.916253+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0130`, median `-0.0089`, brier `0.5082`, calibration_gap `0.6291`
- 5d: hit_rate `0.6250`, avg `-0.0016`, median `0.0043`, brier `0.2536`, calibration_gap `0.1291`
- 10d: hit_rate `0.3750`, avg `-0.0297`, median `-0.0251`, brier `0.3794`, calibration_gap `0.3791`
- 20d: hit_rate `0.1250`, avg `-0.0847`, median `-0.0258`, brier `0.5082`, calibration_gap `0.6291`
- 60d: hit_rate `0.3750`, avg `-0.0116`, median `-0.0081`, brier `0.3755`, calibration_gap `0.3791`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0010`, median `-0.0010`, brier `0.3470`, calibration_gap `0.3043`
- 5d: hit_rate `0.6250`, avg `0.0048`, median `0.0044`, brier `0.2490`, calibration_gap `0.1168`
- 10d: hit_rate `0.4375`, avg `-0.0117`, median `-0.0048`, brier `0.3376`, calibration_gap `0.3043`
- 20d: hit_rate `0.4375`, avg `-0.0317`, median `-0.0026`, brier `0.3470`, calibration_gap `0.3043`
- 60d: hit_rate `0.5000`, avg `0.0022`, median `-0.0034`, brier `0.3094`, calibration_gap `0.2418`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0072`, median `0.0106`, brier `0.2438`, calibration_gap `0.0598`
- 5d: hit_rate `0.7750`, avg `0.0117`, median `0.0128`, brier `0.1878`, calibration_gap `-0.0652`
- 10d: hit_rate `0.6250`, avg `0.0067`, median `0.0180`, brier `0.2505`, calibration_gap `0.0848`
- 20d: hit_rate `0.7000`, avg `0.0056`, median `0.0318`, brier `0.2268`, calibration_gap `0.0098`
- 60d: hit_rate `0.6500`, avg `0.0317`, median `0.0511`, brier `0.2381`, calibration_gap `0.0598`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0065`, median `0.0122`, brier `0.2265`, calibration_gap `-0.1160`
- 5d: hit_rate `0.8750`, avg `0.0097`, median `0.0203`, brier `0.2001`, calibration_gap `-0.3035`
- 10d: hit_rate `0.7500`, avg `0.0024`, median `0.0368`, brier `0.2185`, calibration_gap `-0.1785`
- 20d: hit_rate `0.6250`, avg `0.0166`, median `0.0396`, brier `0.2362`, calibration_gap `-0.0535`
- 60d: hit_rate `0.6250`, avg `0.0830`, median `0.1019`, brier `0.2359`, calibration_gap `-0.0535`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
