# High Confidence Signal Report

Generated at: `2026-09-05T15:19:28.770592+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0005`, median `0.0022`, brier `0.1938`, calibration_gap `0.0073`
- 5d: hit_rate `0.6250`, avg `-0.0044`, median `0.0010`, brier `0.2569`, calibration_gap `0.1323`
- 10d: hit_rate `0.1250`, avg `-0.0177`, median `-0.0200`, brier `0.5105`, calibration_gap `0.6323`
- 20d: hit_rate `0.5000`, avg `0.0080`, median `-0.0017`, brier `0.3141`, calibration_gap `0.2573`
- 60d: hit_rate `0.8750`, avg `0.0387`, median `0.0586`, brier `0.1221`, calibration_gap `-0.1177`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0038`, median `0.0014`, brier `0.2803`, calibration_gap `0.1858`
- 5d: hit_rate `0.5625`, avg `-0.0032`, median `0.0010`, brier `0.2822`, calibration_gap `0.1858`
- 10d: hit_rate `0.1250`, avg `-0.0168`, median `-0.0200`, brier `0.4988`, calibration_gap `0.6233`
- 20d: hit_rate `0.5000`, avg `-0.0011`, median `-0.0017`, brier `0.3107`, calibration_gap `0.2483`
- 60d: hit_rate `0.7500`, avg `0.0290`, median `0.0479`, brier `0.1850`, calibration_gap `-0.0017`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0004`, median `0.0024`, brier `0.2102`, calibration_gap `0.0292`
- 5d: hit_rate `0.7000`, avg `0.0083`, median `0.0093`, brier `0.2080`, calibration_gap `0.0292`
- 10d: hit_rate `0.5000`, avg `0.0053`, median `0.0027`, brier `0.3021`, calibration_gap `0.2292`
- 20d: hit_rate `0.7500`, avg `0.0100`, median `0.0345`, brier `0.1866`, calibration_gap `-0.0208`
- 60d: hit_rate `0.6000`, avg `0.0095`, median `0.0417`, brier `0.2564`, calibration_gap `0.1292`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0002`, median `0.0005`, brier `0.2923`, calibration_gap `0.2101`
- 5d: hit_rate `0.3750`, avg `-0.0013`, median `-0.0068`, brier `0.3450`, calibration_gap `0.3351`
- 10d: hit_rate `0.6875`, avg `0.0181`, median `0.0215`, brier `0.2143`, calibration_gap `0.0226`
- 20d: hit_rate `0.6875`, avg `0.0246`, median `0.0286`, brier `0.2145`, calibration_gap `0.0226`
- 60d: hit_rate `0.8125`, avg `0.0632`, median `0.0880`, brier `0.1645`, calibration_gap `-0.1024`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
