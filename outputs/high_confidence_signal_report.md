# High Confidence Signal Report

Generated at: `2026-10-23T17:12:06.770030+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0042`, median `0.0017`, brier `0.3402`, calibration_gap `0.2972`
- 5d: hit_rate `0.3750`, avg `0.0019`, median `-0.0051`, brier `0.4164`, calibration_gap `0.4222`
- 10d: hit_rate `0.5000`, avg `0.0080`, median `0.0022`, brier `0.3358`, calibration_gap `0.2972`
- 20d: hit_rate `0.8750`, avg `0.0314`, median `0.0299`, brier `0.1172`, calibration_gap `-0.0778`
- 60d: hit_rate `1.0000`, avg `0.0733`, median `0.0738`, brier `0.0412`, calibration_gap `-0.2028`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0055`, median `0.0029`, brier `0.2973`, calibration_gap `0.2214`
- 5d: hit_rate `0.3750`, avg `-0.0016`, median `-0.0051`, brier `0.4032`, calibration_gap `0.4089`
- 10d: hit_rate `0.4375`, avg `0.0062`, median `-0.0014`, brier `0.3620`, calibration_gap `0.3464`
- 20d: hit_rate `0.8750`, avg `0.0234`, median `0.0278`, brier `0.1186`, calibration_gap `-0.0911`
- 60d: hit_rate `0.9375`, avg `0.0635`, median `0.0738`, brier `0.0806`, calibration_gap `-0.1536`

### strong_signal_only
- sample_size: `40`
- 3d: hit_rate `0.6000`, avg `0.0035`, median `0.0058`, brier `0.2482`, calibration_gap `0.0882`
- 5d: hit_rate `0.6750`, avg `0.0061`, median `0.0092`, brier `0.2166`, calibration_gap `0.0132`
- 10d: hit_rate `0.6500`, avg `0.0078`, median `0.0084`, brier `0.2225`, calibration_gap `0.0382`
- 20d: hit_rate `0.6500`, avg `0.0157`, median `0.0160`, brier `0.2274`, calibration_gap `0.0382`
- 60d: hit_rate `0.7250`, avg `0.0183`, median `0.0238`, brier `0.2030`, calibration_gap `-0.0368`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5625`, avg `0.0034`, median `0.0040`, brier `0.2570`, calibration_gap `0.1081`
- 5d: hit_rate `0.6250`, avg `0.0038`, median `0.0051`, brier `0.2355`, calibration_gap `0.0456`
- 10d: hit_rate `0.5000`, avg `-0.0021`, median `0.0017`, brier `0.2795`, calibration_gap `0.1706`
- 20d: hit_rate `0.6875`, avg `0.0103`, median `0.0218`, brier `0.2143`, calibration_gap `-0.0169`
- 60d: hit_rate `0.7500`, avg `0.0233`, median `0.0359`, brier `0.1955`, calibration_gap `-0.0794`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
