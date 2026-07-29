# High Confidence Signal Report

Generated at: `2026-07-29T14:33:55.616243+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0059`, median `0.0118`, brier `0.2678`, calibration_gap `0.1949`
- 5d: hit_rate `0.7500`, avg `-0.0015`, median `0.0017`, brier `0.1882`, calibration_gap `0.0699`
- 10d: hit_rate `0.3750`, avg `-0.0005`, median `-0.0008`, brier `0.4287`, calibration_gap `0.4449`
- 20d: hit_rate `0.7500`, avg `0.0359`, median `0.0475`, brier `0.1915`, calibration_gap `0.0699`
- 60d: hit_rate `0.6250`, avg `0.0560`, median `0.1030`, brier `0.2715`, calibration_gap `0.1949`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0028`, median `0.0082`, brier `0.2295`, calibration_gap `0.1222`
- 5d: hit_rate `0.6875`, avg `-0.0055`, median `0.0012`, brier `0.2267`, calibration_gap `0.1222`
- 10d: hit_rate `0.2500`, avg `-0.0054`, median `-0.0068`, brier `0.4967`, calibration_gap `0.5597`
- 20d: hit_rate `0.5625`, avg `0.0197`, median `0.0034`, brier `0.3040`, calibration_gap `0.2472`
- 60d: hit_rate `0.6250`, avg `0.0445`, median `0.0586`, brier `0.2684`, calibration_gap `0.1847`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `-0.0002`, median `0.0017`, brier `0.2646`, calibration_gap `0.1436`
- 5d: hit_rate `0.6000`, avg `-0.0004`, median `0.0026`, brier `0.2714`, calibration_gap `0.1602`
- 10d: hit_rate `0.4500`, avg `0.0001`, median `-0.0036`, brier `0.3579`, calibration_gap `0.3102`
- 20d: hit_rate `0.6167`, avg `0.0188`, median `0.0205`, brier `0.2671`, calibration_gap `0.1436`
- 60d: hit_rate `0.6333`, avg `0.0383`, median `0.0584`, brier `0.2598`, calibration_gap `0.1269`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0057`, median `0.0034`, brier `0.2514`, calibration_gap `0.0804`
- 5d: hit_rate `0.7500`, avg `0.0141`, median `0.0129`, brier `0.1997`, calibration_gap `-0.1071`
- 10d: hit_rate `0.5000`, avg `0.0078`, median `0.0037`, brier `0.2709`, calibration_gap `0.1429`
- 20d: hit_rate `0.7500`, avg `0.0423`, median `0.0636`, brier `0.2002`, calibration_gap `-0.1071`
- 60d: hit_rate `0.8750`, avg `0.0740`, median `0.0593`, brier `0.1649`, calibration_gap `-0.2321`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
