# High Confidence Signal Report

Generated at: `2026-07-15T14:12:50.283888+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0013`, median `0.0009`, brier `0.2933`, calibration_gap `0.2083`
- 5d: hit_rate `0.8750`, avg `0.0058`, median `0.0067`, brier `0.1401`, calibration_gap `-0.1667`
- 10d: hit_rate `0.7500`, avg `0.0075`, median `0.0089`, brier `0.1917`, calibration_gap `-0.0417`
- 20d: hit_rate `0.3750`, avg `0.0014`, median `-0.0037`, brier `0.3428`, calibration_gap `0.3333`
- 60d: hit_rate `0.6250`, avg `0.0136`, median `0.0280`, brier `0.2410`, calibration_gap `0.0833`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0010`, median `0.0006`, brier `0.2916`, calibration_gap `0.2034`
- 5d: hit_rate `0.7500`, avg `0.0055`, median `0.0067`, brier `0.1906`, calibration_gap `-0.0466`
- 10d: hit_rate `0.8125`, avg `0.0100`, median `0.0106`, brier `0.1662`, calibration_gap `-0.1091`
- 20d: hit_rate `0.5000`, avg `0.0059`, median `-0.0005`, brier `0.2913`, calibration_gap `0.2034`
- 60d: hit_rate `0.5000`, avg `0.0000`, median `-0.0093`, brier `0.2903`, calibration_gap `0.2034`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0061`, median `0.0054`, brier `0.2156`, calibration_gap `-0.0232`
- 5d: hit_rate `0.6000`, avg `0.0070`, median `0.0064`, brier `0.2474`, calibration_gap `0.0768`
- 10d: hit_rate `0.5000`, avg `0.0008`, median `-0.0015`, brier `0.2784`, calibration_gap `0.1768`
- 20d: hit_rate `0.6500`, avg `0.0019`, median `0.0088`, brier `0.2335`, calibration_gap `0.0268`
- 60d: hit_rate `0.5500`, avg `0.0138`, median `0.0276`, brier `0.2614`, calibration_gap `0.1268`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0021`, median `0.0039`, brier `0.2582`, calibration_gap `0.1050`
- 5d: hit_rate `0.6250`, avg `0.0006`, median `0.0063`, brier `0.2368`, calibration_gap `0.0425`
- 10d: hit_rate `0.5000`, avg `0.0005`, median `-0.0026`, brier `0.2779`, calibration_gap `0.1675`
- 20d: hit_rate `0.6875`, avg `-0.0041`, median `0.0116`, brier `0.2159`, calibration_gap `-0.0200`
- 60d: hit_rate `0.3125`, avg `-0.0268`, median `-0.0196`, brier `0.3410`, calibration_gap `0.3550`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
