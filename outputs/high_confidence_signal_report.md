# High Confidence Signal Report

Generated at: `2026-10-06T01:31:01.690195+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0073`, median `0.0085`, brier `0.1974`, calibration_gap `0.0278`
- 5d: hit_rate `0.7500`, avg `0.0074`, median `0.0108`, brier `0.1974`, calibration_gap `0.0278`
- 10d: hit_rate `1.0000`, avg `0.0134`, median `0.0143`, brier `0.0496`, calibration_gap `-0.2222`
- 20d: hit_rate `0.7500`, avg `0.0224`, median `0.0253`, brier `0.1974`, calibration_gap `0.0278`
- 60d: hit_rate `1.0000`, avg `0.0976`, median `0.0940`, brier `0.0496`, calibration_gap `-0.2222`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0026`, median `0.0082`, brier `0.2375`, calibration_gap `0.1130`
- 5d: hit_rate `0.6250`, avg `0.0031`, median `0.0080`, brier `0.2377`, calibration_gap `0.1130`
- 10d: hit_rate `0.7500`, avg `0.0066`, median `0.0083`, brier `0.1636`, calibration_gap `-0.0120`
- 20d: hit_rate `0.8125`, avg `0.0285`, median `0.0387`, brier `0.1658`, calibration_gap `-0.0745`
- 60d: hit_rate `1.0000`, avg `0.1005`, median `0.1069`, brier `0.0709`, calibration_gap `-0.2620`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5667`, avg `0.0018`, median `0.0034`, brier `0.2527`, calibration_gap `0.0571`
- 5d: hit_rate `0.5167`, avg `0.0030`, median `0.0031`, brier `0.2583`, calibration_gap `0.1071`
- 10d: hit_rate `0.6667`, avg `0.0074`, median `0.0053`, brier `0.2177`, calibration_gap `-0.0429`
- 20d: hit_rate `0.7833`, avg `0.0308`, median `0.0304`, brier `0.2032`, calibration_gap `-0.1596`
- 60d: hit_rate `0.9333`, avg `0.0857`, median `0.0998`, brier `0.1578`, calibration_gap `-0.3096`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0007`, median `0.0042`, brier `0.2492`, calibration_gap `-0.0399`
- 5d: hit_rate `0.5000`, avg `0.0074`, median `-0.0032`, brier `0.2488`, calibration_gap `0.0226`
- 10d: hit_rate `0.6875`, avg `0.0132`, median `0.0052`, brier `0.2400`, calibration_gap `-0.1649`
- 20d: hit_rate `0.7500`, avg `0.0348`, median `0.0284`, brier `0.2343`, calibration_gap `-0.2274`
- 60d: hit_rate `0.8750`, avg `0.0828`, median `0.1086`, brier `0.2323`, calibration_gap `-0.3524`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
