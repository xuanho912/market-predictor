# High Confidence Signal Report

Generated at: `2026-10-30T01:27:41.412067+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0101`, median `0.0126`, brier `0.2458`, calibration_gap `0.0744`
- 5d: hit_rate `0.7500`, avg `0.0146`, median `0.0150`, brier `0.1951`, calibration_gap `-0.0506`
- 10d: hit_rate `0.7500`, avg `0.0063`, median `0.0106`, brier `0.1951`, calibration_gap `-0.0506`
- 20d: hit_rate `0.5000`, avg `0.0021`, median `0.0028`, brier `0.2924`, calibration_gap `0.1994`
- 60d: hit_rate `0.7500`, avg `0.0839`, median `0.0867`, brier `0.1951`, calibration_gap `-0.0506`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0066`, median `0.0086`, brier `0.2412`, calibration_gap `0.0644`
- 5d: hit_rate `0.6875`, avg `0.0060`, median `0.0096`, brier `0.2158`, calibration_gap `0.0019`
- 10d: hit_rate `0.5625`, avg `-0.0014`, median `0.0086`, brier `0.2607`, calibration_gap `0.1269`
- 20d: hit_rate `0.3750`, avg `-0.0076`, median `-0.0199`, brier `0.3314`, calibration_gap `0.3144`
- 60d: hit_rate `0.7500`, avg `0.0665`, median `0.0753`, brier `0.1934`, calibration_gap `-0.0606`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0056`, median `0.0181`, brier `0.2388`, calibration_gap `0.0014`
- 5d: hit_rate `0.6500`, avg `0.0046`, median `0.0041`, brier `0.2364`, calibration_gap `0.0014`
- 10d: hit_rate `0.5500`, avg `0.0067`, median `0.0211`, brier `0.2681`, calibration_gap `0.1014`
- 20d: hit_rate `0.5000`, avg `-0.0031`, median `0.0076`, brier `0.2787`, calibration_gap `0.1514`
- 60d: hit_rate `0.9500`, avg `0.0618`, median `0.0627`, brier `0.1453`, calibration_gap `-0.2986`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0022`, median `0.0049`, brier `0.2473`, calibration_gap `0.0187`
- 5d: hit_rate `0.3125`, avg `-0.0109`, median `-0.0123`, brier `0.2837`, calibration_gap `0.2687`
- 10d: hit_rate `0.3750`, avg `-0.0138`, median `-0.0213`, brier `0.2770`, calibration_gap `0.2062`
- 20d: hit_rate `0.5000`, avg `-0.0138`, median `-0.0076`, brier `0.2552`, calibration_gap `0.0812`
- 60d: hit_rate `0.8125`, avg `0.0520`, median `0.0622`, brier `0.2018`, calibration_gap `-0.2313`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
