# High Confidence Signal Report

Generated at: `2026-09-16T06:07:15.626701+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0021`, median `0.0014`, brier `0.2625`, calibration_gap `0.2038`
- 5d: hit_rate `0.6250`, avg `0.0014`, median `0.0010`, brier `0.2760`, calibration_gap `0.2038`
- 10d: hit_rate `0.2500`, avg `-0.0078`, median `-0.0136`, brier `0.5273`, calibration_gap `0.5788`
- 20d: hit_rate `0.5000`, avg `0.0041`, median `0.0087`, brier `0.3644`, calibration_gap `0.3288`
- 60d: hit_rate `0.7500`, avg `0.0399`, median `0.0588`, brier `0.1954`, calibration_gap `0.0788`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0033`, median `0.0037`, brier `0.2631`, calibration_gap `0.1854`
- 5d: hit_rate `0.6250`, avg `-0.0009`, median `0.0020`, brier `0.2699`, calibration_gap `0.1854`
- 10d: hit_rate `0.5000`, avg `-0.0022`, median `-0.0017`, brier `0.3583`, calibration_gap `0.3104`
- 20d: hit_rate `0.6250`, avg `0.0109`, median `0.0254`, brier `0.2774`, calibration_gap `0.1854`
- 60d: hit_rate `0.6875`, avg `0.0383`, median `0.0605`, brier `0.2286`, calibration_gap `0.1229`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0008`, median `0.0035`, brier `0.2802`, calibration_gap `0.1676`
- 5d: hit_rate `0.3125`, avg `-0.0083`, median `-0.0099`, brier `0.3415`, calibration_gap `0.3551`
- 10d: hit_rate `0.3750`, avg `-0.0169`, median `-0.0272`, brier `0.3213`, calibration_gap `0.2926`
- 20d: hit_rate `0.3750`, avg `-0.0081`, median `-0.0092`, brier `0.3210`, calibration_gap `0.2926`
- 60d: hit_rate `0.8750`, avg `0.0282`, median `0.0442`, brier `0.1518`, calibration_gap `-0.2074`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
