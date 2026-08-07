# High Confidence Signal Report

Generated at: `2026-08-07T22:11:18.045818+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0046`, median `0.0069`, brier `0.1303`, calibration_gap `-0.1519`
- 5d: hit_rate `0.8750`, avg `0.0069`, median `0.0112`, brier `0.1303`, calibration_gap `-0.1519`
- 10d: hit_rate `0.8750`, avg `0.0149`, median `0.0199`, brier `0.1303`, calibration_gap `-0.1519`
- 20d: hit_rate `0.5000`, avg `0.0083`, median `0.0002`, brier `0.3037`, calibration_gap `0.2231`
- 60d: hit_rate `0.3750`, avg `0.0028`, median `-0.0336`, brier `0.3559`, calibration_gap `0.3481`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0013`, median `0.0030`, brier `0.2359`, calibration_gap `0.0858`
- 5d: hit_rate `0.6250`, avg `-0.0015`, median `0.0057`, brier `0.2343`, calibration_gap `0.0858`
- 10d: hit_rate `0.6250`, avg `0.0047`, median `0.0117`, brier `0.2349`, calibration_gap `0.0858`
- 20d: hit_rate `0.5625`, avg `0.0051`, median `0.0048`, brier `0.2721`, calibration_gap `0.1483`
- 60d: hit_rate `0.3125`, avg `-0.0043`, median `-0.0308`, brier `0.3730`, calibration_gap `0.3983`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0036`, median `0.0051`, brier `0.2382`, calibration_gap `0.0596`
- 5d: hit_rate `0.6875`, avg `0.0059`, median `0.0057`, brier `0.2129`, calibration_gap `-0.0029`
- 10d: hit_rate `0.5875`, avg `0.0059`, median `0.0082`, brier `0.2504`, calibration_gap `0.0971`
- 20d: hit_rate `0.6750`, avg `0.0100`, median `0.0136`, brier `0.2202`, calibration_gap `0.0096`
- 60d: hit_rate `0.5750`, avg `0.0223`, median `0.0318`, brier `0.2609`, calibration_gap `0.1096`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0089`, median `0.0117`, brier `0.1949`, calibration_gap `-0.0848`
- 5d: hit_rate `0.6250`, avg `0.0042`, median `0.0071`, brier `0.2374`, calibration_gap `0.0402`
- 10d: hit_rate `0.6250`, avg `-0.0063`, median `0.0052`, brier `0.2374`, calibration_gap `0.0402`
- 20d: hit_rate `0.5000`, avg `-0.0198`, median `0.0005`, brier `0.2780`, calibration_gap `0.1652`
- 60d: hit_rate `0.7500`, avg `0.0274`, median `0.0541`, brier `0.1949`, calibration_gap `-0.0848`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
