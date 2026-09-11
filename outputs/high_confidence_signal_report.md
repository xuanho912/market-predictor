# High Confidence Signal Report

Generated at: `2026-09-11T23:33:36.363140+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0024`, median `0.0014`, brier `0.1877`, calibration_gap `0.0401`
- 5d: hit_rate `0.5000`, avg `-0.0019`, median `-0.0009`, brier `0.3281`, calibration_gap `0.2901`
- 10d: hit_rate `0.2500`, avg `-0.0095`, median `-0.0136`, brier `0.4866`, calibration_gap `0.5401`
- 20d: hit_rate `0.5000`, avg `0.0026`, median `0.0084`, brier `0.3425`, calibration_gap `0.2901`
- 60d: hit_rate `0.7500`, avg `0.0389`, median `0.0588`, brier `0.1878`, calibration_gap `0.0401`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0051`, median `0.0004`, brier `0.2842`, calibration_gap `0.2118`
- 5d: hit_rate `0.5000`, avg `-0.0089`, median `-0.0009`, brier `0.3222`, calibration_gap `0.2743`
- 10d: hit_rate `0.2500`, avg `-0.0120`, median `-0.0189`, brier `0.4657`, calibration_gap `0.5243`
- 20d: hit_rate `0.5000`, avg `0.0006`, median `0.0031`, brier `0.3285`, calibration_gap `0.2743`
- 60d: hit_rate `0.5625`, avg `0.0160`, median `0.0311`, brier `0.2832`, calibration_gap `0.2118`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0047`, median `0.0103`, brier `0.2091`, calibration_gap `-0.0316`
- 5d: hit_rate `0.6000`, avg `0.0043`, median `0.0051`, brier `0.2437`, calibration_gap `0.0684`
- 10d: hit_rate `0.6500`, avg `0.0167`, median `0.0169`, brier `0.2268`, calibration_gap `0.0184`
- 20d: hit_rate `0.8000`, avg `0.0306`, median `0.0323`, brier `0.1759`, calibration_gap `-0.1316`
- 60d: hit_rate `0.7500`, avg `0.0466`, median `0.0668`, brier `0.1936`, calibration_gap `-0.0816`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0049`, median `0.0106`, brier `0.2138`, calibration_gap `-0.0229`
- 5d: hit_rate `0.5625`, avg `0.0029`, median `0.0013`, brier `0.2573`, calibration_gap `0.1021`
- 10d: hit_rate `0.5625`, avg `0.0105`, median `0.0098`, brier `0.2584`, calibration_gap `0.1021`
- 20d: hit_rate `0.7500`, avg `0.0255`, median `0.0151`, brier `0.1948`, calibration_gap `-0.0854`
- 60d: hit_rate `0.6875`, avg `0.0285`, median `0.0489`, brier `0.2169`, calibration_gap `-0.0229`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
