# High Confidence Signal Report

Generated at: `2026-10-20T01:30:49.249399+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0029`, median `0.0079`, brier `0.2492`, calibration_gap `0.0536`
- 5d: hit_rate `0.7500`, avg `0.0058`, median `0.0088`, brier `0.1879`, calibration_gap `-0.0714`
- 10d: hit_rate `0.5000`, avg `0.0014`, median `-0.0000`, brier `0.2885`, calibration_gap `0.1786`
- 20d: hit_rate `1.0000`, avg `0.0517`, median `0.0525`, brier `0.1038`, calibration_gap `-0.3214`
- 60d: hit_rate `0.7500`, avg `0.0807`, median `0.1108`, brier `0.1828`, calibration_gap `-0.0714`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0010`, median `0.0030`, brier `0.2611`, calibration_gap `0.0965`
- 5d: hit_rate `0.6875`, avg `0.0036`, median `0.0088`, brier `0.2129`, calibration_gap `-0.0285`
- 10d: hit_rate `0.5625`, avg `0.0034`, median `0.0057`, brier `0.2633`, calibration_gap `0.0965`
- 20d: hit_rate `0.9375`, avg `0.0412`, median `0.0414`, brier `0.1350`, calibration_gap `-0.2785`
- 60d: hit_rate `0.8750`, avg `0.0826`, median `0.0914`, brier `0.1565`, calibration_gap `-0.2160`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.7000`, avg `0.0059`, median `0.0074`, brier `0.2198`, calibration_gap `-0.0754`
- 5d: hit_rate `0.6750`, avg `0.0082`, median `0.0118`, brier `0.2193`, calibration_gap `-0.0504`
- 10d: hit_rate `0.7500`, avg `0.0123`, median `0.0165`, brier `0.2082`, calibration_gap `-0.1254`
- 20d: hit_rate `0.8500`, avg `0.0328`, median `0.0342`, brier `0.1739`, calibration_gap `-0.2254`
- 60d: hit_rate `0.9250`, avg `0.0769`, median `0.0843`, brier `0.1638`, calibration_gap `-0.3004`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `0.0012`, median `-0.0093`, brier `0.2639`, calibration_gap `0.1647`
- 5d: hit_rate `0.5000`, avg `0.0061`, median `0.0002`, brier `0.2526`, calibration_gap `0.0397`
- 10d: hit_rate `0.5625`, avg `0.0073`, median `0.0184`, brier `0.2481`, calibration_gap `-0.0228`
- 20d: hit_rate `0.6250`, avg `0.0280`, median `0.0369`, brier `0.2454`, calibration_gap `-0.0853`
- 60d: hit_rate `1.0000`, avg `0.1382`, median `0.1262`, brier `0.2120`, calibration_gap `-0.4603`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
