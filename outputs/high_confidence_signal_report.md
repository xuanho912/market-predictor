# High Confidence Signal Report

Generated at: `2026-08-18T13:11:59.693579+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0106`, median `0.0124`, brier `0.1509`, calibration_gap `-0.2100`
- 5d: hit_rate `0.6250`, avg `0.0024`, median `0.0112`, brier `0.2279`, calibration_gap `0.0400`
- 10d: hit_rate `0.8750`, avg `0.0127`, median `0.0082`, brier `0.1501`, calibration_gap `-0.2100`
- 20d: hit_rate `0.8750`, avg `0.0326`, median `0.0265`, brier `0.1509`, calibration_gap `-0.2100`
- 60d: hit_rate `0.7500`, avg `0.0492`, median `0.0826`, brier `0.1885`, calibration_gap `-0.0850`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0063`, median `0.0098`, brier `0.2115`, calibration_gap `-0.0345`
- 5d: hit_rate `0.5625`, avg `0.0012`, median `0.0112`, brier `0.2500`, calibration_gap `0.0905`
- 10d: hit_rate `0.7500`, avg `0.0115`, median `0.0082`, brier `0.1935`, calibration_gap `-0.0970`
- 20d: hit_rate `0.8750`, avg `0.0326`, median `0.0265`, brier `0.1574`, calibration_gap `-0.2220`
- 60d: hit_rate `0.8125`, avg `0.0487`, median `0.0826`, brier `0.1762`, calibration_gap `-0.1595`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.7000`, avg `0.0072`, median `0.0086`, brier `0.2194`, calibration_gap `-0.1006`
- 5d: hit_rate `0.6500`, avg `0.0098`, median `0.0100`, brier `0.2328`, calibration_gap `-0.0506`
- 10d: hit_rate `0.7125`, avg `0.0196`, median `0.0174`, brier `0.2175`, calibration_gap `-0.1131`
- 20d: hit_rate `0.9375`, avg `0.0401`, median `0.0310`, brier `0.1759`, calibration_gap `-0.3381`
- 60d: hit_rate `0.8250`, avg `0.0499`, median `0.0568`, brier `0.1971`, calibration_gap `-0.2256`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0074`, median `0.0051`, brier `0.2398`, calibration_gap `-0.0674`
- 5d: hit_rate `0.7500`, avg `0.0155`, median `0.0160`, brier `0.2247`, calibration_gap `-0.1924`
- 10d: hit_rate `0.7500`, avg `0.0239`, median `0.0194`, brier `0.2263`, calibration_gap `-0.1924`
- 20d: hit_rate `1.0000`, avg `0.0377`, median `0.0346`, brier `0.1958`, calibration_gap `-0.4424`
- 60d: hit_rate `0.9375`, avg `0.0552`, median `0.0501`, brier `0.2041`, calibration_gap `-0.3799`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
