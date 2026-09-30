# High Confidence Signal Report

Generated at: `2026-09-30T01:41:26.822381+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0036`, median `0.0031`, brier `0.2695`, calibration_gap `0.2040`
- 5d: hit_rate `0.6250`, avg `-0.0010`, median `0.0056`, brier `0.2695`, calibration_gap `0.2040`
- 10d: hit_rate `0.6250`, avg `-0.0017`, median `0.0023`, brier `0.2759`, calibration_gap `0.2040`
- 20d: hit_rate `0.6250`, avg `0.0159`, median `0.0098`, brier `0.2731`, calibration_gap `0.2040`
- 60d: hit_rate `1.0000`, avg `0.0564`, median `0.0565`, brier `0.0293`, calibration_gap `-0.1710`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0019`, median `0.0051`, brier `0.2672`, calibration_gap `0.1925`
- 5d: hit_rate `0.6250`, avg `-0.0001`, median `0.0068`, brier `0.2672`, calibration_gap `0.1925`
- 10d: hit_rate `0.6250`, avg `-0.0040`, median `0.0040`, brier `0.2704`, calibration_gap `0.1925`
- 20d: hit_rate `0.6875`, avg `0.0132`, median `0.0173`, brier `0.2307`, calibration_gap `0.1300`
- 60d: hit_rate `0.8750`, avg `0.0500`, median `0.0565`, brier `0.1088`, calibration_gap `-0.0575`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `-0.0011`, median `0.0018`, brier `0.2887`, calibration_gap `0.2043`
- 5d: hit_rate `0.5167`, avg `-0.0057`, median `0.0007`, brier `0.3002`, calibration_gap `0.2210`
- 10d: hit_rate `0.5333`, avg `-0.0042`, median `0.0027`, brier `0.3002`, calibration_gap `0.2043`
- 20d: hit_rate `0.6667`, avg `0.0112`, median `0.0180`, brier `0.2391`, calibration_gap `0.0710`
- 60d: hit_rate `0.8333`, avg `0.0470`, median `0.0583`, brier `0.1506`, calibration_gap `-0.0957`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0001`, median `0.0001`, brier `0.2722`, calibration_gap `0.1469`
- 5d: hit_rate `0.5625`, avg `-0.0061`, median `0.0009`, brier `0.2495`, calibration_gap `0.0844`
- 10d: hit_rate `0.6875`, avg `0.0065`, median `0.0134`, brier `0.2156`, calibration_gap `-0.0406`
- 20d: hit_rate `0.8125`, avg `0.0217`, median `0.0319`, brier `0.1785`, calibration_gap `-0.1656`
- 60d: hit_rate `0.8125`, avg `0.0410`, median `0.0588`, brier `0.1785`, calibration_gap `-0.1656`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
