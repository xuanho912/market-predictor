# High Confidence Signal Report

Generated at: `2026-10-06T18:25:45.654305+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0005`, median `0.0031`, brier `0.2612`, calibration_gap `0.1640`
- 5d: hit_rate `0.6250`, avg `-0.0013`, median `0.0056`, brier `0.2612`, calibration_gap `0.1640`
- 10d: hit_rate `0.5000`, avg `-0.0035`, median `-0.0047`, brier `0.3400`, calibration_gap `0.2890`
- 20d: hit_rate `0.7500`, avg `0.0196`, median `0.0173`, brier `0.1915`, calibration_gap `0.0390`
- 60d: hit_rate `1.0000`, avg `0.0443`, median `0.0415`, brier `0.0446`, calibration_gap `-0.2110`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0065`, median `-0.0036`, brier `0.3580`, calibration_gap `0.3406`
- 5d: hit_rate `0.4375`, avg `-0.0109`, median `-0.0156`, brier `0.3580`, calibration_gap `0.3406`
- 10d: hit_rate `0.5000`, avg `-0.0119`, median `-0.0047`, brier `0.3310`, calibration_gap `0.2781`
- 20d: hit_rate `0.5625`, avg `-0.0021`, median `0.0009`, brier `0.2904`, calibration_gap `0.2156`
- 60d: hit_rate `0.8125`, avg `0.0410`, median `0.0501`, brier `0.1487`, calibration_gap `-0.0344`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.3250`, avg `-0.0090`, median `-0.0058`, brier `0.3450`, calibration_gap `0.3435`
- 5d: hit_rate `0.3750`, avg `-0.0133`, median `-0.0082`, brier `0.3307`, calibration_gap `0.2935`
- 10d: hit_rate `0.4750`, avg `-0.0046`, median `-0.0056`, brier `0.2899`, calibration_gap `0.1935`
- 20d: hit_rate `0.6250`, avg `0.0068`, median `0.0168`, brier `0.2406`, calibration_gap `0.0435`
- 60d: hit_rate `0.7250`, avg `0.0376`, median `0.0445`, brier `0.2035`, calibration_gap `-0.0565`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0015`, median `0.0013`, brier `0.2680`, calibration_gap `0.1373`
- 5d: hit_rate `0.5625`, avg `-0.0023`, median `0.0021`, brier `0.2499`, calibration_gap `0.0748`
- 10d: hit_rate `0.5625`, avg `0.0101`, median `0.0097`, brier `0.2495`, calibration_gap `0.0748`
- 20d: hit_rate `0.7500`, avg `0.0148`, median `0.0146`, brier `0.1973`, calibration_gap `-0.1127`
- 60d: hit_rate `0.7500`, avg `0.0161`, median `0.0344`, brier `0.1979`, calibration_gap `-0.1127`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
