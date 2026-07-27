# High Confidence Signal Report

Generated at: `2026-07-27T15:16:26.231642+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.2500`, avg `-0.0132`, median `-0.0096`, brier `0.4823`, calibration_gap `0.5453`
- 5d: hit_rate `0.5000`, avg `-0.0178`, median `-0.0105`, brier `0.3375`, calibration_gap `0.2953`
- 10d: hit_rate `0.1250`, avg `-0.0090`, median `-0.0074`, brier `0.5610`, calibration_gap `0.6703`
- 20d: hit_rate `0.3750`, avg `0.0071`, median `-0.0046`, brier `0.4157`, calibration_gap `0.4203`
- 60d: hit_rate `0.6250`, avg `0.0347`, median `0.0352`, brier `0.2655`, calibration_gap `0.1703`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.4375`, avg `-0.0077`, median `-0.0054`, brier `0.3709`, calibration_gap `0.3518`
- 5d: hit_rate `0.4375`, avg `-0.0130`, median `-0.0106`, brier `0.3697`, calibration_gap `0.3518`
- 10d: hit_rate `0.3125`, avg `-0.0049`, median `-0.0073`, brier `0.4456`, calibration_gap `0.4768`
- 20d: hit_rate `0.5000`, avg `0.0136`, median `0.0075`, brier `0.3376`, calibration_gap `0.2893`
- 60d: hit_rate `0.6250`, avg `0.0393`, median `0.0439`, brier `0.2624`, calibration_gap `0.1643`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.6167`, avg `-0.0004`, median `0.0031`, brier `0.2641`, calibration_gap `0.1322`
- 5d: hit_rate `0.5833`, avg `-0.0002`, median `0.0036`, brier `0.2835`, calibration_gap `0.1656`
- 10d: hit_rate `0.5500`, avg `0.0087`, median `0.0016`, brier `0.3087`, calibration_gap `0.1989`
- 20d: hit_rate `0.6833`, avg `0.0248`, median `0.0274`, brier `0.2300`, calibration_gap `0.0656`
- 60d: hit_rate `0.7333`, avg `0.0463`, median `0.0588`, brier `0.2016`, calibration_gap `0.0156`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0083`, median `0.0117`, brier `0.2151`, calibration_gap `-0.0026`
- 5d: hit_rate `0.5625`, avg `0.0058`, median `0.0072`, brier `0.2615`, calibration_gap `0.1224`
- 10d: hit_rate `0.6875`, avg `0.0151`, median `0.0274`, brier `0.2144`, calibration_gap `-0.0026`
- 20d: hit_rate `0.5625`, avg `0.0165`, median `0.0281`, brier `0.2612`, calibration_gap `0.1224`
- 60d: hit_rate `0.6250`, avg `0.0241`, median `0.0865`, brier `0.2379`, calibration_gap `0.0599`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
