# High Confidence Signal Report

Generated at: `2026-10-09T00:42:55.302354+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0068`, median `0.0079`, brier `0.1859`, calibration_gap `-0.0431`
- 5d: hit_rate `0.6250`, avg `0.0034`, median `0.0074`, brier `0.2347`, calibration_gap `0.0819`
- 10d: hit_rate `0.8750`, avg `0.0070`, median `0.0060`, brier `0.1349`, calibration_gap `-0.1681`
- 20d: hit_rate `0.7500`, avg `0.0337`, median `0.0460`, brier `0.1859`, calibration_gap `-0.0431`
- 60d: hit_rate `0.8750`, avg `0.0681`, median `0.0751`, brier `0.1349`, calibration_gap `-0.1681`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0017`, median `0.0079`, brier `0.2342`, calibration_gap `0.0611`
- 5d: hit_rate `0.6250`, avg `0.0025`, median `0.0080`, brier `0.2378`, calibration_gap `0.0611`
- 10d: hit_rate `0.6875`, avg `0.0023`, median `0.0060`, brier `0.2087`, calibration_gap `-0.0014`
- 20d: hit_rate `0.8750`, avg `0.0325`, median `0.0414`, brier `0.1490`, calibration_gap `-0.1889`
- 60d: hit_rate `0.9375`, avg `0.0914`, median `0.0922`, brier `0.1235`, calibration_gap `-0.2514`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6333`, avg `0.0044`, median `0.0081`, brier `0.2338`, calibration_gap `-0.0201`
- 5d: hit_rate `0.5667`, avg `0.0044`, median `0.0080`, brier `0.2467`, calibration_gap `0.0466`
- 10d: hit_rate `0.6500`, avg `0.0096`, median `0.0050`, brier `0.2286`, calibration_gap `-0.0368`
- 20d: hit_rate `0.9000`, avg `0.0399`, median `0.0334`, brier `0.1764`, calibration_gap `-0.2868`
- 60d: hit_rate `0.8833`, avg `0.0841`, median `0.0939`, brier `0.1707`, calibration_gap `-0.2701`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0018`, median `0.0068`, brier `0.2378`, calibration_gap `-0.0796`
- 5d: hit_rate `0.5000`, avg `0.0008`, median `-0.0038`, brier `0.2502`, calibration_gap `0.0454`
- 10d: hit_rate `0.5625`, avg `0.0079`, median `0.0033`, brier `0.2477`, calibration_gap `-0.0171`
- 20d: hit_rate `0.8125`, avg `0.0394`, median `0.0201`, brier `0.2236`, calibration_gap `-0.2671`
- 60d: hit_rate `0.6875`, avg `0.0862`, median `0.1191`, brier `0.2354`, calibration_gap `-0.1421`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
