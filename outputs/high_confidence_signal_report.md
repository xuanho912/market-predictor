# High Confidence Signal Report

Generated at: `2026-09-04T08:17:05.602147+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0077`, median `0.0116`, brier `0.1914`, calibration_gap `-0.0504`
- 5d: hit_rate `0.6250`, avg `0.0078`, median `0.0088`, brier `0.2402`, calibration_gap `0.0746`
- 10d: hit_rate `0.5000`, avg `0.0099`, median `0.0053`, brier `0.2956`, calibration_gap `0.1996`
- 20d: hit_rate `0.8750`, avg `0.0408`, median `0.0509`, brier `0.1362`, calibration_gap `-0.1754`
- 60d: hit_rate `0.7500`, avg `0.0797`, median `0.1108`, brier `0.1948`, calibration_gap `-0.0504`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0042`, median `0.0116`, brier `0.2133`, calibration_gap `-0.0063`
- 5d: hit_rate `0.6875`, avg `0.0076`, median `0.0116`, brier `0.2169`, calibration_gap `-0.0063`
- 10d: hit_rate `0.6250`, avg `0.0118`, median `0.0141`, brier `0.2446`, calibration_gap `0.0562`
- 20d: hit_rate `0.8125`, avg `0.0364`, median `0.0493`, brier `0.1649`, calibration_gap `-0.1313`
- 60d: hit_rate `0.7500`, avg `0.0622`, median `0.0805`, brier `0.1938`, calibration_gap `-0.0688`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0048`, median `0.0084`, brier `0.2372`, calibration_gap `0.0087`
- 5d: hit_rate `0.6125`, avg `0.0063`, median `0.0089`, brier `0.2378`, calibration_gap `0.0087`
- 10d: hit_rate `0.6625`, avg `0.0130`, median `0.0138`, brier `0.2274`, calibration_gap `-0.0413`
- 20d: hit_rate `0.7625`, avg `0.0271`, median `0.0312`, brier `0.1964`, calibration_gap `-0.1413`
- 60d: hit_rate `0.7250`, avg `0.0510`, median `0.0716`, brier `0.2088`, calibration_gap `-0.1038`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0062`, median `0.0084`, brier `0.2368`, calibration_gap `-0.0439`
- 5d: hit_rate `0.6875`, avg `0.0106`, median `0.0096`, brier `0.2274`, calibration_gap `-0.1064`
- 10d: hit_rate `0.6250`, avg `0.0079`, median `0.0114`, brier `0.2367`, calibration_gap `-0.0439`
- 20d: hit_rate `0.5625`, avg `0.0119`, median `0.0057`, brier `0.2461`, calibration_gap `0.0186`
- 60d: hit_rate `0.6875`, avg `0.0538`, median `0.0711`, brier `0.2259`, calibration_gap `-0.1064`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
