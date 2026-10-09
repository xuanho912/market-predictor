# High Confidence Signal Report

Generated at: `2026-10-09T18:24:08.684739+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0029`, median `0.0031`, brier `0.2628`, calibration_gap `0.1696`
- 5d: hit_rate `0.6250`, avg `-0.0005`, median `0.0068`, brier `0.2628`, calibration_gap `0.1696`
- 10d: hit_rate `0.6250`, avg `0.0035`, median `0.0030`, brier `0.2658`, calibration_gap `0.1696`
- 20d: hit_rate `0.7500`, avg `0.0234`, median `0.0240`, brier `0.1890`, calibration_gap `0.0446`
- 60d: hit_rate `0.8750`, avg `0.0325`, median `0.0378`, brier `0.1141`, calibration_gap `-0.0804`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0009`, brier `0.3285`, calibration_gap `0.2841`
- 5d: hit_rate `0.5000`, avg `-0.0054`, median `-0.0043`, brier `0.3285`, calibration_gap `0.2841`
- 10d: hit_rate `0.6250`, avg `-0.0043`, median `0.0021`, brier `0.2631`, calibration_gap `0.1591`
- 20d: hit_rate `0.6250`, avg `0.0160`, median `0.0173`, brier `0.2566`, calibration_gap `0.1591`
- 60d: hit_rate `0.8125`, avg `0.0349`, median `0.0501`, brier `0.1517`, calibration_gap `-0.0284`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.3375`, avg `-0.0077`, median `-0.0059`, brier `0.3723`, calibration_gap `0.3793`
- 5d: hit_rate `0.4000`, avg `-0.0121`, median `-0.0133`, brier `0.3489`, calibration_gap `0.3168`
- 10d: hit_rate `0.4000`, avg `-0.0090`, median `-0.0070`, brier `0.3454`, calibration_gap `0.3168`
- 20d: hit_rate `0.6000`, avg `0.0142`, median `0.0160`, brier `0.2546`, calibration_gap `0.1168`
- 60d: hit_rate `0.7875`, avg `0.0395`, median `0.0463`, brier `0.1722`, calibration_gap `-0.0707`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0060`, median `0.0040`, brier `0.2345`, calibration_gap `0.0298`
- 5d: hit_rate `0.8125`, avg `0.0048`, median `0.0035`, brier `0.1780`, calibration_gap `-0.1577`
- 10d: hit_rate `0.6875`, avg `0.0047`, median `0.0061`, brier `0.2167`, calibration_gap `-0.0327`
- 20d: hit_rate `0.5625`, avg `0.0103`, median `0.0067`, brier `0.2544`, calibration_gap `0.0923`
- 60d: hit_rate `0.7500`, avg `0.0179`, median `0.0290`, brier `0.1981`, calibration_gap `-0.0952`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
