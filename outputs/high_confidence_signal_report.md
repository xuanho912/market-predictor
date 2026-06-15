# High Confidence Signal Report

Generated at: `2026-06-15T13:43:04.743371+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0026`, median `0.0031`, brier `0.2416`, calibration_gap `0.0892`
- 5d: hit_rate `0.3750`, avg `-0.0075`, median `-0.0157`, brier `0.3477`, calibration_gap `0.3392`
- 10d: hit_rate `0.8750`, avg `0.0117`, median `0.0135`, brier `0.1373`, calibration_gap `-0.1608`
- 20d: hit_rate `0.7500`, avg `0.0097`, median `0.0142`, brier `0.1837`, calibration_gap `-0.0358`
- 60d: hit_rate `0.3750`, avg `-0.0092`, median `-0.0282`, brier `0.3510`, calibration_gap `0.3392`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0038`, median `0.0002`, brier `0.2881`, calibration_gap `0.2021`
- 5d: hit_rate `0.3125`, avg `-0.0087`, median `-0.0104`, brier `0.3640`, calibration_gap `0.3896`
- 10d: hit_rate `0.8125`, avg `0.0093`, median `0.0103`, brier `0.1643`, calibration_gap `-0.1104`
- 20d: hit_rate `0.7500`, avg `0.0100`, median `0.0143`, brier `0.1867`, calibration_gap `-0.0479`
- 60d: hit_rate `0.5000`, avg `0.0076`, median `0.0064`, brier `0.2947`, calibration_gap `0.2021`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0038`, median `0.0046`, brier `0.2444`, calibration_gap `0.0492`
- 5d: hit_rate `0.6250`, avg `0.0046`, median `0.0046`, brier `0.2442`, calibration_gap `0.0367`
- 10d: hit_rate `0.5625`, avg `0.0043`, median `0.0058`, brier `0.2533`, calibration_gap `0.0992`
- 20d: hit_rate `0.6500`, avg `0.0054`, median `0.0158`, brier `0.2214`, calibration_gap `0.0117`
- 60d: hit_rate `0.5625`, avg `0.0233`, median `0.0299`, brier `0.2572`, calibration_gap `0.0992`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0048`, median `0.0088`, brier `0.2345`, calibration_gap `0.0025`
- 5d: hit_rate `0.6875`, avg `0.0084`, median `0.0079`, brier `0.2193`, calibration_gap `-0.0600`
- 10d: hit_rate `0.5000`, avg `-0.0064`, median `-0.0071`, brier `0.2652`, calibration_gap `0.1275`
- 20d: hit_rate `0.3750`, avg `-0.0157`, median `-0.0149`, brier `0.2969`, calibration_gap `0.2525`
- 60d: hit_rate `0.4375`, avg `0.0099`, median `-0.0065`, brier `0.2820`, calibration_gap `0.1900`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
