# High Confidence Signal Report

Generated at: `2026-10-14T01:33:17.331375+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0101`, median `0.0116`, brier `0.1491`, calibration_gap `-0.2042`
- 5d: hit_rate `0.7500`, avg `0.0068`, median `0.0108`, brier `0.1958`, calibration_gap `-0.0792`
- 10d: hit_rate `0.8750`, avg `0.0091`, median `0.0079`, brier `0.1553`, calibration_gap `-0.2042`
- 20d: hit_rate `0.8750`, avg `0.0435`, median `0.0498`, brier `0.1491`, calibration_gap `-0.2042`
- 60d: hit_rate `0.8750`, avg `0.0647`, median `0.0751`, brier `0.1553`, calibration_gap `-0.2042`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0011`, median `0.0030`, brier `0.2470`, calibration_gap `0.0959`
- 5d: hit_rate `0.5625`, avg `-0.0032`, median `0.0073`, brier `0.2508`, calibration_gap `0.0959`
- 10d: hit_rate `0.6250`, avg `-0.0004`, median `0.0040`, brier `0.2322`, calibration_gap `0.0334`
- 20d: hit_rate `0.8125`, avg `0.0324`, median `0.0445`, brier `0.1742`, calibration_gap `-0.1541`
- 60d: hit_rate `0.9375`, avg `0.0712`, median `0.0751`, brier `0.1403`, calibration_gap `-0.2791`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6500`, avg `0.0039`, median `0.0101`, brier `0.2271`, calibration_gap `-0.0366`
- 5d: hit_rate `0.5833`, avg `0.0035`, median `0.0089`, brier `0.2410`, calibration_gap `0.0301`
- 10d: hit_rate `0.6167`, avg `0.0065`, median `0.0044`, brier `0.2320`, calibration_gap `-0.0032`
- 20d: hit_rate `0.9167`, avg `0.0328`, median `0.0318`, brier `0.1689`, calibration_gap `-0.3032`
- 60d: hit_rate `0.8167`, avg `0.0665`, median `0.0836`, brier `0.1882`, calibration_gap `-0.2032`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0023`, median `0.0034`, brier `0.2459`, calibration_gap `-0.0054`
- 5d: hit_rate `0.3750`, avg `-0.0021`, median `-0.0057`, brier `0.2645`, calibration_gap `0.1821`
- 10d: hit_rate `0.5000`, avg `-0.0010`, median `-0.0045`, brier `0.2511`, calibration_gap `0.0571`
- 20d: hit_rate `0.5625`, avg `0.0107`, median `0.0018`, brier `0.2436`, calibration_gap `-0.0054`
- 60d: hit_rate `0.8750`, avg `0.0982`, median `0.1152`, brier `0.2103`, calibration_gap `-0.3179`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
