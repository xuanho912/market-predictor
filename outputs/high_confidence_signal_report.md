# High Confidence Signal Report

Generated at: `2026-10-29T01:22:38.276577+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0090`, median `0.0114`, brier `0.2003`, calibration_gap `-0.0567`
- 5d: hit_rate `0.8750`, avg `0.0117`, median `0.0116`, brier `0.1465`, calibration_gap `-0.1817`
- 10d: hit_rate `0.8750`, avg `0.0116`, median `0.0114`, brier `0.1465`, calibration_gap `-0.1817`
- 20d: hit_rate `0.5000`, avg `0.0052`, median `0.0028`, brier `0.2940`, calibration_gap `0.1933`
- 60d: hit_rate `0.8750`, avg `0.1132`, median `0.1063`, brier `0.1465`, calibration_gap `-0.1817`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0061`, median `0.0074`, brier `0.2380`, calibration_gap `0.0526`
- 5d: hit_rate `0.6875`, avg `0.0072`, median `0.0103`, brier `0.2111`, calibration_gap `-0.0099`
- 10d: hit_rate `0.6875`, avg `0.0051`, median `0.0114`, brier `0.2111`, calibration_gap `-0.0099`
- 20d: hit_rate `0.5000`, avg `-0.0040`, median `0.0028`, brier `0.2849`, calibration_gap `0.1776`
- 60d: hit_rate `0.8750`, avg `0.0799`, median `0.0851`, brier `0.1504`, calibration_gap `-0.1974`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0044`, median `0.0093`, brier `0.2324`, calibration_gap `-0.0396`
- 5d: hit_rate `0.6000`, avg `0.0036`, median `0.0084`, brier `0.2289`, calibration_gap `0.0104`
- 10d: hit_rate `0.6500`, avg `0.0023`, median `0.0096`, brier `0.2207`, calibration_gap `-0.0396`
- 20d: hit_rate `0.6000`, avg `0.0030`, median `0.0040`, brier `0.2443`, calibration_gap `0.0104`
- 60d: hit_rate `0.9000`, avg `0.0901`, median `0.1012`, brier `0.1720`, calibration_gap `-0.2896`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0023`, median `0.0096`, brier `0.2302`, calibration_gap `-0.1092`
- 5d: hit_rate `0.5000`, avg `-0.0013`, median `-0.0008`, brier `0.2526`, calibration_gap `0.0783`
- 10d: hit_rate `0.5000`, avg `-0.0083`, median `-0.0015`, brier `0.2573`, calibration_gap `0.0783`
- 20d: hit_rate `0.6250`, avg `-0.0074`, median `0.0072`, brier `0.2349`, calibration_gap `-0.0467`
- 60d: hit_rate `0.8750`, avg `0.0685`, median `0.0764`, brier `0.1973`, calibration_gap `-0.2967`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
