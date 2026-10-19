# High Confidence Signal Report

Generated at: `2026-10-19T18:46:46.481912+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0045`, median `-0.0058`, brier `0.3701`, calibration_gap `0.3665`
- 5d: hit_rate `0.5000`, avg `-0.0013`, median `-0.0072`, brier `0.3069`, calibration_gap `0.2415`
- 10d: hit_rate `0.3750`, avg `0.0046`, median `-0.0032`, brier `0.3701`, calibration_gap `0.3665`
- 20d: hit_rate `0.8750`, avg `0.0512`, median `0.0584`, brier `0.1255`, calibration_gap `-0.1335`
- 60d: hit_rate `0.8750`, avg `0.1030`, median `0.1233`, brier `0.1255`, calibration_gap `-0.1335`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0055`, median `-0.0016`, brier `0.3361`, calibration_gap `0.2972`
- 5d: hit_rate `0.5000`, avg `-0.0046`, median `0.0012`, brier `0.3044`, calibration_gap `0.2347`
- 10d: hit_rate `0.3125`, avg `0.0024`, median `-0.0060`, brier `0.3933`, calibration_gap `0.4222`
- 20d: hit_rate `0.7500`, avg `0.0327`, median `0.0363`, brier `0.1862`, calibration_gap `-0.0153`
- 60d: hit_rate `0.8125`, avg `0.0718`, median `0.0755`, brier `0.1577`, calibration_gap `-0.0778`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0009`, median `-0.0085`, brier `0.3304`, calibration_gap `0.2979`
- 5d: hit_rate `0.5625`, avg `0.0059`, median `0.0051`, brier `0.2588`, calibration_gap `0.1104`
- 10d: hit_rate `0.6875`, avg `0.0195`, median `0.0212`, brier `0.2127`, calibration_gap `-0.0146`
- 20d: hit_rate `0.8750`, avg `0.0503`, median `0.0533`, brier `0.1478`, calibration_gap `-0.2021`
- 60d: hit_rate `1.0000`, avg `0.1132`, median `0.1263`, brier `0.1072`, calibration_gap `-0.3271`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
