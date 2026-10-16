# High Confidence Signal Report

Generated at: `2026-10-16T16:42:32.864791+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0133`, median `-0.0118`, brier `0.4917`, calibration_gap `0.6175`
- 5d: hit_rate `0.2500`, avg `-0.0165`, median `-0.0226`, brier `0.4286`, calibration_gap `0.4925`
- 10d: hit_rate `0.1250`, avg `-0.0160`, median `-0.0118`, brier `0.4917`, calibration_gap `0.6175`
- 20d: hit_rate `0.6250`, avg `0.0313`, median `0.0363`, brier `0.2455`, calibration_gap `0.1175`
- 60d: hit_rate `0.8750`, avg `0.0841`, median `0.1032`, brier `0.1254`, calibration_gap `-0.1325`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0089`, median `-0.0101`, brier `0.3967`, calibration_gap `0.4236`
- 5d: hit_rate `0.3750`, avg `-0.0136`, median `-0.0216`, brier `0.3651`, calibration_gap `0.3611`
- 10d: hit_rate `0.1875`, avg `-0.0123`, median `-0.0123`, brier `0.4539`, calibration_gap `0.5486`
- 20d: hit_rate `0.5000`, avg `0.0197`, median `0.0000`, brier `0.3019`, calibration_gap `0.2361`
- 60d: hit_rate `0.8125`, avg `0.0670`, median `0.0784`, brier `0.1569`, calibration_gap `-0.0764`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0073`, median `-0.0054`, brier `0.3188`, calibration_gap `0.2973`
- 5d: hit_rate `0.3750`, avg `-0.0108`, median `-0.0167`, brier `0.3227`, calibration_gap `0.2973`
- 10d: hit_rate `0.3125`, avg `-0.0155`, median `-0.0262`, brier `0.3437`, calibration_gap `0.3598`
- 20d: hit_rate `0.5625`, avg `0.0155`, median `0.0150`, brier `0.2580`, calibration_gap `0.1098`
- 60d: hit_rate `0.8750`, avg `0.0762`, median `0.0963`, brier `0.1512`, calibration_gap `-0.2027`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
