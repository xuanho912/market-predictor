# High Confidence Signal Report

Generated at: `2026-09-02T22:45:51.585771+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `-0.0005`, median `0.0014`, brier `0.1923`, calibration_gap `0.0422`
- 5d: hit_rate `0.3750`, avg `-0.0099`, median `-0.0084`, brier `0.3999`, calibration_gap `0.4172`
- 10d: hit_rate `0.1250`, avg `-0.0157`, median `-0.0189`, brier `0.5590`, calibration_gap `0.6672`
- 20d: hit_rate `0.5000`, avg `0.0096`, median `0.0084`, brier `0.3369`, calibration_gap `0.2922`
- 60d: hit_rate `0.8750`, avg `0.0479`, median `0.0588`, brier `0.1165`, calibration_gap `-0.0828`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0027`, median `0.0007`, brier `0.2891`, calibration_gap `0.2155`
- 5d: hit_rate `0.4375`, avg `-0.0093`, median `-0.0045`, brier `0.3601`, calibration_gap `0.3405`
- 10d: hit_rate `0.2500`, avg `-0.0118`, median `-0.0200`, brier `0.4734`, calibration_gap `0.5280`
- 20d: hit_rate `0.5000`, avg `-0.0064`, median `-0.0017`, brier `0.3292`, calibration_gap `0.2780`
- 60d: hit_rate `0.6875`, avg `0.0292`, median `0.0586`, brier `0.2190`, calibration_gap `0.0905`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5250`, avg `0.0003`, median `0.0019`, brier `0.2976`, calibration_gap `0.2119`
- 5d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0021`, brier `0.3124`, calibration_gap `0.2369`
- 10d: hit_rate `0.4750`, avg `0.0061`, median `-0.0008`, brier `0.3259`, calibration_gap `0.2619`
- 20d: hit_rate `0.7250`, avg `0.0206`, median `0.0271`, brier `0.2008`, calibration_gap `0.0119`
- 60d: hit_rate `0.7750`, avg `0.0462`, median `0.0618`, brier `0.1744`, calibration_gap `-0.0381`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0109`, median `0.0144`, brier `0.1888`, calibration_gap `-0.0379`
- 5d: hit_rate `0.6250`, avg `0.0134`, median `0.0149`, brier `0.2424`, calibration_gap `0.0871`
- 10d: hit_rate `0.6250`, avg `0.0095`, median `0.0179`, brier `0.2431`, calibration_gap `0.0871`
- 20d: hit_rate `0.8125`, avg `0.0231`, median `0.0343`, brier `0.1621`, calibration_gap `-0.1004`
- 60d: hit_rate `0.7500`, avg `0.0309`, median `0.0721`, brier `0.1877`, calibration_gap `-0.0379`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
