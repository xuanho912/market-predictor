# High Confidence Signal Report

Generated at: `2026-07-31T14:38:27.788520+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0127`, median `-0.0096`, brier `0.4018`, calibration_gap `0.4083`
- 5d: hit_rate `0.5000`, avg `-0.0176`, median `-0.0108`, brier `0.3327`, calibration_gap `0.2833`
- 10d: hit_rate `0.0000`, avg `-0.0128`, median `-0.0096`, brier `0.6135`, calibration_gap `0.7833`
- 20d: hit_rate `0.5000`, avg `0.0082`, median `0.0094`, brier `0.3309`, calibration_gap `0.2833`
- 60d: hit_rate `0.6250`, avg `0.0230`, median `0.0225`, brier `0.2616`, calibration_gap `0.1583`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0061`, median `-0.0054`, brier `0.3620`, calibration_gap `0.3382`
- 5d: hit_rate `0.6250`, avg `-0.0081`, median `0.0022`, brier `0.2601`, calibration_gap `0.1507`
- 10d: hit_rate `0.2500`, avg `-0.0052`, median `-0.0074`, brier `0.4689`, calibration_gap `0.5257`
- 20d: hit_rate `0.5000`, avg `0.0153`, median `0.0094`, brier `0.3276`, calibration_gap `0.2757`
- 60d: hit_rate `0.6875`, avg `0.0412`, median `0.0352`, brier `0.2253`, calibration_gap `0.0882`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0076`, median `0.0102`, brier `0.2067`, calibration_gap `0.0032`
- 5d: hit_rate `0.6500`, avg `0.0127`, median `0.0156`, brier `0.2273`, calibration_gap `0.0532`
- 10d: hit_rate `0.8500`, avg `0.0308`, median `0.0346`, brier `0.1483`, calibration_gap `-0.1468`
- 20d: hit_rate `0.9000`, avg `0.0518`, median `0.0551`, brier `0.1295`, calibration_gap `-0.1968`
- 60d: hit_rate `0.7000`, avg `0.0425`, median `0.0854`, brier `0.2117`, calibration_gap `0.0032`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0073`, median `-0.0079`, brier `0.3067`, calibration_gap `0.2489`
- 5d: hit_rate `0.2500`, avg `-0.0143`, median `-0.0116`, brier `0.3776`, calibration_gap `0.4364`
- 10d: hit_rate `0.5000`, avg `-0.0054`, median `0.0033`, brier `0.2854`, calibration_gap `0.1864`
- 20d: hit_rate `0.6250`, avg `-0.0203`, median `0.0083`, brier `0.2379`, calibration_gap `0.0614`
- 60d: hit_rate `0.3125`, avg `-0.0777`, median `-0.1215`, brier `0.3542`, calibration_gap `0.3739`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
