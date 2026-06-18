# High Confidence Signal Report

Generated at: `2026-06-18T00:01:45.101792+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0035`, median `0.0059`, brier `0.2504`, calibration_gap `0.1100`
- 5d: hit_rate `0.2500`, avg `-0.0065`, median `-0.0104`, brier `0.4265`, calibration_gap `0.4850`
- 10d: hit_rate `0.7500`, avg `0.0108`, median `0.0069`, brier `0.1839`, calibration_gap `-0.0150`
- 20d: hit_rate `1.0000`, avg `0.0294`, median `0.0300`, brier `0.0703`, calibration_gap `-0.2650`
- 60d: hit_rate `0.8750`, avg `0.0607`, median `0.0790`, brier `0.1273`, calibration_gap `-0.1400`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0033`, median `0.0072`, brier `0.2480`, calibration_gap `0.1028`
- 5d: hit_rate `0.3750`, avg `-0.0041`, median `-0.0082`, brier `0.3644`, calibration_gap `0.3528`
- 10d: hit_rate `0.4375`, avg `0.0041`, median `-0.0016`, brier `0.3242`, calibration_gap `0.2903`
- 20d: hit_rate `0.9375`, avg `0.0289`, median `0.0290`, brier `0.1022`, calibration_gap `-0.2097`
- 60d: hit_rate `0.9375`, avg `0.0675`, median `0.0708`, brier `0.1027`, calibration_gap `-0.2097`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6000`, avg `0.0037`, median `0.0026`, brier `0.2396`, calibration_gap `0.0449`
- 5d: hit_rate `0.5500`, avg `0.0033`, median `0.0043`, brier `0.2602`, calibration_gap `0.0949`
- 10d: hit_rate `0.4500`, avg `0.0049`, median `-0.0041`, brier `0.2913`, calibration_gap `0.1949`
- 20d: hit_rate `0.8000`, avg `0.0186`, median `0.0196`, brier `0.1905`, calibration_gap `-0.1551`
- 60d: hit_rate `0.8000`, avg `0.0648`, median `0.0737`, brier `0.1867`, calibration_gap `-0.1551`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0000`, median `-0.0022`, brier `0.2692`, calibration_gap `0.1332`
- 5d: hit_rate `0.5000`, avg `-0.0012`, median `0.0036`, brier `0.2681`, calibration_gap `0.1332`
- 10d: hit_rate `0.5625`, avg `0.0030`, median `0.0046`, brier `0.2509`, calibration_gap `0.0707`
- 20d: hit_rate `0.6875`, avg `0.0086`, median `0.0215`, brier `0.2167`, calibration_gap `-0.0543`
- 60d: hit_rate `0.6250`, avg `0.0235`, median `0.0633`, brier `0.2337`, calibration_gap `0.0082`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
