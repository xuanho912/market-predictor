# High Confidence Signal Report

Generated at: `2026-11-06T19:27:59.547575+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0177`, median `0.0283`, brier `0.1928`, calibration_gap `0.0442`
- 5d: hit_rate `0.8750`, avg `0.0183`, median `0.0143`, brier `0.1187`, calibration_gap `-0.0808`
- 10d: hit_rate `0.6250`, avg `0.0129`, median `0.0341`, brier `0.2655`, calibration_gap `0.1692`
- 20d: hit_rate `0.7500`, avg `0.0110`, median `0.0278`, brier `0.1928`, calibration_gap `0.0442`
- 60d: hit_rate `0.8750`, avg `0.0566`, median `0.0682`, brier `0.1166`, calibration_gap `-0.0808`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0093`, median `0.0105`, brier `0.2605`, calibration_gap `0.1605`
- 5d: hit_rate `0.6250`, avg `0.0111`, median `0.0129`, brier `0.2570`, calibration_gap `0.1605`
- 10d: hit_rate `0.5000`, avg `0.0099`, median `0.0038`, brier `0.3304`, calibration_gap `0.2855`
- 20d: hit_rate `0.8125`, avg `0.0181`, median `0.0262`, brier `0.1562`, calibration_gap `-0.0270`
- 60d: hit_rate `0.9375`, avg `0.0730`, median `0.0738`, brier `0.0832`, calibration_gap `-0.1520`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0081`, median `0.0110`, brier `0.2419`, calibration_gap `0.1165`
- 5d: hit_rate `0.6250`, avg `0.0112`, median `0.0127`, brier `0.2543`, calibration_gap `0.1415`
- 10d: hit_rate `0.6000`, avg `0.0157`, median `0.0146`, brier `0.2707`, calibration_gap `0.1665`
- 20d: hit_rate `0.8000`, avg `0.0295`, median `0.0345`, brier `0.1616`, calibration_gap `-0.0335`
- 60d: hit_rate `0.8750`, avg `0.0595`, median `0.0705`, brier `0.1198`, calibration_gap `-0.1085`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0030`, median `0.0024`, brier `0.2509`, calibration_gap `0.0531`
- 5d: hit_rate `0.5625`, avg `0.0044`, median `0.0093`, brier `0.2488`, calibration_gap `0.0531`
- 10d: hit_rate `0.7500`, avg `0.0156`, median `0.0237`, brier `0.2053`, calibration_gap `-0.1344`
- 20d: hit_rate `0.6250`, avg `0.0349`, median `0.0464`, brier `0.2327`, calibration_gap `-0.0094`
- 60d: hit_rate `0.7500`, avg `0.0384`, median `0.0398`, brier `0.2053`, calibration_gap `-0.1344`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
