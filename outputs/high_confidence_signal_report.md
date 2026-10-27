# High Confidence Signal Report

Generated at: `2026-10-27T18:04:04.160440+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0056`, median `0.0029`, brier `0.2581`, calibration_gap `0.1353`
- 5d: hit_rate `0.5000`, avg `0.0064`, median `0.0012`, brier `0.3239`, calibration_gap `0.2603`
- 10d: hit_rate `0.6250`, avg `0.0152`, median `0.0143`, brier `0.2501`, calibration_gap `0.1353`
- 20d: hit_rate `0.8750`, avg `0.0334`, median `0.0299`, brier `0.1240`, calibration_gap `-0.1147`
- 60d: hit_rate `1.0000`, avg `0.0675`, median `0.0708`, brier `0.0575`, calibration_gap `-0.2397`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0046`, median `0.0004`, brier `0.3123`, calibration_gap `0.2495`
- 5d: hit_rate `0.3750`, avg `0.0013`, median `-0.0077`, brier `0.3752`, calibration_gap `0.3745`
- 10d: hit_rate `0.4375`, avg `0.0027`, median `-0.0018`, brier `0.3388`, calibration_gap `0.3120`
- 20d: hit_rate `0.8125`, avg `0.0202`, median `0.0265`, brier `0.1558`, calibration_gap `-0.0630`
- 60d: hit_rate `0.9375`, avg `0.0565`, median `0.0654`, brier `0.0928`, calibration_gap `-0.1880`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5875`, avg `0.0040`, median `0.0046`, brier `0.2589`, calibration_gap `0.1107`
- 5d: hit_rate `0.6000`, avg `0.0070`, median `0.0068`, brier `0.2590`, calibration_gap `0.0982`
- 10d: hit_rate `0.6500`, avg `0.0103`, median `0.0090`, brier `0.2358`, calibration_gap `0.0482`
- 20d: hit_rate `0.7000`, avg `0.0168`, median `0.0191`, brier `0.2077`, calibration_gap `-0.0018`
- 60d: hit_rate `0.7625`, avg `0.0339`, median `0.0453`, brier `0.1801`, calibration_gap `-0.0643`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0055`, median `0.0058`, brier `0.2378`, calibration_gap `0.0209`
- 5d: hit_rate `0.6875`, avg `0.0118`, median `0.0171`, brier `0.2200`, calibration_gap `-0.0416`
- 10d: hit_rate `0.6875`, avg `0.0116`, median `0.0168`, brier `0.2185`, calibration_gap `-0.0416`
- 20d: hit_rate `0.5625`, avg `0.0058`, median `0.0182`, brier `0.2541`, calibration_gap `0.0834`
- 60d: hit_rate `0.6250`, avg `0.0089`, median `0.0276`, brier `0.2334`, calibration_gap `0.0209`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
