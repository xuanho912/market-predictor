# High Confidence Signal Report

Generated at: `2026-10-14T09:04:06.596862+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `-0.0054`, median `-0.0033`, brier `0.3168`, calibration_gap `0.2550`
- 5d: hit_rate `0.5000`, avg `-0.0033`, median `-0.0042`, brier `0.3168`, calibration_gap `0.2550`
- 10d: hit_rate `0.6250`, avg `0.0013`, median `0.0003`, brier `0.2541`, calibration_gap `0.1300`
- 20d: hit_rate `0.6250`, avg `0.0166`, median `0.0173`, brier `0.2491`, calibration_gap `0.1300`
- 60d: hit_rate `0.7500`, avg `0.0161`, median `0.0177`, brier `0.1859`, calibration_gap `0.0050`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0023`, median `0.0011`, brier `0.2828`, calibration_gap `0.1848`
- 5d: hit_rate `0.5000`, avg `-0.0078`, median `-0.0029`, brier `0.3123`, calibration_gap `0.2473`
- 10d: hit_rate `0.3750`, avg `-0.0107`, median `-0.0116`, brier `0.3696`, calibration_gap `0.3723`
- 20d: hit_rate `0.5625`, avg `0.0100`, median `0.0078`, brier `0.2778`, calibration_gap `0.1848`
- 60d: hit_rate `0.7500`, avg `0.0216`, median `0.0378`, brier `0.1858`, calibration_gap `-0.0027`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4667`, avg `-0.0044`, median `-0.0016`, brier `0.3065`, calibration_gap `0.2327`
- 5d: hit_rate `0.4667`, avg `-0.0082`, median `-0.0106`, brier `0.3077`, calibration_gap `0.2327`
- 10d: hit_rate `0.4000`, avg `-0.0095`, median `-0.0074`, brier `0.3355`, calibration_gap `0.2993`
- 20d: hit_rate `0.6167`, avg `0.0076`, median `0.0122`, brier `0.2453`, calibration_gap `0.0827`
- 60d: hit_rate `0.6833`, avg `0.0213`, median `0.0397`, brier `0.2155`, calibration_gap `0.0160`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `-0.0001`, median `0.0071`, brier `0.2523`, calibration_gap `0.0957`
- 5d: hit_rate `0.5625`, avg `-0.0021`, median `0.0010`, brier `0.2517`, calibration_gap `0.0957`
- 10d: hit_rate `0.5625`, avg `-0.0025`, median `0.0014`, brier `0.2575`, calibration_gap `0.0957`
- 20d: hit_rate `0.5625`, avg `0.0076`, median `0.0070`, brier `0.2569`, calibration_gap `0.0957`
- 60d: hit_rate `0.6875`, avg `0.0325`, median `0.0303`, brier `0.2147`, calibration_gap `-0.0293`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
