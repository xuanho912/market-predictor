# High Confidence Signal Report

Generated at: `2026-10-17T15:39:22.244666+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0135`, median `0.0143`, brier `0.1888`, calibration_gap `-0.0010`
- 5d: hit_rate `1.0000`, avg `0.0128`, median `0.0088`, brier `0.0630`, calibration_gap `-0.2510`
- 10d: hit_rate `0.5000`, avg `0.0069`, median `0.0053`, brier `0.3141`, calibration_gap `0.2490`
- 20d: hit_rate `0.8750`, avg `0.0340`, median `0.0411`, brier `0.1246`, calibration_gap `-0.1260`
- 60d: hit_rate `0.7500`, avg `0.0530`, median `0.0671`, brier `0.1870`, calibration_gap `-0.0010`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0013`, median `0.0048`, brier `0.2770`, calibration_gap `0.1807`
- 5d: hit_rate `0.6875`, avg `0.0001`, median `0.0030`, brier `0.2141`, calibration_gap `0.0557`
- 10d: hit_rate `0.3750`, avg `0.0002`, median `-0.0036`, brier `0.3690`, calibration_gap `0.3682`
- 20d: hit_rate `0.7500`, avg `0.0266`, median `0.0348`, brier `0.1854`, calibration_gap `-0.0068`
- 60d: hit_rate `0.6875`, avg `0.0501`, median `0.0635`, brier `0.2166`, calibration_gap `0.0557`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5250`, avg `-0.0001`, median `0.0011`, brier `0.2862`, calibration_gap `0.1951`
- 5d: hit_rate `0.7000`, avg `0.0010`, median `0.0037`, brier `0.2090`, calibration_gap `0.0201`
- 10d: hit_rate `0.5000`, avg `0.0025`, median `-0.0001`, brier `0.3025`, calibration_gap `0.2201`
- 20d: hit_rate `0.7250`, avg `0.0225`, median `0.0277`, brier `0.1980`, calibration_gap `-0.0049`
- 60d: hit_rate `0.5750`, avg `0.0286`, median `0.0477`, brier `0.2630`, calibration_gap `0.1451`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0015`, median `0.0045`, brier `0.2591`, calibration_gap `0.0973`
- 5d: hit_rate `0.5000`, avg `-0.0007`, median `-0.0034`, brier `0.2813`, calibration_gap `0.1598`
- 10d: hit_rate `0.5000`, avg `0.0157`, median `0.0007`, brier `0.2813`, calibration_gap `0.1598`
- 20d: hit_rate `0.6250`, avg `0.0302`, median `0.0359`, brier `0.2403`, calibration_gap `0.0348`
- 60d: hit_rate `0.7500`, avg `0.0669`, median `0.1146`, brier `0.2030`, calibration_gap `-0.0902`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
