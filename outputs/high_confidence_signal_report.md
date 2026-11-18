# High Confidence Signal Report

Generated at: `2026-11-18T03:57:22.642745+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0061`, median `0.0073`, brier `0.2753`, calibration_gap `0.1984`
- 5d: hit_rate `0.7500`, avg `0.0073`, median `0.0017`, brier `0.1911`, calibration_gap `0.0734`
- 10d: hit_rate `0.5000`, avg `0.0107`, median `0.0021`, brier `0.3550`, calibration_gap `0.3234`
- 20d: hit_rate `0.5000`, avg `0.0084`, median `0.0027`, brier `0.3574`, calibration_gap `0.3234`
- 60d: hit_rate `0.5000`, avg `0.0073`, median `-0.0034`, brier `0.3589`, calibration_gap `0.3234`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0085`, median `0.0107`, brier `0.2351`, calibration_gap `0.1254`
- 5d: hit_rate `0.7500`, avg `0.0060`, median `0.0076`, brier `0.1907`, calibration_gap `0.0629`
- 10d: hit_rate `0.6250`, avg `0.0099`, median `0.0087`, brier `0.2740`, calibration_gap `0.1879`
- 20d: hit_rate `0.7500`, avg `0.0277`, median `0.0334`, brier `0.1983`, calibration_gap `0.0629`
- 60d: hit_rate `0.6875`, avg `0.0402`, median `0.0552`, brier `0.2378`, calibration_gap `0.1254`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `0.0083`, median `0.0089`, brier `0.2694`, calibration_gap `0.1221`
- 5d: hit_rate `0.6500`, avg `0.0090`, median `0.0064`, brier `0.2443`, calibration_gap `0.0888`
- 10d: hit_rate `0.6333`, avg `0.0170`, median `0.0099`, brier `0.2665`, calibration_gap `0.1055`
- 20d: hit_rate `0.8000`, avg `0.0377`, median `0.0369`, brier `0.1855`, calibration_gap `-0.0612`
- 60d: hit_rate `0.6833`, avg `0.0597`, median `0.0676`, brier `0.2432`, calibration_gap `0.0555`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0051`, median `0.0095`, brier `0.2350`, calibration_gap `-0.0086`
- 5d: hit_rate `0.6250`, avg `0.0193`, median `0.0176`, brier `0.2334`, calibration_gap `-0.0086`
- 10d: hit_rate `0.7500`, avg `0.0451`, median `0.0514`, brier `0.2026`, calibration_gap `-0.1336`
- 20d: hit_rate `0.8125`, avg `0.0672`, median `0.0636`, brier `0.1887`, calibration_gap `-0.1961`
- 60d: hit_rate `0.6875`, avg `0.0881`, median `0.1268`, brier `0.2193`, calibration_gap `-0.0711`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
