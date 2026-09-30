# High Confidence Signal Report

Generated at: `2026-09-30T00:55:33.237007+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0073`, median `0.0085`, brier `0.1920`, calibration_gap `0.0282`
- 5d: hit_rate `0.7500`, avg `0.0069`, median `0.0108`, brier `0.1920`, calibration_gap `0.0282`
- 10d: hit_rate `1.0000`, avg `0.0100`, median `0.0097`, brier `0.0493`, calibration_gap `-0.2218`
- 20d: hit_rate `0.7500`, avg `0.0295`, median `0.0460`, brier `0.1920`, calibration_gap `0.0282`
- 60d: hit_rate `1.0000`, avg `0.0881`, median `0.0844`, brier `0.0493`, calibration_gap `-0.2218`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0050`, median `0.0116`, brier `0.2144`, calibration_gap `0.0630`
- 5d: hit_rate `0.6875`, avg `0.0058`, median `0.0089`, brier `0.2100`, calibration_gap `0.0630`
- 10d: hit_rate `0.7500`, avg `0.0063`, median `0.0083`, brier `0.1678`, calibration_gap `0.0005`
- 20d: hit_rate `0.8750`, avg `0.0341`, median `0.0424`, brier `0.1347`, calibration_gap `-0.1245`
- 60d: hit_rate `0.9375`, avg `0.0930`, median `0.0940`, brier `0.0881`, calibration_gap `-0.1870`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4833`, avg `-0.0007`, median `-0.0014`, brier `0.2640`, calibration_gap `0.1630`
- 5d: hit_rate `0.5167`, avg `0.0011`, median `0.0020`, brier `0.2582`, calibration_gap `0.1297`
- 10d: hit_rate `0.6500`, avg `0.0065`, median `0.0086`, brier `0.2174`, calibration_gap `-0.0037`
- 20d: hit_rate `0.8000`, avg `0.0309`, median `0.0327`, brier `0.1896`, calibration_gap `-0.1537`
- 60d: hit_rate `0.9000`, avg `0.0838`, median `0.0997`, brier `0.1496`, calibration_gap `-0.2537`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0010`, median `0.0027`, brier `0.2518`, calibration_gap `0.0669`
- 5d: hit_rate `0.5000`, avg `0.0045`, median `0.0002`, brier `0.2561`, calibration_gap `0.0669`
- 10d: hit_rate `0.6875`, avg `0.0108`, median `0.0207`, brier `0.2281`, calibration_gap `-0.1206`
- 20d: hit_rate `0.7500`, avg `0.0324`, median `0.0409`, brier `0.2173`, calibration_gap `-0.1831`
- 60d: hit_rate `0.8125`, avg `0.0766`, median `0.0803`, brier `0.2091`, calibration_gap `-0.2456`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
