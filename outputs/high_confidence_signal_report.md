# High Confidence Signal Report

Generated at: `2026-10-15T00:14:16.870967+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0002`, median `0.0031`, brier `0.2455`, calibration_gap `0.0426`
- 5d: hit_rate `0.6250`, avg `0.0022`, median `0.0088`, brier `0.2415`, calibration_gap `0.0426`
- 10d: hit_rate `0.5000`, avg `0.0012`, median `-0.0000`, brier `0.2905`, calibration_gap `0.1676`
- 20d: hit_rate `0.8750`, avg `0.0447`, median `0.0460`, brier `0.1532`, calibration_gap `-0.2074`
- 60d: hit_rate `0.8750`, avg `0.0845`, median `0.1032`, brier `0.1558`, calibration_gap `-0.2074`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0068`, median `0.0116`, brier `0.2059`, calibration_gap `-0.0975`
- 5d: hit_rate `0.6875`, avg `0.0038`, median `0.0080`, brier `0.2201`, calibration_gap `-0.0350`
- 10d: hit_rate `0.6875`, avg `0.0065`, median `0.0076`, brier `0.2272`, calibration_gap `-0.0350`
- 20d: hit_rate `0.8750`, avg `0.0413`, median `0.0460`, brier `0.1597`, calibration_gap `-0.2225`
- 60d: hit_rate `0.8750`, avg `0.0772`, median `0.0859`, brier `0.1599`, calibration_gap `-0.2225`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6833`, avg `0.0077`, median `0.0112`, brier `0.2247`, calibration_gap `-0.0836`
- 5d: hit_rate `0.6500`, avg `0.0092`, median `0.0109`, brier `0.2284`, calibration_gap `-0.0502`
- 10d: hit_rate `0.6833`, avg `0.0100`, median `0.0126`, brier `0.2267`, calibration_gap `-0.0836`
- 20d: hit_rate `0.7833`, avg `0.0351`, median `0.0366`, brier `0.1977`, calibration_gap `-0.1836`
- 60d: hit_rate `0.9333`, avg `0.0961`, median `0.0989`, brier `0.1772`, calibration_gap `-0.3336`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0111`, median `0.0079`, brier `0.2458`, calibration_gap `-0.0866`
- 5d: hit_rate `0.5625`, avg `0.0111`, median `0.0014`, brier `0.2453`, calibration_gap `-0.0241`
- 10d: hit_rate `0.6250`, avg `0.0087`, median `0.0063`, brier `0.2480`, calibration_gap `-0.0866`
- 20d: hit_rate `0.6875`, avg `0.0350`, median `0.0500`, brier `0.2402`, calibration_gap `-0.1491`
- 60d: hit_rate `0.9375`, avg `0.1252`, median `0.1309`, brier `0.2156`, calibration_gap `-0.3991`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
