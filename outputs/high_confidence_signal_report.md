# High Confidence Signal Report

Generated at: `2026-07-13T15:14:46.201845+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0180`, median `-0.0165`, brier `0.4746`, calibration_gap `0.6033`
- 5d: hit_rate `0.0000`, avg `-0.0250`, median `-0.0206`, brier `0.5305`, calibration_gap `0.7283`
- 10d: hit_rate `0.3750`, avg `-0.0118`, median `-0.0206`, brier `0.3637`, calibration_gap `0.3533`
- 20d: hit_rate `0.8750`, avg `0.0057`, median `0.0095`, brier `0.1285`, calibration_gap `-0.1467`
- 60d: hit_rate `0.3750`, avg `-0.0066`, median `-0.0128`, brier `0.3571`, calibration_gap `0.3533`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0095`, median `-0.0079`, brier `0.3589`, calibration_gap `0.3462`
- 5d: hit_rate `0.2500`, avg `-0.0143`, median `-0.0137`, brier `0.4132`, calibration_gap `0.4712`
- 10d: hit_rate `0.3125`, avg `-0.0090`, median `-0.0180`, brier `0.3832`, calibration_gap `0.4087`
- 20d: hit_rate `0.8125`, avg `0.0136`, median `0.0095`, brier `0.1587`, calibration_gap `-0.0913`
- 60d: hit_rate `0.6250`, avg `0.0321`, median `0.0528`, brier `0.2462`, calibration_gap `0.0962`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5000`, avg `-0.0045`, median `0.0001`, brier `0.2931`, calibration_gap `0.1982`
- 5d: hit_rate `0.4667`, avg `-0.0056`, median `-0.0020`, brier `0.3082`, calibration_gap `0.2315`
- 10d: hit_rate `0.4500`, avg `-0.0014`, median `-0.0065`, brier `0.3133`, calibration_gap `0.2482`
- 20d: hit_rate `0.7500`, avg `0.0151`, median `0.0199`, brier `0.1875`, calibration_gap `-0.0518`
- 60d: hit_rate `0.6667`, avg `0.0321`, median `0.0473`, brier `0.2256`, calibration_gap `0.0315`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0000`, median `0.0018`, brier `0.2367`, calibration_gap `0.0530`
- 5d: hit_rate `0.5625`, avg `-0.0026`, median `0.0014`, brier `0.2593`, calibration_gap `0.1155`
- 10d: hit_rate `0.6875`, avg `0.0140`, median `0.0091`, brier `0.2142`, calibration_gap `-0.0095`
- 20d: hit_rate `0.6875`, avg `0.0140`, median `0.0264`, brier `0.2143`, calibration_gap `-0.0095`
- 60d: hit_rate `0.8125`, avg `0.0434`, median `0.0643`, brier `0.1703`, calibration_gap `-0.1345`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
