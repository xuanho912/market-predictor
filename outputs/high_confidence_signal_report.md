# High Confidence Signal Report

Generated at: `2026-09-03T16:28:19.380573+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0051`, median `-0.0095`, brier `0.3845`, calibration_gap `0.3859`
- 5d: hit_rate `0.5000`, avg `-0.0013`, median `-0.0019`, brier `0.3160`, calibration_gap `0.2609`
- 10d: hit_rate `0.2500`, avg `-0.0106`, median `-0.0212`, brier `0.4511`, calibration_gap `0.5109`
- 20d: hit_rate `0.5000`, avg `0.0090`, median `0.0087`, brier `0.3183`, calibration_gap `0.2609`
- 60d: hit_rate `1.0000`, avg `0.0496`, median `0.0479`, brier `0.0572`, calibration_gap `-0.2391`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0025`, median `0.0018`, brier `0.2553`, calibration_gap `0.1290`
- 5d: hit_rate `0.6250`, avg `0.0048`, median `0.0026`, brier `0.2519`, calibration_gap `0.1290`
- 10d: hit_rate `0.3125`, avg `-0.0044`, median `-0.0147`, brier `0.4120`, calibration_gap `0.4415`
- 20d: hit_rate `0.6250`, avg `0.0061`, median `0.0103`, brier `0.2535`, calibration_gap `0.1290`
- 60d: hit_rate `0.9375`, avg `0.0353`, median `0.0479`, brier `0.0920`, calibration_gap `-0.1835`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5250`, avg `0.0016`, median `0.0019`, brier `0.2902`, calibration_gap `0.2015`
- 5d: hit_rate `0.5250`, avg `0.0013`, median `0.0003`, brier `0.2929`, calibration_gap `0.2015`
- 10d: hit_rate `0.4750`, avg `0.0052`, median `-0.0008`, brier `0.3143`, calibration_gap `0.2515`
- 20d: hit_rate `0.8000`, avg `0.0218`, median `0.0274`, brier `0.1678`, calibration_gap `-0.0735`
- 60d: hit_rate `0.8750`, avg `0.0569`, median `0.0651`, brier `0.1318`, calibration_gap `-0.1485`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0044`, median `-0.0007`, brier `0.2943`, calibration_gap `0.2104`
- 5d: hit_rate `0.5625`, avg `0.0043`, median `0.0026`, brier `0.2677`, calibration_gap `0.1479`
- 10d: hit_rate `0.3750`, avg `0.0025`, median `-0.0071`, brier `0.3472`, calibration_gap `0.3354`
- 20d: hit_rate `0.6250`, avg `0.0186`, median `0.0293`, brier `0.2424`, calibration_gap `0.0854`
- 60d: hit_rate `0.7500`, avg `0.0577`, median `0.0708`, brier `0.1902`, calibration_gap `-0.0396`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
