# High Confidence Signal Report

Generated at: `2026-10-21T01:12:27.759199+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0035`, median `0.0074`, brier `0.1978`, calibration_gap `-0.0907`
- 5d: hit_rate `0.8750`, avg `0.0099`, median `0.0107`, brier `0.1516`, calibration_gap `-0.2157`
- 10d: hit_rate `0.7500`, avg `0.0119`, median `0.0162`, brier `0.1978`, calibration_gap `-0.0907`
- 20d: hit_rate `1.0000`, avg `0.0403`, median `0.0384`, brier `0.1164`, calibration_gap `-0.3407`
- 60d: hit_rate `1.0000`, avg `0.1020`, median `0.0982`, brier `0.1164`, calibration_gap `-0.3407`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0049`, median `0.0074`, brier `0.2150`, calibration_gap `-0.0425`
- 5d: hit_rate `0.7500`, avg `0.0063`, median `0.0107`, brier `0.1908`, calibration_gap `-0.1050`
- 10d: hit_rate `0.6250`, avg `0.0098`, median `0.0140`, brier `0.2301`, calibration_gap `0.0200`
- 20d: hit_rate `0.9375`, avg `0.0432`, median `0.0384`, brier `0.1439`, calibration_gap `-0.2925`
- 60d: hit_rate `0.8750`, avg `0.0879`, median `0.0982`, brier `0.1574`, calibration_gap `-0.2300`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0056`, median `0.0092`, brier `0.2219`, calibration_gap `-0.0425`
- 5d: hit_rate `0.6500`, avg `0.0074`, median `0.0107`, brier `0.2167`, calibration_gap `-0.0425`
- 10d: hit_rate `0.6500`, avg `0.0089`, median `0.0183`, brier `0.2240`, calibration_gap `-0.0425`
- 20d: hit_rate `0.8000`, avg `0.0261`, median `0.0322`, brier `0.1867`, calibration_gap `-0.1925`
- 60d: hit_rate `0.8750`, avg `0.0646`, median `0.0696`, brier `0.1789`, calibration_gap `-0.2675`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0014`, median `-0.0040`, brier `0.2504`, calibration_gap `0.0327`
- 5d: hit_rate `0.3750`, avg `-0.0063`, median `-0.0150`, brier `0.2624`, calibration_gap `0.1577`
- 10d: hit_rate `0.4375`, avg `-0.0075`, median `-0.0111`, brier `0.2535`, calibration_gap `0.0952`
- 20d: hit_rate `0.6250`, avg `0.0190`, median `0.0280`, brier `0.2455`, calibration_gap `-0.0923`
- 60d: hit_rate `0.8125`, avg `0.0857`, median `0.1140`, brier `0.2335`, calibration_gap `-0.2798`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
