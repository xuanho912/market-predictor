# High Confidence Signal Report

Generated at: `2026-07-29T00:10:44.139176+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0214`, median `-0.0318`, brier `0.5303`, calibration_gap `0.6500`
- 5d: hit_rate `0.2500`, avg `-0.0286`, median `-0.0289`, brier `0.4638`, calibration_gap `0.5250`
- 10d: hit_rate `0.0000`, avg `-0.0176`, median `-0.0147`, brier `0.6007`, calibration_gap `0.7750`
- 20d: hit_rate `0.5000`, avg `0.0011`, median `0.0138`, brier `0.3274`, calibration_gap `0.2750`
- 60d: hit_rate `0.6250`, avg `0.0278`, median `0.0418`, brier `0.2570`, calibration_gap `0.1500`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0092`, median `-0.0054`, brier `0.3591`, calibration_gap `0.3299`
- 5d: hit_rate `0.4375`, avg `-0.0156`, median `-0.0154`, brier `0.3581`, calibration_gap `0.3299`
- 10d: hit_rate `0.2500`, avg `-0.0067`, median `-0.0074`, brier `0.4596`, calibration_gap `0.5174`
- 20d: hit_rate `0.6875`, avg `0.0112`, median `0.0201`, brier `0.2247`, calibration_gap `0.0799`
- 60d: hit_rate `0.7500`, avg `0.0406`, median `0.0483`, brier `0.1895`, calibration_gap `0.0174`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5750`, avg `0.0006`, median `0.0052`, brier `0.2784`, calibration_gap `0.1539`
- 5d: hit_rate `0.6000`, avg `0.0021`, median `0.0045`, brier `0.2710`, calibration_gap `0.1289`
- 10d: hit_rate `0.6000`, avg `0.0158`, median `0.0177`, brier `0.2797`, calibration_gap `0.1289`
- 20d: hit_rate `0.7500`, avg `0.0356`, median `0.0478`, brier `0.1931`, calibration_gap `-0.0211`
- 60d: hit_rate `0.8000`, avg `0.0652`, median `0.0743`, brier `0.1698`, calibration_gap `-0.0711`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0012`, median `0.0007`, brier `0.2593`, calibration_gap `0.1188`
- 5d: hit_rate `0.5000`, avg `-0.0018`, median `0.0010`, brier `0.2815`, calibration_gap `0.1813`
- 10d: hit_rate `0.5625`, avg `0.0035`, median `0.0129`, brier `0.2591`, calibration_gap `0.1188`
- 20d: hit_rate `0.5625`, avg `-0.0014`, median `0.0241`, brier `0.2600`, calibration_gap `0.1188`
- 60d: hit_rate `0.4375`, avg `-0.0216`, median `-0.0287`, brier `0.3058`, calibration_gap `0.2438`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
