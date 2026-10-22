# High Confidence Signal Report

Generated at: `2026-10-22T23:30:20.131687+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0036`, median `0.0105`, brier `0.3129`, calibration_gap `0.2560`
- 5d: hit_rate `0.5000`, avg `0.0057`, median `-0.0029`, brier `0.3145`, calibration_gap `0.2560`
- 10d: hit_rate `0.7500`, avg `0.0222`, median `0.0224`, brier `0.1908`, calibration_gap `0.0060`
- 20d: hit_rate `0.8750`, avg `0.0404`, median `0.0368`, brier `0.1240`, calibration_gap `-0.1190`
- 60d: hit_rate `1.0000`, avg `0.0767`, median `0.0831`, brier `0.0596`, calibration_gap `-0.2440`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0069`, median `0.0135`, brier `0.2503`, calibration_gap `0.1217`
- 5d: hit_rate `0.5625`, avg `0.0060`, median `0.0006`, brier `0.2814`, calibration_gap `0.1842`
- 10d: hit_rate `0.6875`, avg `0.0178`, median `0.0143`, brier `0.2187`, calibration_gap `0.0592`
- 20d: hit_rate `0.8750`, avg `0.0326`, median `0.0314`, brier `0.1257`, calibration_gap `-0.1283`
- 60d: hit_rate `0.9375`, avg `0.0636`, median `0.0708`, brier `0.0934`, calibration_gap `-0.1908`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6750`, avg `0.0064`, median `0.0070`, brier `0.2217`, calibration_gap `-0.0020`
- 5d: hit_rate `0.7250`, avg `0.0081`, median `0.0126`, brier `0.2039`, calibration_gap `-0.0520`
- 10d: hit_rate `0.7250`, avg `0.0099`, median `0.0177`, brier `0.2013`, calibration_gap `-0.0520`
- 20d: hit_rate `0.6750`, avg `0.0158`, median `0.0138`, brier `0.2231`, calibration_gap `-0.0020`
- 60d: hit_rate `0.6000`, avg `0.0106`, median `0.0083`, brier `0.2454`, calibration_gap `0.0730`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0049`, median `0.0059`, brier `0.2153`, calibration_gap `-0.0420`
- 5d: hit_rate `0.8125`, avg `0.0098`, median `0.0103`, brier `0.1822`, calibration_gap `-0.1670`
- 10d: hit_rate `0.8125`, avg `0.0133`, median `0.0199`, brier `0.1790`, calibration_gap `-0.1670`
- 20d: hit_rate `0.8125`, avg `0.0207`, median `0.0168`, brier `0.1822`, calibration_gap `-0.1670`
- 60d: hit_rate `0.6250`, avg `0.0222`, median `0.0433`, brier `0.2354`, calibration_gap `0.0205`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
