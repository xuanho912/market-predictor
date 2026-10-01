# High Confidence Signal Report

Generated at: `2026-10-01T02:04:24.197578+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0019`, median `0.0031`, brier `0.2680`, calibration_gap `0.2012`
- 5d: hit_rate `0.6250`, avg `-0.0013`, median `0.0056`, brier `0.2680`, calibration_gap `0.2012`
- 10d: hit_rate `0.5000`, avg `-0.0107`, median `-0.0065`, brier `0.3574`, calibration_gap `0.3262`
- 20d: hit_rate `0.6250`, avg `0.0112`, median `0.0098`, brier `0.2726`, calibration_gap `0.2012`
- 60d: hit_rate `0.8750`, avg `0.0378`, median `0.0415`, brier `0.1081`, calibration_gap `-0.0488`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0019`, median `0.0051`, brier `0.2679`, calibration_gap `0.1912`
- 5d: hit_rate `0.6250`, avg `-0.0001`, median `0.0068`, brier `0.2679`, calibration_gap `0.1912`
- 10d: hit_rate `0.6250`, avg `-0.0040`, median `0.0040`, brier `0.2741`, calibration_gap `0.1912`
- 20d: hit_rate `0.6875`, avg `0.0132`, median `0.0173`, brier `0.2318`, calibration_gap `0.1287`
- 60d: hit_rate `0.8750`, avg `0.0500`, median `0.0565`, brier `0.1111`, calibration_gap `-0.0588`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5000`, avg `-0.0003`, median `0.0004`, brier `0.2732`, calibration_gap `0.1536`
- 5d: hit_rate `0.6000`, avg `-0.0035`, median `0.0012`, brier `0.2430`, calibration_gap `0.0536`
- 10d: hit_rate `0.6000`, avg `0.0017`, median `0.0082`, brier `0.2468`, calibration_gap `0.0536`
- 20d: hit_rate `0.7500`, avg `0.0084`, median `0.0159`, brier `0.1959`, calibration_gap `-0.0964`
- 60d: hit_rate `0.7500`, avg `0.0119`, median `0.0297`, brier `0.1937`, calibration_gap `-0.0964`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0006`, median `0.0004`, brier `0.2709`, calibration_gap `0.1478`
- 5d: hit_rate `0.5625`, avg `-0.0048`, median `0.0009`, brier `0.2543`, calibration_gap `0.0853`
- 10d: hit_rate `0.6250`, avg `-0.0004`, median `0.0082`, brier `0.2369`, calibration_gap `0.0228`
- 20d: hit_rate `0.6875`, avg `0.0007`, median `0.0126`, brier `0.2187`, calibration_gap `-0.0397`
- 60d: hit_rate `0.6875`, avg `0.0065`, median `0.0284`, brier `0.2160`, calibration_gap `-0.0397`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
