# High Confidence Signal Report

Generated at: `2026-08-13T22:23:09.517607+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0130`, median `0.0129`, brier `0.0772`, calibration_gap `-0.2776`
- 5d: hit_rate `0.8750`, avg `0.0082`, median `0.0097`, brier `0.1331`, calibration_gap `-0.1526`
- 10d: hit_rate `0.8750`, avg `0.0161`, median `0.0199`, brier `0.1318`, calibration_gap `-0.1526`
- 20d: hit_rate `0.2500`, avg `-0.0009`, median `-0.0114`, brier `0.4085`, calibration_gap `0.4724`
- 60d: hit_rate `0.2500`, avg `-0.0126`, median `-0.0408`, brier `0.4085`, calibration_gap `0.4724`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0052`, median `0.0046`, brier `0.2067`, calibration_gap `0.0225`
- 5d: hit_rate `0.8125`, avg `0.0070`, median `0.0088`, brier `0.1619`, calibration_gap `-0.1025`
- 10d: hit_rate `0.7500`, avg `0.0092`, median `0.0118`, brier `0.1846`, calibration_gap `-0.0400`
- 20d: hit_rate `0.5625`, avg `0.0056`, median `0.0048`, brier `0.2745`, calibration_gap `0.1475`
- 60d: hit_rate `0.3125`, avg `-0.0079`, median `-0.0322`, brier `0.3739`, calibration_gap `0.3975`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0046`, median `0.0050`, brier `0.2392`, calibration_gap `0.0683`
- 5d: hit_rate `0.6375`, avg `0.0050`, median `0.0053`, brier `0.2300`, calibration_gap `0.0433`
- 10d: hit_rate `0.6125`, avg `0.0080`, median `0.0099`, brier `0.2397`, calibration_gap `0.0683`
- 20d: hit_rate `0.6875`, avg `0.0144`, median `0.0156`, brier `0.2172`, calibration_gap `-0.0067`
- 60d: hit_rate `0.6375`, avg `0.0272`, median `0.0456`, brier `0.2394`, calibration_gap `0.0433`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0065`, median `0.0016`, brier `0.2547`, calibration_gap `0.0973`
- 5d: hit_rate `0.5625`, avg `0.0021`, median `0.0032`, brier `0.2556`, calibration_gap `0.0973`
- 10d: hit_rate `0.6250`, avg `0.0053`, median `0.0048`, brier `0.2364`, calibration_gap `0.0348`
- 20d: hit_rate `0.6250`, avg `0.0065`, median `0.0129`, brier `0.2365`, calibration_gap `0.0348`
- 60d: hit_rate `0.6875`, avg `0.0245`, median `0.0555`, brier `0.2171`, calibration_gap `-0.0277`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
