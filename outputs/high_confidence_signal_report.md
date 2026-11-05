# High Confidence Signal Report

Generated at: `2026-11-05T01:56:06.788209+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0107`, median `0.0189`, brier `0.2479`, calibration_gap `0.0806`
- 5d: hit_rate `0.6250`, avg `0.0066`, median `0.0149`, brier `0.2479`, calibration_gap `0.0806`
- 10d: hit_rate `0.5000`, avg `0.0020`, median `0.0043`, brier `0.2999`, calibration_gap `0.2056`
- 20d: hit_rate `0.5000`, avg `-0.0079`, median `-0.0024`, brier `0.2999`, calibration_gap `0.2056`
- 60d: hit_rate `0.8750`, avg `0.0532`, median `0.0674`, brier `0.1456`, calibration_gap `-0.1694`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0019`, median `-0.0006`, brier `0.2880`, calibration_gap `0.1906`
- 5d: hit_rate `0.5625`, avg `0.0002`, median `0.0014`, brier `0.2648`, calibration_gap `0.1281`
- 10d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0204`, brier `0.3337`, calibration_gap `0.3156`
- 20d: hit_rate `0.3750`, avg `-0.0163`, median `-0.0291`, brier `0.3337`, calibration_gap `0.3156`
- 60d: hit_rate `0.8125`, avg `0.0446`, median `0.0444`, brier `0.1694`, calibration_gap `-0.1219`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0048`, median `0.0059`, brier `0.2376`, calibration_gap `-0.0640`
- 5d: hit_rate `0.4375`, avg `-0.0022`, median `-0.0030`, brier `0.2622`, calibration_gap `0.1235`
- 10d: hit_rate `0.4375`, avg `-0.0109`, median `-0.0105`, brier `0.2590`, calibration_gap `0.1235`
- 20d: hit_rate `0.5000`, avg `-0.0178`, median `-0.0148`, brier `0.2541`, calibration_gap `0.0610`
- 60d: hit_rate `0.7500`, avg `0.0517`, median `0.0511`, brier `0.2246`, calibration_gap `-0.1890`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
