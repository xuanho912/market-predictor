# High Confidence Signal Report

Generated at: `2026-11-20T20:25:23.516638+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0130`, median `-0.0089`, brier `0.5175`, calibration_gap `0.6367`
- 5d: hit_rate `0.6250`, avg `-0.0016`, median `0.0043`, brier `0.2552`, calibration_gap `0.1367`
- 10d: hit_rate `0.3750`, avg `-0.0297`, median `-0.0251`, brier `0.3843`, calibration_gap `0.3867`
- 20d: hit_rate `0.1250`, avg `-0.0847`, median `-0.0258`, brier `0.5175`, calibration_gap `0.6367`
- 60d: hit_rate `0.3750`, avg `-0.0116`, median `-0.0081`, brier `0.3809`, calibration_gap `0.3867`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0004`, median `-0.0010`, brier `0.3515`, calibration_gap `0.3119`
- 5d: hit_rate `0.5625`, avg `0.0030`, median `0.0043`, brier `0.2789`, calibration_gap `0.1869`
- 10d: hit_rate `0.4375`, avg `-0.0123`, median `-0.0097`, brier `0.3418`, calibration_gap `0.3119`
- 20d: hit_rate `0.4375`, avg `-0.0320`, median `-0.0026`, brier `0.3515`, calibration_gap `0.3119`
- 60d: hit_rate `0.5625`, avg `0.0110`, median `0.0015`, brier `0.2848`, calibration_gap `0.1869`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0044`, median `0.0144`, brier `0.2372`, calibration_gap `-0.0512`
- 5d: hit_rate `0.8125`, avg `0.0011`, median `0.0234`, brier `0.2095`, calibration_gap `-0.2387`
- 10d: hit_rate `0.6875`, avg `-0.0049`, median `0.0241`, brier `0.2288`, calibration_gap `-0.1137`
- 20d: hit_rate `0.5625`, avg `0.0064`, median `0.0115`, brier `0.2452`, calibration_gap `0.0113`
- 60d: hit_rate `0.6250`, avg `0.0478`, median `0.0956`, brier `0.2367`, calibration_gap `-0.0512`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
