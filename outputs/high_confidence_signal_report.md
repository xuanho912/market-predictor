# High Confidence Signal Report

Generated at: `2026-09-23T17:03:03.175573+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0072`, median `-0.0104`, brier `0.4185`, calibration_gap `0.4320`
- 5d: hit_rate `0.3750`, avg `-0.0103`, median `-0.0166`, brier `0.4185`, calibration_gap `0.4320`
- 10d: hit_rate `0.5000`, avg `-0.0078`, median `-0.0048`, brier `0.3470`, calibration_gap `0.3070`
- 20d: hit_rate `0.6250`, avg `0.0180`, median `0.0173`, brier `0.2668`, calibration_gap `0.1820`
- 60d: hit_rate `0.7500`, avg `0.0221`, median `0.0177`, brier `0.1878`, calibration_gap `0.0570`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0041`, median `-0.0033`, brier `0.3403`, calibration_gap `0.2988`
- 5d: hit_rate `0.5000`, avg `-0.0060`, median `-0.0054`, brier `0.3403`, calibration_gap `0.2988`
- 10d: hit_rate `0.5000`, avg `-0.0103`, median `-0.0048`, brier `0.3414`, calibration_gap `0.2988`
- 20d: hit_rate `0.6875`, avg `0.0165`, median `0.0240`, brier `0.2285`, calibration_gap `0.1113`
- 60d: hit_rate `0.7500`, avg `0.0235`, median `0.0378`, brier `0.1891`, calibration_gap `0.0488`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4833`, avg `-0.0045`, median `-0.0014`, brier `0.3202`, calibration_gap `0.2493`
- 5d: hit_rate `0.4667`, avg `-0.0087`, median `-0.0030`, brier `0.3289`, calibration_gap `0.2660`
- 10d: hit_rate `0.4000`, avg `-0.0058`, median `-0.0070`, brier `0.3653`, calibration_gap `0.3326`
- 20d: hit_rate `0.6000`, avg `0.0099`, median `0.0164`, brier `0.2584`, calibration_gap `0.1326`
- 60d: hit_rate `0.7000`, avg `0.0220`, median `0.0343`, brier `0.2149`, calibration_gap `0.0326`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0024`, median `0.0040`, brier `0.2410`, calibration_gap `0.0386`
- 5d: hit_rate `0.6875`, avg `0.0028`, median `0.0028`, brier `0.2186`, calibration_gap `-0.0239`
- 10d: hit_rate `0.7500`, avg `0.0091`, median `0.0154`, brier `0.1981`, calibration_gap `-0.0864`
- 20d: hit_rate `0.5625`, avg `0.0139`, median `0.0068`, brier `0.2560`, calibration_gap `0.1011`
- 60d: hit_rate `0.8750`, avg `0.0406`, median `0.0501`, brier `0.1520`, calibration_gap `-0.2114`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
