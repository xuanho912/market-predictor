# High Confidence Signal Report

Generated at: `2026-06-22T17:42:40.053819+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0060`, median `-0.0061`, brier `0.3627`, calibration_gap `0.3541`
- 5d: hit_rate `0.0000`, avg `-0.0182`, median `-0.0150`, brier `0.5316`, calibration_gap `0.7291`
- 10d: hit_rate `0.6250`, avg `0.0048`, median `0.0061`, brier `0.2452`, calibration_gap `0.1041`
- 20d: hit_rate `1.0000`, avg `0.0281`, median `0.0302`, brier `0.0735`, calibration_gap `-0.2709`
- 60d: hit_rate `1.0000`, avg `0.0760`, median `0.0869`, brier `0.0735`, calibration_gap `-0.2709`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0022`, median `-0.0001`, brier `0.3025`, calibration_gap `0.2216`
- 5d: hit_rate `0.2500`, avg `-0.0123`, median `-0.0130`, brier `0.4133`, calibration_gap `0.4716`
- 10d: hit_rate `0.3750`, avg `-0.0008`, median `-0.0016`, brier `0.3516`, calibration_gap `0.3466`
- 20d: hit_rate `0.9375`, avg `0.0263`, median `0.0290`, brier `0.1039`, calibration_gap `-0.2159`
- 60d: hit_rate `0.9375`, avg `0.0689`, median `0.0832`, brier `0.1037`, calibration_gap `-0.2159`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4500`, avg `-0.0009`, median `-0.0016`, brier `0.3032`, calibration_gap `0.2274`
- 5d: hit_rate `0.4667`, avg `-0.0035`, median `-0.0054`, brier `0.3037`, calibration_gap `0.2107`
- 10d: hit_rate `0.4000`, avg `-0.0025`, median `-0.0022`, brier `0.3209`, calibration_gap `0.2774`
- 20d: hit_rate `0.7667`, avg `0.0115`, median `0.0191`, brier `0.1795`, calibration_gap `-0.0893`
- 60d: hit_rate `0.6333`, avg `0.0247`, median `0.0400`, brier `0.2283`, calibration_gap `0.0440`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0022`, median `0.0028`, brier `0.2349`, calibration_gap `-0.0053`
- 5d: hit_rate `0.6250`, avg `0.0001`, median `0.0043`, brier `0.2348`, calibration_gap `-0.0053`
- 10d: hit_rate `0.4375`, avg `-0.0010`, median `-0.0035`, brier `0.2791`, calibration_gap `0.1822`
- 20d: hit_rate `0.6250`, avg `0.0084`, median `0.0099`, brier `0.2351`, calibration_gap `-0.0053`
- 60d: hit_rate `0.6250`, avg `0.0205`, median `0.0557`, brier `0.2347`, calibration_gap `-0.0053`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
