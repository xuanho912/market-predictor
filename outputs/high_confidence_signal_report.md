# High Confidence Signal Report

Generated at: `2026-06-17T00:01:27.116796+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0019`, median `0.0041`, brier `0.2412`, calibration_gap `0.0913`
- 5d: hit_rate `0.2500`, avg `-0.0093`, median `-0.0157`, brier `0.4005`, calibration_gap `0.4663`
- 10d: hit_rate `0.7500`, avg `0.0061`, median `0.0075`, brier `0.1877`, calibration_gap `-0.0337`
- 20d: hit_rate `0.7500`, avg `0.0036`, median `0.0142`, brier `0.1835`, calibration_gap `-0.0337`
- 60d: hit_rate `0.5000`, avg `0.0071`, median `0.0049`, brier `0.2982`, calibration_gap `0.2163`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0030`, median `0.0002`, brier `0.2898`, calibration_gap `0.2059`
- 5d: hit_rate `0.2500`, avg `-0.0100`, median `-0.0130`, brier `0.3934`, calibration_gap `0.4559`
- 10d: hit_rate `0.7500`, avg `0.0078`, median `0.0075`, brier `0.1885`, calibration_gap `-0.0441`
- 20d: hit_rate `0.7500`, avg `0.0105`, median `0.0177`, brier `0.1867`, calibration_gap `-0.0441`
- 60d: hit_rate `0.5625`, avg `0.0160`, median `0.0313`, brier `0.2684`, calibration_gap `0.1434`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6500`, avg `0.0059`, median `0.0067`, brier `0.2322`, calibration_gap `0.0157`
- 5d: hit_rate `0.6500`, avg `0.0071`, median `0.0069`, brier `0.2376`, calibration_gap `0.0157`
- 10d: hit_rate `0.6500`, avg `0.0111`, median `0.0129`, brier `0.2302`, calibration_gap `0.0157`
- 20d: hit_rate `0.7625`, avg `0.0172`, median `0.0206`, brier `0.1900`, calibration_gap `-0.0968`
- 60d: hit_rate `0.6375`, avg `0.0335`, median `0.0399`, brier `0.2349`, calibration_gap `0.0282`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0042`, median `0.0067`, brier `0.2169`, calibration_gap `-0.0543`
- 5d: hit_rate `0.7500`, avg `0.0141`, median `0.0190`, brier `0.2005`, calibration_gap `-0.1168`
- 10d: hit_rate `0.8750`, avg `0.0247`, median `0.0222`, brier `0.1685`, calibration_gap `-0.2418`
- 20d: hit_rate `0.8750`, avg `0.0388`, median `0.0517`, brier `0.1678`, calibration_gap `-0.2418`
- 60d: hit_rate `0.8125`, avg `0.0684`, median `0.0708`, brier `0.1841`, calibration_gap `-0.1793`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
