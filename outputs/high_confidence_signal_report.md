# High Confidence Signal Report

Generated at: `2026-09-03T22:42:30.489794+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0027`, median `-0.0035`, brier `0.3189`, calibration_gap `0.2596`
- 5d: hit_rate `0.6250`, avg `0.0005`, median `0.0038`, brier `0.2547`, calibration_gap `0.1346`
- 10d: hit_rate `0.1250`, avg `-0.0165`, median `-0.0218`, brier `0.5130`, calibration_gap `0.6346`
- 20d: hit_rate `0.3750`, avg `-0.0088`, median `-0.0047`, brier `0.3793`, calibration_gap `0.3846`
- 60d: hit_rate `0.8750`, avg `0.0179`, median `0.0396`, brier `0.1223`, calibration_gap `-0.1154`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0035`, median `0.0022`, brier `0.2536`, calibration_gap `0.1269`
- 5d: hit_rate `0.6875`, avg `0.0068`, median `0.0051`, brier `0.2215`, calibration_gap `0.0644`
- 10d: hit_rate `0.3125`, avg `-0.0040`, median `-0.0147`, brier `0.4111`, calibration_gap `0.4394`
- 20d: hit_rate `0.6250`, avg `0.0082`, median `0.0142`, brier `0.2534`, calibration_gap `0.1269`
- 60d: hit_rate `0.8750`, avg `0.0287`, median `0.0479`, brier `0.1241`, calibration_gap `-0.1231`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5833`, avg `0.0004`, median `0.0027`, brier `0.2639`, calibration_gap `0.1428`
- 5d: hit_rate `0.5500`, avg `0.0018`, median `0.0021`, brier `0.2784`, calibration_gap `0.1761`
- 10d: hit_rate `0.4833`, avg `0.0022`, median `-0.0008`, brier `0.3110`, calibration_gap `0.2428`
- 20d: hit_rate `0.7000`, avg `0.0134`, median `0.0236`, brier `0.2112`, calibration_gap `0.0261`
- 60d: hit_rate `0.7667`, avg `0.0362`, median `0.0518`, brier `0.1810`, calibration_gap `-0.0405`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0005`, median `0.0034`, brier `0.2683`, calibration_gap `0.1462`
- 5d: hit_rate `0.5000`, avg `-0.0009`, median `-0.0011`, brier `0.2933`, calibration_gap `0.2087`
- 10d: hit_rate `0.4375`, avg `-0.0008`, median `-0.0008`, brier `0.3195`, calibration_gap `0.2712`
- 20d: hit_rate `0.6250`, avg `0.0113`, median `0.0262`, brier `0.2402`, calibration_gap `0.0837`
- 60d: hit_rate `0.7500`, avg `0.0497`, median `0.0751`, brier `0.1890`, calibration_gap `-0.0413`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
