# High Confidence Signal Report

Generated at: `2026-09-24T23:17:58.782993+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0064`, median `0.0085`, brier `0.1910`, calibration_gap `0.0836`
- 5d: hit_rate `0.7500`, avg `0.0022`, median `0.0068`, brier `0.1910`, calibration_gap `0.0836`
- 10d: hit_rate `0.6250`, avg `-0.0008`, median `0.0041`, brier `0.2882`, calibration_gap `0.2086`
- 20d: hit_rate `0.7500`, avg `0.0247`, median `0.0324`, brier `0.1977`, calibration_gap `0.0836`
- 60d: hit_rate `1.0000`, avg `0.0540`, median `0.0565`, brier `0.0279`, calibration_gap `-0.1664`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0022`, median `0.0085`, brier `0.2691`, calibration_gap `0.1968`
- 5d: hit_rate `0.5625`, avg `-0.0029`, median `0.0056`, brier `0.3073`, calibration_gap `0.2593`
- 10d: hit_rate `0.5000`, avg `-0.0118`, median `-0.0047`, brier `0.3559`, calibration_gap `0.3218`
- 20d: hit_rate `0.6875`, avg `0.0116`, median `0.0173`, brier `0.2329`, calibration_gap `0.1343`
- 60d: hit_rate `0.8750`, avg `0.0502`, median `0.0614`, brier `0.1098`, calibration_gap `-0.0532`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4333`, avg `-0.0049`, median `-0.0037`, brier `0.3189`, calibration_gap `0.2889`
- 5d: hit_rate `0.4833`, avg `-0.0067`, median `-0.0036`, brier `0.3067`, calibration_gap `0.2389`
- 10d: hit_rate `0.5500`, avg `-0.0044`, median `0.0049`, brier `0.2847`, calibration_gap `0.1722`
- 20d: hit_rate `0.6333`, avg `0.0085`, median `0.0156`, brier `0.2417`, calibration_gap `0.0889`
- 60d: hit_rate `0.8333`, avg `0.0496`, median `0.0557`, brier `0.1520`, calibration_gap `-0.1111`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0020`, median `-0.0025`, brier `0.2964`, calibration_gap `0.2183`
- 5d: hit_rate `0.5625`, avg `-0.0020`, median `0.0008`, brier `0.2575`, calibration_gap `0.0933`
- 10d: hit_rate `0.6875`, avg `0.0033`, median `0.0081`, brier `0.2184`, calibration_gap `-0.0317`
- 20d: hit_rate `0.6250`, avg `-0.0008`, median `0.0121`, brier `0.2361`, calibration_gap `0.0308`
- 60d: hit_rate `0.8750`, avg `0.0364`, median `0.0386`, brier `0.1560`, calibration_gap `-0.2192`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
