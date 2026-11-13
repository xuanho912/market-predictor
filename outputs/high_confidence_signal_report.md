# High Confidence Signal Report

Generated at: `2026-11-13T02:17:54.056048+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.7500`, avg `0.0096`, median `0.0127`, brier `0.2013`, calibration_gap `-0.0722`
- 5d: hit_rate `0.7500`, avg `0.0130`, median `0.0148`, brier `0.2013`, calibration_gap `-0.0722`
- 10d: hit_rate `0.7500`, avg `0.0198`, median `0.0223`, brier `0.2013`, calibration_gap `-0.0722`
- 20d: hit_rate `1.0000`, avg `0.0378`, median `0.0313`, brier `0.1041`, calibration_gap `-0.3222`
- 60d: hit_rate `1.0000`, avg `0.0900`, median `0.0898`, brier `0.1041`, calibration_gap `-0.3222`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.8125`, avg `0.0124`, median `0.0147`, brier `0.1830`, calibration_gap `-0.1546`
- 5d: hit_rate `0.8750`, avg `0.0184`, median `0.0214`, brier `0.1661`, calibration_gap `-0.2171`
- 10d: hit_rate `0.8125`, avg `0.0254`, median `0.0259`, brier `0.1830`, calibration_gap `-0.1546`
- 20d: hit_rate `1.0000`, avg `0.0446`, median `0.0360`, brier `0.1175`, calibration_gap `-0.3421`
- 60d: hit_rate `1.0000`, avg `0.0975`, median `0.0937`, brier `0.1175`, calibration_gap `-0.3421`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.7500`, avg `0.0115`, median `0.0127`, brier `0.2192`, calibration_gap `-0.1577`
- 5d: hit_rate `0.7375`, avg `0.0154`, median `0.0179`, brier `0.2219`, calibration_gap `-0.1452`
- 10d: hit_rate `0.7125`, avg `0.0206`, median `0.0264`, brier `0.2220`, calibration_gap `-0.1202`
- 20d: hit_rate `0.8750`, avg `0.0423`, median `0.0380`, brier `0.1898`, calibration_gap `-0.2827`
- 60d: hit_rate `0.9250`, avg `0.0985`, median `0.0980`, brier `0.1767`, calibration_gap `-0.3327`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.8750`, avg `0.0176`, median `0.0161`, brier `0.2263`, calibration_gap `-0.3440`
- 5d: hit_rate `0.8750`, avg `0.0244`, median `0.0211`, brier `0.2284`, calibration_gap `-0.3440`
- 10d: hit_rate `0.6875`, avg `0.0295`, median `0.0337`, brier `0.2373`, calibration_gap `-0.1565`
- 20d: hit_rate `0.9375`, avg `0.0528`, median `0.0408`, brier `0.2249`, calibration_gap `-0.4065`
- 60d: hit_rate `0.8125`, avg `0.1171`, median `0.1069`, brier `0.2321`, calibration_gap `-0.2815`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
