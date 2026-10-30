# High Confidence Signal Report

Generated at: `2026-10-30T02:12:28.235890+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0039`, median `0.0029`, brier `0.2535`, calibration_gap `0.1397`
- 5d: hit_rate `0.5000`, avg `0.0080`, median `0.0023`, brier `0.3245`, calibration_gap `0.2647`
- 10d: hit_rate `0.7500`, avg `0.0193`, median `0.0224`, brier `0.1822`, calibration_gap `0.0147`
- 20d: hit_rate `0.8750`, avg `0.0332`, median `0.0297`, brier `0.1185`, calibration_gap `-0.1103`
- 60d: hit_rate `0.8750`, avg `0.0618`, median `0.0708`, brier `0.1217`, calibration_gap `-0.1103`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0074`, median `0.0072`, brier `0.2488`, calibration_gap `0.1282`
- 5d: hit_rate `0.5625`, avg `0.0099`, median `0.0174`, brier `0.2843`, calibration_gap `0.1907`
- 10d: hit_rate `0.8125`, avg `0.0311`, median `0.0321`, brier `0.1537`, calibration_gap `-0.0593`
- 20d: hit_rate `0.8750`, avg `0.0444`, median `0.0368`, brier `0.1228`, calibration_gap `-0.1218`
- 60d: hit_rate `0.8750`, avg `0.0590`, median `0.0673`, brier `0.1244`, calibration_gap `-0.1218`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6500`, avg `0.0052`, median `0.0063`, brier `0.2284`, calibration_gap `0.0490`
- 5d: hit_rate `0.5833`, avg `0.0074`, median `0.0066`, brier `0.2628`, calibration_gap `0.1157`
- 10d: hit_rate `0.6667`, avg `0.0133`, median `0.0136`, brier `0.2243`, calibration_gap `0.0323`
- 20d: hit_rate `0.7667`, avg `0.0243`, median `0.0284`, brier `0.1818`, calibration_gap `-0.0677`
- 60d: hit_rate `0.7333`, avg `0.0388`, median `0.0536`, brier `0.1921`, calibration_gap `-0.0343`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0073`, median `0.0098`, brier `0.2338`, calibration_gap `0.0238`
- 5d: hit_rate `0.6875`, avg `0.0129`, median `0.0137`, brier `0.2175`, calibration_gap `-0.0387`
- 10d: hit_rate `0.7500`, avg `0.0207`, median `0.0305`, brier `0.1932`, calibration_gap `-0.1012`
- 20d: hit_rate `0.7500`, avg `0.0277`, median `0.0368`, brier `0.1962`, calibration_gap `-0.1012`
- 60d: hit_rate `0.7500`, avg `0.0555`, median `0.0680`, brier `0.1929`, calibration_gap `-0.1012`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
