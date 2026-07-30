# High Confidence Signal Report

Generated at: `2026-07-30T00:08:54.709618+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0043`, median `0.0028`, brier `0.3597`, calibration_gap `0.3403`
- 5d: hit_rate `0.6250`, avg `-0.0091`, median `0.0017`, brier `0.2805`, calibration_gap `0.2153`
- 10d: hit_rate `0.3750`, avg `-0.0006`, median `-0.0004`, brier `0.4482`, calibration_gap `0.4653`
- 20d: hit_rate `0.5000`, avg `0.0159`, median `-0.0001`, brier `0.3688`, calibration_gap `0.3403`
- 60d: hit_rate `0.3750`, avg `0.0212`, median `-0.0243`, brier `0.4558`, calibration_gap `0.4653`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0022`, median `-0.0004`, brier `0.3528`, calibration_gap `0.3251`
- 5d: hit_rate `0.5625`, avg `-0.0064`, median `0.0006`, brier `0.3128`, calibration_gap `0.2626`
- 10d: hit_rate `0.3125`, avg `-0.0035`, median `-0.0036`, brier `0.4749`, calibration_gap `0.5126`
- 20d: hit_rate `0.5625`, avg `0.0139`, median `0.0070`, brier `0.3194`, calibration_gap `0.2626`
- 60d: hit_rate `0.4375`, avg `0.0215`, median `-0.0185`, brier `0.4000`, calibration_gap `0.3876`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6500`, avg `0.0035`, median `0.0082`, brier `0.2468`, calibration_gap `0.0628`
- 5d: hit_rate `0.6167`, avg `0.0059`, median `0.0065`, brier `0.2538`, calibration_gap `0.0961`
- 10d: hit_rate `0.6000`, avg `0.0130`, median `0.0189`, brier `0.2773`, calibration_gap `0.1128`
- 20d: hit_rate `0.7000`, avg `0.0348`, median `0.0421`, brier `0.2312`, calibration_gap `0.0128`
- 60d: hit_rate `0.7333`, avg `0.0673`, median `0.0807`, brier `0.2149`, calibration_gap `-0.0205`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0051`, median `0.0097`, brier `0.2048`, calibration_gap `-0.1221`
- 5d: hit_rate `0.6875`, avg `0.0149`, median `0.0143`, brier `0.2186`, calibration_gap `-0.0596`
- 10d: hit_rate `0.6250`, avg `0.0157`, median `0.0279`, brier `0.2379`, calibration_gap `0.0029`
- 20d: hit_rate `0.7500`, avg `0.0449`, median `0.0643`, brier `0.2039`, calibration_gap `-0.1221`
- 60d: hit_rate `0.7500`, avg `0.0960`, median `0.0940`, brier `0.2039`, calibration_gap `-0.1221`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
