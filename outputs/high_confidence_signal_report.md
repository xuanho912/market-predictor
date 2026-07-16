# High Confidence Signal Report

Generated at: `2026-07-16T22:35:29.344331+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0050`, median `0.0007`, brier `0.2457`, calibration_gap `0.0937`
- 5d: hit_rate `0.3750`, avg `-0.0050`, median `-0.0020`, brier `0.3562`, calibration_gap `0.3437`
- 10d: hit_rate `0.3750`, avg `-0.0066`, median `-0.0125`, brier `0.3553`, calibration_gap `0.3437`
- 20d: hit_rate `0.8750`, avg `0.0229`, median `0.0205`, brier `0.1326`, calibration_gap `-0.1563`
- 60d: hit_rate `0.8750`, avg `0.0591`, median `0.0519`, brier `0.1330`, calibration_gap `-0.1563`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0057`, median `-0.0010`, brier `0.2967`, calibration_gap `0.2143`
- 5d: hit_rate `0.3750`, avg `-0.0071`, median `-0.0036`, brier `0.3515`, calibration_gap `0.3393`
- 10d: hit_rate `0.3125`, avg `-0.0103`, median `-0.0142`, brier `0.3768`, calibration_gap `0.4018`
- 20d: hit_rate `0.7500`, avg `0.0135`, median `0.0163`, brier `0.1868`, calibration_gap `-0.0357`
- 60d: hit_rate `0.6250`, avg `0.0176`, median `0.0384`, brier `0.2406`, calibration_gap `0.0893`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4250`, avg `-0.0086`, median `-0.0083`, brier `0.3203`, calibration_gap `0.2746`
- 5d: hit_rate `0.4500`, avg `-0.0078`, median `-0.0047`, brier `0.3098`, calibration_gap `0.2496`
- 10d: hit_rate `0.3000`, avg `-0.0074`, median `-0.0101`, brier `0.3703`, calibration_gap `0.3996`
- 20d: hit_rate `0.6250`, avg `0.0086`, median `0.0173`, brier `0.2385`, calibration_gap `0.0746`
- 60d: hit_rate `0.6000`, avg `0.0191`, median `0.0311`, brier `0.2476`, calibration_gap `0.0996`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0063`, median `-0.0106`, brier `0.3531`, calibration_gap `0.3708`
- 5d: hit_rate `0.4375`, avg `-0.0020`, median `-0.0019`, brier `0.3078`, calibration_gap `0.2458`
- 10d: hit_rate `0.3750`, avg `-0.0055`, median `-0.0094`, brier `0.3301`, calibration_gap `0.3083`
- 20d: hit_rate `0.6875`, avg `0.0101`, median `0.0157`, brier `0.2152`, calibration_gap `-0.0042`
- 60d: hit_rate `0.5625`, avg `0.0034`, median `0.0224`, brier `0.2615`, calibration_gap `0.1208`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
