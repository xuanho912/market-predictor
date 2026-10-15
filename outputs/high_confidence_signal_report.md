# High Confidence Signal Report

Generated at: `2026-10-15T17:04:55.243027+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0090`, median `-0.0101`, brier `0.4459`, calibration_gap `0.5056`
- 5d: hit_rate `0.3750`, avg `-0.0100`, median `-0.0216`, brier `0.3792`, calibration_gap `0.3806`
- 10d: hit_rate `0.2500`, avg `-0.0103`, median `-0.0082`, brier `0.4459`, calibration_gap `0.5056`
- 20d: hit_rate `0.7500`, avg `0.0403`, median `0.0509`, brier `0.1842`, calibration_gap `0.0056`
- 60d: hit_rate `0.8750`, avg `0.0864`, median `0.1108`, brier `0.1223`, calibration_gap `-0.1194`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0078`, median `-0.0101`, brier `0.4387`, calibration_gap `0.5001`
- 5d: hit_rate `0.3125`, avg `-0.0153`, median `-0.0226`, brier `0.4054`, calibration_gap `0.4376`
- 10d: hit_rate `0.3125`, avg `-0.0077`, median `-0.0082`, brier `0.4086`, calibration_gap `0.4376`
- 20d: hit_rate `0.5000`, avg `0.0206`, median `0.0095`, brier `0.3084`, calibration_gap `0.2501`
- 60d: hit_rate `0.7500`, avg `0.0589`, median `0.0693`, brier `0.1855`, calibration_gap `0.0001`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0102`, median `-0.0116`, brier `0.3734`, calibration_gap `0.4294`
- 5d: hit_rate `0.2500`, avg `-0.0156`, median `-0.0238`, brier `0.3758`, calibration_gap `0.4294`
- 10d: hit_rate `0.2500`, avg `-0.0205`, median `-0.0259`, brier `0.3738`, calibration_gap `0.4294`
- 20d: hit_rate `0.6250`, avg `0.0136`, median `0.0337`, brier `0.2367`, calibration_gap `0.0544`
- 60d: hit_rate `0.8125`, avg `0.0787`, median `0.1011`, brier `0.1720`, calibration_gap `-0.1331`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
