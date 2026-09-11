# High Confidence Signal Report

Generated at: `2026-09-11T08:20:01.949994+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0012`, median `0.0014`, brier `0.2603`, calibration_gap `0.1749`
- 5d: hit_rate `0.6250`, avg `0.0010`, median `0.0010`, brier `0.2661`, calibration_gap `0.1749`
- 10d: hit_rate `0.1250`, avg `-0.0157`, median `-0.0204`, brier `0.5668`, calibration_gap `0.6749`
- 20d: hit_rate `0.3750`, avg `-0.0101`, median `-0.0055`, brier `0.4203`, calibration_gap `0.4249`
- 60d: hit_rate `0.6250`, avg `0.0221`, median `0.0453`, brier `0.2635`, calibration_gap `0.1749`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0048`, median `0.0038`, brier `0.2235`, calibration_gap `0.0966`
- 5d: hit_rate `0.7500`, avg `0.0022`, median `0.0039`, brier `0.1933`, calibration_gap `0.0341`
- 10d: hit_rate `0.3125`, avg `-0.0085`, median `-0.0200`, brier `0.4441`, calibration_gap `0.4716`
- 20d: hit_rate `0.6250`, avg `0.0028`, median `0.0142`, brier `0.2703`, calibration_gap `0.1591`
- 60d: hit_rate `0.6250`, avg `0.0269`, median `0.0586`, brier `0.2598`, calibration_gap `0.1591`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `-0.0009`, median `0.0052`, brier `0.2764`, calibration_gap `0.1578`
- 5d: hit_rate `0.5500`, avg `-0.0041`, median `0.0015`, brier `0.2763`, calibration_gap `0.1578`
- 10d: hit_rate `0.4250`, avg `0.0015`, median `-0.0048`, brier `0.3434`, calibration_gap `0.2828`
- 20d: hit_rate `0.6500`, avg `0.0173`, median `0.0150`, brier `0.2376`, calibration_gap `0.0578`
- 60d: hit_rate `0.6500`, avg `0.0393`, median `0.0538`, brier `0.2424`, calibration_gap `0.0578`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0043`, median `0.0111`, brier `0.2329`, calibration_gap `0.0362`
- 5d: hit_rate `0.5625`, avg `0.0032`, median `0.0040`, brier `0.2549`, calibration_gap `0.0987`
- 10d: hit_rate `0.5625`, avg `0.0045`, median `0.0119`, brier `0.2558`, calibration_gap `0.0987`
- 20d: hit_rate `0.6875`, avg `0.0170`, median `0.0111`, brier `0.2148`, calibration_gap `-0.0263`
- 60d: hit_rate `0.7500`, avg `0.0426`, median `0.0538`, brier `0.1945`, calibration_gap `-0.0888`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
