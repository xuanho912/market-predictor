# High Confidence Signal Report

Generated at: `2026-07-26T13:59:39.581450+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0033`, median `0.0007`, brier `0.2642`, calibration_gap `0.1750`
- 5d: hit_rate `0.5000`, avg `-0.0078`, median `-0.0029`, brier `0.3378`, calibration_gap `0.3000`
- 10d: hit_rate `0.5000`, avg `-0.0003`, median `-0.0034`, brier `0.3419`, calibration_gap `0.3000`
- 20d: hit_rate `0.5000`, avg `0.0122`, median `0.0091`, brier `0.3421`, calibration_gap `0.3000`
- 60d: hit_rate `0.6250`, avg `0.0315`, median `0.0453`, brier `0.2649`, calibration_gap `0.1750`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `-0.0004`, median `0.0011`, brier `0.2270`, calibration_gap `0.1033`
- 5d: hit_rate `0.6250`, avg `-0.0010`, median `0.0010`, brier `0.2638`, calibration_gap `0.1658`
- 10d: hit_rate `0.5000`, avg `-0.0012`, median `-0.0034`, brier `0.3348`, calibration_gap `0.2908`
- 20d: hit_rate `0.5625`, avg `0.0138`, median `0.0178`, brier `0.3000`, calibration_gap `0.2283`
- 60d: hit_rate `0.6875`, avg `0.0297`, median `0.0434`, brier `0.2266`, calibration_gap `0.1033`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `0.0018`, median `0.0043`, brier `0.2474`, calibration_gap `0.0961`
- 5d: hit_rate `0.6333`, avg `0.0065`, median `0.0065`, brier `0.2476`, calibration_gap `0.0794`
- 10d: hit_rate `0.6833`, avg `0.0126`, median `0.0176`, brier `0.2312`, calibration_gap `0.0294`
- 20d: hit_rate `0.6833`, avg `0.0268`, median `0.0248`, brier `0.2318`, calibration_gap `0.0294`
- 60d: hit_rate `0.7833`, avg `0.0505`, median `0.0595`, brier `0.1886`, calibration_gap `-0.0706`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0077`, median `0.0057`, brier `0.2376`, calibration_gap `0.0146`
- 5d: hit_rate `0.6875`, avg `0.0150`, median `0.0211`, brier `0.2192`, calibration_gap `-0.0479`
- 10d: hit_rate `0.7500`, avg `0.0180`, median `0.0249`, brier `0.1929`, calibration_gap `-0.1104`
- 20d: hit_rate `0.7500`, avg `0.0305`, median `0.0283`, brier `0.2100`, calibration_gap `-0.1104`
- 60d: hit_rate `0.9375`, avg `0.0865`, median `0.1027`, brier `0.1436`, calibration_gap `-0.2979`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
