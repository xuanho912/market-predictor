# High Confidence Signal Report

Generated at: `2026-08-20T04:22:10.474095+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `40`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `4`
- 3d: hit_rate `1.0000`, avg `0.0142`, median `0.0147`, brier `0.0695`, calibration_gap `-0.2637`
- 5d: hit_rate `1.0000`, avg `0.0139`, median `0.0130`, brier `0.0695`, calibration_gap `-0.2637`
- 10d: hit_rate `1.0000`, avg `0.0192`, median `0.0199`, brier `0.0695`, calibration_gap `-0.2637`
- 20d: hit_rate `0.5000`, avg `0.0129`, median `0.0051`, brier `0.3087`, calibration_gap `0.2363`
- 60d: hit_rate `0.5000`, avg `0.0226`, median `0.0233`, brier `0.3087`, calibration_gap `0.2363`

### top_20_confidence_signals
- sample_size: `8`
- 3d: hit_rate `1.0000`, avg `0.0089`, median `0.0069`, brier `0.0761`, calibration_gap `-0.2756`
- 5d: hit_rate `1.0000`, avg `0.0112`, median `0.0112`, brier `0.0761`, calibration_gap `-0.2756`
- 10d: hit_rate `1.0000`, avg `0.0197`, median `0.0202`, brier `0.0761`, calibration_gap `-0.2756`
- 20d: hit_rate `0.5000`, avg `0.0063`, median `0.0002`, brier `0.3038`, calibration_gap `0.2244`
- 60d: hit_rate `0.2500`, avg `-0.0052`, median `-0.0336`, brier `0.4082`, calibration_gap `0.4744`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.5500`, avg `0.0015`, median `0.0015`, brier `0.2595`, calibration_gap `0.1387`
- 5d: hit_rate `0.6500`, avg `0.0050`, median `0.0050`, brier `0.2221`, calibration_gap `0.0387`
- 10d: hit_rate `0.6500`, avg `0.0031`, median `0.0101`, brier `0.2204`, calibration_gap `0.0387`
- 20d: hit_rate `0.7250`, avg `0.0105`, median `0.0125`, brier `0.2047`, calibration_gap `-0.0363`
- 60d: hit_rate `0.5000`, avg `0.0142`, median `0.0002`, brier `0.2896`, calibration_gap `0.1887`

### low_confidence_reference
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0054`, median `0.0111`, brier `0.2360`, calibration_gap `0.0410`
- 5d: hit_rate `0.5000`, avg `0.0010`, median `0.0006`, brier `0.2768`, calibration_gap `0.1660`
- 10d: hit_rate `0.3750`, avg `-0.0127`, median `-0.0016`, brier `0.3189`, calibration_gap `0.2910`
- 20d: hit_rate `0.7500`, avg `0.0061`, median `0.0155`, brier `0.1957`, calibration_gap `-0.0840`
- 60d: hit_rate `0.6250`, avg `0.0323`, median `0.0361`, brier `0.2360`, calibration_gap `0.0410`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
