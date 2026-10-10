# High Confidence Signal Report

Generated at: `2026-10-10T01:58:36.187287+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0029`, median `0.0031`, brier `0.2631`, calibration_gap `0.1692`
- 5d: hit_rate `0.6250`, avg `-0.0005`, median `0.0068`, brier `0.2631`, calibration_gap `0.1692`
- 10d: hit_rate `0.6250`, avg `0.0035`, median `0.0030`, brier `0.2659`, calibration_gap `0.1692`
- 20d: hit_rate `0.7500`, avg `0.0234`, median `0.0240`, brier `0.1891`, calibration_gap `0.0442`
- 60d: hit_rate `0.8750`, avg `0.0325`, median `0.0378`, brier `0.1144`, calibration_gap `-0.0808`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0015`, median `-0.0009`, brier `0.3284`, calibration_gap `0.2835`
- 5d: hit_rate `0.5000`, avg `-0.0054`, median `-0.0043`, brier `0.3284`, calibration_gap `0.2835`
- 10d: hit_rate `0.6250`, avg `-0.0043`, median `0.0021`, brier `0.2631`, calibration_gap `0.1585`
- 20d: hit_rate `0.6250`, avg `0.0160`, median `0.0173`, brier `0.2564`, calibration_gap `0.1585`
- 60d: hit_rate `0.8125`, avg `0.0349`, median `0.0501`, brier `0.1520`, calibration_gap `-0.0290`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4333`, avg `-0.0050`, median `-0.0037`, brier `0.3349`, calibration_gap `0.2876`
- 5d: hit_rate `0.4667`, avg `-0.0093`, median `-0.0068`, brier `0.3275`, calibration_gap `0.2543`
- 10d: hit_rate `0.4167`, avg `-0.0079`, median `-0.0065`, brier `0.3424`, calibration_gap `0.3043`
- 20d: hit_rate `0.6167`, avg `0.0106`, median `0.0159`, brier `0.2478`, calibration_gap `0.1043`
- 60d: hit_rate `0.7500`, avg `0.0283`, median `0.0434`, brier `0.1900`, calibration_gap `-0.0290`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0060`, median `0.0040`, brier `0.2345`, calibration_gap `0.0311`
- 5d: hit_rate `0.8125`, avg `0.0048`, median `0.0035`, brier `0.1778`, calibration_gap `-0.1564`
- 10d: hit_rate `0.6875`, avg `0.0047`, median `0.0061`, brier `0.2168`, calibration_gap `-0.0314`
- 20d: hit_rate `0.5625`, avg `0.0103`, median `0.0067`, brier `0.2552`, calibration_gap `0.0936`
- 60d: hit_rate `0.7500`, avg `0.0179`, median `0.0290`, brier `0.1984`, calibration_gap `-0.0939`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
