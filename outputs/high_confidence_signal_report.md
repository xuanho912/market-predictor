# High Confidence Signal Report

Generated at: `2026-11-18T20:34:52.097798+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0004`, median `0.0056`, brier `0.2781`, calibration_gap `0.1925`
- 5d: hit_rate `0.7500`, avg `0.0073`, median `0.0064`, brier `0.1908`, calibration_gap `0.0675`
- 10d: hit_rate `0.6250`, avg `0.0118`, median `0.0155`, brier `0.2696`, calibration_gap `0.1925`
- 20d: hit_rate `0.5000`, avg `0.0131`, median `0.0027`, brier `0.3560`, calibration_gap `0.3175`
- 60d: hit_rate `0.3750`, avg `0.0026`, median `-0.0099`, brier `0.4275`, calibration_gap `0.4425`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0075`, median `0.0073`, brier `0.2722`, calibration_gap `0.1826`
- 5d: hit_rate `0.7500`, avg `0.0088`, median `0.0076`, brier `0.1903`, calibration_gap `0.0576`
- 10d: hit_rate `0.6250`, avg `0.0125`, median `0.0143`, brier `0.2677`, calibration_gap `0.1826`
- 20d: hit_rate `0.6875`, avg `0.0208`, median `0.0201`, brier `0.2350`, calibration_gap `0.1201`
- 60d: hit_rate `0.6250`, avg `0.0266`, median `0.0258`, brier `0.2725`, calibration_gap `0.1826`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `0.0061`, median `0.0083`, brier `0.2824`, calibration_gap `0.1522`
- 5d: hit_rate `0.6000`, avg `0.0062`, median `0.0034`, brier `0.2615`, calibration_gap `0.1356`
- 10d: hit_rate `0.5667`, avg `0.0080`, median `0.0055`, brier `0.2773`, calibration_gap `0.1689`
- 20d: hit_rate `0.6833`, avg `0.0186`, median `0.0305`, brier `0.2303`, calibration_gap `0.0522`
- 60d: hit_rate `0.7333`, avg `0.0523`, median `0.0634`, brier `0.2087`, calibration_gap `0.0022`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0029`, median `0.0228`, brier `0.2356`, calibration_gap `-0.0148`
- 5d: hit_rate `0.6250`, avg `0.0092`, median `0.0123`, brier `0.2346`, calibration_gap `-0.0148`
- 10d: hit_rate `0.6250`, avg `0.0072`, median `0.0302`, brier `0.2348`, calibration_gap `-0.0148`
- 20d: hit_rate `0.6250`, avg `-0.0058`, median `0.0300`, brier `0.2353`, calibration_gap `-0.0148`
- 60d: hit_rate `0.6875`, avg `0.0363`, median `0.0659`, brier `0.2207`, calibration_gap `-0.0773`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
