# High Confidence Signal Report

Generated at: `2026-09-21T18:15:54.900137+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0019`, median `0.0014`, brier `0.2652`, calibration_gap `0.1680`
- 5d: hit_rate `0.3750`, avg `-0.0106`, median `-0.0084`, brier `0.4090`, calibration_gap `0.4180`
- 10d: hit_rate `0.3750`, avg `-0.0108`, median `-0.0136`, brier `0.4085`, calibration_gap `0.4180`
- 20d: hit_rate `0.3750`, avg `0.0088`, median `-0.0027`, brier `0.4082`, calibration_gap `0.4180`
- 60d: hit_rate `0.6250`, avg `0.0258`, median `0.0434`, brier `0.2649`, calibration_gap `0.1680`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0060`, median `-0.0048`, brier `0.3640`, calibration_gap `0.3460`
- 5d: hit_rate `0.4375`, avg `-0.0082`, median `-0.0084`, brier `0.3672`, calibration_gap `0.3460`
- 10d: hit_rate `0.4375`, avg `-0.0054`, median `-0.0090`, brier `0.3671`, calibration_gap `0.3460`
- 20d: hit_rate `0.6250`, avg `0.0176`, median `0.0293`, brier `0.2641`, calibration_gap `0.1585`
- 60d: hit_rate `0.7500`, avg `0.0435`, median `0.0618`, brier `0.1925`, calibration_gap `0.0335`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4333`, avg `-0.0042`, median `-0.0037`, brier `0.3378`, calibration_gap `0.2901`
- 5d: hit_rate `0.4833`, avg `-0.0068`, median `-0.0030`, brier `0.3189`, calibration_gap `0.2401`
- 10d: hit_rate `0.3833`, avg `-0.0025`, median `-0.0071`, brier `0.3633`, calibration_gap `0.3401`
- 20d: hit_rate `0.6000`, avg `0.0139`, median `0.0157`, brier `0.2603`, calibration_gap `0.1235`
- 60d: hit_rate `0.7167`, avg `0.0313`, median `0.0352`, brier `0.2089`, calibration_gap `0.0068`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0022`, median `0.0044`, brier `0.2818`, calibration_gap `0.1672`
- 5d: hit_rate `0.6250`, avg `0.0093`, median `0.0072`, brier `0.2418`, calibration_gap `0.0422`
- 10d: hit_rate `0.6250`, avg `0.0132`, median `0.0127`, brier `0.2376`, calibration_gap `0.0422`
- 20d: hit_rate `0.6875`, avg `0.0312`, median `0.0326`, brier `0.2189`, calibration_gap `-0.0203`
- 60d: hit_rate `0.9375`, avg `0.0594`, median `0.0449`, brier `0.1345`, calibration_gap `-0.2703`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
