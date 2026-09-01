# High Confidence Signal Report

Generated at: `2026-09-01T08:56:23.714381+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0018`, median `0.0012`, brier `0.1923`, calibration_gap `0.0294`
- 5d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0029`, brier `0.3247`, calibration_gap `0.2794`
- 10d: hit_rate `0.3750`, avg `-0.0044`, median `-0.0073`, brier `0.4063`, calibration_gap `0.4044`
- 20d: hit_rate `0.6250`, avg `0.0123`, median `0.0166`, brier `0.2602`, calibration_gap `0.1544`
- 60d: hit_rate `0.8750`, avg `0.0486`, median `0.0588`, brier `0.1190`, calibration_gap `-0.0956`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0060`, median `-0.0026`, brier `0.3844`, calibration_gap `0.3943`
- 5d: hit_rate `0.4375`, avg `-0.0074`, median `-0.0084`, brier `0.3530`, calibration_gap `0.3318`
- 10d: hit_rate `0.3750`, avg `-0.0067`, median `-0.0109`, brier `0.3945`, calibration_gap `0.3943`
- 20d: hit_rate `0.6250`, avg `0.0025`, median `0.0166`, brier `0.2565`, calibration_gap `0.1443`
- 60d: hit_rate `0.7500`, avg `0.0354`, median `0.0519`, brier `0.1855`, calibration_gap `0.0193`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5125`, avg `-0.0015`, median `0.0007`, brier `0.2952`, calibration_gap `0.2119`
- 5d: hit_rate `0.5000`, avg `-0.0021`, median `-0.0011`, brier `0.2988`, calibration_gap `0.2244`
- 10d: hit_rate `0.4125`, avg `0.0005`, median `-0.0073`, brier `0.3411`, calibration_gap `0.3119`
- 20d: hit_rate `0.7000`, avg `0.0114`, median `0.0185`, brier `0.2122`, calibration_gap `0.0244`
- 60d: hit_rate `0.7125`, avg `0.0365`, median `0.0518`, brier `0.2083`, calibration_gap `0.0119`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0046`, median `-0.0058`, brier `0.2779`, calibration_gap `0.1752`
- 5d: hit_rate `0.3750`, avg `-0.0069`, median `-0.0103`, brier `0.3207`, calibration_gap `0.3002`
- 10d: hit_rate `0.3750`, avg `-0.0025`, median `-0.0131`, brier `0.3239`, calibration_gap `0.3002`
- 20d: hit_rate `0.6250`, avg `0.0095`, median `0.0064`, brier `0.2399`, calibration_gap `0.0502`
- 60d: hit_rate `0.8750`, avg `0.0671`, median `0.0590`, brier `0.1514`, calibration_gap `-0.1998`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
