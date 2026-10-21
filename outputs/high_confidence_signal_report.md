# High Confidence Signal Report

Generated at: `2026-10-21T01:32:18.868335+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0130`, median `-0.0116`, brier `0.4727`, calibration_gap `0.6009`
- 5d: hit_rate `0.1250`, avg `-0.0167`, median `-0.0218`, brier `0.4700`, calibration_gap `0.6009`
- 10d: hit_rate `0.1250`, avg `-0.0159`, median `-0.0142`, brier `0.4727`, calibration_gap `0.6009`
- 20d: hit_rate `0.5000`, avg `0.0165`, median `0.0144`, brier `0.2971`, calibration_gap `0.2259`
- 60d: hit_rate `0.7500`, avg `0.0395`, median `0.0502`, brier `0.1851`, calibration_gap `-0.0241`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.2500`, avg `-0.0119`, median `-0.0116`, brier `0.4103`, calibration_gap `0.4698`
- 5d: hit_rate `0.3125`, avg `-0.0135`, median `-0.0207`, brier `0.3822`, calibration_gap `0.4073`
- 10d: hit_rate `0.3125`, avg `-0.0068`, median `-0.0082`, brier `0.3840`, calibration_gap `0.4073`
- 20d: hit_rate `0.6250`, avg `0.0225`, median `0.0255`, brier `0.2430`, calibration_gap `0.0948`
- 60d: hit_rate `0.7500`, avg `0.0552`, median `0.0639`, brier `0.1870`, calibration_gap `-0.0302`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0012`, median `0.0028`, brier `0.2587`, calibration_gap `0.1224`
- 5d: hit_rate `0.7000`, avg `0.0045`, median `0.0069`, brier `0.2094`, calibration_gap `-0.0276`
- 10d: hit_rate `0.7000`, avg `0.0099`, median `0.0092`, brier `0.2093`, calibration_gap `-0.0276`
- 20d: hit_rate `0.8000`, avg `0.0153`, median `0.0214`, brier `0.1756`, calibration_gap `-0.1276`
- 60d: hit_rate `0.5500`, avg `-0.0091`, median `0.0203`, brier `0.2607`, calibration_gap `0.1224`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0033`, median `0.0027`, brier `0.2572`, calibration_gap `0.0883`
- 5d: hit_rate `0.5000`, avg `-0.0030`, median `-0.0057`, brier `0.2737`, calibration_gap `0.1508`
- 10d: hit_rate `0.3750`, avg `-0.0110`, median `-0.0209`, brier `0.3110`, calibration_gap `0.2758`
- 20d: hit_rate `0.5000`, avg `-0.0047`, median `-0.0033`, brier `0.2747`, calibration_gap `0.1508`
- 60d: hit_rate `0.6875`, avg `0.0419`, median `0.0444`, brier `0.2185`, calibration_gap `-0.0367`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
