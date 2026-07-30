# High Confidence Signal Report

Generated at: `2026-07-30T14:35:01.848058+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0112`, median `-0.0044`, brier `0.3381`, calibration_gap `0.2927`
- 5d: hit_rate `0.6250`, avg `-0.0150`, median `0.0010`, brier `0.2621`, calibration_gap `0.1677`
- 10d: hit_rate `0.2500`, avg `-0.0048`, median `-0.0074`, brier `0.4849`, calibration_gap `0.5427`
- 20d: hit_rate `0.3750`, avg `-0.0002`, median `-0.0044`, brier `0.4071`, calibration_gap `0.4177`
- 60d: hit_rate `0.5000`, avg `0.0130`, median `0.0045`, brier `0.3340`, calibration_gap `0.2927`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0078`, median `-0.0044`, brier `0.3348`, calibration_gap `0.2853`
- 5d: hit_rate `0.5000`, avg `-0.0109`, median `-0.0009`, brier `0.3290`, calibration_gap `0.2853`
- 10d: hit_rate `0.1875`, avg `-0.0089`, median `-0.0101`, brier `0.5111`, calibration_gap `0.5978`
- 20d: hit_rate `0.5000`, avg `0.0039`, median `-0.0005`, brier `0.3332`, calibration_gap `0.2853`
- 60d: hit_rate `0.5625`, avg `0.0259`, median `0.0225`, brier `0.2957`, calibration_gap `0.2228`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0036`, median `0.0070`, brier `0.2406`, calibration_gap `0.0868`
- 5d: hit_rate `0.5750`, avg `0.0014`, median `0.0021`, brier `0.2717`, calibration_gap `0.1618`
- 10d: hit_rate `0.4750`, avg `0.0052`, median `-0.0003`, brier `0.3327`, calibration_gap `0.2618`
- 20d: hit_rate `0.8000`, avg `0.0309`, median `0.0371`, brier `0.1799`, calibration_gap `-0.0632`
- 60d: hit_rate `0.7250`, avg `0.0481`, median `0.0648`, brier `0.2107`, calibration_gap `0.0118`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0046`, median `0.0058`, brier `0.1907`, calibration_gap `-0.0659`
- 5d: hit_rate `0.5000`, avg `0.0041`, median `0.0022`, brier `0.2824`, calibration_gap `0.1841`
- 10d: hit_rate `0.5625`, avg `0.0070`, median `0.0220`, brier `0.2622`, calibration_gap `0.1216`
- 20d: hit_rate `0.8750`, avg `0.0211`, median `0.0189`, brier `0.1463`, calibration_gap `-0.1909`
- 60d: hit_rate `0.5625`, avg `0.0044`, median `0.0211`, brier `0.2622`, calibration_gap `0.1216`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
