# High Confidence Signal Report

Generated at: `2026-10-28T18:23:50.106704+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0044`, median `0.0029`, brier `0.2545`, calibration_gap `0.1219`
- 5d: hit_rate `0.3750`, avg `0.0040`, median `-0.0085`, brier `0.3774`, calibration_gap `0.3719`
- 10d: hit_rate `0.7500`, avg `0.0176`, median `0.0188`, brier `0.1863`, calibration_gap `-0.0031`
- 20d: hit_rate `0.7500`, avg `0.0254`, median `0.0297`, brier `0.1856`, calibration_gap `-0.0031`
- 60d: hit_rate `0.8750`, avg `0.0501`, median `0.0708`, brier `0.1232`, calibration_gap `-0.1281`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0032`, median `0.0027`, brier `0.2788`, calibration_gap `0.1764`
- 5d: hit_rate `0.5000`, avg `0.0024`, median `0.0029`, brier `0.3114`, calibration_gap `0.2389`
- 10d: hit_rate `0.5625`, avg `0.0072`, median `0.0054`, brier `0.2735`, calibration_gap `0.1764`
- 20d: hit_rate `0.6250`, avg `0.0138`, median `0.0205`, brier `0.2445`, calibration_gap `0.1139`
- 60d: hit_rate `0.8125`, avg `0.0528`, median `0.0708`, brier `0.1557`, calibration_gap `-0.0736`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6500`, avg `0.0052`, median `0.0058`, brier `0.2324`, calibration_gap `0.0328`
- 5d: hit_rate `0.6333`, avg `0.0083`, median `0.0099`, brier `0.2422`, calibration_gap `0.0495`
- 10d: hit_rate `0.7667`, avg `0.0154`, median `0.0185`, brier `0.1920`, calibration_gap `-0.0838`
- 20d: hit_rate `0.7667`, avg `0.0259`, median `0.0287`, brier `0.1797`, calibration_gap `-0.0838`
- 60d: hit_rate `0.7333`, avg `0.0361`, median `0.0509`, brier `0.1917`, calibration_gap `-0.0505`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0039`, median `0.0058`, brier `0.2364`, calibration_gap `0.0194`
- 5d: hit_rate `0.6875`, avg `0.0088`, median `0.0130`, brier `0.2166`, calibration_gap `-0.0431`
- 10d: hit_rate `0.8750`, avg `0.0193`, median `0.0262`, brier `0.1619`, calibration_gap `-0.2306`
- 20d: hit_rate `0.5625`, avg `0.0189`, median `0.0233`, brier `0.2531`, calibration_gap `0.0819`
- 60d: hit_rate `0.6875`, avg `0.0246`, median `0.0375`, brier `0.2134`, calibration_gap `-0.0431`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
