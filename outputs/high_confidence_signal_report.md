# High Confidence Signal Report

Generated at: `2026-11-20T12:12:41.799288+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0033`, median `0.0013`, brier `0.3665`, calibration_gap `0.3183`
- 5d: hit_rate `0.7500`, avg `0.0149`, median `0.0122`, brier `0.1896`, calibration_gap `0.0683`
- 10d: hit_rate `0.7500`, avg `0.0292`, median `0.0394`, brier `0.1891`, calibration_gap `0.0683`
- 20d: hit_rate `0.6250`, avg `0.0288`, median `0.0188`, brier `0.2863`, calibration_gap `0.1933`
- 60d: hit_rate `0.7500`, avg `0.0423`, median `0.0258`, brier `0.1975`, calibration_gap `0.0683`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0069`, median `0.0073`, brier `0.3129`, calibration_gap `0.2391`
- 5d: hit_rate `0.6250`, avg `0.0043`, median `0.0033`, brier `0.2596`, calibration_gap `0.1766`
- 10d: hit_rate `0.5625`, avg `0.0077`, median `0.0077`, brier `0.2962`, calibration_gap `0.2391`
- 20d: hit_rate `0.7500`, avg `0.0281`, median `0.0279`, brier `0.2015`, calibration_gap `0.0516`
- 60d: hit_rate `0.5625`, avg `0.0280`, median `0.0015`, brier `0.3003`, calibration_gap `0.2391`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0125`, median `0.0095`, brier `0.2472`, calibration_gap `0.0522`
- 5d: hit_rate `0.6750`, avg `0.0140`, median `0.0110`, brier `0.2305`, calibration_gap `0.0272`
- 10d: hit_rate `0.7750`, avg `0.0270`, median `0.0235`, brier `0.1982`, calibration_gap `-0.0728`
- 20d: hit_rate `0.8250`, avg `0.0465`, median `0.0446`, brier `0.1776`, calibration_gap `-0.1228`
- 60d: hit_rate `0.7500`, avg `0.0738`, median `0.0806`, brier `0.1935`, calibration_gap `-0.0478`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0084`, median `0.0114`, brier `0.2193`, calibration_gap `-0.0792`
- 5d: hit_rate `0.6875`, avg `0.0239`, median `0.0237`, brier `0.2195`, calibration_gap `-0.0792`
- 10d: hit_rate `0.6875`, avg `0.0256`, median `0.0437`, brier `0.2211`, calibration_gap `-0.0792`
- 20d: hit_rate `0.7500`, avg `0.0323`, median `0.0506`, brier `0.2089`, calibration_gap `-0.1417`
- 60d: hit_rate `0.6875`, avg `0.0549`, median `0.0878`, brier `0.2225`, calibration_gap `-0.0792`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
