# High Confidence Signal Report

Generated at: `2026-06-15T15:20:52.565065+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0003`, median `0.0031`, brier `0.2421`, calibration_gap `0.0880`
- 5d: hit_rate `0.5000`, avg `-0.0034`, median `-0.0047`, brier `0.2972`, calibration_gap `0.2130`
- 10d: hit_rate `0.8750`, avg `0.0113`, median `0.0135`, brier `0.1382`, calibration_gap `-0.1620`
- 20d: hit_rate `0.7500`, avg `0.0076`, median `0.0123`, brier `0.1846`, calibration_gap `-0.0370`
- 60d: hit_rate `0.2500`, avg `-0.0320`, median `-0.0398`, brier `0.4003`, calibration_gap `0.4630`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0017`, median `0.0028`, brier `0.2638`, calibration_gap `0.1383`
- 5d: hit_rate `0.3750`, avg `-0.0046`, median `-0.0068`, brier `0.3395`, calibration_gap `0.3258`
- 10d: hit_rate `0.7500`, avg `0.0073`, median `0.0075`, brier `0.1889`, calibration_gap `-0.0492`
- 20d: hit_rate `0.7500`, avg `0.0097`, median `0.0143`, brier `0.1883`, calibration_gap `-0.0492`
- 60d: hit_rate `0.4375`, avg `0.0019`, median `-0.0186`, brier `0.3178`, calibration_gap `0.2633`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0094`, median `0.0129`, brier `0.2031`, calibration_gap `-0.1211`
- 5d: hit_rate `0.8125`, avg `0.0156`, median `0.0139`, brier `0.1875`, calibration_gap `-0.1836`
- 10d: hit_rate `0.6875`, avg `0.0143`, median `0.0249`, brier `0.2202`, calibration_gap `-0.0586`
- 20d: hit_rate `0.6875`, avg `0.0086`, median `0.0171`, brier `0.2191`, calibration_gap `-0.0586`
- 60d: hit_rate `0.5625`, avg `0.0308`, median `0.0300`, brier `0.2506`, calibration_gap `0.0664`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
