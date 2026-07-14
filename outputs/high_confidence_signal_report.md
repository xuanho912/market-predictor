# High Confidence Signal Report

Generated at: `2026-07-14T14:16:51.414025+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0003`, median `0.0046`, brier `0.2447`, calibration_gap `0.0831`
- 5d: hit_rate `0.7500`, avg `0.0045`, median `0.0096`, brier `0.1935`, calibration_gap `-0.0419`
- 10d: hit_rate `0.6250`, avg `0.0044`, median `0.0140`, brier `0.2447`, calibration_gap `0.0831`
- 20d: hit_rate `0.5000`, avg `-0.0011`, median `0.0001`, brier `0.2909`, calibration_gap `0.2081`
- 60d: hit_rate `0.3750`, avg `-0.0194`, median `-0.0373`, brier `0.3421`, calibration_gap `0.3331`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0016`, median `0.0046`, brier `0.2426`, calibration_gap `0.0781`
- 5d: hit_rate `0.5000`, avg `0.0002`, median `0.0024`, brier `0.2910`, calibration_gap `0.2031`
- 10d: hit_rate `0.5625`, avg `0.0005`, median `0.0078`, brier `0.2670`, calibration_gap `0.1406`
- 20d: hit_rate `0.7500`, avg `0.0105`, median `0.0060`, brier `0.1910`, calibration_gap `-0.0469`
- 60d: hit_rate `0.4375`, avg `-0.0031`, median `-0.0222`, brier `0.3160`, calibration_gap `0.2656`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `0.0026`, median `0.0054`, brier `0.2398`, calibration_gap `0.0614`
- 5d: hit_rate `0.5500`, avg `0.0037`, median `0.0060`, brier `0.2690`, calibration_gap `0.1364`
- 10d: hit_rate `0.5500`, avg `0.0033`, median `0.0024`, brier `0.2672`, calibration_gap `0.1364`
- 20d: hit_rate `0.7250`, avg `0.0069`, median `0.0123`, brier `0.2021`, calibration_gap `-0.0386`
- 60d: hit_rate `0.5250`, avg `0.0125`, median `0.0025`, brier `0.2760`, calibration_gap `0.1614`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0017`, median `0.0078`, brier `0.2376`, calibration_gap `0.0509`
- 5d: hit_rate `0.6875`, avg `0.0047`, median `0.0100`, brier `0.2155`, calibration_gap `-0.0116`
- 10d: hit_rate `0.5625`, avg `0.0083`, median `0.0015`, brier `0.2598`, calibration_gap `0.1134`
- 20d: hit_rate `0.8125`, avg `0.0166`, median `0.0232`, brier `0.1707`, calibration_gap `-0.1366`
- 60d: hit_rate `0.6875`, avg `0.0332`, median `0.0458`, brier `0.2152`, calibration_gap `-0.0116`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
