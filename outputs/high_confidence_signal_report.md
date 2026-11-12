# High Confidence Signal Report

Generated at: `2026-11-12T03:28:35.662051+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0094`, median `-0.0065`, brier `0.5043`, calibration_gap `0.6311`
- 5d: hit_rate `0.1250`, avg `-0.0131`, median `-0.0150`, brier `0.5093`, calibration_gap `0.6311`
- 10d: hit_rate `0.7500`, avg `0.0114`, median `0.0137`, brier `0.1815`, calibration_gap `0.0061`
- 20d: hit_rate `0.8750`, avg `0.0210`, median `0.0289`, brier `0.1203`, calibration_gap `-0.1189`
- 60d: hit_rate `1.0000`, avg `0.0770`, median `0.0874`, brier `0.0596`, calibration_gap `-0.2439`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0034`, median `-0.0051`, brier `0.4042`, calibration_gap `0.4332`
- 5d: hit_rate `0.3750`, avg `-0.0026`, median `-0.0113`, brier `0.3777`, calibration_gap `0.3707`
- 10d: hit_rate `0.5625`, avg `0.0102`, median `0.0101`, brier `0.2727`, calibration_gap `0.1832`
- 20d: hit_rate `0.8750`, avg `0.0267`, median `0.0281`, brier `0.1247`, calibration_gap `-0.1293`
- 60d: hit_rate `1.0000`, avg `0.0725`, median `0.0798`, brier `0.0648`, calibration_gap `-0.2543`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4333`, avg `-0.0015`, median `-0.0027`, brier `0.3238`, calibration_gap `0.2662`
- 5d: hit_rate `0.4667`, avg `-0.0014`, median `-0.0056`, brier `0.3098`, calibration_gap `0.2328`
- 10d: hit_rate `0.5333`, avg `0.0057`, median `0.0063`, brier `0.2810`, calibration_gap `0.1662`
- 20d: hit_rate `0.8000`, avg `0.0211`, median `0.0248`, brier `0.1694`, calibration_gap `-0.1005`
- 60d: hit_rate `0.7333`, avg `0.0388`, median `0.0567`, brier `0.1940`, calibration_gap `-0.0338`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0013`, median `0.0009`, brier `0.2695`, calibration_gap `0.1343`
- 5d: hit_rate `0.5000`, avg `-0.0022`, median `0.0011`, brier `0.2702`, calibration_gap `0.1343`
- 10d: hit_rate `0.5625`, avg `0.0032`, median `0.0049`, brier `0.2506`, calibration_gap `0.0718`
- 20d: hit_rate `0.7500`, avg `0.0153`, median `0.0191`, brier `0.1995`, calibration_gap `-0.1157`
- 60d: hit_rate `0.6875`, avg `0.0351`, median `0.0653`, brier `0.2151`, calibration_gap `-0.0532`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
