# High Confidence Signal Report

Generated at: `2026-07-06T23:55:54.243223+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0118`, median `-0.0090`, brier `0.4624`, calibration_gap `0.5916`
- 5d: hit_rate `0.3750`, avg `-0.0051`, median `-0.0029`, brier `0.3572`, calibration_gap `0.3416`
- 10d: hit_rate `0.5000`, avg `-0.0011`, median `-0.0038`, brier `0.3024`, calibration_gap `0.2166`
- 20d: hit_rate `0.5000`, avg `-0.0060`, median `-0.0069`, brier `0.2885`, calibration_gap `0.2166`
- 60d: hit_rate `0.3750`, avg `-0.0169`, median `-0.0459`, brier `0.3427`, calibration_gap `0.3416`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0046`, median `-0.0019`, brier `0.3513`, calibration_gap `0.3330`
- 5d: hit_rate `0.6250`, avg `0.0007`, median `0.0034`, brier `0.2491`, calibration_gap `0.0830`
- 10d: hit_rate `0.5625`, avg `0.0042`, median `0.0055`, brier `0.2721`, calibration_gap `0.1455`
- 20d: hit_rate `0.6250`, avg `0.0024`, median `0.0120`, brier `0.2392`, calibration_gap `0.0830`
- 60d: hit_rate `0.3750`, avg `-0.0228`, median `-0.0398`, brier `0.3412`, calibration_gap `0.3330`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.4750`, avg `-0.0031`, median `-0.0005`, brier `0.3034`, calibration_gap `0.2075`
- 5d: hit_rate `0.4500`, avg `-0.0046`, median `-0.0023`, brier `0.3073`, calibration_gap `0.2325`
- 10d: hit_rate `0.4250`, avg `0.0017`, median `-0.0060`, brier `0.3150`, calibration_gap `0.2575`
- 20d: hit_rate `0.5750`, avg `0.0060`, median `0.0072`, brier `0.2539`, calibration_gap `0.1075`
- 60d: hit_rate `0.6000`, avg `0.0248`, median `0.0456`, brier `0.2484`, calibration_gap `0.0825`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0038`, median `0.0017`, brier `0.2360`, calibration_gap `0.0229`
- 5d: hit_rate `0.5000`, avg `-0.0046`, median `-0.0049`, brier `0.2729`, calibration_gap `0.1479`
- 10d: hit_rate `0.3125`, avg `-0.0071`, median `-0.0152`, brier `0.3284`, calibration_gap `0.3354`
- 20d: hit_rate `0.6875`, avg `-0.0005`, median `0.0050`, brier `0.2150`, calibration_gap `-0.0396`
- 60d: hit_rate `0.3750`, avg `-0.0091`, median `-0.0176`, brier `0.3110`, calibration_gap `0.2729`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
