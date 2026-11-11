# High Confidence Signal Report

Generated at: `2026-11-11T19:38:46.232131+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.1250`, avg `-0.0094`, median `-0.0065`, brier `0.5034`, calibration_gap `0.6300`
- 5d: hit_rate `0.1250`, avg `-0.0131`, median `-0.0150`, brier `0.5075`, calibration_gap `0.6300`
- 10d: hit_rate `0.7500`, avg `0.0114`, median `0.0137`, brier `0.1815`, calibration_gap `0.0050`
- 20d: hit_rate `0.8750`, avg `0.0210`, median `0.0289`, brier `0.1203`, calibration_gap `-0.1200`
- 60d: hit_rate `1.0000`, avg `0.0770`, median `0.0874`, brier `0.0601`, calibration_gap `-0.2450`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0033`, median `-0.0051`, brier `0.4037`, calibration_gap `0.4323`
- 5d: hit_rate `0.3125`, avg `-0.0040`, median `-0.0113`, brier `0.4056`, calibration_gap `0.4323`
- 10d: hit_rate `0.6250`, avg `0.0121`, median `0.0108`, brier `0.2440`, calibration_gap `0.1198`
- 20d: hit_rate `0.8750`, avg `0.0254`, median `0.0240`, brier `0.1250`, calibration_gap `-0.1302`
- 60d: hit_rate `1.0000`, avg `0.0684`, median `0.0798`, brier `0.0653`, calibration_gap `-0.2552`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4500`, avg `-0.0006`, median `-0.0017`, brier `0.3195`, calibration_gap `0.2488`
- 5d: hit_rate `0.4667`, avg `-0.0007`, median `-0.0056`, brier `0.3094`, calibration_gap `0.2321`
- 10d: hit_rate `0.5500`, avg `0.0067`, median `0.0063`, brier `0.2769`, calibration_gap `0.1488`
- 20d: hit_rate `0.8000`, avg `0.0217`, median `0.0248`, brier `0.1696`, calibration_gap `-0.1012`
- 60d: hit_rate `0.7333`, avg `0.0369`, median `0.0567`, brier `0.1942`, calibration_gap `-0.0345`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0044`, median `0.0036`, brier `0.2537`, calibration_gap `0.0705`
- 5d: hit_rate `0.5000`, avg `0.0001`, median `0.0011`, brier `0.2698`, calibration_gap `0.1330`
- 10d: hit_rate `0.6250`, avg `0.0070`, median `0.0049`, brier `0.2355`, calibration_gap `0.0080`
- 20d: hit_rate `0.7500`, avg `0.0175`, median `0.0191`, brier `0.1996`, calibration_gap `-0.1170`
- 60d: hit_rate `0.6875`, avg `0.0280`, median `0.0653`, brier `0.2150`, calibration_gap `-0.0545`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
