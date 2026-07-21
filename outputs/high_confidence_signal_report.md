# High Confidence Signal Report

Generated at: `2026-07-21T21:39:47.188188+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0068`, median `0.0007`, brier `0.2545`, calibration_gap `0.1341`
- 5d: hit_rate `0.3750`, avg `-0.0135`, median `-0.0084`, brier `0.3779`, calibration_gap `0.3841`
- 10d: hit_rate `0.1250`, avg `-0.0156`, median `-0.0189`, brier `0.5107`, calibration_gap `0.6341`
- 20d: hit_rate `0.5000`, avg `0.0034`, median `0.0084`, brier `0.3120`, calibration_gap `0.2591`
- 60d: hit_rate `0.7500`, avg `0.0328`, median `0.0519`, brier `0.1833`, calibration_gap `0.0091`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0042`, median `0.0014`, brier `0.2508`, calibration_gap `0.1235`
- 5d: hit_rate `0.5000`, avg `-0.0051`, median `-0.0009`, brier `0.3127`, calibration_gap `0.2485`
- 10d: hit_rate `0.2500`, avg `-0.0068`, median `-0.0152`, brier `0.4383`, calibration_gap `0.4985`
- 20d: hit_rate `0.6250`, avg `0.0089`, median `0.0201`, brier `0.2493`, calibration_gap `0.1235`
- 60d: hit_rate `0.7500`, avg `0.0399`, median `0.0586`, brier `0.1850`, calibration_gap `-0.0015`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.4000`, avg `-0.0104`, median `-0.0097`, brier `0.3498`, calibration_gap `0.3292`
- 5d: hit_rate `0.3500`, avg `-0.0151`, median `-0.0162`, brier `0.3718`, calibration_gap `0.3792`
- 10d: hit_rate `0.2500`, avg `-0.0058`, median `-0.0074`, brier `0.4206`, calibration_gap `0.4792`
- 20d: hit_rate `0.6500`, avg `0.0139`, median `0.0239`, brier `0.2316`, calibration_gap `0.0792`
- 60d: hit_rate `0.7000`, avg `0.0420`, median `0.0593`, brier `0.2085`, calibration_gap `0.0292`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0019`, median `0.0046`, brier `0.2138`, calibration_gap `0.0021`
- 5d: hit_rate `0.4375`, avg `0.0029`, median `-0.0008`, brier `0.3091`, calibration_gap `0.2521`
- 10d: hit_rate `0.3125`, avg `-0.0109`, median `-0.0157`, brier `0.3564`, calibration_gap `0.3771`
- 20d: hit_rate `0.6250`, avg `-0.0116`, median `0.0039`, brier `0.2400`, calibration_gap `0.0646`
- 60d: hit_rate `0.5000`, avg `-0.0136`, median `0.0002`, brier `0.2873`, calibration_gap `0.1896`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
