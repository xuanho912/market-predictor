# High Confidence Signal Report

Generated at: `2026-06-16T08:19:30.815984+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0010`, median `0.0009`, brier `0.2695`, calibration_gap `0.1526`
- 5d: hit_rate `0.6250`, avg `0.0032`, median `0.0089`, brier `0.2295`, calibration_gap `0.0276`
- 10d: hit_rate `0.5000`, avg `0.0012`, median `0.0101`, brier `0.2683`, calibration_gap `0.1526`
- 20d: hit_rate `0.6250`, avg `-0.0110`, median `0.0106`, brier `0.2295`, calibration_gap `0.0276`
- 60d: hit_rate `1.0000`, avg `0.0687`, median `0.0696`, brier `0.1209`, calibration_gap `-0.3474`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0043`, median `0.0069`, brier `0.2356`, calibration_gap `0.0149`
- 5d: hit_rate `0.6875`, avg `0.0058`, median `0.0106`, brier `0.2157`, calibration_gap `-0.0476`
- 10d: hit_rate `0.5625`, avg `0.0039`, median `0.0147`, brier `0.2508`, calibration_gap `0.0774`
- 20d: hit_rate `0.7500`, avg `0.0037`, median `0.0162`, brier `0.1993`, calibration_gap `-0.1101`
- 60d: hit_rate `0.9375`, avg `0.0649`, median `0.0696`, brier `0.1457`, calibration_gap `-0.2976`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6375`, avg `0.0044`, median `0.0068`, brier `0.2325`, calibration_gap `-0.0490`
- 5d: hit_rate `0.6125`, avg `0.0016`, median `0.0070`, brier `0.2330`, calibration_gap `-0.0240`
- 10d: hit_rate `0.6000`, avg `0.0069`, median `0.0086`, brier `0.2392`, calibration_gap `-0.0115`
- 20d: hit_rate `0.7500`, avg `0.0123`, median `0.0164`, brier `0.2148`, calibration_gap `-0.1615`
- 60d: hit_rate `0.7250`, avg `0.0371`, median `0.0447`, brier `0.2163`, calibration_gap `-0.1365`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0066`, median `0.0084`, brier `0.2478`, calibration_gap `-0.0175`
- 5d: hit_rate `0.4375`, avg `-0.0118`, median `-0.0092`, brier `0.2573`, calibration_gap `0.1075`
- 10d: hit_rate `0.4375`, avg `0.0054`, median `-0.0110`, brier `0.2570`, calibration_gap `0.1075`
- 20d: hit_rate `0.8125`, avg `0.0170`, median `0.0146`, brier `0.2236`, calibration_gap `-0.2675`
- 60d: hit_rate `0.8125`, avg `0.0554`, median `0.0435`, brier `0.2228`, calibration_gap `-0.2675`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
