# High Confidence Signal Report

Generated at: `2026-11-11T01:32:27.770726+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0046`, median `-0.0096`, brier `0.4272`, calibration_gap `0.4903`
- 5d: hit_rate `0.2500`, avg `-0.0113`, median `-0.0155`, brier `0.4272`, calibration_gap `0.4903`
- 10d: hit_rate `0.1250`, avg `-0.0335`, median `-0.0428`, brier `0.4912`, calibration_gap `0.6153`
- 20d: hit_rate `0.1250`, avg `-0.0332`, median `-0.0291`, brier `0.4912`, calibration_gap `0.6153`
- 60d: hit_rate `0.6250`, avg `0.0232`, median `0.0295`, brier `0.2545`, calibration_gap `0.1153`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0002`, median `-0.0028`, brier `0.3358`, calibration_gap `0.2923`
- 5d: hit_rate `0.4375`, avg `-0.0015`, median `-0.0119`, brier `0.3358`, calibration_gap `0.2923`
- 10d: hit_rate `0.3125`, avg `-0.0130`, median `-0.0288`, brier `0.3946`, calibration_gap `0.4173`
- 20d: hit_rate `0.3125`, avg `-0.0233`, median `-0.0291`, brier `0.3946`, calibration_gap `0.4173`
- 60d: hit_rate `0.7500`, avg `0.0365`, median `0.0403`, brier `0.1935`, calibration_gap `-0.0202`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0134`, median `0.0114`, brier `0.2199`, calibration_gap `-0.1761`
- 5d: hit_rate `0.5625`, avg `0.0095`, median `0.0090`, brier `0.2442`, calibration_gap `0.0114`
- 10d: hit_rate `0.5625`, avg `0.0055`, median `0.0009`, brier `0.2475`, calibration_gap `0.0114`
- 20d: hit_rate `0.5625`, avg `0.0025`, median `0.0040`, brier `0.2463`, calibration_gap `0.0114`
- 60d: hit_rate `0.9375`, avg `0.1049`, median `0.1185`, brier `0.1918`, calibration_gap `-0.3636`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
