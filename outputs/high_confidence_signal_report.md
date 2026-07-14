# High Confidence Signal Report

Generated at: `2026-07-14T00:04:27.983198+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0132`, median `-0.0151`, brier `0.4266`, calibration_gap `0.4868`
- 5d: hit_rate `0.2500`, avg `-0.0207`, median `-0.0206`, brier `0.4264`, calibration_gap `0.4868`
- 10d: hit_rate `0.2500`, avg `-0.0127`, median `-0.0147`, brier `0.4255`, calibration_gap `0.4868`
- 20d: hit_rate `0.7500`, avg `0.0040`, median `0.0093`, brier `0.1840`, calibration_gap `-0.0132`
- 60d: hit_rate `0.5000`, avg `0.0123`, median `0.0126`, brier `0.3033`, calibration_gap `0.2368`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0125`, median `-0.0141`, brier `0.3907`, calibration_gap `0.4169`
- 5d: hit_rate `0.2500`, avg `-0.0179`, median `-0.0155`, brier `0.4185`, calibration_gap `0.4794`
- 10d: hit_rate `0.2500`, avg `-0.0122`, median `-0.0175`, brier `0.4178`, calibration_gap `0.4794`
- 20d: hit_rate `0.8125`, avg `0.0112`, median `0.0095`, brier `0.1585`, calibration_gap `-0.0831`
- 60d: hit_rate `0.6250`, avg `0.0375`, median `0.0528`, brier `0.2457`, calibration_gap `0.1044`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5000`, avg `-0.0034`, median `0.0001`, brier `0.2973`, calibration_gap `0.2038`
- 5d: hit_rate `0.4667`, avg `-0.0053`, median `-0.0009`, brier `0.3105`, calibration_gap `0.2372`
- 10d: hit_rate `0.4500`, avg `-0.0002`, median `-0.0046`, brier `0.3158`, calibration_gap `0.2538`
- 20d: hit_rate `0.7167`, avg `0.0174`, median `0.0208`, brier `0.1998`, calibration_gap `-0.0128`
- 60d: hit_rate `0.6667`, avg `0.0389`, median `0.0567`, brier `0.2241`, calibration_gap `0.0372`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0057`, median `0.0104`, brier `0.2377`, calibration_gap `0.0546`
- 5d: hit_rate `0.5625`, avg `0.0031`, median `0.0073`, brier `0.2600`, calibration_gap `0.1171`
- 10d: hit_rate `0.5625`, avg `0.0044`, median `0.0105`, brier `0.2594`, calibration_gap `0.1171`
- 20d: hit_rate `0.5625`, avg `0.0026`, median `0.0180`, brier `0.2603`, calibration_gap `0.1171`
- 60d: hit_rate `0.7500`, avg `0.0446`, median `0.0545`, brier `0.1917`, calibration_gap `-0.0704`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
