# High Confidence Signal Report

Generated at: `2026-11-04T19:50:11.168242+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0176`, median `0.0210`, brier `0.1239`, calibration_gap `-0.1268`
- 5d: hit_rate `0.7500`, avg `0.0164`, median `0.0247`, brier `0.1844`, calibration_gap `-0.0018`
- 10d: hit_rate `0.8750`, avg `0.0296`, median `0.0409`, brier `0.1233`, calibration_gap `-0.1268`
- 20d: hit_rate `0.8750`, avg `0.0357`, median `0.0484`, brier `0.1233`, calibration_gap `-0.1268`
- 60d: hit_rate `0.8750`, avg `0.0620`, median `0.0697`, brier `0.1229`, calibration_gap `-0.1268`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0031`, median `0.0029`, brier `0.2713`, calibration_gap `0.1774`
- 5d: hit_rate `0.5000`, avg `0.0054`, median `-0.0017`, brier `0.3016`, calibration_gap `0.2399`
- 10d: hit_rate `0.7500`, avg `0.0180`, median `0.0274`, brier `0.1848`, calibration_gap `-0.0101`
- 20d: hit_rate `0.7500`, avg `0.0296`, median `0.0314`, brier `0.1846`, calibration_gap `-0.0101`
- 60d: hit_rate `0.8125`, avg `0.0540`, median `0.0669`, brier `0.1551`, calibration_gap `-0.0726`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `0.0031`, median `0.0063`, brier `0.2376`, calibration_gap `0.0637`
- 5d: hit_rate `0.6167`, avg `0.0082`, median `0.0101`, brier `0.2489`, calibration_gap `0.0637`
- 10d: hit_rate `0.7000`, avg `0.0158`, median `0.0199`, brier `0.2121`, calibration_gap `-0.0196`
- 20d: hit_rate `0.7500`, avg `0.0246`, median `0.0295`, brier `0.1881`, calibration_gap `-0.0696`
- 60d: hit_rate `0.7167`, avg `0.0385`, median `0.0538`, brier `0.2019`, calibration_gap `-0.0363`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0018`, median `0.0029`, brier `0.2645`, calibration_gap `0.1152`
- 5d: hit_rate `0.6875`, avg `0.0088`, median `0.0116`, brier `0.2210`, calibration_gap `-0.0723`
- 10d: hit_rate `0.7500`, avg `0.0152`, median `0.0198`, brier `0.2038`, calibration_gap `-0.1348`
- 20d: hit_rate `0.6250`, avg `0.0145`, median `0.0216`, brier `0.2304`, calibration_gap `-0.0098`
- 60d: hit_rate `0.6250`, avg `0.0470`, median `0.0558`, brier `0.2295`, calibration_gap `-0.0098`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
