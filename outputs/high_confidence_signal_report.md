# High Confidence Signal Report

Generated at: `2026-10-20T01:45:59.946531+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0045`, median `-0.0058`, brier `0.3730`, calibration_gap `0.3708`
- 5d: hit_rate `0.5000`, avg `-0.0013`, median `-0.0072`, brier `0.3084`, calibration_gap `0.2458`
- 10d: hit_rate `0.3750`, avg `0.0046`, median `-0.0032`, brier `0.3730`, calibration_gap `0.3708`
- 20d: hit_rate `0.8750`, avg `0.0512`, median `0.0584`, brier `0.1245`, calibration_gap `-0.1292`
- 60d: hit_rate `0.8750`, avg `0.1030`, median `0.1233`, brier `0.1245`, calibration_gap `-0.1292`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0046`, median `-0.0016`, brier `0.3387`, calibration_gap `0.3015`
- 5d: hit_rate `0.5625`, avg `-0.0044`, median `0.0025`, brier `0.2779`, calibration_gap `0.1765`
- 10d: hit_rate `0.3125`, avg `-0.0000`, median `-0.0082`, brier `0.3969`, calibration_gap `0.4265`
- 20d: hit_rate `0.7500`, avg `0.0299`, median `0.0255`, brier `0.1865`, calibration_gap `-0.0110`
- 60d: hit_rate `0.7500`, avg `0.0630`, median `0.0661`, brier `0.1858`, calibration_gap `-0.0110`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0009`, median `-0.0085`, brier `0.3308`, calibration_gap `0.2977`
- 5d: hit_rate `0.5625`, avg `0.0059`, median `0.0051`, brier `0.2589`, calibration_gap `0.1102`
- 10d: hit_rate `0.6875`, avg `0.0195`, median `0.0212`, brier `0.2127`, calibration_gap `-0.0148`
- 20d: hit_rate `0.8750`, avg `0.0503`, median `0.0533`, brier `0.1479`, calibration_gap `-0.2023`
- 60d: hit_rate `1.0000`, avg `0.1132`, median `0.1263`, brier `0.1073`, calibration_gap `-0.3273`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
