# High Confidence Signal Report

Generated at: `2026-09-08T16:41:26.124505+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0033`, median `-0.0004`, brier `0.3186`, calibration_gap `0.2704`
- 5d: hit_rate `0.5000`, avg `-0.0065`, median `-0.0029`, brier `0.3205`, calibration_gap `0.2704`
- 10d: hit_rate `0.1250`, avg `-0.0135`, median `-0.0189`, brier `0.5294`, calibration_gap `0.6454`
- 20d: hit_rate `0.5000`, avg `-0.0001`, median `0.0087`, brier `0.3264`, calibration_gap `0.2704`
- 60d: hit_rate `0.7500`, avg `0.0341`, median `0.0519`, brier `0.1843`, calibration_gap `0.0204`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0062`, median `-0.0060`, brier `0.4084`, calibration_gap `0.4465`
- 5d: hit_rate `0.4375`, avg `-0.0075`, median `-0.0045`, brier `0.3463`, calibration_gap `0.3215`
- 10d: hit_rate `0.2500`, avg `-0.0120`, median `-0.0161`, brier `0.4508`, calibration_gap `0.5090`
- 20d: hit_rate `0.5625`, avg `-0.0046`, median `0.0093`, brier `0.2884`, calibration_gap `0.1965`
- 60d: hit_rate `0.6875`, avg `0.0259`, median `0.0396`, brier `0.2163`, calibration_gap `0.0715`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5750`, avg `0.0006`, median `0.0021`, brier `0.2604`, calibration_gap `0.1258`
- 5d: hit_rate `0.5750`, avg `0.0037`, median `0.0080`, brier `0.2577`, calibration_gap `0.1258`
- 10d: hit_rate `0.4750`, avg `0.0034`, median `-0.0069`, brier `0.3015`, calibration_gap `0.2258`
- 20d: hit_rate `0.7250`, avg `0.0175`, median `0.0149`, brier `0.2058`, calibration_gap `-0.0242`
- 60d: hit_rate `0.7750`, avg `0.0455`, median `0.0518`, brier `0.1796`, calibration_gap `-0.0742`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0025`, median `0.0057`, brier `0.2593`, calibration_gap `0.1204`
- 5d: hit_rate `0.5000`, avg `0.0027`, median `0.0033`, brier `0.2819`, calibration_gap `0.1829`
- 10d: hit_rate `0.5000`, avg `0.0093`, median `-0.0009`, brier `0.2814`, calibration_gap `0.1829`
- 20d: hit_rate `0.9375`, avg `0.0334`, median `0.0262`, brier `0.1230`, calibration_gap `-0.2546`
- 60d: hit_rate `0.7500`, avg `0.0653`, median `0.0743`, brier `0.1917`, calibration_gap `-0.0671`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
