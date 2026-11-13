# High Confidence Signal Report

Generated at: `2026-11-13T19:45:58.479631+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.0000`, avg `-0.0173`, median `-0.0123`, brier `0.6337`, calibration_gap `0.7960`
- 5d: hit_rate `0.3750`, avg `-0.0126`, median `-0.0134`, brier `0.4162`, calibration_gap `0.4210`
- 10d: hit_rate `0.0000`, avg `-0.0165`, median `-0.0165`, brier `0.6337`, calibration_gap `0.7960`
- 20d: hit_rate `0.3750`, avg `-0.0045`, median `-0.0227`, brier `0.4113`, calibration_gap `0.4210`
- 60d: hit_rate `0.3750`, avg `-0.0045`, median `-0.0484`, brier `0.4113`, calibration_gap `0.4210`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0097`, median `-0.0097`, brier `0.5115`, calibration_gap `0.5939`
- 5d: hit_rate `0.4375`, avg `-0.0095`, median `-0.0031`, brier `0.3669`, calibration_gap `0.3439`
- 10d: hit_rate `0.1250`, avg `-0.0116`, median `-0.0110`, brier `0.5453`, calibration_gap `0.6564`
- 20d: hit_rate `0.4375`, avg `0.0003`, median `-0.0017`, brier `0.3649`, calibration_gap `0.3439`
- 60d: hit_rate `0.3125`, avg `-0.0148`, median `-0.0362`, brier `0.4333`, calibration_gap `0.4689`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.4500`, avg `0.0013`, median `-0.0032`, brier `0.3368`, calibration_gap `0.2638`
- 5d: hit_rate `0.5500`, avg `0.0034`, median `0.0030`, brier `0.2902`, calibration_gap `0.1638`
- 10d: hit_rate `0.4125`, avg `0.0049`, median `-0.0081`, brier `0.3543`, calibration_gap `0.3013`
- 20d: hit_rate `0.6000`, avg `0.0132`, median `0.0153`, brier `0.2643`, calibration_gap `0.1138`
- 60d: hit_rate `0.5125`, avg `0.0154`, median `0.0039`, brier `0.3035`, calibration_gap `0.2013`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0105`, median `0.0149`, brier `0.2162`, calibration_gap `-0.0318`
- 5d: hit_rate `0.7500`, avg `0.0148`, median `0.0099`, brier `0.1974`, calibration_gap `-0.0943`
- 10d: hit_rate `0.6250`, avg `0.0159`, median `0.0182`, brier `0.2372`, calibration_gap `0.0307`
- 20d: hit_rate `0.7500`, avg `0.0261`, median `0.0221`, brier `0.1982`, calibration_gap `-0.0943`
- 60d: hit_rate `0.6875`, avg `0.0356`, median `0.0480`, brier `0.2174`, calibration_gap `-0.0318`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
