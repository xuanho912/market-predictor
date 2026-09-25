# High Confidence Signal Report

Generated at: `2026-09-25T01:13:05.737500+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0101`, median `0.0126`, brier `0.1209`, calibration_gap `-0.0943`
- 5d: hit_rate `0.8750`, avg `0.0111`, median `0.0144`, brier `0.1209`, calibration_gap `-0.0943`
- 10d: hit_rate `1.0000`, avg `0.0106`, median `0.0103`, brier `0.0482`, calibration_gap `-0.2193`
- 20d: hit_rate `0.8750`, avg `0.0339`, median `0.0460`, brier `0.1209`, calibration_gap `-0.0943`
- 60d: hit_rate `1.0000`, avg `0.0925`, median `0.0844`, brier `0.0482`, calibration_gap `-0.2193`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0023`, median `0.0085`, brier `0.2390`, calibration_gap `0.1276`
- 5d: hit_rate `0.6875`, avg `0.0046`, median `0.0089`, brier `0.2119`, calibration_gap `0.0651`
- 10d: hit_rate `0.7500`, avg `0.0048`, median `0.0083`, brier `0.1695`, calibration_gap `0.0026`
- 20d: hit_rate `0.8750`, avg `0.0344`, median `0.0445`, brier `0.1319`, calibration_gap `-0.1224`
- 60d: hit_rate `1.0000`, avg `0.1005`, median `0.1016`, brier `0.0624`, calibration_gap `-0.2474`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5167`, avg `0.0003`, median `0.0008`, brier `0.2626`, calibration_gap `0.1278`
- 5d: hit_rate `0.5167`, avg `0.0024`, median `0.0031`, brier `0.2576`, calibration_gap `0.1278`
- 10d: hit_rate `0.6833`, avg `0.0077`, median `0.0081`, brier `0.2155`, calibration_gap `-0.0389`
- 20d: hit_rate `0.7833`, avg `0.0311`, median `0.0307`, brier `0.1938`, calibration_gap `-0.1389`
- 60d: hit_rate `0.9333`, avg `0.0860`, median `0.0997`, brier `0.1432`, calibration_gap `-0.2889`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0026`, median `-0.0042`, brier `0.2528`, calibration_gap `0.0496`
- 5d: hit_rate `0.3750`, avg `0.0018`, median `-0.0095`, brier `0.2651`, calibration_gap `0.1746`
- 10d: hit_rate `0.6875`, avg `0.0086`, median `0.0089`, brier `0.2330`, calibration_gap `-0.1379`
- 20d: hit_rate `0.7500`, avg `0.0346`, median `0.0284`, brier `0.2244`, calibration_gap `-0.2004`
- 60d: hit_rate `0.8125`, avg `0.0765`, median `0.0787`, brier `0.2193`, calibration_gap `-0.2629`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
