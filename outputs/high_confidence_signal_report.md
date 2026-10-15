# High Confidence Signal Report

Generated at: `2026-10-15T08:37:05.627794+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0079`, median `-0.0001`, brier `0.3138`, calibration_gap `0.2439`
- 5d: hit_rate `0.6250`, avg `-0.0009`, median `0.0074`, brier `0.2523`, calibration_gap `0.1189`
- 10d: hit_rate `0.3750`, avg `-0.0041`, median `-0.0059`, brier `0.3730`, calibration_gap `0.3689`
- 20d: hit_rate `0.8750`, avg `0.0337`, median `0.0363`, brier `0.1249`, calibration_gap `-0.1311`
- 60d: hit_rate `1.0000`, avg `0.0617`, median `0.0501`, brier `0.0656`, calibration_gap `-0.2561`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0052`, median `-0.0001`, brier `0.3099`, calibration_gap `0.2392`
- 5d: hit_rate `0.5000`, avg `-0.0047`, median `-0.0007`, brier `0.3082`, calibration_gap `0.2392`
- 10d: hit_rate `0.4375`, avg `-0.0054`, median `-0.0039`, brier `0.3390`, calibration_gap `0.3017`
- 20d: hit_rate `0.6875`, avg `0.0258`, median `0.0289`, brier `0.2154`, calibration_gap `0.0517`
- 60d: hit_rate `0.8125`, avg `0.0441`, median `0.0463`, brier `0.1560`, calibration_gap `-0.0733`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `-0.0026`, median `0.0007`, brier `0.2786`, calibration_gap `0.1799`
- 5d: hit_rate `0.5000`, avg `-0.0070`, median `-0.0030`, brier `0.3021`, calibration_gap `0.2299`
- 10d: hit_rate `0.4500`, avg `-0.0050`, median `-0.0071`, brier `0.3240`, calibration_gap `0.2799`
- 20d: hit_rate `0.6000`, avg `0.0136`, median `0.0173`, brier `0.2554`, calibration_gap `0.1299`
- 60d: hit_rate `0.7500`, avg `0.0282`, median `0.0434`, brier `0.1873`, calibration_gap `-0.0201`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0089`, median `-0.0106`, brier `0.3390`, calibration_gap `0.3532`
- 5d: hit_rate `0.2500`, avg `-0.0147`, median `-0.0220`, brier `0.3618`, calibration_gap `0.4157`
- 10d: hit_rate `0.3750`, avg `-0.0110`, median `-0.0144`, brier `0.3188`, calibration_gap `0.2907`
- 20d: hit_rate `0.6250`, avg `0.0182`, median `0.0153`, brier `0.2373`, calibration_gap `0.0407`
- 60d: hit_rate `0.7500`, avg `0.0715`, median `0.0987`, brier `0.1968`, calibration_gap `-0.0843`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
