# High Confidence Signal Report

Generated at: `2026-11-17T04:10:33.272866+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0012`, median `-0.0014`, brier `0.3401`, calibration_gap `0.3060`
- 5d: hit_rate `0.5000`, avg `-0.0103`, median `-0.0064`, brier `0.3401`, calibration_gap `0.3060`
- 10d: hit_rate `0.3750`, avg `-0.0035`, median `-0.0036`, brier `0.4200`, calibration_gap `0.4310`
- 20d: hit_rate `0.6250`, avg `0.0183`, median `0.0189`, brier `0.2656`, calibration_gap `0.1810`
- 60d: hit_rate `0.5000`, avg `0.0318`, median `0.0271`, brier `0.3411`, calibration_gap `0.3060`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3750`, avg `-0.0059`, median `-0.0101`, brier `0.4093`, calibration_gap `0.4221`
- 5d: hit_rate `0.4375`, avg `-0.0111`, median `-0.0108`, brier `0.3727`, calibration_gap `0.3596`
- 10d: hit_rate `0.3750`, avg `-0.0032`, median `-0.0060`, brier `0.4132`, calibration_gap `0.4221`
- 20d: hit_rate `0.5625`, avg `0.0130`, median `0.0184`, brier `0.2995`, calibration_gap `0.2346`
- 60d: hit_rate `0.5000`, avg `0.0221`, median `0.0117`, brier `0.3389`, calibration_gap `0.2971`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5000`, avg `0.0008`, median `-0.0001`, brier `0.3210`, calibration_gap `0.2240`
- 5d: hit_rate `0.5000`, avg `-0.0030`, median `-0.0001`, brier `0.3201`, calibration_gap `0.2240`
- 10d: hit_rate `0.4667`, avg `0.0013`, median `-0.0015`, brier `0.3238`, calibration_gap `0.2573`
- 20d: hit_rate `0.7000`, avg `0.0199`, median `0.0293`, brier `0.2218`, calibration_gap `0.0240`
- 60d: hit_rate `0.6667`, avg `0.0444`, median `0.0702`, brier `0.2321`, calibration_gap `0.0573`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0017`, median `0.0073`, brier `0.2486`, calibration_gap `0.0527`
- 5d: hit_rate `0.5625`, avg `0.0022`, median `0.0089`, brier `0.2487`, calibration_gap `0.0527`
- 10d: hit_rate `0.5625`, avg `-0.0069`, median `0.0063`, brier `0.2491`, calibration_gap `0.0527`
- 20d: hit_rate `0.6875`, avg `0.0173`, median `0.0177`, brier `0.2219`, calibration_gap `-0.0723`
- 60d: hit_rate `0.6250`, avg `0.0329`, median `0.0301`, brier `0.2358`, calibration_gap `-0.0098`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
