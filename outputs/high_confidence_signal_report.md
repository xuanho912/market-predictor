# High Confidence Signal Report

Generated at: `2026-11-06T02:06:10.442364+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0008`, median `0.0058`, brier `0.2969`, calibration_gap `0.2585`
- 5d: hit_rate `0.6250`, avg `0.0055`, median `0.0101`, brier `0.2367`, calibration_gap `0.1335`
- 10d: hit_rate `0.6250`, avg `0.0245`, median `0.0439`, brier `0.2367`, calibration_gap `0.1335`
- 20d: hit_rate `0.6250`, avg `0.0197`, median `0.0529`, brier `0.2367`, calibration_gap `0.1335`
- 60d: hit_rate `0.8750`, avg `0.0629`, median `0.0793`, brier `0.1151`, calibration_gap `-0.1165`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0073`, median `-0.0142`, brier `0.3778`, calibration_gap `0.4249`
- 5d: hit_rate `0.3125`, avg `-0.0082`, median `-0.0186`, brier `0.3749`, calibration_gap `0.4249`
- 10d: hit_rate `0.3750`, avg `-0.0009`, median `-0.0210`, brier `0.3473`, calibration_gap `0.3624`
- 20d: hit_rate `0.3125`, avg `-0.0152`, median `-0.0279`, brier `0.3749`, calibration_gap `0.4249`
- 60d: hit_rate `0.7500`, avg `0.0375`, median `0.0350`, brier `0.1789`, calibration_gap `-0.0126`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0004`, median `0.0066`, brier `0.2473`, calibration_gap `-0.0353`
- 5d: hit_rate `0.5000`, avg `-0.0023`, median `0.0003`, brier `0.2504`, calibration_gap `0.0272`
- 10d: hit_rate `0.2500`, avg `-0.0064`, median `-0.0168`, brier `0.2656`, calibration_gap `0.2772`
- 20d: hit_rate `0.2500`, avg `-0.0372`, median `-0.0420`, brier `0.2659`, calibration_gap `0.2772`
- 60d: hit_rate `0.8125`, avg `0.0657`, median `0.0689`, brier `0.2345`, calibration_gap `-0.2853`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
