# High Confidence Signal Report

Generated at: `2026-09-23T01:10:42.742780+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0029`, median `0.0116`, brier `0.1796`, calibration_gap `-0.0689`
- 5d: hit_rate `0.6250`, avg `-0.0002`, median `0.0074`, brier `0.2370`, calibration_gap `0.0561`
- 10d: hit_rate `0.6250`, avg `-0.0029`, median `0.0021`, brier `0.2370`, calibration_gap `0.0561`
- 20d: hit_rate `0.8750`, avg `0.0386`, median `0.0498`, brier `0.1410`, calibration_gap `-0.1939`
- 60d: hit_rate `0.8750`, avg `0.0632`, median `0.0738`, brier `0.1597`, calibration_gap `-0.1939`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0037`, median `0.0079`, brier `0.2094`, calibration_gap `-0.0261`
- 5d: hit_rate `0.6250`, avg `0.0003`, median `0.0080`, brier `0.2363`, calibration_gap `0.0364`
- 10d: hit_rate `0.6250`, avg `0.0024`, median `0.0021`, brier `0.2381`, calibration_gap `0.0364`
- 20d: hit_rate `0.9375`, avg `0.0382`, median `0.0460`, brier `0.1347`, calibration_gap `-0.2761`
- 60d: hit_rate `0.9375`, avg `0.0664`, median `0.0651`, brier `0.1441`, calibration_gap `-0.2761`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6375`, avg `0.0042`, median `0.0101`, brier `0.2301`, calibration_gap `-0.0388`
- 5d: hit_rate `0.6250`, avg `0.0049`, median `0.0099`, brier `0.2378`, calibration_gap `-0.0263`
- 10d: hit_rate `0.6375`, avg `0.0091`, median `0.0100`, brier `0.2344`, calibration_gap `-0.0388`
- 20d: hit_rate `0.8375`, avg `0.0328`, median `0.0301`, brier `0.1910`, calibration_gap `-0.2388`
- 60d: hit_rate `0.8500`, avg `0.0664`, median `0.0826`, brier `0.1895`, calibration_gap `-0.2513`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0039`, median `0.0029`, brier `0.2341`, calibration_gap `-0.0710`
- 5d: hit_rate `0.6250`, avg `0.0047`, median `0.0060`, brier `0.2391`, calibration_gap `-0.0710`
- 10d: hit_rate `0.6250`, avg `0.0137`, median `0.0108`, brier `0.2363`, calibration_gap `-0.0710`
- 20d: hit_rate `0.8125`, avg `0.0349`, median `0.0283`, brier `0.2154`, calibration_gap `-0.2585`
- 60d: hit_rate `0.8750`, avg `0.0644`, median `0.0768`, brier `0.2075`, calibration_gap `-0.3210`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
