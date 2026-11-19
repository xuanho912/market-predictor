# High Confidence Signal Report

Generated at: `2026-11-19T03:54:54.509543+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0004`, median `0.0056`, brier `0.2781`, calibration_gap `0.1924`
- 5d: hit_rate `0.7500`, avg `0.0073`, median `0.0064`, brier `0.1905`, calibration_gap `0.0674`
- 10d: hit_rate `0.6250`, avg `0.0118`, median `0.0155`, brier `0.2689`, calibration_gap `0.1924`
- 20d: hit_rate `0.5000`, avg `0.0131`, median `0.0027`, brier `0.3556`, calibration_gap `0.3174`
- 60d: hit_rate `0.3750`, avg `0.0026`, median `-0.0099`, brier `0.4269`, calibration_gap `0.4424`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0039`, median `0.0054`, brier `0.3087`, calibration_gap `0.2450`
- 5d: hit_rate `0.6250`, avg `0.0037`, median `0.0017`, brier `0.2631`, calibration_gap `0.1825`
- 10d: hit_rate `0.5625`, avg `0.0061`, median `0.0085`, brier `0.3038`, calibration_gap `0.2450`
- 20d: hit_rate `0.6250`, avg `0.0156`, median `0.0137`, brier `0.2714`, calibration_gap `0.1825`
- 60d: hit_rate `0.6250`, avg `0.0255`, median `0.0318`, brier `0.2722`, calibration_gap `0.1825`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `0.0086`, median `0.0122`, brier `0.2600`, calibration_gap `0.0846`
- 5d: hit_rate `0.6500`, avg `0.0096`, median `0.0075`, brier `0.2312`, calibration_gap `0.0596`
- 10d: hit_rate `0.6000`, avg `0.0091`, median `0.0062`, brier `0.2500`, calibration_gap `0.1096`
- 20d: hit_rate `0.7500`, avg `0.0214`, median `0.0345`, brier `0.1936`, calibration_gap `-0.0404`
- 60d: hit_rate `0.7750`, avg `0.0584`, median `0.0634`, brier `0.1873`, calibration_gap `-0.0654`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0029`, median `0.0228`, brier `0.2352`, calibration_gap `-0.0146`
- 5d: hit_rate `0.6250`, avg `0.0092`, median `0.0123`, brier `0.2345`, calibration_gap `-0.0146`
- 10d: hit_rate `0.6250`, avg `0.0072`, median `0.0302`, brier `0.2348`, calibration_gap `-0.0146`
- 20d: hit_rate `0.6250`, avg `-0.0058`, median `0.0300`, brier `0.2349`, calibration_gap `-0.0146`
- 60d: hit_rate `0.6875`, avg `0.0363`, median `0.0659`, brier `0.2205`, calibration_gap `-0.0771`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
