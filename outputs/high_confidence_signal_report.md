# High Confidence Signal Report

Generated at: `2026-08-28T12:50:58.877463+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0031`, median `0.0007`, brier `0.2558`, calibration_gap `0.1305`
- 5d: hit_rate `0.3750`, avg `-0.0085`, median `-0.0084`, brier `0.3754`, calibration_gap `0.3805`
- 10d: hit_rate `0.2500`, avg `-0.0119`, median `-0.0127`, brier `0.4448`, calibration_gap `0.5055`
- 20d: hit_rate `0.6250`, avg `0.0062`, median `0.0166`, brier `0.2497`, calibration_gap `0.1305`
- 60d: hit_rate `0.7500`, avg `0.0251`, median `0.0396`, brier `0.1824`, calibration_gap `0.0055`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0004`, median `0.0012`, brier `0.2515`, calibration_gap `0.1204`
- 5d: hit_rate `0.4375`, avg `-0.0055`, median `-0.0079`, brier `0.3382`, calibration_gap `0.3079`
- 10d: hit_rate `0.4375`, avg `-0.0035`, median `-0.0073`, brier `0.3452`, calibration_gap `0.3079`
- 20d: hit_rate `0.6875`, avg `0.0049`, median `0.0166`, brier `0.2188`, calibration_gap `0.0579`
- 60d: hit_rate `0.7500`, avg `0.0337`, median `0.0396`, brier `0.1855`, calibration_gap `-0.0046`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `0.0008`, median `0.0039`, brier `0.2584`, calibration_gap `0.1146`
- 5d: hit_rate `0.5333`, avg `0.0012`, median `0.0021`, brier `0.2772`, calibration_gap `0.1646`
- 10d: hit_rate `0.5000`, avg `0.0028`, median `-0.0020`, brier `0.2876`, calibration_gap `0.1979`
- 20d: hit_rate `0.6833`, avg `0.0107`, median `0.0198`, brier `0.2131`, calibration_gap `0.0146`
- 60d: hit_rate `0.6500`, avg `0.0306`, median `0.0209`, brier `0.2309`, calibration_gap `0.0479`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0038`, median `0.0104`, brier `0.2388`, calibration_gap `0.0466`
- 5d: hit_rate `0.5000`, avg `0.0016`, median `-0.0004`, brier `0.2804`, calibration_gap `0.1716`
- 10d: hit_rate `0.5000`, avg `0.0001`, median `-0.0060`, brier `0.2770`, calibration_gap `0.1716`
- 20d: hit_rate `0.5625`, avg `0.0050`, median `0.0028`, brier `0.2581`, calibration_gap `0.1091`
- 60d: hit_rate `0.8125`, avg `0.0597`, median `0.0558`, brier `0.1698`, calibration_gap `-0.1409`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
