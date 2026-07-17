# High Confidence Signal Report

Generated at: `2026-07-17T22:29:03.600381+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0067`, median `0.0056`, brier `0.1319`, calibration_gap `-0.1446`
- 5d: hit_rate `0.6250`, avg `0.0021`, median `0.0010`, brier `0.2437`, calibration_gap `0.1054`
- 10d: hit_rate `0.2500`, avg `-0.0092`, median `-0.0104`, brier `0.4201`, calibration_gap `0.4804`
- 20d: hit_rate `0.6250`, avg `0.0172`, median `0.0205`, brier `0.2452`, calibration_gap `0.1054`
- 60d: hit_rate `0.6250`, avg `0.0234`, median `0.0453`, brier `0.2443`, calibration_gap `0.1054`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0022`, median `0.0037`, brier `0.2145`, calibration_gap `0.0339`
- 5d: hit_rate `0.5625`, avg `-0.0015`, median `0.0010`, brier `0.2702`, calibration_gap `0.1589`
- 10d: hit_rate `0.1875`, avg `-0.0125`, median `-0.0161`, brier `0.4370`, calibration_gap `0.5339`
- 20d: hit_rate `0.6250`, avg `0.0028`, median `0.0072`, brier `0.2439`, calibration_gap `0.0964`
- 60d: hit_rate `0.5625`, avg `0.0171`, median `0.0216`, brier `0.2702`, calibration_gap `0.1589`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `-0.0021`, median `0.0041`, brier `0.2289`, calibration_gap `0.0431`
- 5d: hit_rate `0.5750`, avg `-0.0020`, median `0.0027`, brier `0.2593`, calibration_gap `0.1181`
- 10d: hit_rate `0.3250`, avg `-0.0030`, median `-0.0115`, brier `0.3565`, calibration_gap `0.3681`
- 20d: hit_rate `0.7250`, avg `0.0168`, median `0.0199`, brier `0.1995`, calibration_gap `-0.0319`
- 60d: hit_rate `0.7750`, avg `0.0525`, median `0.0899`, brier `0.1827`, calibration_gap `-0.0819`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0039`, median `0.0079`, brier `0.2144`, calibration_gap `-0.0169`
- 5d: hit_rate `0.6875`, avg `0.0079`, median `0.0081`, brier `0.2133`, calibration_gap `-0.0169`
- 10d: hit_rate `0.7500`, avg `0.0139`, median `0.0199`, brier `0.1954`, calibration_gap `-0.0794`
- 20d: hit_rate `0.9375`, avg `0.0367`, median `0.0436`, brier `0.1298`, calibration_gap `-0.2669`
- 60d: hit_rate `0.6875`, avg `0.0560`, median `0.0631`, brier `0.2129`, calibration_gap `-0.0169`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
