# High Confidence Signal Report

Generated at: `2026-09-22T23:47:56.192979+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0032`, median `-0.0036`, brier `0.3334`, calibration_gap `0.2816`
- 5d: hit_rate `0.5000`, avg `-0.0091`, median `-0.0029`, brier `0.3331`, calibration_gap `0.2816`
- 10d: hit_rate `0.3750`, avg `-0.0075`, median `-0.0090`, brier `0.3987`, calibration_gap `0.4066`
- 20d: hit_rate `0.3750`, avg `0.0039`, median `-0.0047`, brier `0.3992`, calibration_gap `0.4066`
- 60d: hit_rate `0.5000`, avg `0.0124`, median `0.0042`, brier `0.3285`, calibration_gap `0.2816`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0101`, median `-0.0108`, brier `0.3912`, calibration_gap `0.3971`
- 5d: hit_rate `0.3125`, avg `-0.0136`, median `-0.0166`, brier `0.4240`, calibration_gap `0.4596`
- 10d: hit_rate `0.1875`, avg `-0.0168`, median `-0.0149`, brier `0.4901`, calibration_gap `0.5846`
- 20d: hit_rate `0.4375`, avg `0.0046`, median `-0.0014`, brier `0.3587`, calibration_gap `0.3346`
- 60d: hit_rate `0.6250`, avg `0.0175`, median `0.0177`, brier `0.2572`, calibration_gap `0.1471`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4833`, avg `-0.0038`, median `-0.0014`, brier `0.3127`, calibration_gap `0.2289`
- 5d: hit_rate `0.4833`, avg `-0.0074`, median `-0.0010`, brier `0.3158`, calibration_gap `0.2289`
- 10d: hit_rate `0.4000`, avg `-0.0051`, median `-0.0072`, brier `0.3503`, calibration_gap `0.3123`
- 20d: hit_rate `0.6000`, avg `0.0103`, median `0.0176`, brier `0.2608`, calibration_gap `0.1123`
- 60d: hit_rate `0.7000`, avg `0.0236`, median `0.0343`, brier `0.2184`, calibration_gap `0.0123`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0010`, median `0.0061`, brier `0.2404`, calibration_gap `0.0351`
- 5d: hit_rate `0.6875`, avg `0.0036`, median `0.0065`, brier `0.2201`, calibration_gap `-0.0274`
- 10d: hit_rate `0.6250`, avg `0.0088`, median `0.0074`, brier `0.2390`, calibration_gap `0.0351`
- 20d: hit_rate `0.6250`, avg `0.0144`, median `0.0230`, brier `0.2356`, calibration_gap `0.0351`
- 60d: hit_rate `0.8125`, avg `0.0300`, median `0.0357`, brier `0.1794`, calibration_gap `-0.1524`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
