# High Confidence Signal Report

Generated at: `2026-06-26T05:41:04.143793+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0069`, median `-0.0015`, brier `0.3546`, calibration_gap `0.3493`
- 5d: hit_rate `0.1250`, avg `-0.0150`, median `-0.0176`, brier `0.4673`, calibration_gap `0.5993`
- 10d: hit_rate `0.8750`, avg `0.0123`, median `0.0135`, brier `0.1336`, calibration_gap `-0.1507`
- 20d: hit_rate `1.0000`, avg `0.0222`, median `0.0277`, brier `0.0760`, calibration_gap `-0.2757`
- 60d: hit_rate `0.6250`, avg `0.0242`, median `0.0380`, brier `0.2439`, calibration_gap `0.0993`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0008`, median `0.0002`, brier `0.2973`, calibration_gap `0.2144`
- 5d: hit_rate `0.1875`, avg `-0.0113`, median `-0.0130`, brier `0.4311`, calibration_gap `0.5269`
- 10d: hit_rate `0.5625`, avg `0.0035`, median `0.0048`, brier `0.2622`, calibration_gap `0.1519`
- 20d: hit_rate `0.8750`, avg `0.0156`, median `0.0233`, brier `0.1313`, calibration_gap `-0.1606`
- 60d: hit_rate `0.7500`, avg `0.0400`, median `0.0599`, brier `0.1916`, calibration_gap `-0.0356`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5000`, avg `0.0015`, median `0.0004`, brier `0.2784`, calibration_gap `0.1700`
- 5d: hit_rate `0.4500`, avg `-0.0009`, median `-0.0027`, brier `0.3109`, calibration_gap `0.2200`
- 10d: hit_rate `0.4750`, avg `0.0029`, median `-0.0015`, brier `0.2909`, calibration_gap `0.1950`
- 20d: hit_rate `0.7250`, avg `0.0141`, median `0.0184`, brier `0.1902`, calibration_gap `-0.0550`
- 60d: hit_rate `0.8250`, avg `0.0557`, median `0.0696`, brier `0.1627`, calibration_gap `-0.1550`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0018`, median `0.0017`, brier `0.2489`, calibration_gap `0.0521`
- 5d: hit_rate `0.5625`, avg `0.0015`, median `0.0053`, brier `0.2480`, calibration_gap `0.0521`
- 10d: hit_rate `0.5625`, avg `0.0005`, median `0.0028`, brier `0.2482`, calibration_gap `0.0521`
- 20d: hit_rate `0.5000`, avg `0.0001`, median `-0.0010`, brier `0.2633`, calibration_gap `0.1146`
- 60d: hit_rate `0.5000`, avg `0.0053`, median `-0.0049`, brier `0.2634`, calibration_gap `0.1146`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
