# High Confidence Signal Report

Generated at: `2026-06-24T23:47:20.528717+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0007`, median `-0.0013`, brier `0.3816`, calibration_gap `0.3834`
- 5d: hit_rate `0.1250`, avg `-0.0108`, median `-0.0108`, brier `0.5112`, calibration_gap `0.6334`
- 10d: hit_rate `0.5000`, avg `0.0046`, median `0.0022`, brier `0.3147`, calibration_gap `0.2584`
- 20d: hit_rate `0.8750`, avg `0.0247`, median `0.0287`, brier `0.1247`, calibration_gap `-0.1166`
- 60d: hit_rate `1.0000`, avg `0.0821`, median `0.0936`, brier `0.0584`, calibration_gap `-0.2416`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0025`, median `0.0004`, brier `0.3142`, calibration_gap `0.2485`
- 5d: hit_rate `0.2500`, avg `-0.0073`, median `-0.0077`, brier `0.4380`, calibration_gap `0.4985`
- 10d: hit_rate `0.4375`, avg `0.0039`, median `-0.0014`, brier `0.3406`, calibration_gap `0.3110`
- 20d: hit_rate `0.9375`, avg `0.0238`, median `0.0265`, brier `0.0965`, calibration_gap `-0.1890`
- 60d: hit_rate `1.0000`, avg `0.0752`, median `0.0745`, brier `0.0634`, calibration_gap `-0.2515`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0037`, median `0.0043`, brier `0.2557`, calibration_gap `0.0767`
- 5d: hit_rate `0.5750`, avg `0.0023`, median `0.0067`, brier `0.2464`, calibration_gap `0.0517`
- 10d: hit_rate `0.5250`, avg `0.0042`, median `0.0016`, brier `0.2637`, calibration_gap `0.1017`
- 20d: hit_rate `0.7250`, avg `0.0186`, median `0.0306`, brier `0.2087`, calibration_gap `-0.0983`
- 60d: hit_rate `0.8000`, avg `0.0569`, median `0.0705`, brier `0.1907`, calibration_gap `-0.1733`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0039`, median `0.0050`, brier `0.2489`, calibration_gap `0.0414`
- 5d: hit_rate `0.6250`, avg `0.0002`, median `0.0100`, brier `0.2355`, calibration_gap `-0.0211`
- 10d: hit_rate `0.5625`, avg `0.0082`, median `0.0040`, brier `0.2497`, calibration_gap `0.0414`
- 20d: hit_rate `0.7500`, avg `0.0215`, median `0.0398`, brier `0.2070`, calibration_gap `-0.1461`
- 60d: hit_rate `0.8750`, avg `0.0728`, median `0.0743`, brier `0.1819`, calibration_gap `-0.2711`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
