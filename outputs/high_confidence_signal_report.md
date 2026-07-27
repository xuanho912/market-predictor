# High Confidence Signal Report

Generated at: `2026-07-27T22:38:25.992292+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0085`, median `-0.0054`, brier `0.4111`, calibration_gap `0.4220`
- 5d: hit_rate `0.5000`, avg `-0.0135`, median `-0.0026`, brier `0.3372`, calibration_gap `0.2970`
- 10d: hit_rate `0.0000`, avg `-0.0115`, median `-0.0076`, brier `0.6352`, calibration_gap `0.7970`
- 20d: hit_rate `0.5000`, avg `0.0135`, median `0.0096`, brier `0.3439`, calibration_gap `0.2970`
- 60d: hit_rate `0.6250`, avg `0.0359`, median `0.0352`, brier `0.2646`, calibration_gap `0.1720`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0084`, median `-0.0054`, brier `0.3705`, calibration_gap `0.3533`
- 5d: hit_rate `0.4375`, avg `-0.0133`, median `-0.0106`, brier `0.3696`, calibration_gap `0.3533`
- 10d: hit_rate `0.3125`, avg `-0.0040`, median `-0.0073`, brier `0.4480`, calibration_gap `0.4783`
- 20d: hit_rate `0.5625`, avg `0.0183`, median `0.0205`, brier `0.3018`, calibration_gap `0.2283`
- 60d: hit_rate `0.6875`, avg `0.0457`, median `0.0519`, brier `0.2261`, calibration_gap `0.1033`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6000`, avg `-0.0014`, median `0.0017`, brier `0.2702`, calibration_gap `0.1510`
- 5d: hit_rate `0.5500`, avg `-0.0013`, median `0.0022`, brier `0.2981`, calibration_gap `0.2010`
- 10d: hit_rate `0.5500`, avg `0.0079`, median `0.0036`, brier `0.3092`, calibration_gap `0.2010`
- 20d: hit_rate `0.6667`, avg `0.0229`, median `0.0274`, brier `0.2383`, calibration_gap `0.0844`
- 60d: hit_rate `0.7333`, avg `0.0469`, median `0.0591`, brier `0.2007`, calibration_gap `0.0177`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0017`, median `0.0027`, brier `0.2614`, calibration_gap `0.1177`
- 5d: hit_rate `0.4375`, avg `-0.0083`, median `-0.0074`, brier `0.3040`, calibration_gap `0.2427`
- 10d: hit_rate `0.6875`, avg `0.0081`, median `0.0177`, brier `0.2138`, calibration_gap `-0.0073`
- 20d: hit_rate `0.6875`, avg `0.0035`, median `0.0174`, brier `0.2144`, calibration_gap `-0.0073`
- 60d: hit_rate `0.5000`, avg `-0.0007`, median `0.0027`, brier `0.2809`, calibration_gap `0.1802`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
