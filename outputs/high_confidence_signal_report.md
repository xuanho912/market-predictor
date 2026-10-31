# High Confidence Signal Report

Generated at: `2026-10-31T01:18:15.637016+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0057`, median `-0.0096`, brier `0.4378`, calibration_gap `0.4932`
- 5d: hit_rate `0.2500`, avg `-0.0159`, median `-0.0155`, brier `0.4378`, calibration_gap `0.4932`
- 10d: hit_rate `0.0000`, avg `-0.0414`, median `-0.0412`, brier `0.5526`, calibration_gap `0.7432`
- 20d: hit_rate `0.0000`, avg `-0.0411`, median `-0.0362`, brier `0.5526`, calibration_gap `0.7432`
- 60d: hit_rate `0.6250`, avg `0.0089`, median `0.0107`, brier `0.2609`, calibration_gap `0.1182`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0003`, median `-0.0033`, brier `0.3407`, calibration_gap `0.2916`
- 5d: hit_rate `0.4375`, avg `-0.0038`, median `-0.0073`, brier `0.3398`, calibration_gap `0.2916`
- 10d: hit_rate `0.2500`, avg `-0.0154`, median `-0.0291`, brier `0.4241`, calibration_gap `0.4791`
- 20d: hit_rate `0.2500`, avg `-0.0178`, median `-0.0254`, brier `0.4241`, calibration_gap `0.4791`
- 60d: hit_rate `0.5625`, avg `0.0217`, median `0.0107`, brier `0.2782`, calibration_gap `0.1666`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0093`, median `0.0080`, brier `0.2157`, calibration_gap `-0.1687`
- 5d: hit_rate `0.5625`, avg `0.0070`, median `0.0048`, brier `0.2412`, calibration_gap `0.0188`
- 10d: hit_rate `0.5000`, avg `-0.0023`, median `-0.0023`, brier `0.2560`, calibration_gap `0.0813`
- 20d: hit_rate `0.6250`, avg `0.0022`, median `0.0163`, brier `0.2372`, calibration_gap `-0.0437`
- 60d: hit_rate `0.9375`, avg `0.1030`, median `0.1118`, brier `0.1852`, calibration_gap `-0.3562`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
