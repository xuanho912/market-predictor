# High Confidence Signal Report

Generated at: `2026-10-20T17:10:44.183926+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0101`, brier `0.4191`, calibration_gap `0.4782`
- 5d: hit_rate `0.5000`, avg `-0.0069`, median `-0.0093`, brier `0.3053`, calibration_gap `0.2282`
- 10d: hit_rate `0.3750`, avg `0.0008`, median `-0.0032`, brier `0.3640`, calibration_gap `0.3532`
- 20d: hit_rate `0.8750`, avg `0.0479`, median `0.0584`, brier `0.1303`, calibration_gap `-0.1468`
- 60d: hit_rate `0.8750`, avg `0.1003`, median `0.1233`, brier `0.1303`, calibration_gap `-0.1468`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0105`, median `-0.0116`, brier `0.3849`, calibration_gap `0.4105`
- 5d: hit_rate `0.3750`, avg `-0.0092`, median `-0.0188`, brier `0.3555`, calibration_gap `0.3480`
- 10d: hit_rate `0.3125`, avg `-0.0035`, median `-0.0082`, brier `0.3846`, calibration_gap `0.4105`
- 20d: hit_rate `0.6250`, avg `0.0249`, median `0.0255`, brier `0.2412`, calibration_gap `0.0980`
- 60d: hit_rate `0.7500`, avg `0.0642`, median `0.0661`, brier `0.1867`, calibration_gap `-0.0270`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0008`, median `0.0028`, brier `0.2595`, calibration_gap `0.1212`
- 5d: hit_rate `0.7000`, avg `0.0047`, median `0.0069`, brier `0.2099`, calibration_gap `-0.0288`
- 10d: hit_rate `0.7000`, avg `0.0095`, median `0.0078`, brier `0.2096`, calibration_gap `-0.0288`
- 20d: hit_rate `0.7500`, avg `0.0152`, median `0.0214`, brier `0.1919`, calibration_gap `-0.0788`
- 60d: hit_rate `0.5500`, avg `-0.0077`, median `0.0203`, brier `0.2618`, calibration_gap `0.1212`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0017`, median `0.0007`, brier `0.2731`, calibration_gap `0.1515`
- 5d: hit_rate `0.6250`, avg `0.0048`, median `0.0021`, brier `0.2341`, calibration_gap `0.0265`
- 10d: hit_rate `0.5625`, avg `0.0044`, median `0.0053`, brier `0.2541`, calibration_gap `0.0890`
- 20d: hit_rate `0.5000`, avg `0.0113`, median `0.0010`, brier `0.2739`, calibration_gap `0.1515`
- 60d: hit_rate `0.6875`, avg `0.0551`, median `0.0835`, brier `0.2176`, calibration_gap `-0.0360`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
