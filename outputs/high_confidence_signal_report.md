# High Confidence Signal Report

Generated at: `2026-09-26T01:34:32.596357+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0073`, median `0.0085`, brier `0.1825`, calibration_gap `0.0259`
- 5d: hit_rate `0.7500`, avg `0.0069`, median `0.0108`, brier `0.1825`, calibration_gap `0.0259`
- 10d: hit_rate `1.0000`, avg `0.0100`, median `0.0097`, brier `0.0505`, calibration_gap `-0.2241`
- 20d: hit_rate `0.7500`, avg `0.0295`, median `0.0460`, brier `0.1825`, calibration_gap `0.0259`
- 60d: hit_rate `1.0000`, avg `0.0881`, median `0.0844`, brier `0.0505`, calibration_gap `-0.2241`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0050`, median `0.0116`, brier `0.2080`, calibration_gap `0.0568`
- 5d: hit_rate `0.6875`, avg `0.0058`, median `0.0089`, brier `0.2076`, calibration_gap `0.0568`
- 10d: hit_rate `0.7500`, avg `0.0063`, median `0.0083`, brier `0.1688`, calibration_gap `-0.0057`
- 20d: hit_rate `0.8750`, avg `0.0341`, median `0.0424`, brier `0.1328`, calibration_gap `-0.1307`
- 60d: hit_rate `0.9375`, avg `0.0930`, median `0.0940`, brier `0.0936`, calibration_gap `-0.1932`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6250`, avg `0.0035`, median `0.0062`, brier `0.2367`, calibration_gap `0.0486`
- 5d: hit_rate `0.6250`, avg `0.0055`, median `0.0080`, brier `0.2373`, calibration_gap `0.0486`
- 10d: hit_rate `0.7500`, avg `0.0093`, median `0.0111`, brier `0.1929`, calibration_gap `-0.0764`
- 20d: hit_rate `0.7750`, avg `0.0291`, median `0.0319`, brier `0.1877`, calibration_gap `-0.1014`
- 60d: hit_rate `0.9250`, avg `0.0827`, median `0.0933`, brier `0.1308`, calibration_gap `-0.2514`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0028`, median `0.0103`, brier `0.2392`, calibration_gap `-0.0644`
- 5d: hit_rate `0.5000`, avg `0.0070`, median `0.0013`, brier `0.2543`, calibration_gap `0.0606`
- 10d: hit_rate `0.7500`, avg `0.0162`, median `0.0173`, brier `0.2249`, calibration_gap `-0.1894`
- 20d: hit_rate `0.7500`, avg `0.0362`, median `0.0311`, brier `0.2208`, calibration_gap `-0.1894`
- 60d: hit_rate `0.6875`, avg `0.0606`, median `0.0725`, brier `0.2302`, calibration_gap `-0.1269`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
