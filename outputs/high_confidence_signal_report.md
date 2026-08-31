# High Confidence Signal Report

Generated at: `2026-08-31T19:11:00.324433+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0018`, median `0.0012`, brier `0.1920`, calibration_gap `0.0311`
- 5d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0029`, brier `0.3259`, calibration_gap `0.2811`
- 10d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0073`, brier `0.4074`, calibration_gap `0.4061`
- 20d: hit_rate `0.6250`, avg `0.0123`, median `0.0166`, brier `0.2607`, calibration_gap `0.1561`
- 60d: hit_rate `0.8750`, avg `0.0486`, median `0.0588`, brier `0.1187`, calibration_gap `-0.0939`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0045`, median `-0.0015`, brier `0.3534`, calibration_gap `0.3335`
- 5d: hit_rate `0.5000`, avg `-0.0044`, median `-0.0029`, brier `0.3223`, calibration_gap `0.2710`
- 10d: hit_rate `0.3750`, avg `-0.0053`, median `-0.0109`, brier `0.3954`, calibration_gap `0.3960`
- 20d: hit_rate `0.6250`, avg `0.0038`, median `0.0166`, brier `0.2567`, calibration_gap `0.1460`
- 60d: hit_rate `0.7500`, avg `0.0305`, median `0.0396`, brier `0.1854`, calibration_gap `0.0210`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5167`, avg `0.0000`, median `0.0007`, brier `0.2944`, calibration_gap `0.2099`
- 5d: hit_rate `0.4667`, avg `-0.0023`, median `-0.0053`, brier `0.3158`, calibration_gap `0.2599`
- 10d: hit_rate `0.4000`, avg `0.0016`, median `-0.0069`, brier `0.3479`, calibration_gap `0.3265`
- 20d: hit_rate `0.7000`, avg `0.0114`, median `0.0205`, brier `0.2114`, calibration_gap `0.0265`
- 60d: hit_rate `0.7667`, avg `0.0486`, median `0.0620`, brier `0.1850`, calibration_gap `-0.0401`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0034`, median `-0.0014`, brier `0.2786`, calibration_gap `0.1776`
- 5d: hit_rate `0.3750`, avg `-0.0048`, median `-0.0103`, brier `0.3231`, calibration_gap `0.3026`
- 10d: hit_rate `0.3750`, avg `-0.0015`, median `-0.0092`, brier `0.3275`, calibration_gap `0.3026`
- 20d: hit_rate `0.6250`, avg `0.0107`, median `0.0072`, brier `0.2403`, calibration_gap `0.0526`
- 60d: hit_rate `0.8750`, avg `0.0664`, median `0.0590`, brier `0.1502`, calibration_gap `-0.1974`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
