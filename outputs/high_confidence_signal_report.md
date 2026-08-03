# High Confidence Signal Report

Generated at: `2026-08-03T15:23:53.487544+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0099`, median `-0.0090`, brier `0.3802`, calibration_gap `0.3848`
- 5d: hit_rate `0.6250`, avg `-0.0056`, median `0.0012`, brier `0.2534`, calibration_gap `0.1348`
- 10d: hit_rate `0.1250`, avg `-0.0062`, median `-0.0129`, brier `0.5119`, calibration_gap `0.6348`
- 20d: hit_rate `0.3750`, avg `-0.0064`, median `-0.0126`, brier `0.3735`, calibration_gap `0.3848`
- 60d: hit_rate `0.3750`, avg `-0.0014`, median `-0.0108`, brier `0.3735`, calibration_gap `0.3848`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0104`, median `-0.0096`, brier `0.4030`, calibration_gap `0.4370`
- 5d: hit_rate `0.6875`, avg `-0.0041`, median `0.0017`, brier `0.2195`, calibration_gap `0.0620`
- 10d: hit_rate `0.1875`, avg `-0.0060`, median `-0.0129`, brier `0.4689`, calibration_gap `0.5620`
- 20d: hit_rate `0.4375`, avg `-0.0079`, median `-0.0073`, brier `0.3400`, calibration_gap `0.3120`
- 60d: hit_rate `0.3750`, avg `-0.0180`, median `-0.0156`, brier `0.3704`, calibration_gap `0.3745`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0065`, median `0.0094`, brier `0.2239`, calibration_gap `0.0550`
- 5d: hit_rate `0.5500`, avg `0.0050`, median `0.0091`, brier `0.2651`, calibration_gap `0.1550`
- 10d: hit_rate `0.7000`, avg `0.0217`, median `0.0276`, brier `0.2061`, calibration_gap `0.0050`
- 20d: hit_rate `0.8500`, avg `0.0441`, median `0.0478`, brier `0.1449`, calibration_gap `-0.1450`
- 60d: hit_rate `0.8000`, avg `0.0572`, median `0.0730`, brier `0.1718`, calibration_gap `-0.0950`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0002`, median `-0.0031`, brier `0.3046`, calibration_gap `0.2416`
- 5d: hit_rate `0.6250`, avg `0.0029`, median `0.0043`, brier `0.2378`, calibration_gap `0.0541`
- 10d: hit_rate `0.5625`, avg `0.0043`, median `0.0046`, brier `0.2602`, calibration_gap `0.1166`
- 20d: hit_rate `0.5625`, avg `0.0011`, median `0.0122`, brier `0.2595`, calibration_gap `0.1166`
- 60d: hit_rate `0.5000`, avg `-0.0150`, median `0.0027`, brier `0.2804`, calibration_gap `0.1791`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
