# High Confidence Signal Report

Generated at: `2026-08-07T13:42:37.297571+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0046`, median `0.0069`, brier `0.1312`, calibration_gap `-0.1536`
- 5d: hit_rate `0.8750`, avg `0.0069`, median `0.0112`, brier `0.1312`, calibration_gap `-0.1536`
- 10d: hit_rate `0.8750`, avg `0.0149`, median `0.0199`, brier `0.1312`, calibration_gap `-0.1536`
- 20d: hit_rate `0.5000`, avg `0.0083`, median `0.0002`, brier `0.3026`, calibration_gap `0.2214`
- 60d: hit_rate `0.3750`, avg `0.0028`, median `-0.0336`, brier `0.3543`, calibration_gap `0.3464`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0003`, median `0.0008`, brier `0.2602`, calibration_gap `0.1469`
- 5d: hit_rate `0.6875`, avg `0.0027`, median `0.0089`, brier `0.2104`, calibration_gap `0.0219`
- 10d: hit_rate `0.6250`, avg `0.0082`, median `0.0127`, brier `0.2348`, calibration_gap `0.0844`
- 20d: hit_rate `0.6875`, avg `0.0174`, median `0.0130`, brier `0.2227`, calibration_gap `0.0219`
- 60d: hit_rate `0.4375`, avg `0.0147`, median `-0.0187`, brier `0.3233`, calibration_gap `0.2719`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6667`, avg `0.0062`, median `0.0097`, brier `0.2235`, calibration_gap `0.0121`
- 5d: hit_rate `0.6833`, avg `0.0070`, median `0.0081`, brier `0.2166`, calibration_gap `-0.0046`
- 10d: hit_rate `0.6333`, avg `0.0097`, median `0.0109`, brier `0.2345`, calibration_gap `0.0454`
- 20d: hit_rate `0.7167`, avg `0.0170`, median `0.0210`, brier `0.2032`, calibration_gap `-0.0379`
- 60d: hit_rate `0.6667`, avg `0.0354`, median `0.0590`, brier `0.2252`, calibration_gap `0.0121`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0088`, median `0.0130`, brier `0.2374`, calibration_gap `0.0381`
- 5d: hit_rate `0.6875`, avg `0.0047`, median `0.0071`, brier `0.2160`, calibration_gap `-0.0244`
- 10d: hit_rate `0.6875`, avg `0.0007`, median `0.0052`, brier `0.2157`, calibration_gap `-0.0244`
- 20d: hit_rate `0.5625`, avg `-0.0117`, median `0.0073`, brier `0.2554`, calibration_gap `0.1006`
- 60d: hit_rate `0.6875`, avg `0.0216`, median `0.0623`, brier `0.2162`, calibration_gap `-0.0244`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
