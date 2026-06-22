# High Confidence Signal Report

Generated at: `2026-06-22T23:54:26.864134+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0060`, median `-0.0061`, brier `0.3626`, calibration_gap `0.3544`
- 5d: hit_rate `0.0000`, avg `-0.0182`, median `-0.0150`, brier `0.5321`, calibration_gap `0.7294`
- 10d: hit_rate `0.6250`, avg `0.0048`, median `0.0061`, brier `0.2446`, calibration_gap `0.1044`
- 20d: hit_rate `1.0000`, avg `0.0281`, median `0.0302`, brier `0.0733`, calibration_gap `-0.2706`
- 60d: hit_rate `1.0000`, avg `0.0760`, median `0.0869`, brier `0.0733`, calibration_gap `-0.2706`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0028`, median `-0.0017`, brier `0.3280`, calibration_gap `0.2843`
- 5d: hit_rate `0.2500`, avg `-0.0119`, median `-0.0130`, brier `0.4137`, calibration_gap `0.4718`
- 10d: hit_rate `0.4375`, avg `0.0023`, median `-0.0008`, brier `0.3254`, calibration_gap `0.2843`
- 20d: hit_rate `0.9375`, avg `0.0291`, median `0.0302`, brier `0.1040`, calibration_gap `-0.2157`
- 60d: hit_rate `0.9375`, avg `0.0718`, median `0.0890`, brier `0.1036`, calibration_gap `-0.2157`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4500`, avg `-0.0012`, median `-0.0017`, brier `0.3027`, calibration_gap `0.2264`
- 5d: hit_rate `0.4500`, avg `-0.0041`, median `-0.0066`, brier `0.3095`, calibration_gap `0.2264`
- 10d: hit_rate `0.3833`, avg `-0.0039`, median `-0.0033`, brier `0.3261`, calibration_gap `0.2931`
- 20d: hit_rate `0.7500`, avg `0.0102`, median `0.0179`, brier `0.1856`, calibration_gap `-0.0736`
- 60d: hit_rate `0.6333`, avg `0.0241`, median `0.0400`, brier `0.2279`, calibration_gap `0.0431`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0012`, median `0.0041`, brier `0.2196`, calibration_gap `-0.0697`
- 5d: hit_rate `0.6250`, avg `0.0024`, median `0.0044`, brier `0.2347`, calibration_gap `-0.0072`
- 10d: hit_rate `0.5000`, avg `0.0029`, median `0.0004`, brier `0.2638`, calibration_gap `0.1178`
- 20d: hit_rate `0.6250`, avg `0.0082`, median `0.0068`, brier `0.2344`, calibration_gap `-0.0072`
- 60d: hit_rate `0.7500`, avg `0.0256`, median `0.0557`, brier `0.2052`, calibration_gap `-0.1322`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
