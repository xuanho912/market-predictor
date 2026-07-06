# High Confidence Signal Report

Generated at: `2026-07-06T14:50:47.843425+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.0000`, avg `-0.0137`, median `-0.0097`, brier `0.5167`, calibration_gap `0.7186`
- 5d: hit_rate `0.2500`, avg `-0.0124`, median `-0.0114`, brier `0.4125`, calibration_gap `0.4686`
- 10d: hit_rate `0.2500`, avg `-0.0103`, median `-0.0128`, brier `0.4104`, calibration_gap `0.4686`
- 20d: hit_rate `0.5000`, avg `-0.0062`, median `-0.0053`, brier `0.2886`, calibration_gap `0.2186`
- 60d: hit_rate `0.2500`, avg `-0.0384`, median `-0.0651`, brier `0.3956`, calibration_gap `0.4686`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0092`, median `-0.0070`, brier `0.4289`, calibration_gap `0.5232`
- 5d: hit_rate `0.5000`, avg `-0.0045`, median `-0.0005`, brier `0.3006`, calibration_gap `0.2107`
- 10d: hit_rate `0.3750`, avg `-0.0016`, median `-0.0038`, brier `0.3507`, calibration_gap `0.3357`
- 20d: hit_rate `0.6875`, avg `0.0108`, median `0.0145`, brier `0.2137`, calibration_gap `0.0232`
- 60d: hit_rate `0.5000`, avg `0.0020`, median `-0.0121`, brier `0.2923`, calibration_gap `0.2107`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4750`, avg `-0.0024`, median `-0.0005`, brier `0.3068`, calibration_gap `0.2072`
- 5d: hit_rate `0.4500`, avg `-0.0039`, median `-0.0023`, brier `0.3094`, calibration_gap `0.2322`
- 10d: hit_rate `0.4500`, avg `0.0029`, median `-0.0045`, brier `0.3096`, calibration_gap `0.2322`
- 20d: hit_rate `0.6500`, avg `0.0114`, median `0.0119`, brier `0.2284`, calibration_gap `0.0322`
- 60d: hit_rate `0.6250`, avg `0.0332`, median `0.0516`, brier `0.2392`, calibration_gap `0.0572`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0067`, median `0.0063`, brier `0.2180`, calibration_gap `-0.0448`
- 5d: hit_rate `0.5000`, avg `-0.0027`, median `-0.0026`, brier `0.2726`, calibration_gap `0.1427`
- 10d: hit_rate `0.5000`, avg `0.0019`, median `0.0007`, brier `0.2721`, calibration_gap `0.1427`
- 20d: hit_rate `0.7500`, avg `0.0020`, median `0.0032`, brier `0.2001`, calibration_gap `-0.1073`
- 60d: hit_rate `0.5000`, avg `0.0100`, median `0.0031`, brier `0.2713`, calibration_gap `0.1427`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
