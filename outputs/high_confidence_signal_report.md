# High Confidence Signal Report

Generated at: `2026-11-12T02:35:24.158635+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0069`, median `-0.0096`, brier `0.3936`, calibration_gap `0.4478`
- 5d: hit_rate `0.2500`, avg `-0.0104`, median `-0.0180`, brier `0.3936`, calibration_gap `0.4478`
- 10d: hit_rate `0.1250`, avg `-0.0342`, median `-0.0472`, brier `0.4405`, calibration_gap `0.5728`
- 20d: hit_rate `0.1250`, avg `-0.0358`, median `-0.0321`, brier `0.4405`, calibration_gap `0.5728`
- 60d: hit_rate `0.5000`, avg `0.0136`, median `0.0108`, brier `0.2899`, calibration_gap `0.1978`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0009`, median `-0.0017`, brier `0.2936`, calibration_gap `0.1869`
- 5d: hit_rate `0.4375`, avg `-0.0004`, median `-0.0073`, brier `0.3155`, calibration_gap `0.2494`
- 10d: hit_rate `0.3750`, avg `-0.0126`, median `-0.0324`, brier `0.3390`, calibration_gap `0.3119`
- 20d: hit_rate `0.3750`, avg `-0.0143`, median `-0.0225`, brier `0.3390`, calibration_gap `0.3119`
- 60d: hit_rate `0.6250`, avg `0.0301`, median `0.0403`, brier `0.2415`, calibration_gap `0.0619`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0043`, median `0.0122`, brier `0.2339`, calibration_gap `-0.0370`
- 5d: hit_rate `0.6250`, avg `0.0060`, median `0.0110`, brier `0.2381`, calibration_gap `-0.0120`
- 10d: hit_rate `0.6250`, avg `0.0114`, median `0.0233`, brier `0.2424`, calibration_gap `-0.0120`
- 20d: hit_rate `0.6750`, avg `0.0148`, median `0.0232`, brier `0.2326`, calibration_gap `-0.0620`
- 60d: hit_rate `0.9000`, avg `0.0651`, median `0.0757`, brier `0.1720`, calibration_gap `-0.2870`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `-0.0029`, median `0.0114`, brier `0.2258`, calibration_gap `-0.1118`
- 5d: hit_rate `0.6250`, avg `0.0031`, median `0.0095`, brier `0.2371`, calibration_gap `-0.0493`
- 10d: hit_rate `0.6250`, avg `0.0053`, median `0.0099`, brier `0.2365`, calibration_gap `-0.0493`
- 20d: hit_rate `0.6250`, avg `-0.0012`, median `0.0039`, brier `0.2365`, calibration_gap `-0.0493`
- 60d: hit_rate `0.8125`, avg `0.0527`, median `0.0696`, brier `0.2059`, calibration_gap `-0.2368`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
