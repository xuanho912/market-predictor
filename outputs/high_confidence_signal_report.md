# High Confidence Signal Report

Generated at: `2026-09-19T15:55:47.709339+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0024`, median `0.0100`, brier `0.1894`, calibration_gap `0.0665`
- 5d: hit_rate `0.6250`, avg `-0.0038`, median `0.0010`, brier `0.2711`, calibration_gap `0.1915`
- 10d: hit_rate `0.5000`, avg `-0.0012`, median `-0.0018`, brier `0.3554`, calibration_gap `0.3165`
- 20d: hit_rate `0.6250`, avg `0.0219`, median `0.0293`, brier `0.2719`, calibration_gap `0.1915`
- 60d: hit_rate `0.7500`, avg `0.0439`, median `0.0588`, brier `0.1924`, calibration_gap `0.0665`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `-0.0008`, median `0.0034`, brier `0.2254`, calibration_gap `0.1163`
- 5d: hit_rate `0.5625`, avg `-0.0039`, median `0.0010`, brier `0.3028`, calibration_gap `0.2413`
- 10d: hit_rate `0.4375`, avg `-0.0065`, median `-0.0105`, brier `0.3818`, calibration_gap `0.3663`
- 20d: hit_rate `0.6875`, avg `0.0252`, median `0.0308`, brier `0.2313`, calibration_gap `0.1163`
- 60d: hit_rate `0.8750`, avg `0.0506`, median `0.0595`, brier `0.1180`, calibration_gap `-0.0712`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5500`, avg `-0.0030`, median `0.0021`, brier `0.2923`, calibration_gap `0.1931`
- 5d: hit_rate `0.5500`, avg `-0.0059`, median `0.0010`, brier `0.2972`, calibration_gap `0.1931`
- 10d: hit_rate `0.4667`, avg `-0.0024`, median `-0.0053`, brier `0.3351`, calibration_gap `0.2764`
- 20d: hit_rate `0.6167`, avg `0.0141`, median `0.0156`, brier `0.2482`, calibration_gap `0.1264`
- 60d: hit_rate `0.7500`, avg `0.0375`, median `0.0501`, brier `0.1874`, calibration_gap `-0.0069`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0011`, median `0.0088`, brier `0.2153`, calibration_gap `-0.0164`
- 5d: hit_rate `0.7500`, avg `0.0025`, median `0.0071`, brier `0.1949`, calibration_gap `-0.0789`
- 10d: hit_rate `0.5625`, avg `0.0002`, median `0.0014`, brier `0.2604`, calibration_gap `0.1086`
- 20d: hit_rate `0.5000`, avg `0.0103`, median `-0.0001`, brier `0.2807`, calibration_gap `0.1711`
- 60d: hit_rate `0.8125`, avg `0.0412`, median `0.0434`, brier `0.1734`, calibration_gap `-0.1414`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
