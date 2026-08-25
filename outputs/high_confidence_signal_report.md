# High Confidence Signal Report

Generated at: `2026-08-25T23:35:43.104606+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0018`, median `0.0012`, brier `0.1980`, calibration_gap `0.0119`
- 5d: hit_rate `0.5000`, avg `-0.0044`, median `-0.0029`, brier `0.3111`, calibration_gap `0.2619`
- 10d: hit_rate `0.2500`, avg `-0.0122`, median `-0.0136`, brier `0.4551`, calibration_gap `0.5119`
- 20d: hit_rate `0.5000`, avg `0.0006`, median `0.0047`, brier `0.3184`, calibration_gap `0.2619`
- 60d: hit_rate `0.7500`, avg `0.0268`, median `0.0453`, brier `0.1846`, calibration_gap `0.0119`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `-0.0002`, median `0.0012`, brier `0.2510`, calibration_gap `0.1242`
- 5d: hit_rate `0.5000`, avg `-0.0037`, median `-0.0029`, brier `0.3077`, calibration_gap `0.2492`
- 10d: hit_rate `0.3125`, avg `-0.0068`, median `-0.0128`, brier `0.4097`, calibration_gap `0.4367`
- 20d: hit_rate `0.5000`, avg `-0.0064`, median `0.0047`, brier `0.3116`, calibration_gap `0.2492`
- 60d: hit_rate `0.5625`, avg `0.0109`, median `0.0314`, brier `0.2752`, calibration_gap `0.1867`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `0.0027`, median `0.0051`, brier `0.2422`, calibration_gap `0.0697`
- 5d: hit_rate `0.5500`, avg `0.0024`, median `0.0034`, brier `0.2645`, calibration_gap `0.1364`
- 10d: hit_rate `0.5667`, avg `0.0057`, median `0.0062`, brier `0.2563`, calibration_gap `0.1197`
- 20d: hit_rate `0.6833`, avg `0.0080`, median `0.0241`, brier `0.2143`, calibration_gap `0.0030`
- 60d: hit_rate `0.6667`, avg `0.0253`, median `0.0299`, brier `0.2247`, calibration_gap `0.0197`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0006`, median `0.0086`, brier `0.2345`, calibration_gap `0.0303`
- 5d: hit_rate `0.3750`, avg `-0.0043`, median `-0.0089`, brier `0.3103`, calibration_gap `0.2803`
- 10d: hit_rate `0.4375`, avg `-0.0038`, median `-0.0021`, brier `0.2927`, calibration_gap `0.2178`
- 20d: hit_rate `0.6250`, avg `0.0014`, median `0.0202`, brier `0.2340`, calibration_gap `0.0303`
- 60d: hit_rate `0.7500`, avg `0.0547`, median `0.0587`, brier `0.1944`, calibration_gap `-0.0947`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
