# High Confidence Signal Report

Generated at: `2026-08-12T21:12:00.401415+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0142`, median `0.0129`, brier `0.0766`, calibration_gap `-0.2766`
- 5d: hit_rate `0.8750`, avg `0.0079`, median `0.0097`, brier `0.1334`, calibration_gap `-0.1516`
- 10d: hit_rate `0.8750`, avg `0.0150`, median `0.0179`, brier `0.1358`, calibration_gap `-0.1516`
- 20d: hit_rate `0.3750`, avg `0.0023`, median `-0.0053`, brier `0.3593`, calibration_gap `0.3484`
- 60d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0373`, brier `0.3593`, calibration_gap `0.3484`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0059`, median `0.0074`, brier `0.1585`, calibration_gap `-0.0985`
- 5d: hit_rate `0.8125`, avg `0.0054`, median `0.0103`, brier `0.1613`, calibration_gap `-0.0985`
- 10d: hit_rate `0.7500`, avg `0.0105`, median `0.0146`, brier `0.1881`, calibration_gap `-0.0360`
- 20d: hit_rate `0.5000`, avg `0.0041`, median `-0.0008`, brier `0.2999`, calibration_gap `0.2140`
- 60d: hit_rate `0.4375`, avg `0.0002`, median `-0.0247`, brier `0.3252`, calibration_gap `0.2765`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0029`, median `0.0043`, brier `0.2416`, calibration_gap `0.0734`
- 5d: hit_rate `0.6875`, avg `0.0038`, median `0.0049`, brier `0.2131`, calibration_gap `-0.0016`
- 10d: hit_rate `0.6125`, avg `0.0075`, median `0.0077`, brier `0.2417`, calibration_gap `0.0734`
- 20d: hit_rate `0.6750`, avg `0.0129`, median `0.0127`, brier `0.2230`, calibration_gap `0.0109`
- 60d: hit_rate `0.5750`, avg `0.0198`, median `0.0267`, brier `0.2601`, calibration_gap `0.1109`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0069`, median `0.0073`, brier `0.2153`, calibration_gap `-0.0199`
- 5d: hit_rate `0.6875`, avg `0.0026`, median `0.0051`, brier `0.2147`, calibration_gap `-0.0199`
- 10d: hit_rate `0.6250`, avg `0.0097`, median `0.0093`, brier `0.2354`, calibration_gap `0.0426`
- 20d: hit_rate `0.7500`, avg `0.0211`, median `0.0175`, brier `0.1948`, calibration_gap `-0.0824`
- 60d: hit_rate `0.5625`, avg `0.0340`, median `0.0283`, brier `0.2578`, calibration_gap `0.1051`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
