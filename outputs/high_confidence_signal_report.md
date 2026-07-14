# High Confidence Signal Report

Generated at: `2026-07-14T21:30:01.028010+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0030`, median `-0.0032`, brier `0.3437`, calibration_gap `0.3306`
- 5d: hit_rate `0.7500`, avg `0.0029`, median `0.0049`, brier `0.1927`, calibration_gap `-0.0444`
- 10d: hit_rate `0.6250`, avg `0.0007`, median `0.0039`, brier `0.2446`, calibration_gap `0.0806`
- 20d: hit_rate `0.3750`, avg `-0.0005`, median `-0.0037`, brier `0.3372`, calibration_gap `0.3306`
- 60d: hit_rate `0.5000`, avg `-0.0202`, median `-0.0120`, brier `0.2903`, calibration_gap `0.2056`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0059`, median `-0.0032`, brier `0.3405`, calibration_gap `0.3256`
- 5d: hit_rate `0.4375`, avg `-0.0043`, median `-0.0027`, brier `0.3139`, calibration_gap `0.2631`
- 10d: hit_rate `0.5000`, avg `-0.0051`, median `-0.0007`, brier `0.2910`, calibration_gap `0.2006`
- 20d: hit_rate `0.6250`, avg `0.0103`, median `0.0083`, brier `0.2393`, calibration_gap `0.0756`
- 60d: hit_rate `0.6250`, avg `0.0146`, median `0.0309`, brier `0.2404`, calibration_gap `0.0756`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.7000`, avg `0.0061`, median `0.0066`, brier `0.2129`, calibration_gap `-0.0174`
- 5d: hit_rate `0.6500`, avg `0.0090`, median `0.0095`, brier `0.2343`, calibration_gap `0.0326`
- 10d: hit_rate `0.5500`, avg `0.0026`, median `0.0042`, brier `0.2678`, calibration_gap `0.1326`
- 20d: hit_rate `0.6500`, avg `0.0099`, median `0.0169`, brier `0.2303`, calibration_gap `0.0326`
- 60d: hit_rate `0.6500`, avg `0.0212`, median `0.0276`, brier `0.2298`, calibration_gap `0.0326`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0089`, median `0.0124`, brier `0.1726`, calibration_gap `-0.1423`
- 5d: hit_rate `0.8750`, avg `0.0113`, median `0.0124`, brier `0.1516`, calibration_gap `-0.2048`
- 10d: hit_rate `0.5625`, avg `0.0104`, median `0.0133`, brier `0.2574`, calibration_gap `0.1077`
- 20d: hit_rate `0.8125`, avg `0.0183`, median `0.0202`, brier `0.1718`, calibration_gap `-0.1423`
- 60d: hit_rate `0.6875`, avg `0.0213`, median `0.0196`, brier `0.2152`, calibration_gap `-0.0173`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
