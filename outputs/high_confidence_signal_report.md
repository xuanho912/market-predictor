# High Confidence Signal Report

Generated at: `2026-07-11T00:09:42.578108+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.3750`, avg `-0.0029`, median `-0.0009`, brier `0.3501`, calibration_gap `0.3396`
- 5d: hit_rate `0.3750`, avg `-0.0030`, median `-0.0032`, brier `0.3501`, calibration_gap `0.3396`
- 10d: hit_rate `0.6250`, avg `-0.0007`, median `0.0082`, brier `0.2435`, calibration_gap `0.0896`
- 20d: hit_rate `0.3750`, avg `-0.0217`, median `-0.0101`, brier `0.3472`, calibration_gap `0.3396`
- 60d: hit_rate `0.2500`, avg `-0.0321`, median `-0.0398`, brier `0.3992`, calibration_gap `0.4646`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0012`, median `0.0019`, brier `0.2951`, calibration_gap `0.2080`
- 5d: hit_rate `0.5625`, avg `0.0029`, median `0.0049`, brier `0.2695`, calibration_gap `0.1455`
- 10d: hit_rate `0.5000`, avg `-0.0004`, median `0.0026`, brier `0.2920`, calibration_gap `0.2080`
- 20d: hit_rate `0.5000`, avg `-0.0083`, median `-0.0005`, brier `0.2932`, calibration_gap `0.2080`
- 60d: hit_rate `0.4375`, avg `-0.0101`, median `-0.0305`, brier `0.3200`, calibration_gap `0.2705`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.5167`, avg `-0.0026`, median `0.0008`, brier `0.2804`, calibration_gap `0.1674`
- 5d: hit_rate `0.5333`, avg `-0.0027`, median `0.0028`, brier `0.2722`, calibration_gap `0.1507`
- 10d: hit_rate `0.5833`, avg `0.0038`, median `0.0032`, brier `0.2558`, calibration_gap `0.1007`
- 20d: hit_rate `0.6833`, avg `0.0046`, median `0.0120`, brier `0.2184`, calibration_gap `0.0007`
- 60d: hit_rate `0.5167`, avg `0.0040`, median `0.0151`, brier `0.2816`, calibration_gap `0.1674`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0020`, median `0.0028`, brier `0.2559`, calibration_gap `0.0985`
- 5d: hit_rate `0.5000`, avg `0.0017`, median `0.0020`, brier `0.2757`, calibration_gap `0.1610`
- 10d: hit_rate `0.6250`, avg `0.0130`, median `0.0096`, brier `0.2371`, calibration_gap `0.0360`
- 20d: hit_rate `0.8750`, avg `0.0175`, median `0.0116`, brier `0.1550`, calibration_gap `-0.2140`
- 60d: hit_rate `0.5625`, avg `0.0101`, median `0.0300`, brier `0.2557`, calibration_gap `0.0985`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
