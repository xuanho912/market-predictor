# High Confidence Signal Report

Generated at: `2026-06-16T15:33:50.032973+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0019`, median `0.0041`, brier `0.2416`, calibration_gap `0.0897`
- 5d: hit_rate `0.2500`, avg `-0.0093`, median `-0.0157`, brier `0.3983`, calibration_gap `0.4647`
- 10d: hit_rate `0.7500`, avg `0.0061`, median `0.0075`, brier `0.1884`, calibration_gap `-0.0353`
- 20d: hit_rate `0.7500`, avg `0.0036`, median `0.0142`, brier `0.1842`, calibration_gap `-0.0353`
- 60d: hit_rate `0.5000`, avg `0.0071`, median `0.0049`, brier `0.2997`, calibration_gap `0.2147`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0038`, median `0.0002`, brier `0.2873`, calibration_gap `0.2025`
- 5d: hit_rate `0.3125`, avg `-0.0087`, median `-0.0104`, brier `0.3651`, calibration_gap `0.3900`
- 10d: hit_rate `0.8125`, avg `0.0093`, median `0.0103`, brier `0.1660`, calibration_gap `-0.1100`
- 20d: hit_rate `0.7500`, avg `0.0100`, median `0.0143`, brier `0.1878`, calibration_gap `-0.0475`
- 60d: hit_rate `0.5000`, avg `0.0076`, median `0.0064`, brier `0.2932`, calibration_gap `0.2025`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0049`, median `0.0058`, brier `0.2404`, calibration_gap `0.0385`
- 5d: hit_rate `0.6375`, avg `0.0072`, median `0.0062`, brier `0.2418`, calibration_gap `0.0260`
- 10d: hit_rate `0.6125`, avg `0.0079`, median `0.0094`, brier `0.2418`, calibration_gap `0.0510`
- 20d: hit_rate `0.7125`, avg `0.0105`, median `0.0184`, brier `0.2056`, calibration_gap `-0.0490`
- 60d: hit_rate `0.6250`, avg `0.0279`, median `0.0329`, brier `0.2410`, calibration_gap `0.0385`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0062`, median `0.0088`, brier `0.2345`, calibration_gap `0.0062`
- 5d: hit_rate `0.7500`, avg `0.0170`, median `0.0146`, brier `0.2026`, calibration_gap `-0.1188`
- 10d: hit_rate `0.6875`, avg `0.0089`, median `0.0185`, brier `0.2190`, calibration_gap `-0.0563`
- 20d: hit_rate `0.6875`, avg `0.0131`, median `0.0313`, brier `0.2178`, calibration_gap `-0.0563`
- 60d: hit_rate `0.8125`, avg `0.0518`, median `0.0636`, brier `0.1854`, calibration_gap `-0.1813`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
