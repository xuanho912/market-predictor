# High Confidence Signal Report

Generated at: `2026-11-17T20:58:31.435940+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0061`, median `0.0073`, brier `0.2772`, calibration_gap `0.1999`
- 5d: hit_rate `0.7500`, avg `0.0073`, median `0.0017`, brier `0.1909`, calibration_gap `0.0749`
- 10d: hit_rate `0.5000`, avg `0.0107`, median `0.0021`, brier `0.3553`, calibration_gap `0.3249`
- 20d: hit_rate `0.5000`, avg `0.0084`, median `0.0027`, brier `0.3594`, calibration_gap `0.3249`
- 60d: hit_rate `0.5000`, avg `0.0073`, median `-0.0034`, brier `0.3596`, calibration_gap `0.3249`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0085`, median `0.0107`, brier `0.2356`, calibration_gap `0.1262`
- 5d: hit_rate `0.7500`, avg `0.0060`, median `0.0076`, brier `0.1904`, calibration_gap `0.0637`
- 10d: hit_rate `0.6250`, avg `0.0099`, median `0.0087`, brier `0.2740`, calibration_gap `0.1887`
- 20d: hit_rate `0.7500`, avg `0.0277`, median `0.0334`, brier `0.1992`, calibration_gap `0.0637`
- 60d: hit_rate `0.6875`, avg `0.0402`, median `0.0552`, brier `0.2378`, calibration_gap `0.1262`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `0.0091`, median `0.0089`, brier `0.2688`, calibration_gap `0.1227`
- 5d: hit_rate `0.6667`, avg `0.0101`, median `0.0091`, brier `0.2347`, calibration_gap `0.0727`
- 10d: hit_rate `0.6500`, avg `0.0182`, median `0.0116`, brier `0.2572`, calibration_gap `0.0894`
- 20d: hit_rate `0.7833`, avg `0.0366`, median `0.0369`, brier `0.1946`, calibration_gap `-0.0439`
- 60d: hit_rate `0.6833`, avg `0.0602`, median `0.0676`, brier `0.2436`, calibration_gap `0.0561`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0010`, median `0.0075`, brier `0.2501`, calibration_gap `0.0531`
- 5d: hit_rate `0.6250`, avg `0.0151`, median `0.0176`, brier `0.2350`, calibration_gap `-0.0094`
- 10d: hit_rate `0.7500`, avg `0.0449`, median `0.0514`, brier `0.2045`, calibration_gap `-0.1344`
- 20d: hit_rate `0.8125`, avg `0.0577`, median `0.0636`, brier `0.1906`, calibration_gap `-0.1969`
- 60d: hit_rate `0.6250`, avg `0.0745`, median `0.1210`, brier `0.2351`, calibration_gap `-0.0094`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
