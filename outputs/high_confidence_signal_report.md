# High Confidence Signal Report

Generated at: `2026-10-01T00:11:00.570148+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0095`, median `0.0126`, brier `0.1910`, calibration_gap `0.0189`
- 5d: hit_rate `0.7500`, avg `0.0072`, median `0.0118`, brier `0.1910`, calibration_gap `0.0189`
- 10d: hit_rate `1.0000`, avg `0.0090`, median `0.0083`, brier `0.0535`, calibration_gap `-0.2311`
- 20d: hit_rate `0.7500`, avg `0.0265`, median `0.0342`, brier `0.1910`, calibration_gap `0.0189`
- 60d: hit_rate `1.0000`, avg `0.0987`, median `0.0940`, brier `0.0535`, calibration_gap `-0.2311`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0050`, median `0.0116`, brier `0.2153`, calibration_gap `0.0558`
- 5d: hit_rate `0.6875`, avg `0.0058`, median `0.0089`, brier `0.2125`, calibration_gap `0.0558`
- 10d: hit_rate `0.7500`, avg `0.0063`, median `0.0083`, brier `0.1708`, calibration_gap `-0.0067`
- 20d: hit_rate `0.8750`, avg `0.0341`, median `0.0424`, brier `0.1356`, calibration_gap `-0.1317`
- 60d: hit_rate `0.9375`, avg `0.0930`, median `0.0940`, brier `0.0911`, calibration_gap `-0.1942`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6000`, avg `0.0030`, median `0.0043`, brier `0.2441`, calibration_gap `0.0774`
- 5d: hit_rate `0.6000`, avg `0.0039`, median `0.0056`, brier `0.2450`, calibration_gap `0.0774`
- 10d: hit_rate `0.7500`, avg `0.0092`, median `0.0100`, brier `0.1878`, calibration_gap `-0.0726`
- 20d: hit_rate `0.8500`, avg `0.0369`, median `0.0387`, brier `0.1669`, calibration_gap `-0.1726`
- 60d: hit_rate `0.9250`, avg `0.0906`, median `0.1058`, brier `0.1272`, calibration_gap `-0.2476`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0026`, median `-0.0075`, brier `0.2651`, calibration_gap `0.1107`
- 5d: hit_rate `0.5000`, avg `0.0059`, median `-0.0040`, brier `0.2505`, calibration_gap `0.0482`
- 10d: hit_rate `0.6875`, avg `0.0125`, median `0.0162`, brier `0.2341`, calibration_gap `-0.1393`
- 20d: hit_rate `0.8125`, avg `0.0461`, median `0.0311`, brier `0.2210`, calibration_gap `-0.2643`
- 60d: hit_rate `0.7500`, avg `0.0783`, median `0.0891`, brier `0.2274`, calibration_gap `-0.2018`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
