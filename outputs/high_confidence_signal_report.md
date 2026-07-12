# High Confidence Signal Report

Generated at: `2026-07-12T13:59:01.819403+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0031`, median `0.0080`, brier `0.2428`, calibration_gap `0.0917`
- 5d: hit_rate `0.6250`, avg `0.0040`, median `0.0097`, brier `0.2428`, calibration_gap `0.0917`
- 10d: hit_rate `0.6250`, avg `0.0083`, median `0.0098`, brier `0.2437`, calibration_gap `0.0917`
- 20d: hit_rate `0.7500`, avg `0.0119`, median `0.0209`, brier `0.1892`, calibration_gap `-0.0333`
- 60d: hit_rate `0.3750`, avg `-0.0022`, median `-0.0204`, brier `0.3483`, calibration_gap `0.3417`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0014`, median `0.0046`, brier `0.2411`, calibration_gap `0.0823`
- 5d: hit_rate `0.5000`, avg `0.0015`, median `0.0028`, brier `0.2910`, calibration_gap `0.2073`
- 10d: hit_rate `0.6250`, avg `0.0055`, median `0.0098`, brier `0.2419`, calibration_gap `0.0823`
- 20d: hit_rate `0.8125`, avg `0.0188`, median `0.0241`, brier `0.1655`, calibration_gap `-0.1052`
- 60d: hit_rate `0.5625`, avg `0.0233`, median `0.0368`, brier `0.2700`, calibration_gap `0.1448`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5500`, avg `-0.0005`, median `0.0019`, brier `0.2666`, calibration_gap `0.1358`
- 5d: hit_rate `0.5667`, avg `-0.0003`, median `0.0035`, brier `0.2606`, calibration_gap `0.1191`
- 10d: hit_rate `0.5333`, avg `-0.0010`, median `0.0029`, brier `0.2726`, calibration_gap `0.1525`
- 20d: hit_rate `0.7000`, avg `0.0028`, median `0.0120`, brier `0.2110`, calibration_gap `-0.0142`
- 60d: hit_rate `0.5333`, avg `0.0061`, median `0.0112`, brier `0.2731`, calibration_gap `0.1525`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0021`, median `0.0055`, brier `0.2371`, calibration_gap `0.0349`
- 5d: hit_rate `0.6250`, avg `0.0024`, median `0.0057`, brier `0.2374`, calibration_gap `0.0349`
- 10d: hit_rate `0.6875`, avg `0.0055`, median `0.0095`, brier `0.2156`, calibration_gap `-0.0276`
- 20d: hit_rate `0.6875`, avg `0.0097`, median `0.0100`, brier `0.2161`, calibration_gap `-0.0276`
- 60d: hit_rate `0.5000`, avg `0.0178`, median `0.0031`, brier `0.2740`, calibration_gap `0.1599`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
