# High Confidence Signal Report

Generated at: `2026-09-08T22:49:59.078373+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0033`, median `-0.0004`, brier `0.3191`, calibration_gap `0.2726`
- 5d: hit_rate `0.5000`, avg `-0.0065`, median `-0.0029`, brier `0.3213`, calibration_gap `0.2726`
- 10d: hit_rate `0.1250`, avg `-0.0135`, median `-0.0189`, brier `0.5322`, calibration_gap `0.6476`
- 20d: hit_rate `0.5000`, avg `-0.0001`, median `0.0087`, brier `0.3282`, calibration_gap `0.2726`
- 60d: hit_rate `0.7500`, avg `0.0341`, median `0.0519`, brier `0.1848`, calibration_gap `0.0226`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0062`, median `-0.0060`, brier `0.4094`, calibration_gap `0.4484`
- 5d: hit_rate `0.4375`, avg `-0.0075`, median `-0.0045`, brier `0.3477`, calibration_gap `0.3234`
- 10d: hit_rate `0.2500`, avg `-0.0120`, median `-0.0161`, brier `0.4528`, calibration_gap `0.5109`
- 20d: hit_rate `0.5625`, avg `-0.0046`, median `0.0093`, brier `0.2895`, calibration_gap `0.1984`
- 60d: hit_rate `0.6875`, avg `0.0259`, median `0.0396`, brier `0.2173`, calibration_gap `0.0734`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0012`, median `0.0032`, brier `0.2338`, calibration_gap `0.0673`
- 5d: hit_rate `0.7000`, avg `0.0095`, median `0.0109`, brier `0.2086`, calibration_gap `0.0173`
- 10d: hit_rate `0.5500`, avg `0.0053`, median `0.0025`, brier `0.2786`, calibration_gap `0.1673`
- 20d: hit_rate `0.6000`, avg `0.0095`, median `0.0048`, brier `0.2549`, calibration_gap `0.1173`
- 60d: hit_rate `0.8500`, avg `0.0345`, median `0.0395`, brier `0.1451`, calibration_gap `-0.1327`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0011`, median `-0.0008`, brier `0.2804`, calibration_gap `0.1810`
- 5d: hit_rate `0.4375`, avg `-0.0031`, median `-0.0053`, brier `0.3027`, calibration_gap `0.2435`
- 10d: hit_rate `0.4375`, avg `0.0094`, median `-0.0059`, brier `0.3035`, calibration_gap `0.2435`
- 20d: hit_rate `0.9375`, avg `0.0369`, median `0.0299`, brier `0.1245`, calibration_gap `-0.2565`
- 60d: hit_rate `0.8750`, avg `0.0846`, median `0.0827`, brier `0.1490`, calibration_gap `-0.1940`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
