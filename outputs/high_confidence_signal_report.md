# High Confidence Signal Report

Generated at: `2026-08-11T23:27:41.513980+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0034`, median `0.0069`, brier `0.1866`, calibration_gap `-0.0234`
- 5d: hit_rate `0.8750`, avg `0.0081`, median `0.0130`, brier `0.1320`, calibration_gap `-0.1484`
- 10d: hit_rate `0.7500`, avg `0.0118`, median `0.0199`, brier `0.1866`, calibration_gap `-0.0234`
- 20d: hit_rate `0.3750`, avg `0.0043`, median `-0.0114`, brier `0.3586`, calibration_gap `0.3516`
- 60d: hit_rate `0.3750`, avg `0.0043`, median `-0.0274`, brier `0.3586`, calibration_gap `0.3516`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0010`, median `0.0008`, brier `0.2406`, calibration_gap `0.0921`
- 5d: hit_rate `0.7500`, avg `0.0054`, median `0.0069`, brier `0.1866`, calibration_gap `-0.0329`
- 10d: hit_rate `0.6250`, avg `0.0094`, median `0.0127`, brier `0.2401`, calibration_gap `0.0921`
- 20d: hit_rate `0.6250`, avg `0.0163`, median `0.0094`, brier `0.2476`, calibration_gap `0.0921`
- 60d: hit_rate `0.4375`, avg `0.0081`, median `-0.0108`, brier `0.3259`, calibration_gap `0.2796`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0023`, median `0.0043`, brier `0.2402`, calibration_gap `0.0659`
- 5d: hit_rate `0.6750`, avg `0.0037`, median `0.0048`, brier `0.2178`, calibration_gap `0.0159`
- 10d: hit_rate `0.5375`, avg `0.0055`, median `0.0027`, brier `0.2719`, calibration_gap `0.1534`
- 20d: hit_rate `0.6625`, avg `0.0112`, median `0.0120`, brier `0.2263`, calibration_gap `0.0284`
- 60d: hit_rate `0.5625`, avg `0.0240`, median `0.0383`, brier `0.2671`, calibration_gap `0.1284`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0077`, median `0.0087`, brier `0.1945`, calibration_gap `-0.0789`
- 5d: hit_rate `0.6250`, avg `0.0067`, median `0.0071`, brier `0.2383`, calibration_gap `0.0461`
- 10d: hit_rate `0.6250`, avg `0.0132`, median `0.0052`, brier `0.2379`, calibration_gap `0.0461`
- 20d: hit_rate `0.6875`, avg `0.0215`, median `0.0121`, brier `0.2150`, calibration_gap `-0.0164`
- 60d: hit_rate `0.8125`, avg `0.0495`, median `0.0692`, brier `0.1714`, calibration_gap `-0.1414`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
