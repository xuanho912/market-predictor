# High Confidence Signal Report

Generated at: `2026-08-16T13:03:53.442585+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0130`, median `0.0129`, brier `0.0762`, calibration_gap `-0.2759`
- 5d: hit_rate `0.8750`, avg `0.0082`, median `0.0097`, brier `0.1298`, calibration_gap `-0.1509`
- 10d: hit_rate `0.8750`, avg `0.0161`, median `0.0199`, brier `0.1312`, calibration_gap `-0.1509`
- 20d: hit_rate `0.2500`, avg `-0.0009`, median `-0.0114`, brier `0.4104`, calibration_gap `0.4741`
- 60d: hit_rate `0.2500`, avg `-0.0126`, median `-0.0408`, brier `0.4104`, calibration_gap `0.4741`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0053`, median `0.0051`, brier `0.2074`, calibration_gap `0.0252`
- 5d: hit_rate `0.8125`, avg `0.0066`, median `0.0088`, brier `0.1590`, calibration_gap `-0.0998`
- 10d: hit_rate `0.7500`, avg `0.0094`, median `0.0118`, brier `0.1854`, calibration_gap `-0.0373`
- 20d: hit_rate `0.5625`, avg `0.0061`, median `0.0048`, brier `0.2754`, calibration_gap `0.1502`
- 60d: hit_rate `0.3125`, avg `-0.0071`, median `-0.0322`, brier `0.3756`, calibration_gap `0.4002`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6000`, avg `0.0031`, median `0.0043`, brier `0.2454`, calibration_gap `0.0820`
- 5d: hit_rate `0.6375`, avg `0.0038`, median `0.0043`, brier `0.2308`, calibration_gap `0.0445`
- 10d: hit_rate `0.6000`, avg `0.0092`, median `0.0109`, brier `0.2459`, calibration_gap `0.0820`
- 20d: hit_rate `0.6750`, avg `0.0172`, median `0.0201`, brier `0.2221`, calibration_gap `0.0070`
- 60d: hit_rate `0.6250`, avg `0.0326`, median `0.0394`, brier `0.2447`, calibration_gap `0.0570`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0048`, median `0.0055`, brier `0.2340`, calibration_gap `0.0341`
- 5d: hit_rate `0.6250`, avg `0.0049`, median `0.0044`, brier `0.2357`, calibration_gap `0.0341`
- 10d: hit_rate `0.6250`, avg `0.0124`, median `0.0131`, brier `0.2375`, calibration_gap `0.0341`
- 20d: hit_rate `0.6250`, avg `0.0143`, median `0.0318`, brier `0.2361`, calibration_gap `0.0341`
- 60d: hit_rate `0.7500`, avg `0.0478`, median `0.0553`, brier `0.1980`, calibration_gap `-0.0909`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
