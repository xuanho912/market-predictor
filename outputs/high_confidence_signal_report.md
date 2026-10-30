# High Confidence Signal Report

Generated at: `2026-10-30T18:09:39.502448+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0071`, median `0.0017`, brier `0.3437`, calibration_gap `0.3124`
- 5d: hit_rate `0.5000`, avg `0.0105`, median `0.0049`, brier `0.3437`, calibration_gap `0.3124`
- 10d: hit_rate `0.5000`, avg `0.0179`, median `0.0111`, brier `0.3482`, calibration_gap `0.3124`
- 20d: hit_rate `0.8750`, avg `0.0362`, median `0.0300`, brier `0.1179`, calibration_gap `-0.0626`
- 60d: hit_rate `1.0000`, avg `0.0790`, median `0.0738`, brier `0.0354`, calibration_gap `-0.1876`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0073`, median `0.0075`, brier `0.3019`, calibration_gap `0.2362`
- 5d: hit_rate `0.4375`, avg `0.0058`, median `-0.0038`, brier `0.3719`, calibration_gap `0.3612`
- 10d: hit_rate `0.5625`, avg `0.0146`, median `0.0135`, brier `0.3043`, calibration_gap `0.2362`
- 20d: hit_rate `0.8750`, avg `0.0325`, median `0.0299`, brier `0.1172`, calibration_gap `-0.0763`
- 60d: hit_rate `0.9375`, avg `0.0738`, median `0.0745`, brier `0.0759`, calibration_gap `-0.1388`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4750`, avg `0.0016`, median `-0.0013`, brier `0.3328`, calibration_gap `0.2916`
- 5d: hit_rate `0.4750`, avg `0.0048`, median `-0.0038`, brier `0.3346`, calibration_gap `0.2916`
- 10d: hit_rate `0.6000`, avg `0.0135`, median `0.0160`, brier `0.2690`, calibration_gap `0.1666`
- 20d: hit_rate `0.8000`, avg `0.0307`, median `0.0307`, brier `0.1598`, calibration_gap `-0.0334`
- 60d: hit_rate `0.8750`, avg `0.0602`, median `0.0705`, brier `0.1164`, calibration_gap `-0.1084`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0019`, median `-0.0059`, brier `0.3230`, calibration_gap `0.3306`
- 5d: hit_rate `0.7500`, avg `0.0037`, median `0.0126`, brier `0.1981`, calibration_gap `-0.1069`
- 10d: hit_rate `0.6875`, avg `0.0022`, median `0.0137`, brier `0.2151`, calibration_gap `-0.0444`
- 20d: hit_rate `0.5000`, avg `-0.0103`, median `-0.0136`, brier `0.2690`, calibration_gap `0.1431`
- 60d: hit_rate `0.5000`, avg `0.0003`, median `-0.0003`, brier `0.2702`, calibration_gap `0.1431`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
