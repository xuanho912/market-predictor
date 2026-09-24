# High Confidence Signal Report

Generated at: `2026-09-24T01:33:38.950451+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0035`, median `0.0079`, brier `0.1731`, calibration_gap `-0.0159`
- 5d: hit_rate `0.7500`, avg `0.0060`, median `0.0089`, brier `0.1794`, calibration_gap `-0.0159`
- 10d: hit_rate `0.6250`, avg `0.0034`, median `0.0021`, brier `0.2301`, calibration_gap `0.1091`
- 20d: hit_rate `1.0000`, avg `0.0483`, median `0.0498`, brier `0.0712`, calibration_gap `-0.2659`
- 60d: hit_rate `0.8750`, avg `0.0663`, median `0.0738`, brier `0.1282`, calibration_gap `-0.1409`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0017`, median `0.0079`, brier `0.2303`, calibration_gap `0.0853`
- 5d: hit_rate `0.6250`, avg `0.0025`, median `0.0080`, brier `0.2335`, calibration_gap `0.0853`
- 10d: hit_rate `0.6875`, avg `0.0023`, median `0.0060`, brier `0.2089`, calibration_gap `0.0228`
- 20d: hit_rate `0.8750`, avg `0.0325`, median `0.0414`, brier `0.1348`, calibration_gap `-0.1647`
- 60d: hit_rate `0.9375`, avg `0.0914`, median `0.0922`, brier `0.1133`, calibration_gap `-0.2272`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5625`, avg `0.0026`, median `0.0041`, brier `0.2493`, calibration_gap `0.0497`
- 5d: hit_rate `0.5750`, avg `0.0050`, median `0.0073`, brier `0.2512`, calibration_gap `0.0372`
- 10d: hit_rate `0.6125`, avg `0.0079`, median `0.0071`, brier `0.2356`, calibration_gap `-0.0003`
- 20d: hit_rate `0.7875`, avg `0.0329`, median `0.0337`, brier `0.1924`, calibration_gap `-0.1753`
- 60d: hit_rate `0.8625`, avg `0.0815`, median `0.0982`, brier `0.1765`, calibration_gap `-0.2503`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0033`, median `0.0081`, brier `0.2395`, calibration_gap `-0.0793`
- 5d: hit_rate `0.8125`, avg `0.0162`, median `0.0160`, brier `0.2198`, calibration_gap `-0.2668`
- 10d: hit_rate `0.6250`, avg `0.0205`, median `0.0178`, brier `0.2416`, calibration_gap `-0.0793`
- 20d: hit_rate `0.8125`, avg `0.0475`, median `0.0343`, brier `0.2242`, calibration_gap `-0.2668`
- 60d: hit_rate `0.6875`, avg `0.0770`, median `0.1128`, brier `0.2367`, calibration_gap `-0.1418`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
