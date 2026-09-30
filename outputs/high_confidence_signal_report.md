# High Confidence Signal Report

Generated at: `2026-09-30T18:04:03.393677+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0005`, median `0.0031`, brier `0.2667`, calibration_gap `0.1942`
- 5d: hit_rate `0.6250`, avg `-0.0013`, median `0.0056`, brier `0.2667`, calibration_gap `0.1942`
- 10d: hit_rate `0.5000`, avg `-0.0035`, median `-0.0047`, brier `0.3550`, calibration_gap `0.3192`
- 20d: hit_rate `0.7500`, avg `0.0196`, median `0.0173`, brier `0.1936`, calibration_gap `0.0692`
- 60d: hit_rate `1.0000`, avg `0.0443`, median `0.0415`, brier `0.0328`, calibration_gap `-0.1808`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0019`, median `0.0051`, brier `0.2664`, calibration_gap `0.1827`
- 5d: hit_rate `0.6250`, avg `-0.0001`, median `0.0068`, brier `0.2664`, calibration_gap `0.1827`
- 10d: hit_rate `0.6250`, avg `-0.0040`, median `0.0040`, brier `0.2729`, calibration_gap `0.1827`
- 20d: hit_rate `0.6875`, avg `0.0132`, median `0.0173`, brier `0.2299`, calibration_gap `0.1202`
- 60d: hit_rate `0.8750`, avg `0.0500`, median `0.0565`, brier `0.1118`, calibration_gap `-0.0673`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5750`, avg `0.0018`, median `0.0034`, brier `0.2700`, calibration_gap `0.1544`
- 5d: hit_rate `0.6000`, avg `-0.0024`, median `0.0024`, brier `0.2614`, calibration_gap `0.1294`
- 10d: hit_rate `0.6000`, avg `-0.0005`, median `0.0056`, brier `0.2666`, calibration_gap `0.1294`
- 20d: hit_rate `0.7000`, avg `0.0100`, median `0.0157`, brier `0.2225`, calibration_gap `0.0294`
- 60d: hit_rate `0.8000`, avg `0.0312`, median `0.0366`, brier `0.1602`, calibration_gap `-0.0706`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0019`, median `0.0025`, brier `0.2543`, calibration_gap `0.0871`
- 5d: hit_rate `0.5625`, avg `-0.0047`, median `0.0013`, brier `0.2550`, calibration_gap `0.0871`
- 10d: hit_rate `0.6250`, avg `0.0023`, median `0.0089`, brier `0.2382`, calibration_gap `0.0246`
- 20d: hit_rate `0.6875`, avg `0.0028`, median `0.0126`, brier `0.2187`, calibration_gap `-0.0379`
- 60d: hit_rate `0.6875`, avg `0.0044`, median `0.0284`, brier `0.2163`, calibration_gap `-0.0379`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
