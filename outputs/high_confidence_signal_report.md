# High Confidence Signal Report

Generated at: `2026-11-05T07:57:29.995556+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0176`, median `0.0210`, brier `0.1234`, calibration_gap `-0.1250`
- 5d: hit_rate `0.7500`, avg `0.0164`, median `0.0247`, brier `0.1844`, calibration_gap `-0.0000`
- 10d: hit_rate `0.8750`, avg `0.0296`, median `0.0409`, brier `0.1232`, calibration_gap `-0.1250`
- 20d: hit_rate `0.8750`, avg `0.0357`, median `0.0484`, brier `0.1232`, calibration_gap `-0.1250`
- 60d: hit_rate `0.8750`, avg `0.0620`, median `0.0697`, brier `0.1227`, calibration_gap `-0.1250`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0061`, median `0.0052`, brier `0.2424`, calibration_gap `0.1159`
- 5d: hit_rate `0.5000`, avg `0.0070`, median `-0.0017`, brier `0.3016`, calibration_gap `0.2409`
- 10d: hit_rate `0.6875`, avg `0.0150`, median `0.0224`, brier `0.2134`, calibration_gap `0.0534`
- 20d: hit_rate `0.8125`, avg `0.0332`, median `0.0360`, brier `0.1559`, calibration_gap `-0.0716`
- 60d: hit_rate `0.8125`, avg `0.0532`, median `0.0669`, brier `0.1552`, calibration_gap `-0.0716`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `0.0031`, median `0.0063`, brier `0.2374`, calibration_gap `0.0636`
- 5d: hit_rate `0.6167`, avg `0.0082`, median `0.0101`, brier `0.2490`, calibration_gap `0.0636`
- 10d: hit_rate `0.7000`, avg `0.0158`, median `0.0199`, brier `0.2120`, calibration_gap `-0.0198`
- 20d: hit_rate `0.7500`, avg `0.0246`, median `0.0295`, brier `0.1878`, calibration_gap `-0.0698`
- 60d: hit_rate `0.7167`, avg `0.0385`, median `0.0538`, brier `0.2017`, calibration_gap `-0.0364`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0018`, median `0.0029`, brier `0.2646`, calibration_gap `0.1141`
- 5d: hit_rate `0.6875`, avg `0.0088`, median `0.0116`, brier `0.2211`, calibration_gap `-0.0734`
- 10d: hit_rate `0.7500`, avg `0.0152`, median `0.0198`, brier `0.2038`, calibration_gap `-0.1359`
- 20d: hit_rate `0.6250`, avg `0.0145`, median `0.0216`, brier `0.2293`, calibration_gap `-0.0109`
- 60d: hit_rate `0.6250`, avg `0.0470`, median `0.0558`, brier `0.2284`, calibration_gap `-0.0109`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
