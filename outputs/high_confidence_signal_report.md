# High Confidence Signal Report

Generated at: `2026-06-25T23:56:24.308521+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0007`, median `-0.0013`, brier `0.3800`, calibration_gap `0.3828`
- 5d: hit_rate `0.1250`, avg `-0.0108`, median `-0.0108`, brier `0.5097`, calibration_gap `0.6328`
- 10d: hit_rate `0.5000`, avg `0.0046`, median `0.0022`, brier `0.3149`, calibration_gap `0.2578`
- 20d: hit_rate `0.8750`, avg `0.0247`, median `0.0287`, brier `0.1248`, calibration_gap `-0.1172`
- 60d: hit_rate `1.0000`, avg `0.0821`, median `0.0936`, brier `0.0587`, calibration_gap `-0.2422`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0025`, median `0.0004`, brier `0.3127`, calibration_gap `0.2476`
- 5d: hit_rate `0.2500`, avg `-0.0073`, median `-0.0077`, brier `0.4361`, calibration_gap `0.4976`
- 10d: hit_rate `0.4375`, avg `0.0039`, median `-0.0014`, brier `0.3403`, calibration_gap `0.3101`
- 20d: hit_rate `0.9375`, avg `0.0238`, median `0.0265`, brier `0.0969`, calibration_gap `-0.1899`
- 60d: hit_rate `1.0000`, avg `0.0752`, median `0.0745`, brier `0.0639`, calibration_gap `-0.2524`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5333`, avg `0.0036`, median `0.0020`, brier `0.2692`, calibration_gap `0.1281`
- 5d: hit_rate `0.4500`, avg `-0.0007`, median `-0.0038`, brier `0.3068`, calibration_gap `0.2114`
- 10d: hit_rate `0.4667`, avg `0.0027`, median `-0.0014`, brier `0.2966`, calibration_gap `0.1947`
- 20d: hit_rate `0.7667`, avg `0.0187`, median `0.0279`, brier `0.1823`, calibration_gap `-0.1053`
- 60d: hit_rate `0.8167`, avg `0.0582`, median `0.0720`, brier `0.1657`, calibration_gap `-0.1553`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0029`, median `-0.0007`, brier `0.2610`, calibration_gap `0.0975`
- 5d: hit_rate `0.5000`, avg `-0.0004`, median `0.0011`, brier `0.2589`, calibration_gap `0.0975`
- 10d: hit_rate `0.5000`, avg `0.0050`, median `-0.0014`, brier `0.2616`, calibration_gap `0.0975`
- 20d: hit_rate `0.6875`, avg `0.0141`, median `0.0176`, brier `0.2225`, calibration_gap `-0.0900`
- 60d: hit_rate `0.8125`, avg `0.0620`, median `0.0739`, brier `0.1981`, calibration_gap `-0.2150`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
