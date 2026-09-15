# High Confidence Signal Report

Generated at: `2026-09-15T01:25:40.446776+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0114`, median `0.0122`, brier `0.1392`, calibration_gap `-0.1656`
- 5d: hit_rate `0.8750`, avg `0.0112`, median `0.0089`, brier `0.1556`, calibration_gap `-0.1656`
- 10d: hit_rate `0.7500`, avg `0.0087`, median `0.0074`, brier `0.2095`, calibration_gap `-0.0406`
- 20d: hit_rate `1.0000`, avg `0.0549`, median `0.0572`, brier `0.0853`, calibration_gap `-0.2906`
- 60d: hit_rate `0.8750`, avg `0.0813`, median `0.0844`, brier `0.1556`, calibration_gap `-0.1656`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0012`, median `0.0047`, brier `0.2226`, calibration_gap `0.0528`
- 5d: hit_rate `0.7500`, avg `0.0057`, median `0.0089`, brier `0.1968`, calibration_gap `-0.0722`
- 10d: hit_rate `0.6875`, avg `0.0076`, median `0.0086`, brier `0.2237`, calibration_gap `-0.0097`
- 20d: hit_rate `1.0000`, avg `0.0465`, median `0.0460`, brier `0.1054`, calibration_gap `-0.3222`
- 60d: hit_rate `0.8750`, avg `0.0701`, median `0.0738`, brier `0.1574`, calibration_gap `-0.1972`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0038`, median `0.0081`, brier `0.2466`, calibration_gap `-0.0066`
- 5d: hit_rate `0.5000`, avg `0.0066`, median `0.0002`, brier `0.2506`, calibration_gap `0.0559`
- 10d: hit_rate `0.6875`, avg `0.0137`, median `0.0213`, brier `0.2329`, calibration_gap `-0.1316`
- 20d: hit_rate `0.8750`, avg `0.0457`, median `0.0489`, brier `0.2102`, calibration_gap `-0.3191`
- 60d: hit_rate `0.7500`, avg `0.0660`, median `0.0844`, brier `0.2252`, calibration_gap `-0.1941`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
