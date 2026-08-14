# High Confidence Signal Report

Generated at: `2026-08-14T23:10:36.062049+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0130`, median `0.0129`, brier `0.0779`, calibration_gap `-0.2789`
- 5d: hit_rate `0.8750`, avg `0.0082`, median `0.0097`, brier `0.1323`, calibration_gap `-0.1539`
- 10d: hit_rate `0.8750`, avg `0.0161`, median `0.0199`, brier `0.1326`, calibration_gap `-0.1539`
- 20d: hit_rate `0.2500`, avg `-0.0009`, median `-0.0114`, brier `0.4097`, calibration_gap `0.4711`
- 60d: hit_rate `0.2500`, avg `-0.0126`, median `-0.0408`, brier `0.4097`, calibration_gap `0.4711`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0029`, median `0.0051`, brier `0.1836`, calibration_gap `-0.0383`
- 5d: hit_rate `0.8125`, avg `0.0060`, median `0.0088`, brier `0.1601`, calibration_gap `-0.1008`
- 10d: hit_rate `0.7500`, avg `0.0090`, median `0.0127`, brier `0.1863`, calibration_gap `-0.0383`
- 20d: hit_rate `0.5000`, avg `-0.0001`, median `0.0024`, brier `0.2991`, calibration_gap `0.2117`
- 60d: hit_rate `0.4375`, avg `0.0062`, median `-0.0247`, brier `0.3249`, calibration_gap `0.2742`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5750`, avg `0.0025`, median `0.0022`, brier `0.2533`, calibration_gap `0.1076`
- 5d: hit_rate `0.5875`, avg `0.0012`, median `0.0029`, brier `0.2484`, calibration_gap `0.0951`
- 10d: hit_rate `0.5625`, avg `0.0048`, median `0.0058`, brier `0.2586`, calibration_gap `0.1201`
- 20d: hit_rate `0.6375`, avg `0.0092`, median `0.0146`, brier `0.2359`, calibration_gap `0.0451`
- 60d: hit_rate `0.5875`, avg `0.0190`, median `0.0281`, brier `0.2565`, calibration_gap `0.0951`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0044`, median `0.0017`, brier `0.2746`, calibration_gap `0.1602`
- 5d: hit_rate `0.5000`, avg `-0.0022`, median `-0.0030`, brier `0.2764`, calibration_gap `0.1602`
- 10d: hit_rate `0.5000`, avg `0.0075`, median `-0.0040`, brier `0.2773`, calibration_gap `0.1602`
- 20d: hit_rate `0.6875`, avg `0.0176`, median `0.0206`, brier `0.2159`, calibration_gap `-0.0273`
- 60d: hit_rate `0.7500`, avg `0.0325`, median `0.0310`, brier `0.1972`, calibration_gap `-0.0898`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
