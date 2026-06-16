# High Confidence Signal Report

Generated at: `2026-06-16T14:42:19.010122+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0019`, median `0.0041`, brier `0.2420`, calibration_gap `0.0880`
- 5d: hit_rate `0.2500`, avg `-0.0093`, median `-0.0157`, brier `0.3970`, calibration_gap `0.4630`
- 10d: hit_rate `0.7500`, avg `0.0061`, median `0.0075`, brier `0.1881`, calibration_gap `-0.0370`
- 20d: hit_rate `0.7500`, avg `0.0036`, median `0.0142`, brier `0.1840`, calibration_gap `-0.0370`
- 60d: hit_rate `0.5000`, avg `0.0071`, median `0.0049`, brier `0.2998`, calibration_gap `0.2130`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0027`, median `0.0002`, brier `0.2869`, calibration_gap `0.2009`
- 5d: hit_rate `0.3125`, avg `-0.0069`, median `-0.0075`, brier `0.3636`, calibration_gap `0.3884`
- 10d: hit_rate `0.7500`, avg `0.0074`, median `0.0075`, brier `0.1890`, calibration_gap `-0.0491`
- 20d: hit_rate `0.8125`, avg `0.0118`, median `0.0190`, brier `0.1650`, calibration_gap `-0.1116`
- 60d: hit_rate `0.5000`, avg `0.0102`, median `0.0064`, brier `0.2934`, calibration_gap `0.2009`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0047`, median `0.0051`, brier `0.2406`, calibration_gap `0.0367`
- 5d: hit_rate `0.6375`, avg `0.0060`, median `0.0056`, brier `0.2405`, calibration_gap `0.0242`
- 10d: hit_rate `0.6000`, avg `0.0074`, median `0.0083`, brier `0.2441`, calibration_gap `0.0617`
- 20d: hit_rate `0.6875`, avg `0.0091`, median `0.0171`, brier `0.2125`, calibration_gap `-0.0258`
- 60d: hit_rate `0.6125`, avg `0.0281`, median `0.0329`, brier `0.2441`, calibration_gap `0.0492`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0059`, median `0.0086`, brier `0.2342`, calibration_gap `0.0036`
- 5d: hit_rate `0.6875`, avg `0.0116`, median `0.0100`, brier `0.2186`, calibration_gap `-0.0589`
- 10d: hit_rate `0.6250`, avg `0.0099`, median `0.0185`, brier `0.2348`, calibration_gap `0.0036`
- 20d: hit_rate `0.6250`, avg `0.0123`, median `0.0200`, brier `0.2338`, calibration_gap `0.0036`
- 60d: hit_rate `0.7500`, avg `0.0513`, median `0.0577`, brier `0.2021`, calibration_gap `-0.1214`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
