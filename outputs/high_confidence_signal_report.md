# High Confidence Signal Report

Generated at: `2026-10-01T18:27:23.425262+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0117`, median `0.0126`, brier `0.1076`, calibration_gap `-0.0149`
- 5d: hit_rate `0.8750`, avg `0.0080`, median `0.0076`, brier `0.1076`, calibration_gap `-0.0149`
- 10d: hit_rate `0.7500`, avg `0.0029`, median `0.0058`, brier `0.1961`, calibration_gap `0.1101`
- 20d: hit_rate `0.7500`, avg `0.0295`, median `0.0460`, brier `0.1971`, calibration_gap `0.1101`
- 60d: hit_rate `1.0000`, avg `0.0586`, median `0.0625`, brier `0.0197`, calibration_gap `-0.1399`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.7500`, avg `0.0075`, median `0.0124`, brier `0.1909`, calibration_gap `0.0958`
- 5d: hit_rate `0.6875`, avg `0.0049`, median `0.0076`, brier `0.2315`, calibration_gap `0.1583`
- 10d: hit_rate `0.6875`, avg `0.0005`, median `0.0060`, brier `0.2348`, calibration_gap `0.1583`
- 20d: hit_rate `0.7500`, avg `0.0180`, median `0.0205`, brier `0.1942`, calibration_gap `0.0958`
- 60d: hit_rate `1.0000`, avg `0.0763`, median `0.0751`, brier `0.0241`, calibration_gap `-0.1542`

### strong_signal_only
- sample_size: `0`
- 3d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 5d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 10d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 20d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`
- 60d: hit_rate `n/a`, avg `n/a`, median `n/a`, brier `n/a`, calibration_gap `n/a`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0013`, median `-0.0037`, brier `0.3052`, calibration_gap `0.2664`
- 5d: hit_rate `0.5000`, avg `-0.0072`, median `-0.0003`, brier `0.2698`, calibration_gap `0.1414`
- 10d: hit_rate `0.6250`, avg `-0.0013`, median `0.0074`, brier `0.2357`, calibration_gap `0.0164`
- 20d: hit_rate `0.6250`, avg `-0.0007`, median `0.0126`, brier `0.2329`, calibration_gap `0.0164`
- 60d: hit_rate `0.7500`, avg `0.0174`, median `0.0306`, brier `0.1976`, calibration_gap `-0.1086`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
