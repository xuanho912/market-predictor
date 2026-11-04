# High Confidence Signal Report

Generated at: `2026-11-04T02:48:20.195792+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0110`, median `0.0143`, brier `0.2636`, calibration_gap `0.1731`
- 5d: hit_rate `0.6250`, avg `0.0124`, median `0.0121`, brier `0.2636`, calibration_gap `0.1731`
- 10d: hit_rate `0.5000`, avg `0.0189`, median `0.0111`, brier `0.3364`, calibration_gap `0.2981`
- 20d: hit_rate `0.8750`, avg `0.0391`, median `0.0301`, brier `0.1194`, calibration_gap `-0.0769`
- 60d: hit_rate `1.0000`, avg `0.0746`, median `0.0738`, brier `0.0409`, calibration_gap `-0.2019`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0038`, median `0.0017`, brier `0.3284`, calibration_gap `0.2851`
- 5d: hit_rate `0.4375`, avg `0.0058`, median `-0.0038`, brier `0.3618`, calibration_gap `0.3476`
- 10d: hit_rate `0.5625`, avg `0.0148`, median `0.0151`, brier `0.2966`, calibration_gap `0.2226`
- 20d: hit_rate `0.8125`, avg `0.0282`, median `0.0284`, brier `0.1538`, calibration_gap `-0.0274`
- 60d: hit_rate `0.9375`, avg `0.0719`, median `0.0738`, brier `0.0810`, calibration_gap `-0.1524`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6000`, avg `0.0096`, median `0.0129`, brier `0.2738`, calibration_gap `0.1809`
- 5d: hit_rate `0.5000`, avg `0.0091`, median `0.0038`, brier `0.3268`, calibration_gap `0.2809`
- 10d: hit_rate `0.6500`, avg `0.0196`, median `0.0224`, brier `0.2484`, calibration_gap `0.1309`
- 20d: hit_rate `0.8500`, avg `0.0337`, median `0.0299`, brier `0.1342`, calibration_gap `-0.0691`
- 60d: hit_rate `0.9500`, avg `0.0738`, median `0.0739`, brier `0.0760`, calibration_gap `-0.1691`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0001`, median `0.0068`, brier `0.2409`, calibration_gap `0.0234`
- 5d: hit_rate `0.5625`, avg `-0.0032`, median `0.0106`, brier `0.2420`, calibration_gap `0.0234`
- 10d: hit_rate `0.7500`, avg `0.0069`, median `0.0134`, brier `0.2133`, calibration_gap `-0.1641`
- 20d: hit_rate `0.5000`, avg `0.0111`, median `0.0107`, brier `0.2537`, calibration_gap `0.0859`
- 60d: hit_rate `0.6250`, avg `0.0186`, median `0.0242`, brier `0.2329`, calibration_gap `-0.0391`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
