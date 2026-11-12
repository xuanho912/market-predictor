# High Confidence Signal Report

Generated at: `2026-11-12T19:57:13.977473+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.0000`, avg `-0.0138`, median `-0.0114`, brier `0.6388`, calibration_gap `0.7991`
- 5d: hit_rate `0.6250`, avg `-0.0055`, median `0.0011`, brier `0.2640`, calibration_gap `0.1741`
- 10d: hit_rate `0.0000`, avg `-0.0128`, median `-0.0128`, brier `0.6388`, calibration_gap `0.7991`
- 20d: hit_rate `0.3750`, avg `-0.0126`, median `-0.0227`, brier `0.4240`, calibration_gap `0.4241`
- 60d: hit_rate `0.1250`, avg `-0.0460`, median `-0.0556`, brier `0.5644`, calibration_gap `0.6741`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.1875`, avg `-0.0081`, median `-0.0090`, brier `0.5101`, calibration_gap `0.5924`
- 5d: hit_rate `0.5000`, avg `-0.0057`, median `-0.0007`, brier `0.3227`, calibration_gap `0.2799`
- 10d: hit_rate `0.1875`, avg `-0.0095`, median `-0.0105`, brier `0.5126`, calibration_gap `0.5924`
- 20d: hit_rate `0.5000`, avg `0.0006`, median `-0.0001`, brier `0.3389`, calibration_gap `0.2799`
- 60d: hit_rate `0.1250`, avg `-0.0322`, median `-0.0510`, brier `0.5390`, calibration_gap `0.6549`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6500`, avg `0.0062`, median `0.0084`, brier `0.2308`, calibration_gap `0.0157`
- 5d: hit_rate `0.6500`, avg `0.0087`, median `0.0106`, brier `0.2353`, calibration_gap `0.0157`
- 10d: hit_rate `0.6000`, avg `0.0095`, median `0.0108`, brier `0.2562`, calibration_gap `0.0657`
- 20d: hit_rate `0.7750`, avg `0.0239`, median `0.0170`, brier `0.1920`, calibration_gap `-0.1093`
- 60d: hit_rate `0.5750`, avg `0.0144`, median `0.0247`, brier `0.2572`, calibration_gap `0.0907`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0083`, median `0.0101`, brier `0.2174`, calibration_gap `-0.0403`
- 5d: hit_rate `0.8125`, avg `0.0180`, median `0.0162`, brier `0.1809`, calibration_gap `-0.1653`
- 10d: hit_rate `0.8125`, avg `0.0263`, median `0.0293`, brier `0.1783`, calibration_gap `-0.1653`
- 20d: hit_rate `0.8750`, avg `0.0408`, median `0.0339`, brier `0.1613`, calibration_gap `-0.2278`
- 60d: hit_rate `0.6250`, avg `0.0077`, median `0.0482`, brier `0.2342`, calibration_gap `0.0222`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
