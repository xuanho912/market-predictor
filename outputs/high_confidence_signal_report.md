# High Confidence Signal Report

Generated at: `2026-10-10T00:24:42.393935+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0068`, median `0.0079`, brier `0.1825`, calibration_gap `-0.0335`
- 5d: hit_rate `0.6250`, avg `0.0034`, median `0.0074`, brier `0.2339`, calibration_gap `0.0915`
- 10d: hit_rate `0.8750`, avg `0.0070`, median `0.0060`, brier `0.1320`, calibration_gap `-0.1585`
- 20d: hit_rate `0.7500`, avg `0.0337`, median `0.0460`, brier `0.1825`, calibration_gap `-0.0335`
- 60d: hit_rate `0.8750`, avg `0.0681`, median `0.0751`, brier `0.1320`, calibration_gap `-0.1585`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0017`, median `0.0079`, brier `0.2339`, calibration_gap `0.0683`
- 5d: hit_rate `0.6250`, avg `0.0025`, median `0.0080`, brier `0.2357`, calibration_gap `0.0683`
- 10d: hit_rate `0.6875`, avg `0.0023`, median `0.0060`, brier `0.2087`, calibration_gap `0.0058`
- 20d: hit_rate `0.8750`, avg `0.0325`, median `0.0414`, brier `0.1457`, calibration_gap `-0.1817`
- 60d: hit_rate `0.9375`, avg `0.0914`, median `0.0922`, brier `0.1205`, calibration_gap `-0.2442`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5667`, avg `0.0018`, median `0.0041`, brier `0.2470`, calibration_gap `0.0548`
- 5d: hit_rate `0.5000`, avg `0.0013`, median `0.0011`, brier `0.2606`, calibration_gap `0.1215`
- 10d: hit_rate `0.6000`, avg `0.0043`, median `0.0042`, brier `0.2354`, calibration_gap `0.0215`
- 20d: hit_rate `0.8667`, avg `0.0307`, median `0.0318`, brier `0.1774`, calibration_gap `-0.2452`
- 60d: hit_rate `0.8500`, avg `0.0695`, median `0.0843`, brier `0.1752`, calibration_gap `-0.2285`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0011`, median `0.0050`, brier `0.2471`, calibration_gap `0.0009`
- 5d: hit_rate `0.4375`, avg `-0.0031`, median `-0.0093`, brier `0.2646`, calibration_gap `0.1259`
- 10d: hit_rate `0.3125`, avg `-0.0088`, median `-0.0102`, brier `0.2792`, calibration_gap `0.2509`
- 20d: hit_rate `0.5625`, avg `0.0045`, median `0.0051`, brier `0.2480`, calibration_gap `0.0009`
- 60d: hit_rate `0.7500`, avg `0.0572`, median `0.0726`, brier `0.2239`, calibration_gap `-0.1866`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
