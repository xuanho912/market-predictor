# High Confidence Signal Report

Generated at: `2026-08-13T23:29:17.461212+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `20`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `2`
- 3d: hit_rate `1.0000`, avg `0.0182`, median `0.0182`, brier `0.0778`, calibration_gap `-0.2790`
- 5d: hit_rate `0.5000`, avg `-0.0054`, median `-0.0054`, brier `0.3015`, calibration_gap `0.2210`
- 10d: hit_rate `0.5000`, avg `0.0024`, median `0.0024`, brier `0.2962`, calibration_gap `0.2210`
- 20d: hit_rate `0.0000`, avg `-0.0181`, median `-0.0181`, brier `0.5199`, calibration_gap `0.7210`
- 60d: hit_rate `0.0000`, avg `-0.0536`, median `-0.0536`, brier `0.5199`, calibration_gap `0.7210`

### top_20_confidence_signals
- sample_size: `4`
- 3d: hit_rate `1.0000`, avg `0.0199`, median `0.0182`, brier `0.0880`, calibration_gap `-0.2961`
- 5d: hit_rate `0.5000`, avg `0.0002`, median `-0.0054`, brier `0.2937`, calibration_gap `0.2039`
- 10d: hit_rate `0.5000`, avg `-0.0077`, median `0.0024`, brier `0.2911`, calibration_gap `0.2039`
- 20d: hit_rate `0.2500`, avg `-0.0119`, median `-0.0181`, brier `0.4029`, calibration_gap `0.4539`
- 60d: hit_rate `0.2500`, avg `0.0083`, median `-0.0290`, brier `0.4029`, calibration_gap `0.4539`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0083`, median `0.0104`, brier `0.2214`, calibration_gap `0.0274`
- 5d: hit_rate `0.5500`, avg `0.0021`, median `0.0013`, brier `0.2622`, calibration_gap `0.1274`
- 10d: hit_rate `0.5500`, avg `0.0073`, median `0.0090`, brier `0.2648`, calibration_gap `0.1274`
- 20d: hit_rate `0.6000`, avg `0.0173`, median `0.0107`, brier `0.2541`, calibration_gap `0.0774`
- 60d: hit_rate `0.8000`, avg `0.0525`, median `0.0637`, brier `0.1837`, calibration_gap `-0.1226`

### low_confidence_reference
- sample_size: `4`
- 3d: hit_rate `0.2500`, avg `-0.0022`, median `-0.0032`, brier `0.3553`, calibration_gap `0.4113`
- 5d: hit_rate `0.2500`, avg `-0.0102`, median `-0.0070`, brier `0.3553`, calibration_gap `0.4113`
- 10d: hit_rate `0.5000`, avg `-0.0081`, median `-0.0047`, brier `0.2771`, calibration_gap `0.1613`
- 20d: hit_rate `0.7500`, avg `-0.0188`, median `0.0107`, brier `0.1965`, calibration_gap `-0.0887`
- 60d: hit_rate `0.7500`, avg `0.0256`, median `0.0415`, brier `0.1965`, calibration_gap `-0.0887`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
