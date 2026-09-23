# High Confidence Signal Report

Generated at: `2026-09-23T23:03:23.939978+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0029`, median `-0.0041`, brier `0.3455`, calibration_gap `0.3095`
- 5d: hit_rate `0.5000`, avg `-0.0081`, median `-0.0078`, brier `0.3455`, calibration_gap `0.3095`
- 10d: hit_rate `0.3750`, avg `-0.0144`, median `-0.0116`, brier `0.4225`, calibration_gap `0.4345`
- 20d: hit_rate `0.6250`, avg `0.0078`, median `0.0078`, brier `0.2675`, calibration_gap `0.1845`
- 60d: hit_rate `0.7500`, avg `0.0145`, median `0.0054`, brier `0.1880`, calibration_gap `0.0595`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0041`, median `-0.0033`, brier `0.3412`, calibration_gap `0.3015`
- 5d: hit_rate `0.5000`, avg `-0.0060`, median `-0.0054`, brier `0.3412`, calibration_gap `0.3015`
- 10d: hit_rate `0.5000`, avg `-0.0103`, median `-0.0048`, brier `0.3428`, calibration_gap `0.3015`
- 20d: hit_rate `0.6875`, avg `0.0165`, median `0.0240`, brier `0.2289`, calibration_gap `0.1140`
- 60d: hit_rate `0.7500`, avg `0.0235`, median `0.0378`, brier `0.1892`, calibration_gap `0.0515`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4833`, avg `-0.0041`, median `-0.0014`, brier `0.3202`, calibration_gap `0.2487`
- 5d: hit_rate `0.4833`, avg `-0.0082`, median `-0.0010`, brier `0.3218`, calibration_gap `0.2487`
- 10d: hit_rate `0.4000`, avg `-0.0059`, median `-0.0070`, brier `0.3651`, calibration_gap `0.3321`
- 20d: hit_rate `0.6000`, avg `0.0094`, median `0.0157`, brier `0.2582`, calibration_gap `0.1321`
- 60d: hit_rate `0.6833`, avg `0.0192`, median `0.0306`, brier `0.2199`, calibration_gap `0.0487`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0044`, median `0.0051`, brier `0.2189`, calibration_gap `-0.0267`
- 5d: hit_rate `0.7500`, avg `0.0059`, median `0.0095`, brier `0.1971`, calibration_gap `-0.0892`
- 10d: hit_rate `0.7500`, avg `0.0144`, median `0.0168`, brier `0.1983`, calibration_gap `-0.0892`
- 20d: hit_rate `0.6875`, avg `0.0179`, median `0.0286`, brier `0.2085`, calibration_gap `-0.0267`
- 60d: hit_rate `0.8125`, avg `0.0325`, median `0.0434`, brier `0.1705`, calibration_gap `-0.1517`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
