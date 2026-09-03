# High Confidence Signal Report

Generated at: `2026-09-03T00:49:25.501761+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0077`, median `0.0116`, brier `0.1914`, calibration_gap `-0.0505`
- 5d: hit_rate `0.6250`, avg `0.0078`, median `0.0088`, brier `0.2401`, calibration_gap `0.0745`
- 10d: hit_rate `0.5000`, avg `0.0099`, median `0.0053`, brier `0.2955`, calibration_gap `0.1995`
- 20d: hit_rate `0.8750`, avg `0.0408`, median `0.0509`, brier `0.1362`, calibration_gap `-0.1755`
- 60d: hit_rate `0.7500`, avg `0.0797`, median `0.1108`, brier `0.1947`, calibration_gap `-0.0505`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0029`, median `0.0116`, brier `0.2327`, calibration_gap `0.0561`
- 5d: hit_rate `0.6875`, avg `0.0071`, median `0.0088`, brier `0.2169`, calibration_gap `-0.0064`
- 10d: hit_rate `0.6250`, avg `0.0123`, median `0.0147`, brier `0.2446`, calibration_gap `0.0561`
- 20d: hit_rate `0.8125`, avg `0.0348`, median `0.0483`, brier `0.1650`, calibration_gap `-0.1314`
- 60d: hit_rate `0.7500`, avg `0.0604`, median `0.0805`, brier `0.1938`, calibration_gap `-0.0689`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0048`, median `0.0084`, brier `0.2372`, calibration_gap `0.0086`
- 5d: hit_rate `0.6125`, avg `0.0063`, median `0.0089`, brier `0.2378`, calibration_gap `0.0086`
- 10d: hit_rate `0.6625`, avg `0.0130`, median `0.0138`, brier `0.2274`, calibration_gap `-0.0414`
- 20d: hit_rate `0.7625`, avg `0.0271`, median `0.0312`, brier `0.1964`, calibration_gap `-0.1414`
- 60d: hit_rate `0.7250`, avg `0.0510`, median `0.0716`, brier `0.2089`, calibration_gap `-0.1039`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0062`, median `0.0084`, brier `0.2368`, calibration_gap `-0.0441`
- 5d: hit_rate `0.6875`, avg `0.0106`, median `0.0096`, brier `0.2274`, calibration_gap `-0.1066`
- 10d: hit_rate `0.6250`, avg `0.0079`, median `0.0114`, brier `0.2368`, calibration_gap `-0.0441`
- 20d: hit_rate `0.5625`, avg `0.0119`, median `0.0057`, brier `0.2461`, calibration_gap `0.0184`
- 60d: hit_rate `0.6875`, avg `0.0538`, median `0.0711`, brier `0.2260`, calibration_gap `-0.1066`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
