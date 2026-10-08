# High Confidence Signal Report

Generated at: `2026-10-08T00:32:47.277952+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0073`, median `0.0085`, brier `0.1968`, calibration_gap `0.0070`
- 5d: hit_rate `0.7500`, avg `0.0074`, median `0.0108`, brier `0.1968`, calibration_gap `0.0070`
- 10d: hit_rate `1.0000`, avg `0.0134`, median `0.0143`, brier `0.0594`, calibration_gap `-0.2430`
- 20d: hit_rate `0.7500`, avg `0.0224`, median `0.0253`, brier `0.1968`, calibration_gap `0.0070`
- 60d: hit_rate `1.0000`, avg `0.0976`, median `0.0940`, brier `0.0594`, calibration_gap `-0.2430`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0015`, median `0.0079`, brier `0.2384`, calibration_gap `0.0988`
- 5d: hit_rate `0.6250`, avg `0.0019`, median `0.0080`, brier `0.2388`, calibration_gap `0.0988`
- 10d: hit_rate `0.6875`, avg `0.0022`, median `0.0060`, brier `0.1904`, calibration_gap `0.0363`
- 20d: hit_rate `0.8125`, avg `0.0251`, median `0.0358`, brier `0.1686`, calibration_gap `-0.0887`
- 60d: hit_rate `0.9375`, avg `0.0936`, median `0.0940`, brier `0.0986`, calibration_gap `-0.2137`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5500`, avg `0.0004`, median `0.0025`, brier `0.2527`, calibration_gap `0.0727`
- 5d: hit_rate `0.4833`, avg `0.0006`, median `-0.0035`, brier `0.2611`, calibration_gap `0.1394`
- 10d: hit_rate `0.6333`, avg `0.0053`, median `0.0042`, brier `0.2269`, calibration_gap `-0.0106`
- 20d: hit_rate `0.8500`, avg `0.0342`, median `0.0322`, brier `0.1915`, calibration_gap `-0.2273`
- 60d: hit_rate `0.9333`, avg `0.0864`, median `0.0996`, brier `0.1579`, calibration_gap `-0.3106`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0042`, median `-0.0041`, brier `0.2505`, calibration_gap `0.0329`
- 5d: hit_rate `0.3750`, avg `-0.0006`, median `-0.0113`, brier `0.2556`, calibration_gap `0.1579`
- 10d: hit_rate `0.6250`, avg `0.0075`, median `0.0033`, brier `0.2392`, calibration_gap `-0.0921`
- 20d: hit_rate `0.9375`, avg `0.0428`, median `0.0310`, brier `0.2219`, calibration_gap `-0.4046`
- 60d: hit_rate `0.8750`, avg `0.0886`, median `0.1086`, brier `0.2248`, calibration_gap `-0.3421`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
