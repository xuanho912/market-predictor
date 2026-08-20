# High Confidence Signal Report

Generated at: `2026-08-20T02:34:10.008913+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0089`, median `0.0069`, brier `0.0757`, calibration_gap `-0.2749`
- 5d: hit_rate `1.0000`, avg `0.0112`, median `0.0112`, brier `0.0757`, calibration_gap `-0.2749`
- 10d: hit_rate `1.0000`, avg `0.0197`, median `0.0202`, brier `0.0757`, calibration_gap `-0.2749`
- 20d: hit_rate `0.5000`, avg `0.0063`, median `0.0002`, brier `0.3044`, calibration_gap `0.2251`
- 60d: hit_rate `0.2500`, avg `-0.0052`, median `-0.0336`, brier `0.4088`, calibration_gap `0.4751`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0030`, median `0.0034`, brier `0.2068`, calibration_gap `0.0228`
- 5d: hit_rate `0.7500`, avg `0.0043`, median `0.0063`, brier `0.1823`, calibration_gap `-0.0397`
- 10d: hit_rate `0.7500`, avg `0.0125`, median `0.0164`, brier `0.1820`, calibration_gap `-0.0397`
- 20d: hit_rate `0.6875`, avg `0.0182`, median `0.0100`, brier `0.2229`, calibration_gap `0.0228`
- 60d: hit_rate `0.4375`, avg `0.0212`, median `-0.0187`, brier `0.3238`, calibration_gap `0.2728`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5875`, avg `0.0036`, median `0.0050`, brier `0.2468`, calibration_gap `0.0878`
- 5d: hit_rate `0.5875`, avg `0.0040`, median `0.0039`, brier `0.2444`, calibration_gap `0.0878`
- 10d: hit_rate `0.6500`, avg `0.0062`, median `0.0102`, brier `0.2259`, calibration_gap `0.0253`
- 20d: hit_rate `0.7125`, avg `0.0154`, median `0.0179`, brier `0.2068`, calibration_gap `-0.0372`
- 60d: hit_rate `0.6125`, avg `0.0269`, median `0.0407`, brier `0.2454`, calibration_gap `0.0628`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0025`, median `0.0040`, brier `0.2531`, calibration_gap `0.0859`
- 5d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0018`, brier `0.2709`, calibration_gap `0.1484`
- 10d: hit_rate `0.6875`, avg `0.0018`, median `0.0067`, brier `0.2164`, calibration_gap `-0.0391`
- 20d: hit_rate `0.6250`, avg `-0.0024`, median `0.0217`, brier `0.2359`, calibration_gap `0.0234`
- 60d: hit_rate `0.5625`, avg `-0.0158`, median `0.0180`, brier `0.2548`, calibration_gap `0.0859`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
