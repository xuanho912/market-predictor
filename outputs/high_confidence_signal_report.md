# High Confidence Signal Report

Generated at: `2026-08-13T23:54:10.895374+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `60`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `6`
- 3d: hit_rate `1.0000`, avg `0.0118`, median `0.0129`, brier `0.0753`, calibration_gap `-0.2742`
- 5d: hit_rate `0.8333`, avg `0.0069`, median `0.0089`, brier `0.1498`, calibration_gap `-0.1075`
- 10d: hit_rate `0.8333`, avg `0.0117`, median `0.0127`, brier `0.1481`, calibration_gap `-0.1075`
- 20d: hit_rate `0.3333`, avg `-0.0066`, median `-0.0092`, brier `0.3805`, calibration_gap `0.3925`
- 60d: hit_rate `0.1667`, avg `-0.0225`, median `-0.0398`, brier `0.4507`, calibration_gap `0.5592`

### top_20_confidence_signals
- sample_size: `12`
- 3d: hit_rate `0.8333`, avg `0.0070`, median `0.0065`, brier `0.1499`, calibration_gap `-0.1239`
- 5d: hit_rate `0.8333`, avg `0.0074`, median `0.0091`, brier `0.1555`, calibration_gap `-0.1239`
- 10d: hit_rate `0.8333`, avg `0.0128`, median `0.0164`, brier `0.1528`, calibration_gap `-0.1239`
- 20d: hit_rate `0.5833`, avg `0.0044`, median `0.0048`, brier `0.2690`, calibration_gap `0.1261`
- 60d: hit_rate `0.3333`, avg `-0.0004`, median `-0.0247`, brier `0.3707`, calibration_gap `0.3761`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6000`, avg `0.0047`, median `0.0050`, brier `0.2422`, calibration_gap `0.0788`
- 5d: hit_rate `0.6667`, avg `0.0051`, median `0.0057`, brier `0.2195`, calibration_gap `0.0121`
- 10d: hit_rate `0.5833`, avg `0.0076`, median `0.0082`, brier `0.2497`, calibration_gap `0.0955`
- 20d: hit_rate `0.6500`, avg `0.0110`, median `0.0127`, brier `0.2314`, calibration_gap `0.0288`
- 60d: hit_rate `0.6667`, avg `0.0283`, median `0.0448`, brier `0.2301`, calibration_gap `0.0121`

### low_confidence_reference
- sample_size: `12`
- 3d: hit_rate `0.5000`, avg `0.0054`, median `-0.0012`, brier `0.2752`, calibration_gap `0.1587`
- 5d: hit_rate `0.5833`, avg `0.0028`, median `0.0032`, brier `0.2490`, calibration_gap `0.0754`
- 10d: hit_rate `0.6667`, avg `0.0101`, median `0.0090`, brier `0.2235`, calibration_gap `-0.0080`
- 20d: hit_rate `0.6667`, avg `0.0165`, median `0.0197`, brier `0.2235`, calibration_gap `-0.0080`
- 60d: hit_rate `0.8333`, avg `0.0577`, median `0.0730`, brier `0.1703`, calibration_gap `-0.1746`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
