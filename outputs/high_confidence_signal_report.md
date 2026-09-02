# High Confidence Signal Report

Generated at: `2026-09-02T16:38:15.619977+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0030`, median `0.0007`, brier `0.2606`, calibration_gap `0.1718`
- 5d: hit_rate `0.3750`, avg `-0.0098`, median `-0.0084`, brier `0.4023`, calibration_gap `0.4218`
- 10d: hit_rate `0.1250`, avg `-0.0153`, median `-0.0189`, brier `0.5652`, calibration_gap `0.6718`
- 20d: hit_rate `0.5000`, avg `-0.0016`, median `0.0084`, brier `0.3400`, calibration_gap `0.2968`
- 60d: hit_rate `0.7500`, avg `0.0330`, median `0.0519`, brier `0.1855`, calibration_gap `0.0468`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0027`, median `0.0007`, brier `0.2910`, calibration_gap `0.2196`
- 5d: hit_rate `0.4375`, avg `-0.0093`, median `-0.0045`, brier `0.3619`, calibration_gap `0.3446`
- 10d: hit_rate `0.2500`, avg `-0.0118`, median `-0.0200`, brier `0.4775`, calibration_gap `0.5321`
- 20d: hit_rate `0.5000`, avg `-0.0064`, median `-0.0017`, brier `0.3317`, calibration_gap `0.2821`
- 60d: hit_rate `0.6875`, avg `0.0292`, median `0.0586`, brier `0.2209`, calibration_gap `0.0946`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5250`, avg `0.0003`, median `0.0019`, brier `0.2978`, calibration_gap `0.2120`
- 5d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0021`, brier `0.3123`, calibration_gap `0.2370`
- 10d: hit_rate `0.4750`, avg `0.0061`, median `-0.0008`, brier `0.3256`, calibration_gap `0.2620`
- 20d: hit_rate `0.7250`, avg `0.0206`, median `0.0271`, brier `0.2002`, calibration_gap `0.0120`
- 60d: hit_rate `0.7750`, avg `0.0462`, median `0.0618`, brier `0.1747`, calibration_gap `-0.0380`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0080`, median `0.0059`, brier `0.1885`, calibration_gap `-0.0390`
- 5d: hit_rate `0.7500`, avg `0.0118`, median `0.0106`, brier `0.1882`, calibration_gap `-0.0390`
- 10d: hit_rate `0.6875`, avg `0.0114`, median `0.0179`, brier `0.2152`, calibration_gap `0.0235`
- 20d: hit_rate `0.6875`, avg `0.0128`, median `0.0250`, brier `0.2146`, calibration_gap `0.0235`
- 60d: hit_rate `0.7500`, avg `0.0198`, median `0.0567`, brier `0.1891`, calibration_gap `-0.0390`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
