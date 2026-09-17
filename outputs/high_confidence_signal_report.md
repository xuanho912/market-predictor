# High Confidence Signal Report

Generated at: `2026-09-17T08:57:06.523451+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0066`, median `0.0100`, brier `0.1073`, calibration_gap `-0.0351`
- 5d: hit_rate `0.6250`, avg `0.0023`, median `0.0010`, brier `0.2771`, calibration_gap `0.2149`
- 10d: hit_rate `0.3750`, avg `-0.0081`, median `-0.0136`, brier `0.4546`, calibration_gap `0.4649`
- 20d: hit_rate `0.5000`, avg `0.0113`, median `0.0179`, brier `0.3641`, calibration_gap `0.3399`
- 60d: hit_rate `0.7500`, avg `0.0439`, median `0.0630`, brier `0.1977`, calibration_gap `0.0899`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0043`, median `0.0072`, brier `0.2272`, calibration_gap `0.1351`
- 5d: hit_rate `0.6250`, avg `-0.0000`, median `0.0020`, brier `0.2727`, calibration_gap `0.1976`
- 10d: hit_rate `0.6250`, avg `0.0020`, median `0.0087`, brier `0.2836`, calibration_gap `0.1976`
- 20d: hit_rate `0.6250`, avg `0.0173`, median `0.0311`, brier `0.2779`, calibration_gap `0.1976`
- 60d: hit_rate `0.6875`, avg `0.0430`, median `0.0635`, brier `0.2320`, calibration_gap `0.1351`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0077`, median `-0.0134`, brier `0.3358`, calibration_gap `0.3497`
- 5d: hit_rate `0.5625`, avg `-0.0011`, median `0.0012`, brier `0.2551`, calibration_gap `0.0997`
- 10d: hit_rate `0.5000`, avg `0.0021`, median `0.0050`, brier `0.2749`, calibration_gap `0.1622`
- 20d: hit_rate `0.5625`, avg `0.0220`, median `0.0127`, brier `0.2550`, calibration_gap `0.0997`
- 60d: hit_rate `0.9375`, avg `0.0715`, median `0.0910`, brier `0.1344`, calibration_gap `-0.2753`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
