# High Confidence Signal Report

Generated at: `2026-07-15T06:01:19.749300+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0066`, median `-0.0082`, brier `0.3363`, calibration_gap `0.3162`
- 5d: hit_rate `0.3750`, avg `-0.0058`, median `-0.0137`, brier `0.3428`, calibration_gap `0.3162`
- 10d: hit_rate `0.5000`, avg `-0.0001`, median `0.0014`, brier `0.2842`, calibration_gap `0.1912`
- 20d: hit_rate `1.0000`, avg `0.0282`, median `0.0224`, brier `0.0955`, calibration_gap `-0.3088`
- 60d: hit_rate `0.5000`, avg `0.0264`, median `0.0158`, brier `0.2959`, calibration_gap `0.1912`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0074`, median `-0.0126`, brier `0.3445`, calibration_gap `0.3601`
- 5d: hit_rate `0.4375`, avg `-0.0054`, median `-0.0104`, brier `0.3089`, calibration_gap `0.2351`
- 10d: hit_rate `0.6250`, avg `0.0068`, median `0.0123`, brier `0.2397`, calibration_gap `0.0476`
- 20d: hit_rate `1.0000`, avg `0.0353`, median `0.0298`, brier `0.1077`, calibration_gap `-0.3274`
- 60d: hit_rate `0.6250`, avg `0.0462`, median `0.0601`, brier `0.2456`, calibration_gap `0.0476`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6500`, avg `0.0028`, median `0.0056`, brier `0.2356`, calibration_gap `-0.0329`
- 5d: hit_rate `0.6000`, avg `0.0045`, median `0.0085`, brier `0.2399`, calibration_gap `0.0171`
- 10d: hit_rate `0.7333`, avg `0.0136`, median `0.0141`, brier `0.2114`, calibration_gap `-0.1162`
- 20d: hit_rate `0.8833`, avg `0.0311`, median `0.0313`, brier `0.1727`, calibration_gap `-0.2662`
- 60d: hit_rate `0.8167`, avg `0.0537`, median `0.0747`, brier `0.1866`, calibration_gap `-0.1996`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0067`, median `0.0125`, brier `0.2103`, calibration_gap `-0.1599`
- 5d: hit_rate `0.5000`, avg `0.0039`, median `0.0025`, brier `0.2577`, calibration_gap `0.0901`
- 10d: hit_rate `0.6875`, avg `0.0159`, median `0.0138`, brier `0.2256`, calibration_gap `-0.0974`
- 20d: hit_rate `0.8750`, avg `0.0351`, median `0.0344`, brier `0.1896`, calibration_gap `-0.2849`
- 60d: hit_rate `0.6250`, avg `0.0280`, median `0.0634`, brier `0.2355`, calibration_gap `-0.0349`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
