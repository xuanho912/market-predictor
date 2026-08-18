# High Confidence Signal Report

Generated at: `2026-08-18T23:33:49.120535+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `40`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `4`
- 3d: hit_rate `0.5000`, avg `-0.0044`, median `-0.0042`, brier `0.3077`, calibration_gap `0.2344`
- 5d: hit_rate `0.7500`, avg `0.0032`, median `0.0039`, brier `0.1866`, calibration_gap `-0.0156`
- 10d: hit_rate `0.2500`, avg `-0.0054`, median `-0.0098`, brier `0.4234`, calibration_gap `0.4844`
- 20d: hit_rate `0.5000`, avg `0.0024`, median `0.0064`, brier `0.3017`, calibration_gap `0.2344`
- 60d: hit_rate `0.7500`, avg `0.0374`, median `0.0453`, brier `0.1860`, calibration_gap `-0.0156`

### top_20_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0034`, median `0.0004`, brier `0.2474`, calibration_gap `0.1033`
- 5d: hit_rate `0.7500`, avg `0.0006`, median `0.0010`, brier `0.1868`, calibration_gap `-0.0217`
- 10d: hit_rate `0.2500`, avg `-0.0068`, median `-0.0129`, brier `0.4162`, calibration_gap `0.4783`
- 20d: hit_rate `0.3750`, avg `0.0008`, median `-0.0044`, brier `0.3566`, calibration_gap `0.3533`
- 60d: hit_rate `0.6250`, avg `0.0270`, median `0.0396`, brier `0.2443`, calibration_gap `0.1033`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0073`, median `-0.0074`, brier `0.3259`, calibration_gap `0.3019`
- 5d: hit_rate `0.2500`, avg `-0.0127`, median `-0.0062`, brier `0.3692`, calibration_gap `0.4269`
- 10d: hit_rate `0.2500`, avg `-0.0162`, median `-0.0177`, brier `0.3710`, calibration_gap `0.4269`
- 20d: hit_rate `0.6250`, avg `-0.0185`, median `0.0022`, brier `0.2372`, calibration_gap `0.0519`
- 60d: hit_rate `0.3750`, avg `-0.0234`, median `-0.0302`, brier `0.3259`, calibration_gap `0.3019`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
