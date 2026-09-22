# High Confidence Signal Report

Generated at: `2026-09-22T06:19:49.539378+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0019`, median `0.0014`, brier `0.2646`, calibration_gap `0.1626`
- 5d: hit_rate `0.3750`, avg `-0.0106`, median `-0.0084`, brier `0.4056`, calibration_gap `0.4126`
- 10d: hit_rate `0.3750`, avg `-0.0108`, median `-0.0136`, brier `0.4034`, calibration_gap `0.4126`
- 20d: hit_rate `0.3750`, avg `0.0088`, median `-0.0027`, brier `0.4039`, calibration_gap `0.4126`
- 60d: hit_rate `0.6250`, avg `0.0258`, median `0.0434`, brier `0.2638`, calibration_gap `0.1626`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0074`, median `-0.0083`, brier `0.3960`, calibration_gap `0.4043`
- 5d: hit_rate `0.3750`, avg `-0.0110`, median `-0.0129`, brier `0.3985`, calibration_gap `0.4043`
- 10d: hit_rate `0.3750`, avg `-0.0061`, median `-0.0095`, brier `0.3975`, calibration_gap `0.4043`
- 20d: hit_rate `0.6250`, avg `0.0147`, median `0.0242`, brier `0.2624`, calibration_gap `0.1543`
- 60d: hit_rate `0.7500`, avg `0.0442`, median `0.0618`, brier `0.1923`, calibration_gap `0.0293`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4500`, avg `-0.0040`, median `-0.0027`, brier `0.3262`, calibration_gap `0.2704`
- 5d: hit_rate `0.4667`, avg `-0.0075`, median `-0.0055`, brier `0.3226`, calibration_gap `0.2538`
- 10d: hit_rate `0.4000`, avg `-0.0034`, median `-0.0070`, brier `0.3508`, calibration_gap `0.3204`
- 20d: hit_rate `0.6167`, avg `0.0132`, median `0.0143`, brier `0.2528`, calibration_gap `0.1038`
- 60d: hit_rate `0.7333`, avg `0.0314`, median `0.0397`, brier `0.2024`, calibration_gap `-0.0129`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0004`, median `-0.0024`, brier `0.2993`, calibration_gap `0.2275`
- 5d: hit_rate `0.5625`, avg `0.0015`, median `0.0032`, brier `0.2602`, calibration_gap `0.1025`
- 10d: hit_rate `0.5000`, avg `0.0011`, median `0.0003`, brier `0.2789`, calibration_gap `0.1650`
- 20d: hit_rate `0.6250`, avg `0.0118`, median `0.0180`, brier `0.2422`, calibration_gap `0.0400`
- 60d: hit_rate `0.8750`, avg `0.0304`, median `0.0367`, brier `0.1590`, calibration_gap `-0.2100`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
