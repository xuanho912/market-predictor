# High Confidence Signal Report

Generated at: `2026-07-08T23:58:10.701809+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0141`, median `-0.0089`, brier `0.3730`, calibration_gap `0.3691`
- 5d: hit_rate `0.2500`, avg `-0.0175`, median `-0.0145`, brier `0.4327`, calibration_gap `0.4941`
- 10d: hit_rate `0.3750`, avg `-0.0067`, median `-0.0092`, brier `0.3754`, calibration_gap `0.3691`
- 20d: hit_rate `0.8750`, avg `0.0193`, median `0.0302`, brier `0.1239`, calibration_gap `-0.1309`
- 60d: hit_rate `0.8750`, avg `0.0618`, median `0.0761`, brier `0.1239`, calibration_gap `-0.1309`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0069`, median `-0.0054`, brier `0.3370`, calibration_gap `0.2968`
- 5d: hit_rate `0.4375`, avg `-0.0090`, median `-0.0130`, brier `0.3390`, calibration_gap `0.2968`
- 10d: hit_rate `0.3750`, avg `-0.0024`, median `-0.0066`, brier `0.3665`, calibration_gap `0.3593`
- 20d: hit_rate `0.8750`, avg `0.0289`, median `0.0302`, brier `0.1282`, calibration_gap `-0.1407`
- 60d: hit_rate `0.8750`, avg `0.0698`, median `0.0827`, brier `0.1280`, calibration_gap `-0.1407`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0004`, median `0.0022`, brier `0.2777`, calibration_gap `0.1534`
- 5d: hit_rate `0.5250`, avg `-0.0019`, median `0.0016`, brier `0.2925`, calibration_gap `0.1784`
- 10d: hit_rate `0.5000`, avg `0.0031`, median `-0.0001`, brier `0.3014`, calibration_gap `0.2034`
- 20d: hit_rate `0.7750`, avg `0.0174`, median `0.0209`, brier `0.1773`, calibration_gap `-0.0716`
- 60d: hit_rate `0.7500`, avg `0.0417`, median `0.0522`, brier `0.1853`, calibration_gap `-0.0466`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0062`, median `0.0079`, brier `0.1943`, calibration_gap `-0.0869`
- 5d: hit_rate `0.6875`, avg `0.0070`, median `0.0080`, brier `0.2151`, calibration_gap `-0.0244`
- 10d: hit_rate `0.6250`, avg `0.0104`, median `0.0165`, brier `0.2357`, calibration_gap `0.0381`
- 20d: hit_rate `0.6250`, avg `-0.0019`, median `0.0166`, brier `0.2346`, calibration_gap `0.0381`
- 60d: hit_rate `0.6250`, avg `0.0207`, median `0.0482`, brier `0.2342`, calibration_gap `0.0381`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
