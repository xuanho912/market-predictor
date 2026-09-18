# High Confidence Signal Report

Generated at: `2026-09-18T00:54:01.605109+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0090`, median `0.0116`, brier `0.1280`, calibration_gap `-0.1337`
- 5d: hit_rate `0.8750`, avg `0.0096`, median `0.0089`, brier `0.1369`, calibration_gap `-0.1337`
- 10d: hit_rate `0.7500`, avg `0.0068`, median `0.0074`, brier `0.1975`, calibration_gap `-0.0087`
- 20d: hit_rate `1.0000`, avg `0.0519`, median `0.0548`, brier `0.0674`, calibration_gap `-0.2587`
- 60d: hit_rate `0.8750`, avg `0.0724`, median `0.0751`, brier `0.1369`, calibration_gap `-0.1337`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0004`, median `0.0031`, brier `0.2463`, calibration_gap `0.1457`
- 5d: hit_rate `0.5625`, avg `0.0004`, median `0.0073`, brier `0.2508`, calibration_gap `0.1457`
- 10d: hit_rate `0.6250`, avg `0.0015`, median `0.0040`, brier `0.2418`, calibration_gap `0.0832`
- 20d: hit_rate `0.8750`, avg `0.0402`, median `0.0460`, brier `0.1260`, calibration_gap `-0.1668`
- 60d: hit_rate `0.9375`, avg `0.0906`, median `0.0922`, brier `0.1214`, calibration_gap `-0.2293`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.5875`, avg `0.0023`, median `0.0054`, brier `0.2407`, calibration_gap `0.0343`
- 5d: hit_rate `0.5625`, avg `0.0032`, median `0.0065`, brier `0.2475`, calibration_gap `0.0593`
- 10d: hit_rate `0.6625`, avg `0.0102`, median `0.0096`, brier `0.2294`, calibration_gap `-0.0407`
- 20d: hit_rate `0.8125`, avg `0.0321`, median `0.0346`, brier `0.1862`, calibration_gap `-0.1907`
- 60d: hit_rate `0.8000`, avg `0.0697`, median `0.0896`, brier `0.1874`, calibration_gap `-0.1782`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0078`, median `-0.0017`, brier `0.2556`, calibration_gap `0.0676`
- 5d: hit_rate `0.5000`, avg `-0.0047`, median `-0.0032`, brier `0.2544`, calibration_gap `0.0676`
- 10d: hit_rate `0.6250`, avg `0.0061`, median `0.0073`, brier `0.2408`, calibration_gap `-0.0574`
- 20d: hit_rate `0.7500`, avg `0.0322`, median `0.0490`, brier `0.2203`, calibration_gap `-0.1824`
- 60d: hit_rate `0.6250`, avg `0.0291`, median `0.0644`, brier `0.2409`, calibration_gap `-0.0574`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
