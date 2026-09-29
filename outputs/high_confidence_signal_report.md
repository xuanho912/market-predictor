# High Confidence Signal Report

Generated at: `2026-09-29T18:07:43.142880+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0096`, median `0.0085`, brier `0.1919`, calibration_gap `0.0813`
- 5d: hit_rate `0.7500`, avg `0.0034`, median `0.0068`, brier `0.1919`, calibration_gap `0.0813`
- 10d: hit_rate `0.7500`, avg `0.0029`, median `0.0060`, brier `0.1968`, calibration_gap `0.0813`
- 20d: hit_rate `0.6250`, avg `0.0206`, median `0.0228`, brier `0.2754`, calibration_gap `0.2063`
- 60d: hit_rate `1.0000`, avg `0.0633`, median `0.0717`, brier `0.0285`, calibration_gap `-0.1687`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0019`, median `0.0051`, brier `0.2675`, calibration_gap `0.1947`
- 5d: hit_rate `0.6250`, avg `-0.0001`, median `0.0068`, brier `0.2675`, calibration_gap `0.1947`
- 10d: hit_rate `0.6250`, avg `-0.0040`, median `0.0040`, brier `0.2699`, calibration_gap `0.1947`
- 20d: hit_rate `0.6875`, avg `0.0132`, median `0.0173`, brier `0.2317`, calibration_gap `0.1322`
- 60d: hit_rate `0.8750`, avg `0.0500`, median `0.0565`, brier `0.1082`, calibration_gap `-0.0553`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0032`, median `-0.0043`, brier `0.2880`, calibration_gap `0.2068`
- 5d: hit_rate `0.5625`, avg `-0.0062`, median `0.0009`, brier `0.2495`, calibration_gap `0.0818`
- 10d: hit_rate `0.6250`, avg `0.0048`, median `0.0134`, brier `0.2319`, calibration_gap `0.0193`
- 20d: hit_rate `0.8750`, avg `0.0259`, median `0.0342`, brier `0.1620`, calibration_gap `-0.2307`
- 60d: hit_rate `0.8750`, avg `0.0541`, median `0.0604`, brier `0.1620`, calibration_gap `-0.2307`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
