# High Confidence Signal Report

Generated at: `2026-08-13T13:50:48.667270+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0130`, median `0.0129`, brier `0.0768`, calibration_gap `-0.2771`
- 5d: hit_rate `0.8750`, avg `0.0082`, median `0.0097`, brier `0.1331`, calibration_gap `-0.1521`
- 10d: hit_rate `0.8750`, avg `0.0161`, median `0.0199`, brier `0.1319`, calibration_gap `-0.1521`
- 20d: hit_rate `0.2500`, avg `-0.0009`, median `-0.0114`, brier `0.4087`, calibration_gap `0.4729`
- 60d: hit_rate `0.2500`, avg `-0.0126`, median `-0.0408`, brier `0.4087`, calibration_gap `0.4729`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0037`, median `0.0046`, brier `0.2065`, calibration_gap `0.0226`
- 5d: hit_rate `0.7500`, avg `0.0051`, median `0.0088`, brier `0.1862`, calibration_gap `-0.0399`
- 10d: hit_rate `0.6875`, avg `0.0079`, median `0.0117`, brier `0.2085`, calibration_gap `0.0226`
- 20d: hit_rate `0.5625`, avg `0.0066`, median `0.0048`, brier `0.2746`, calibration_gap `0.1476`
- 60d: hit_rate `0.3750`, avg `-0.0047`, median `-0.0308`, brier `0.3500`, calibration_gap `0.3351`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0046`, median `0.0050`, brier `0.2392`, calibration_gap `0.0688`
- 5d: hit_rate `0.6375`, avg `0.0050`, median `0.0053`, brier `0.2301`, calibration_gap `0.0438`
- 10d: hit_rate `0.6125`, avg `0.0080`, median `0.0099`, brier `0.2397`, calibration_gap `0.0688`
- 20d: hit_rate `0.6875`, avg `0.0144`, median `0.0156`, brier `0.2170`, calibration_gap `-0.0062`
- 60d: hit_rate `0.6375`, avg `0.0272`, median `0.0456`, brier `0.2391`, calibration_gap `0.0438`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0056`, median `-0.0012`, brier `0.2755`, calibration_gap `0.1605`
- 5d: hit_rate `0.5000`, avg `0.0006`, median `-0.0017`, brier `0.2765`, calibration_gap `0.1605`
- 10d: hit_rate `0.5625`, avg `0.0037`, median `0.0015`, brier `0.2572`, calibration_gap `0.0980`
- 20d: hit_rate `0.6250`, avg `0.0070`, median `0.0150`, brier `0.2366`, calibration_gap `0.0355`
- 60d: hit_rate `0.6875`, avg `0.0247`, median `0.0555`, brier `0.2171`, calibration_gap `-0.0270`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
