# High Confidence Signal Report

Generated at: `2026-09-15T17:02:52.842135+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0021`, median `0.0014`, brier `0.2635`, calibration_gap `0.2057`
- 5d: hit_rate `0.6250`, avg `0.0014`, median `0.0010`, brier `0.2773`, calibration_gap `0.2057`
- 10d: hit_rate `0.2500`, avg `-0.0078`, median `-0.0136`, brier `0.5294`, calibration_gap `0.5807`
- 20d: hit_rate `0.5000`, avg `0.0041`, median `0.0087`, brier `0.3659`, calibration_gap `0.3307`
- 60d: hit_rate `0.7500`, avg `0.0399`, median `0.0588`, brier `0.1966`, calibration_gap `0.0807`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0033`, median `0.0037`, brier `0.2634`, calibration_gap `0.1871`
- 5d: hit_rate `0.6250`, avg `-0.0009`, median `0.0020`, brier `0.2703`, calibration_gap `0.1871`
- 10d: hit_rate `0.5000`, avg `-0.0022`, median `-0.0017`, brier `0.3596`, calibration_gap `0.3121`
- 20d: hit_rate `0.6250`, avg `0.0109`, median `0.0254`, brier `0.2778`, calibration_gap `0.1871`
- 60d: hit_rate `0.6875`, avg `0.0383`, median `0.0605`, brier `0.2294`, calibration_gap `0.1246`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0008`, median `0.0035`, brier `0.2791`, calibration_gap `0.1652`
- 5d: hit_rate `0.3125`, avg `-0.0083`, median `-0.0099`, brier `0.3389`, calibration_gap `0.3527`
- 10d: hit_rate `0.4375`, avg `-0.0127`, median `-0.0259`, brier `0.2969`, calibration_gap `0.2277`
- 20d: hit_rate `0.4375`, avg `-0.0037`, median `-0.0035`, brier `0.2970`, calibration_gap `0.2277`
- 60d: hit_rate `0.8750`, avg `0.0311`, median `0.0442`, brier `0.1532`, calibration_gap `-0.2098`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
