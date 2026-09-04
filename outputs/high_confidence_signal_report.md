# High Confidence Signal Report

Generated at: `2026-09-04T16:25:31.535886+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0092`, median `-0.0095`, brier `0.3795`, calibration_gap `0.3807`
- 5d: hit_rate `0.5000`, avg `-0.0069`, median `-0.0045`, brier `0.3199`, calibration_gap `0.2557`
- 10d: hit_rate `0.1250`, avg `-0.0175`, median `-0.0221`, brier `0.5093`, calibration_gap `0.6307`
- 20d: hit_rate `0.3750`, avg `0.0049`, median `-0.0047`, brier `0.3762`, calibration_gap `0.3807`
- 60d: hit_rate `1.0000`, avg `0.0540`, median `0.0537`, brier `0.0598`, calibration_gap `-0.2443`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0031`, median `0.0014`, brier `0.2830`, calibration_gap `0.1851`
- 5d: hit_rate `0.6250`, avg `-0.0008`, median `0.0026`, brier `0.2532`, calibration_gap `0.1226`
- 10d: hit_rate `0.1875`, avg `-0.0118`, median `-0.0189`, brier `0.4678`, calibration_gap `0.5601`
- 20d: hit_rate `0.6250`, avg `0.0110`, median `0.0048`, brier `0.2520`, calibration_gap `0.1226`
- 60d: hit_rate `0.8750`, avg `0.0394`, median `0.0537`, brier `0.1245`, calibration_gap `-0.1274`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5167`, avg `-0.0020`, median `0.0011`, brier `0.2921`, calibration_gap `0.2081`
- 5d: hit_rate `0.5167`, avg `-0.0004`, median `0.0003`, brier `0.2924`, calibration_gap `0.2081`
- 10d: hit_rate `0.4500`, avg `0.0032`, median `-0.0048`, brier `0.3251`, calibration_gap `0.2747`
- 20d: hit_rate `0.7333`, avg `0.0163`, median `0.0247`, brier `0.1954`, calibration_gap `-0.0086`
- 60d: hit_rate `0.7333`, avg `0.0377`, median `0.0609`, brier `0.1953`, calibration_gap `-0.0086`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0024`, median `0.0020`, brier `0.2931`, calibration_gap `0.2074`
- 5d: hit_rate `0.4375`, avg `-0.0009`, median `-0.0043`, brier `0.3186`, calibration_gap `0.2699`
- 10d: hit_rate `0.3750`, avg `-0.0001`, median `-0.0082`, brier `0.3454`, calibration_gap `0.3324`
- 20d: hit_rate `0.4375`, avg `0.0055`, median `-0.0072`, brier `0.3196`, calibration_gap `0.2699`
- 60d: hit_rate `0.6250`, avg `0.0333`, median `0.0636`, brier `0.2416`, calibration_gap `0.0824`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
