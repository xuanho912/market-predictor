# High Confidence Signal Report

Generated at: `2026-10-28T00:59:05.345186+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0027`, median `0.0017`, brier `0.2908`, calibration_gap `0.1973`
- 5d: hit_rate `0.6250`, avg `0.0028`, median `0.0103`, brier `0.2375`, calibration_gap `0.0723`
- 10d: hit_rate `0.6250`, avg `-0.0052`, median `0.0086`, brier `0.2375`, calibration_gap `0.0723`
- 20d: hit_rate `0.2500`, avg `-0.0238`, median `-0.0201`, brier `0.3887`, calibration_gap `0.4473`
- 60d: hit_rate `0.8750`, avg `0.0971`, median `0.0948`, brier `0.1483`, calibration_gap `-0.1777`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0043`, median `0.0028`, brier `0.2859`, calibration_gap `0.1850`
- 5d: hit_rate `0.5625`, avg `0.0010`, median `0.0062`, brier `0.2592`, calibration_gap `0.1225`
- 10d: hit_rate `0.5000`, avg `-0.0080`, median `-0.0096`, brier `0.2802`, calibration_gap `0.1850`
- 20d: hit_rate `0.3125`, avg `-0.0199`, median `-0.0228`, brier `0.3558`, calibration_gap `0.3725`
- 60d: hit_rate `0.8750`, avg `0.0698`, median `0.0674`, brier `0.1491`, calibration_gap `-0.1900`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0056`, median `0.0181`, brier `0.2389`, calibration_gap `-0.0041`
- 5d: hit_rate `0.6500`, avg `0.0046`, median `0.0041`, brier `0.2346`, calibration_gap `-0.0041`
- 10d: hit_rate `0.5500`, avg `0.0067`, median `0.0211`, brier `0.2639`, calibration_gap `0.0959`
- 20d: hit_rate `0.5000`, avg `-0.0031`, median `0.0076`, brier `0.2751`, calibration_gap `0.1459`
- 60d: hit_rate `0.9500`, avg `0.0618`, median `0.0627`, brier `0.1492`, calibration_gap `-0.3041`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0055`, median `0.0112`, brier `0.2350`, calibration_gap `-0.0448`
- 5d: hit_rate `0.4375`, avg `-0.0032`, median `-0.0030`, brier `0.2634`, calibration_gap `0.1427`
- 10d: hit_rate `0.4375`, avg `-0.0128`, median `-0.0105`, brier `0.2632`, calibration_gap `0.1427`
- 20d: hit_rate `0.4375`, avg `-0.0177`, median `-0.0193`, brier `0.2650`, calibration_gap `0.1427`
- 60d: hit_rate `0.9375`, avg `0.0638`, median `0.0654`, brier `0.1874`, calibration_gap `-0.3573`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
