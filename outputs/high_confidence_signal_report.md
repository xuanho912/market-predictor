# High Confidence Signal Report

Generated at: `2026-09-16T01:24:24.620145+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0114`, median `0.0122`, brier `0.1368`, calibration_gap `-0.1557`
- 5d: hit_rate `0.8750`, avg `0.0112`, median `0.0089`, brier `0.1579`, calibration_gap `-0.1557`
- 10d: hit_rate `0.7500`, avg `0.0087`, median `0.0074`, brier `0.2144`, calibration_gap `-0.0307`
- 20d: hit_rate `1.0000`, avg `0.0549`, median `0.0572`, brier `0.0803`, calibration_gap `-0.2807`
- 60d: hit_rate `0.8750`, avg `0.0813`, median `0.0844`, brier `0.1579`, calibration_gap `-0.1557`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0011`, median `0.0079`, brier `0.2217`, calibration_gap `0.0598`
- 5d: hit_rate `0.6875`, avg `0.0037`, median `0.0080`, brier `0.2171`, calibration_gap `-0.0027`
- 10d: hit_rate `0.6250`, avg `0.0047`, median `0.0050`, brier `0.2453`, calibration_gap `0.0598`
- 20d: hit_rate `0.9375`, avg `0.0453`, median `0.0460`, brier `0.1172`, calibration_gap `-0.2527`
- 60d: hit_rate `0.8125`, avg `0.0673`, median `0.0794`, brier `0.1756`, calibration_gap `-0.1277`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0036`, median `0.0080`, brier `0.2594`, calibration_gap `0.0753`
- 5d: hit_rate `0.6000`, avg `0.0047`, median `0.0088`, brier `0.2361`, calibration_gap `0.0253`
- 10d: hit_rate `0.6000`, avg `0.0082`, median `0.0120`, brier `0.2467`, calibration_gap `0.0253`
- 20d: hit_rate `0.7500`, avg `0.0207`, median `0.0295`, brier `0.1950`, calibration_gap `-0.1247`
- 60d: hit_rate `0.8500`, avg `0.0697`, median `0.0888`, brier `0.1758`, calibration_gap `-0.2247`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0152`, median `0.0123`, brier `0.2332`, calibration_gap `-0.2838`
- 5d: hit_rate `0.7500`, avg `0.0214`, median `0.0232`, brier `0.2361`, calibration_gap `-0.2213`
- 10d: hit_rate `0.9375`, avg `0.0368`, median `0.0291`, brier `0.2266`, calibration_gap `-0.4088`
- 20d: hit_rate `0.8750`, avg `0.0459`, median `0.0442`, brier `0.2294`, calibration_gap `-0.3463`
- 60d: hit_rate `0.8125`, avg `0.0961`, median `0.1142`, brier `0.2328`, calibration_gap `-0.2838`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
