# High Confidence Signal Report

Generated at: `2026-08-11T13:48:21.122071+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_useful_proxy`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.8750`, avg `0.0046`, median `0.0069`, brier `0.1315`, calibration_gap `-0.1515`
- 5d: hit_rate `0.8750`, avg `0.0069`, median `0.0112`, brier `0.1315`, calibration_gap `-0.1515`
- 10d: hit_rate `0.8750`, avg `0.0149`, median `0.0199`, brier `0.1315`, calibration_gap `-0.1515`
- 20d: hit_rate `0.5000`, avg `0.0083`, median `0.0002`, brier `0.3032`, calibration_gap `0.2235`
- 60d: hit_rate `0.3750`, avg `0.0028`, median `-0.0336`, brier `0.3552`, calibration_gap `0.3485`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0033`, median `0.0034`, brier `0.2121`, calibration_gap `0.0258`
- 5d: hit_rate `0.8125`, avg `0.0093`, median `0.0112`, brier `0.1613`, calibration_gap `-0.0992`
- 10d: hit_rate `0.7500`, avg `0.0159`, median `0.0179`, brier `0.1863`, calibration_gap `-0.0367`
- 20d: hit_rate `0.6875`, avg `0.0200`, median `0.0158`, brier `0.2214`, calibration_gap `0.0258`
- 60d: hit_rate `0.5000`, avg `0.0200`, median `0.0008`, brier `0.2989`, calibration_gap `0.2133`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6250`, avg `0.0027`, median `0.0051`, brier `0.2380`, calibration_gap `0.0631`
- 5d: hit_rate `0.6625`, avg `0.0046`, median `0.0053`, brier `0.2218`, calibration_gap `0.0256`
- 10d: hit_rate `0.5750`, avg `0.0067`, median `0.0065`, brier `0.2555`, calibration_gap `0.1131`
- 20d: hit_rate `0.6875`, avg `0.0130`, median `0.0146`, brier `0.2156`, calibration_gap `0.0006`
- 60d: hit_rate `0.6000`, avg `0.0303`, median `0.0456`, brier `0.2519`, calibration_gap `0.0881`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0076`, median `0.0093`, brier `0.2157`, calibration_gap `-0.0175`
- 5d: hit_rate `0.5625`, avg `0.0032`, median `0.0057`, brier `0.2593`, calibration_gap `0.1075`
- 10d: hit_rate `0.6250`, avg `0.0010`, median `0.0052`, brier `0.2382`, calibration_gap `0.0450`
- 20d: hit_rate `0.6250`, avg `0.0025`, median `0.0121`, brier `0.2364`, calibration_gap `0.0450`
- 60d: hit_rate `0.8125`, avg `0.0500`, median `0.0724`, brier `0.1729`, calibration_gap `-0.1425`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
