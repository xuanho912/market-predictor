# High Confidence Signal Report

Generated at: `2026-09-01T23:34:41.249509+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0013`, median `0.0014`, brier `0.2638`, calibration_gap `0.1946`
- 5d: hit_rate `0.5000`, avg `-0.0030`, median `-0.0009`, brier `0.3465`, calibration_gap `0.3196`
- 10d: hit_rate `0.1250`, avg `-0.0155`, median `-0.0204`, brier `0.5957`, calibration_gap `0.6946`
- 20d: hit_rate `0.3750`, avg `-0.0119`, median `-0.0055`, brier `0.4306`, calibration_gap `0.4446`
- 60d: hit_rate `0.6250`, avg `0.0223`, median `0.0453`, brier `0.2664`, calibration_gap `0.1946`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0005`, median `0.0007`, brier `0.2964`, calibration_gap `0.2394`
- 5d: hit_rate `0.5625`, avg `-0.0029`, median `0.0010`, brier `0.3033`, calibration_gap `0.2394`
- 10d: hit_rate `0.3750`, avg `-0.0029`, median `-0.0073`, brier `0.4266`, calibration_gap `0.4269`
- 20d: hit_rate `0.6875`, avg `0.0115`, median `0.0250`, brier `0.2386`, calibration_gap `0.1144`
- 60d: hit_rate `0.8125`, avg `0.0540`, median `0.0630`, brier `0.1565`, calibration_gap `-0.0106`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0028`, median `0.0014`, brier `0.2914`, calibration_gap `0.2079`
- 5d: hit_rate `0.5750`, avg `0.0012`, median `0.0016`, brier `0.2833`, calibration_gap `0.1829`
- 10d: hit_rate `0.5250`, avg `0.0039`, median `0.0024`, brier `0.3171`, calibration_gap `0.2329`
- 20d: hit_rate `0.7250`, avg `0.0177`, median `0.0236`, brier `0.2119`, calibration_gap `0.0329`
- 60d: hit_rate `0.7750`, avg `0.0505`, median `0.0655`, brier `0.1825`, calibration_gap `-0.0171`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0119`, median `0.0132`, brier `0.1636`, calibration_gap `-0.1048`
- 5d: hit_rate `0.5625`, avg `0.0078`, median `0.0015`, brier `0.2676`, calibration_gap `0.1452`
- 10d: hit_rate `0.3750`, avg `-0.0056`, median `-0.0132`, brier `0.3458`, calibration_gap `0.3327`
- 20d: hit_rate `0.5625`, avg `0.0035`, median `0.0207`, brier `0.2671`, calibration_gap `0.1452`
- 60d: hit_rate `0.6250`, avg `-0.0031`, median `0.0172`, brier `0.2410`, calibration_gap `0.0827`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
