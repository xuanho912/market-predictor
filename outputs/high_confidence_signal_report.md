# High Confidence Signal Report

Generated at: `2026-08-17T23:10:53.198322+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0039`, median `0.0030`, brier `0.1889`, calibration_gap `-0.0247`
- 5d: hit_rate `0.8750`, avg `0.0095`, median `0.0106`, brier `0.1323`, calibration_gap `-0.1497`
- 10d: hit_rate `0.7500`, avg `0.0138`, median `0.0199`, brier `0.1889`, calibration_gap `-0.0247`
- 20d: hit_rate `0.3750`, avg `0.0026`, median `-0.0114`, brier `0.3539`, calibration_gap `0.3503`
- 60d: hit_rate `0.3750`, avg `0.0020`, median `-0.0274`, brier `0.3539`, calibration_gap `0.3503`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0041`, median `0.0030`, brier `0.1886`, calibration_gap `-0.0326`
- 5d: hit_rate `0.8125`, avg `0.0035`, median `0.0052`, brier `0.1600`, calibration_gap `-0.0951`
- 10d: hit_rate `0.5625`, avg `0.0028`, median `0.0117`, brier `0.2682`, calibration_gap `0.1549`
- 20d: hit_rate `0.3125`, avg `-0.0077`, median `-0.0075`, brier `0.3769`, calibration_gap `0.4049`
- 60d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0274`, brier `0.3501`, calibration_gap `0.3424`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5875`, avg `0.0025`, median `0.0025`, brier `0.2511`, calibration_gap `0.0968`
- 5d: hit_rate `0.6250`, avg `0.0026`, median `0.0031`, brier `0.2353`, calibration_gap `0.0593`
- 10d: hit_rate `0.5375`, avg `0.0047`, median `0.0066`, brier `0.2721`, calibration_gap `0.1468`
- 20d: hit_rate `0.6125`, avg `0.0103`, median `0.0160`, brier `0.2480`, calibration_gap `0.0718`
- 60d: hit_rate `0.6000`, avg `0.0216`, median `0.0307`, brier `0.2544`, calibration_gap `0.0843`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0051`, median `0.0018`, brier `0.2744`, calibration_gap `0.1583`
- 5d: hit_rate `0.5000`, avg `0.0017`, median `-0.0018`, brier `0.2748`, calibration_gap `0.1583`
- 10d: hit_rate `0.5000`, avg `0.0027`, median `0.0001`, brier `0.2759`, calibration_gap `0.1583`
- 20d: hit_rate `0.6875`, avg `0.0145`, median `0.0243`, brier `0.2165`, calibration_gap `-0.0292`
- 60d: hit_rate `0.8750`, avg `0.0549`, median `0.0709`, brier `0.1570`, calibration_gap `-0.2167`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
