# High Confidence Signal Report

Generated at: `2026-10-23T23:59:42.112654+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0013`, median `0.0004`, brier `0.3430`, calibration_gap `0.2985`
- 5d: hit_rate `0.2500`, avg `-0.0011`, median `-0.0077`, brier `0.4912`, calibration_gap `0.5485`
- 10d: hit_rate `0.6250`, avg `0.0092`, median `0.0068`, brier `0.2629`, calibration_gap `0.1735`
- 20d: hit_rate `0.8750`, avg `0.0294`, median `0.0297`, brier `0.1165`, calibration_gap `-0.0765`
- 60d: hit_rate `1.0000`, avg `0.0739`, median `0.0738`, brier `0.0407`, calibration_gap `-0.2015`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0027`, median `0.0004`, brier `0.3321`, calibration_gap `0.2855`
- 5d: hit_rate `0.3750`, avg `-0.0017`, median `-0.0055`, brier `0.4061`, calibration_gap `0.4105`
- 10d: hit_rate `0.5000`, avg `0.0069`, median `0.0024`, brier `0.3293`, calibration_gap `0.2855`
- 20d: hit_rate `0.8125`, avg `0.0216`, median `0.0278`, brier `0.1510`, calibration_gap `-0.0270`
- 60d: hit_rate `0.9375`, avg `0.0634`, median `0.0732`, brier `0.0803`, calibration_gap `-0.1520`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0020`, median `0.0023`, brier `0.2674`, calibration_gap `0.1427`
- 5d: hit_rate `0.6250`, avg `0.0025`, median `0.0052`, brier `0.2350`, calibration_gap `0.0677`
- 10d: hit_rate `0.6500`, avg `0.0069`, median `0.0082`, brier `0.2242`, calibration_gap `0.0427`
- 20d: hit_rate `0.6750`, avg `0.0128`, median `0.0132`, brier `0.2177`, calibration_gap `0.0177`
- 60d: hit_rate `0.7000`, avg `0.0225`, median `0.0171`, brier `0.2115`, calibration_gap `-0.0073`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0008`, median `0.0002`, brier `0.2796`, calibration_gap `0.1753`
- 5d: hit_rate `0.5000`, avg `-0.0017`, median `-0.0011`, brier `0.2795`, calibration_gap `0.1753`
- 10d: hit_rate `0.5625`, avg `-0.0014`, median `0.0030`, brier `0.2577`, calibration_gap `0.1128`
- 20d: hit_rate `0.6250`, avg `0.0004`, median `0.0076`, brier `0.2364`, calibration_gap `0.0503`
- 60d: hit_rate `0.6875`, avg `0.0166`, median `0.0282`, brier `0.2166`, calibration_gap `-0.0122`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
