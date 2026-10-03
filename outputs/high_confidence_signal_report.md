# High Confidence Signal Report

Generated at: `2026-10-03T01:55:16.951911+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0116`, median `0.0124`, brier `0.1131`, calibration_gap `-0.0364`
- 5d: hit_rate `0.8750`, avg `0.0085`, median `0.0076`, brier `0.1131`, calibration_gap `-0.0364`
- 10d: hit_rate `0.7500`, avg `0.0062`, median `0.0097`, brier `0.1984`, calibration_gap `0.0886`
- 20d: hit_rate `0.7500`, avg `0.0225`, median `0.0235`, brier `0.1987`, calibration_gap `0.0886`
- 60d: hit_rate `1.0000`, avg `0.0682`, median `0.0717`, brier `0.0261`, calibration_gap `-0.1614`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0069`, median `0.0124`, brier `0.1918`, calibration_gap `0.0755`
- 5d: hit_rate `0.6875`, avg `0.0047`, median `0.0076`, brier `0.2301`, calibration_gap `0.1380`
- 10d: hit_rate `0.6875`, avg `0.0023`, median `0.0060`, brier `0.2334`, calibration_gap `0.1380`
- 20d: hit_rate `0.7500`, avg `0.0170`, median `0.0173`, brier `0.1945`, calibration_gap `0.0755`
- 60d: hit_rate `1.0000`, avg `0.0727`, median `0.0751`, brier `0.0307`, calibration_gap `-0.1745`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0009`, median `0.0030`, brier `0.2755`, calibration_gap `0.1810`
- 5d: hit_rate `0.5750`, avg `-0.0017`, median `0.0038`, brier `0.2775`, calibration_gap `0.1560`
- 10d: hit_rate `0.5750`, avg `-0.0013`, median `0.0049`, brier `0.2802`, calibration_gap `0.1560`
- 20d: hit_rate `0.6750`, avg `0.0101`, median `0.0157`, brier `0.2318`, calibration_gap `0.0560`
- 60d: hit_rate `0.8750`, avg `0.0424`, median `0.0445`, brier `0.1308`, calibration_gap `-0.1440`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `0.0002`, median `-0.0024`, brier `0.2856`, calibration_gap `0.1967`
- 5d: hit_rate `0.5625`, avg `-0.0023`, median `0.0021`, brier `0.2524`, calibration_gap `0.0717`
- 10d: hit_rate `0.6250`, avg `0.0072`, median `0.0074`, brier `0.2355`, calibration_gap `0.0092`
- 20d: hit_rate `0.6250`, avg `0.0078`, median `0.0126`, brier `0.2347`, calibration_gap `0.0092`
- 60d: hit_rate `0.8125`, avg `0.0199`, median `0.0320`, brier `0.1835`, calibration_gap `-0.1783`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
