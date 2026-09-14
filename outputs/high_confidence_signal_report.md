# High Confidence Signal Report

Generated at: `2026-09-14T23:17:01.096087+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0038`, median `0.0056`, brier `0.1861`, calibration_gap `0.0638`
- 5d: hit_rate `0.6250`, avg `0.0008`, median `0.0010`, brier `0.2710`, calibration_gap `0.1888`
- 10d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0136`, brier `0.5129`, calibration_gap `0.5638`
- 20d: hit_rate `0.5000`, avg `0.0067`, median `0.0087`, brier `0.3574`, calibration_gap `0.3138`
- 60d: hit_rate `0.7500`, avg `0.0398`, median `0.0588`, brier `0.1936`, calibration_gap `0.0638`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0028`, median `0.0014`, brier `0.2568`, calibration_gap `0.1712`
- 5d: hit_rate `0.6250`, avg `-0.0018`, median `0.0020`, brier `0.2644`, calibration_gap `0.1712`
- 10d: hit_rate `0.3750`, avg `-0.0080`, median `-0.0136`, brier `0.4205`, calibration_gap `0.4212`
- 20d: hit_rate `0.5625`, avg `-0.0002`, median `0.0138`, brier `0.3068`, calibration_gap `0.2337`
- 60d: hit_rate `0.5625`, avg `0.0190`, median `0.0453`, brier `0.2953`, calibration_gap `0.2337`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0074`, median `0.0116`, brier `0.1967`, calibration_gap `-0.0977`
- 5d: hit_rate `0.6875`, avg `0.0081`, median `0.0090`, brier `0.2176`, calibration_gap `-0.0352`
- 10d: hit_rate `0.6875`, avg `0.0170`, median `0.0130`, brier `0.2191`, calibration_gap `-0.0352`
- 20d: hit_rate `0.7500`, avg `0.0335`, median `0.0364`, brier `0.1987`, calibration_gap `-0.0977`
- 60d: hit_rate `0.8125`, avg `0.0604`, median `0.0668`, brier `0.1794`, calibration_gap `-0.1602`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
