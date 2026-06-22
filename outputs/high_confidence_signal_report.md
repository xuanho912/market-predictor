# High Confidence Signal Report

Generated at: `2026-06-22T15:54:58.791155+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0058`, median `-0.0061`, brier `0.3619`, calibration_gap `0.3535`
- 5d: hit_rate `0.1250`, avg `-0.0173`, median `-0.0150`, brier `0.4757`, calibration_gap `0.6035`
- 10d: hit_rate `0.5000`, avg `0.0039`, median `0.0025`, brier `0.2996`, calibration_gap `0.2285`
- 20d: hit_rate `1.0000`, avg `0.0278`, median `0.0302`, brier `0.0738`, calibration_gap `-0.2715`
- 60d: hit_rate `1.0000`, avg `0.0737`, median `0.0832`, brier `0.0738`, calibration_gap `-0.2715`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0011`, median `-0.0001`, brier `0.3015`, calibration_gap `0.2212`
- 5d: hit_rate `0.2500`, avg `-0.0113`, median `-0.0130`, brier `0.4128`, calibration_gap `0.4712`
- 10d: hit_rate `0.3750`, avg `-0.0003`, median `-0.0016`, brier `0.3511`, calibration_gap `0.3462`
- 20d: hit_rate `0.9375`, avg `0.0282`, median `0.0297`, brier `0.1043`, calibration_gap `-0.2163`
- 60d: hit_rate `0.9375`, avg `0.0694`, median `0.0832`, brier `0.1039`, calibration_gap `-0.2163`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4667`, avg `-0.0001`, median `-0.0014`, brier `0.2989`, calibration_gap `0.2100`
- 5d: hit_rate `0.4667`, avg `-0.0034`, median `-0.0054`, brier `0.3054`, calibration_gap `0.2100`
- 10d: hit_rate `0.4000`, avg `-0.0027`, median `-0.0022`, brier `0.3225`, calibration_gap `0.2767`
- 20d: hit_rate `0.7500`, avg `0.0103`, median `0.0179`, brier `0.1853`, calibration_gap `-0.0733`
- 60d: hit_rate `0.6333`, avg `0.0241`, median `0.0400`, brier `0.2278`, calibration_gap `0.0434`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0001`, median `0.0028`, brier `0.2352`, calibration_gap `-0.0060`
- 5d: hit_rate `0.6250`, avg `0.0007`, median `0.0043`, brier `0.2351`, calibration_gap `-0.0060`
- 10d: hit_rate `0.4375`, avg `0.0010`, median `-0.0022`, brier `0.2804`, calibration_gap `0.1815`
- 20d: hit_rate `0.6250`, avg `0.0070`, median `0.0068`, brier `0.2350`, calibration_gap `-0.0060`
- 60d: hit_rate `0.6875`, avg `0.0231`, median `0.0557`, brier `0.2193`, calibration_gap `-0.0685`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
