# High Confidence Signal Report

Generated at: `2026-09-09T16:42:19.803814+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0009`, median `-0.0004`, brier `0.3303`, calibration_gap `0.2999`
- 5d: hit_rate `0.5000`, avg `-0.0029`, median `-0.0009`, brier `0.3351`, calibration_gap `0.2999`
- 10d: hit_rate `0.1250`, avg `-0.0160`, median `-0.0204`, brier `0.5693`, calibration_gap `0.6749`
- 20d: hit_rate `0.3750`, avg `-0.0131`, median `-0.0055`, brier `0.4165`, calibration_gap `0.4249`
- 60d: hit_rate `0.6250`, avg `0.0207`, median `0.0453`, brier `0.2574`, calibration_gap `0.1749`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0038`, median `-0.0026`, brier `0.3938`, calibration_gap `0.4101`
- 5d: hit_rate `0.4375`, avg `-0.0076`, median `-0.0045`, brier `0.3626`, calibration_gap `0.3476`
- 10d: hit_rate `0.3125`, avg `-0.0072`, median `-0.0095`, brier `0.4455`, calibration_gap `0.4726`
- 20d: hit_rate `0.5625`, avg `-0.0030`, median `0.0159`, brier `0.3012`, calibration_gap `0.2226`
- 60d: hit_rate `0.6875`, avg `0.0322`, median `0.0588`, brier `0.2217`, calibration_gap `0.0976`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6000`, avg `0.0025`, median `0.0052`, brier `0.2634`, calibration_gap `0.1169`
- 5d: hit_rate `0.5500`, avg `0.0014`, median `0.0017`, brier `0.2833`, calibration_gap `0.1669`
- 10d: hit_rate `0.4500`, avg `0.0084`, median `-0.0024`, brier `0.3287`, calibration_gap `0.2669`
- 20d: hit_rate `0.8000`, avg `0.0276`, median `0.0306`, brier `0.1740`, calibration_gap `-0.0831`
- 60d: hit_rate `0.7750`, avg `0.0591`, median `0.0664`, brier `0.1818`, calibration_gap `-0.0581`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0054`, median `0.0092`, brier `0.2152`, calibration_gap `-0.0052`
- 5d: hit_rate `0.6250`, avg `0.0098`, median `0.0112`, brier `0.2363`, calibration_gap `0.0573`
- 10d: hit_rate `0.5625`, avg `0.0198`, median `0.0103`, brier `0.2612`, calibration_gap `0.1198`
- 20d: hit_rate `0.9375`, avg `0.0429`, median `0.0374`, brier `0.1247`, calibration_gap `-0.2552`
- 60d: hit_rate `0.8125`, avg `0.0760`, median `0.0772`, brier `0.1702`, calibration_gap `-0.1302`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
