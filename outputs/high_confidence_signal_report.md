# High Confidence Signal Report

Generated at: `2026-06-16T13:41:57.062083+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0026`, median `0.0031`, brier `0.2414`, calibration_gap `0.0863`
- 5d: hit_rate `0.3750`, avg `-0.0075`, median `-0.0157`, brier `0.3450`, calibration_gap `0.3363`
- 10d: hit_rate `0.8750`, avg `0.0117`, median `0.0135`, brier `0.1386`, calibration_gap `-0.1637`
- 20d: hit_rate `0.7500`, avg `0.0097`, median `0.0142`, brier `0.1853`, calibration_gap `-0.0387`
- 60d: hit_rate `0.3750`, avg `-0.0092`, median `-0.0282`, brier `0.3499`, calibration_gap `0.3363`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0017`, median `0.0028`, brier `0.2632`, calibration_gap `0.1367`
- 5d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0057`, brier `0.3379`, calibration_gap `0.3242`
- 10d: hit_rate `0.6875`, avg `0.0059`, median `0.0075`, brier `0.2113`, calibration_gap `0.0117`
- 20d: hit_rate `0.7500`, avg `0.0088`, median `0.0143`, brier `0.1885`, calibration_gap `-0.0508`
- 60d: hit_rate `0.3750`, avg `-0.0021`, median `-0.0252`, brier `0.3403`, calibration_gap `0.3242`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0066`, median `0.0097`, brier `0.2028`, calibration_gap `-0.1225`
- 5d: hit_rate `0.8125`, avg `0.0156`, median `0.0126`, brier `0.1873`, calibration_gap `-0.1850`
- 10d: hit_rate `0.6250`, avg `0.0114`, median `0.0153`, brier `0.2353`, calibration_gap `0.0025`
- 20d: hit_rate `0.6250`, avg `0.0089`, median `0.0168`, brier `0.2342`, calibration_gap `0.0025`
- 60d: hit_rate `0.5625`, avg `0.0323`, median `0.0284`, brier `0.2500`, calibration_gap `0.0650`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
