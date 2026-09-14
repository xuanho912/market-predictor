# High Confidence Signal Report

Generated at: `2026-09-14T18:07:26.566132+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0021`, median `0.0014`, brier `0.2574`, calibration_gap `0.1852`
- 5d: hit_rate `0.6250`, avg `0.0014`, median `0.0010`, brier `0.2694`, calibration_gap `0.1852`
- 10d: hit_rate `0.2500`, avg `-0.0078`, median `-0.0136`, brier `0.5095`, calibration_gap `0.5602`
- 20d: hit_rate `0.5000`, avg `0.0041`, median `0.0087`, brier `0.3550`, calibration_gap `0.3102`
- 60d: hit_rate `0.7500`, avg `0.0399`, median `0.0588`, brier `0.1919`, calibration_gap `0.0602`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0023`, median `0.0014`, brier `0.2567`, calibration_gap `0.1669`
- 5d: hit_rate `0.5625`, avg `-0.0034`, median `0.0010`, brier `0.2970`, calibration_gap `0.2294`
- 10d: hit_rate `0.4375`, avg `-0.0052`, median `-0.0073`, brier `0.3836`, calibration_gap `0.3544`
- 20d: hit_rate `0.6250`, avg `0.0067`, median `0.0205`, brier `0.2723`, calibration_gap `0.1669`
- 60d: hit_rate `0.6250`, avg `0.0282`, median `0.0588`, brier `0.2587`, calibration_gap `0.1669`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7500`, avg `0.0084`, median `0.0116`, brier `0.1962`, calibration_gap `-0.1001`
- 5d: hit_rate `0.6000`, avg `0.0043`, median `0.0037`, brier `0.2400`, calibration_gap `0.0499`
- 10d: hit_rate `0.6000`, avg `0.0150`, median `0.0078`, brier `0.2411`, calibration_gap `0.0499`
- 20d: hit_rate `0.8000`, avg `0.0369`, median `0.0323`, brier `0.1814`, calibration_gap `-0.1501`
- 60d: hit_rate `0.8000`, avg `0.0668`, median `0.0743`, brier `0.1815`, calibration_gap `-0.1501`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0072`, median `0.0116`, brier `0.2165`, calibration_gap `-0.0402`
- 5d: hit_rate `0.5625`, avg `0.0013`, median `0.0013`, brier `0.2511`, calibration_gap `0.0848`
- 10d: hit_rate `0.6250`, avg `0.0130`, median `0.0078`, brier `0.2326`, calibration_gap `0.0223`
- 20d: hit_rate `0.8125`, avg `0.0328`, median `0.0323`, brier `0.1780`, calibration_gap `-0.1652`
- 60d: hit_rate `0.8125`, avg `0.0630`, median `0.0743`, brier `0.1782`, calibration_gap `-0.1652`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
