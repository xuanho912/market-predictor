# High Confidence Signal Report

Generated at: `2026-07-30T22:42:08.610930+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0164`, median `-0.0096`, brier `0.4697`, calibration_gap `0.5332`
- 5d: hit_rate `0.5000`, avg `-0.0135`, median `-0.0018`, brier `0.3271`, calibration_gap `0.2832`
- 10d: hit_rate `0.0000`, avg `-0.0141`, median `-0.0129`, brier `0.6135`, calibration_gap `0.7832`
- 20d: hit_rate `0.3750`, avg `-0.0083`, median `-0.0120`, brier `0.3958`, calibration_gap `0.4082`
- 60d: hit_rate `0.3750`, avg `-0.0089`, median `-0.0108`, brier `0.3958`, calibration_gap `0.4082`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0103`, median `-0.0092`, brier `0.3610`, calibration_gap `0.3349`
- 5d: hit_rate `0.5000`, avg `-0.0116`, median `-0.0020`, brier `0.3226`, calibration_gap `0.2724`
- 10d: hit_rate `0.2500`, avg `-0.0061`, median `-0.0101`, brier `0.4667`, calibration_gap `0.5224`
- 20d: hit_rate `0.5000`, avg `0.0034`, median `-0.0005`, brier `0.3241`, calibration_gap `0.2724`
- 60d: hit_rate `0.5625`, avg `0.0224`, median `0.0225`, brier `0.2909`, calibration_gap `0.2099`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `0.0032`, median `0.0034`, brier `0.2552`, calibration_gap `0.0990`
- 5d: hit_rate `0.5833`, avg `0.0037`, median `0.0034`, brier `0.2674`, calibration_gap `0.1323`
- 10d: hit_rate `0.5500`, avg `0.0072`, median `0.0079`, brier `0.2893`, calibration_gap `0.1657`
- 20d: hit_rate `0.7833`, avg `0.0233`, median `0.0339`, brier `0.1860`, calibration_gap `-0.0677`
- 60d: hit_rate `0.6500`, avg `0.0227`, median `0.0449`, brier `0.2366`, calibration_gap `0.0657`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0081`, median `0.0099`, brier `0.1707`, calibration_gap `-0.1360`
- 5d: hit_rate `0.5625`, avg `0.0069`, median `0.0091`, brier `0.2602`, calibration_gap `0.1140`
- 10d: hit_rate `0.6875`, avg `0.0111`, median `0.0172`, brier `0.2169`, calibration_gap `-0.0110`
- 20d: hit_rate `1.0000`, avg `0.0406`, median `0.0398`, brier `0.1046`, calibration_gap `-0.3235`
- 60d: hit_rate `0.7500`, avg `0.0395`, median `0.0460`, brier `0.1928`, calibration_gap `-0.0735`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
