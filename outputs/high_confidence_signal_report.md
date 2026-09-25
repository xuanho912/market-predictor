# High Confidence Signal Report

Generated at: `2026-09-25T01:34:22.878554+00:00`

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
- sample_size: `80`
- 3d: hit_rate `0.4875`, avg `-0.0023`, median `-0.0011`, brier `0.2975`, calibration_gap `0.2138`
- 5d: hit_rate `0.5250`, avg `-0.0030`, median `0.0009`, brier `0.2875`, calibration_gap `0.1763`
- 10d: hit_rate `0.6000`, avg `0.0001`, median `0.0061`, brier `0.2660`, calibration_gap `0.1013`
- 20d: hit_rate `0.6750`, avg `0.0152`, median `0.0204`, brier `0.2303`, calibration_gap `0.0263`
- 60d: hit_rate `0.8750`, avg `0.0620`, median `0.0791`, brier `0.1471`, calibration_gap `-0.1737`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0027`, median `0.0077`, brier `0.2580`, calibration_gap `0.0542`
- 5d: hit_rate `0.6875`, avg `0.0052`, median `0.0046`, brier `0.2220`, calibration_gap `-0.0708`
- 10d: hit_rate `0.7500`, avg `0.0090`, median `0.0129`, brier `0.2112`, calibration_gap `-0.1333`
- 20d: hit_rate `0.8750`, avg `0.0229`, median `0.0228`, brier `0.1835`, calibration_gap `-0.2583`
- 60d: hit_rate `0.9375`, avg `0.0652`, median `0.0833`, brier `0.1657`, calibration_gap `-0.3208`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
