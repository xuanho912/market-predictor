# High Confidence Signal Report

Generated at: `2026-07-22T14:24:59.449495+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0057`, median `0.0007`, brier `0.2549`, calibration_gap `0.1267`
- 5d: hit_rate `0.5000`, avg `-0.0102`, median `-0.0070`, brier `0.3135`, calibration_gap `0.2517`
- 10d: hit_rate `0.3750`, avg `-0.0019`, median `-0.0125`, brier `0.3791`, calibration_gap `0.3767`
- 20d: hit_rate `0.6250`, avg `0.0109`, median `0.0205`, brier `0.2489`, calibration_gap `0.1267`
- 60d: hit_rate `0.8750`, avg `0.0494`, median `0.0588`, brier `0.1247`, calibration_gap `-0.1233`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0051`, median `0.0007`, brier `0.2781`, calibration_gap `0.1802`
- 5d: hit_rate `0.4375`, avg `-0.0083`, median `-0.0069`, brier `0.3377`, calibration_gap `0.3052`
- 10d: hit_rate `0.3125`, avg `-0.0042`, median `-0.0141`, brier `0.4004`, calibration_gap `0.4302`
- 20d: hit_rate `0.6875`, avg `0.0139`, median `0.0205`, brier `0.2181`, calibration_gap `0.0552`
- 60d: hit_rate `0.8125`, avg `0.0459`, median `0.0597`, brier `0.1567`, calibration_gap `-0.0698`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.3500`, avg `-0.0113`, median `-0.0130`, brier `0.3656`, calibration_gap `0.3726`
- 5d: hit_rate `0.4000`, avg `-0.0119`, median `-0.0102`, brier `0.3470`, calibration_gap `0.3226`
- 10d: hit_rate `0.3500`, avg `-0.0035`, median `-0.0074`, brier `0.3713`, calibration_gap `0.3726`
- 20d: hit_rate `0.6500`, avg `0.0115`, median `0.0209`, brier `0.2330`, calibration_gap `0.0726`
- 60d: hit_rate `0.7000`, avg `0.0365`, median `0.0526`, brier `0.2105`, calibration_gap `0.0226`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0017`, median `-0.0004`, brier `0.2822`, calibration_gap `0.1851`
- 5d: hit_rate `0.3125`, avg `-0.0034`, median `-0.0024`, brier `0.3522`, calibration_gap `0.3726`
- 10d: hit_rate `0.4375`, avg `-0.0055`, median `-0.0058`, brier `0.3055`, calibration_gap `0.2476`
- 20d: hit_rate `0.7500`, avg `0.0052`, median `0.0177`, brier `0.1926`, calibration_gap `-0.0649`
- 60d: hit_rate `0.5000`, avg `-0.0126`, median `0.0009`, brier `0.2860`, calibration_gap `0.1851`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
