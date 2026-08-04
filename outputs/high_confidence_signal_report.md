# High Confidence Signal Report

Generated at: `2026-08-04T21:46:43.568684+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0006`, median `0.0056`, brier `0.2475`, calibration_gap `0.1029`
- 5d: hit_rate `0.8750`, avg `0.0073`, median `0.0106`, brier `0.1363`, calibration_gap `-0.1471`
- 10d: hit_rate `0.5000`, avg `0.0053`, median `0.0063`, brier `0.3022`, calibration_gap `0.2279`
- 20d: hit_rate `0.5000`, avg `0.0081`, median `0.0062`, brier `0.3048`, calibration_gap `0.2279`
- 60d: hit_rate `0.5000`, avg `0.0052`, median `-0.0032`, brier `0.3048`, calibration_gap `0.2279`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0015`, median `0.0030`, brier `0.2449`, calibration_gap `0.0941`
- 5d: hit_rate `0.8125`, avg `0.0053`, median `0.0069`, brier `0.1629`, calibration_gap `-0.0934`
- 10d: hit_rate `0.5000`, avg `0.0030`, median `0.0002`, brier `0.2978`, calibration_gap `0.2191`
- 20d: hit_rate `0.5625`, avg `0.0040`, median `0.0026`, brier `0.2733`, calibration_gap `0.1566`
- 60d: hit_rate `0.3750`, avg `-0.0050`, median `-0.0172`, brier `0.3520`, calibration_gap `0.3441`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6833`, avg `0.0032`, median `0.0078`, brier `0.2173`, calibration_gap `0.0070`
- 5d: hit_rate `0.6667`, avg `0.0038`, median `0.0061`, brier `0.2230`, calibration_gap `0.0237`
- 10d: hit_rate `0.5667`, avg `0.0044`, median `0.0055`, brier `0.2616`, calibration_gap `0.1237`
- 20d: hit_rate `0.6667`, avg `0.0080`, median `0.0123`, brier `0.2226`, calibration_gap `0.0237`
- 60d: hit_rate `0.6500`, avg `0.0264`, median `0.0456`, brier `0.2332`, calibration_gap `0.0403`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0021`, median `0.0032`, brier `0.2364`, calibration_gap `0.0481`
- 5d: hit_rate `0.6250`, avg `0.0022`, median `0.0057`, brier `0.2369`, calibration_gap `0.0481`
- 10d: hit_rate `0.5000`, avg `-0.0032`, median `-0.0045`, brier `0.2789`, calibration_gap `0.1731`
- 20d: hit_rate `0.6250`, avg `-0.0035`, median `0.0120`, brier `0.2369`, calibration_gap `0.0481`
- 60d: hit_rate `0.8125`, avg `0.0451`, median `0.0661`, brier `0.1719`, calibration_gap `-0.1394`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
