# High Confidence Signal Report

Generated at: `2026-06-19T23:43:29.400099+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0039`, median `-0.0040`, brier `0.4098`, calibration_gap `0.4695`
- 5d: hit_rate `0.7500`, avg `0.0015`, median `0.0042`, brier `0.1935`, calibration_gap `-0.0305`
- 10d: hit_rate `0.5000`, avg `0.0012`, median `0.0009`, brier `0.2948`, calibration_gap `0.2195`
- 20d: hit_rate `0.6250`, avg `-0.0052`, median `0.0066`, brier `0.2380`, calibration_gap `0.0945`
- 60d: hit_rate `0.1250`, avg `-0.0506`, median `-0.0719`, brier `0.4648`, calibration_gap `0.5945`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0042`, median `-0.0077`, brier `0.3983`, calibration_gap `0.4582`
- 5d: hit_rate `0.7500`, avg `0.0050`, median `0.0042`, brier `0.1930`, calibration_gap `-0.0418`
- 10d: hit_rate `0.4375`, avg `0.0023`, median `-0.0033`, brier `0.3171`, calibration_gap `0.2707`
- 20d: hit_rate `0.6875`, avg `0.0080`, median `0.0138`, brier `0.2146`, calibration_gap `0.0207`
- 60d: hit_rate `0.3125`, avg `-0.0170`, median `-0.0243`, brier `0.3768`, calibration_gap `0.3957`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `0.0089`, median `0.0091`, brier `0.2403`, calibration_gap `0.0024`
- 5d: hit_rate `0.6750`, avg `0.0081`, median `0.0070`, brier `0.2328`, calibration_gap `-0.0476`
- 10d: hit_rate `0.6250`, avg `0.0109`, median `0.0134`, brier `0.2420`, calibration_gap `0.0024`
- 20d: hit_rate `0.6000`, avg `0.0102`, median `0.0169`, brier `0.2506`, calibration_gap `0.0274`
- 60d: hit_rate `0.7250`, avg `0.0410`, median `0.0525`, brier `0.2168`, calibration_gap `-0.0976`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0114`, median `0.0181`, brier `0.2221`, calibration_gap `-0.1016`
- 5d: hit_rate `0.8125`, avg `0.0125`, median `0.0116`, brier `0.2037`, calibration_gap `-0.2266`
- 10d: hit_rate `0.7500`, avg `0.0168`, median `0.0282`, brier `0.2143`, calibration_gap `-0.1641`
- 20d: hit_rate `0.7500`, avg `0.0218`, median `0.0295`, brier `0.2104`, calibration_gap `-0.1641`
- 60d: hit_rate `0.8125`, avg `0.0499`, median `0.0525`, brier `0.2063`, calibration_gap `-0.2266`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
