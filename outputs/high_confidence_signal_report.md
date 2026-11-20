# High Confidence Signal Report

Generated at: `2026-11-20T02:01:48.404107+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0017`, median `-0.0040`, brier `0.3895`, calibration_gap `0.4008`
- 5d: hit_rate `0.3750`, avg `-0.0041`, median `-0.0090`, brier `0.3989`, calibration_gap `0.4008`
- 10d: hit_rate `0.7500`, avg `0.0143`, median `0.0122`, brier `0.1922`, calibration_gap `0.0258`
- 20d: hit_rate `1.0000`, avg `0.0563`, median `0.0562`, brier `0.0506`, calibration_gap `-0.2242`
- 60d: hit_rate `1.0000`, avg `0.1068`, median `0.1129`, brier `0.0506`, calibration_gap `-0.2242`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0065`, brier `0.3739`, calibration_gap `0.3820`
- 5d: hit_rate `0.3125`, avg `-0.0057`, median `-0.0082`, brier `0.4096`, calibration_gap `0.4445`
- 10d: hit_rate `0.6250`, avg `0.0110`, median `0.0122`, brier `0.2477`, calibration_gap `0.1320`
- 20d: hit_rate `1.0000`, avg `0.0586`, median `0.0629`, brier `0.0597`, calibration_gap `-0.2430`
- 60d: hit_rate `1.0000`, avg `0.1149`, median `0.1177`, brier `0.0597`, calibration_gap `-0.2430`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `0.0083`, median `0.0067`, brier `0.2510`, calibration_gap `0.0068`
- 5d: hit_rate `0.5250`, avg `0.0102`, median `0.0023`, brier `0.2812`, calibration_gap `0.1068`
- 10d: hit_rate `0.7500`, avg `0.0278`, median `0.0226`, brier `0.2089`, calibration_gap `-0.1182`
- 20d: hit_rate `0.9000`, avg `0.0620`, median `0.0631`, brier `0.1650`, calibration_gap `-0.2682`
- 60d: hit_rate `0.9250`, avg `0.1243`, median `0.1321`, brier `0.1583`, calibration_gap `-0.2932`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0215`, median `0.0342`, brier `0.2438`, calibration_gap `-0.2993`
- 5d: hit_rate `0.7500`, avg `0.0383`, median `0.0460`, brier `0.2473`, calibration_gap `-0.2368`
- 10d: hit_rate `0.8125`, avg `0.0572`, median `0.0656`, brier `0.2445`, calibration_gap `-0.2993`
- 20d: hit_rate `0.9375`, avg `0.1024`, median `0.0896`, brier `0.2407`, calibration_gap `-0.4243`
- 60d: hit_rate `1.0000`, avg `0.1875`, median `0.2131`, brier `0.2372`, calibration_gap `-0.4868`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
