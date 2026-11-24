# High Confidence Signal Report

Generated at: `2026-11-24T11:00:41.511120+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.5000`, avg `0.0046`, median `-0.0004`, brier `0.3353`, calibration_gap `0.2911`
- 5d: hit_rate `0.6250`, avg `0.0106`, median `0.0213`, brier `0.2630`, calibration_gap `0.1661`
- 10d: hit_rate `0.6250`, avg `0.0231`, median `0.0363`, brier `0.2630`, calibration_gap `0.1661`
- 20d: hit_rate `0.5000`, avg `0.0109`, median `0.0059`, brier `0.3325`, calibration_gap `0.2911`
- 60d: hit_rate `0.7500`, avg `0.0291`, median `0.0030`, brier `0.1900`, calibration_gap `0.0411`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.3125`, avg `-0.0055`, median `-0.0051`, brier `0.4276`, calibration_gap `0.4661`
- 5d: hit_rate `0.4375`, avg `0.0007`, median `-0.0053`, brier `0.3581`, calibration_gap `0.3411`
- 10d: hit_rate `0.6250`, avg `0.0104`, median `0.0054`, brier `0.2589`, calibration_gap `0.1536`
- 20d: hit_rate `0.5625`, avg `0.0109`, median `0.0077`, brier `0.2928`, calibration_gap `0.2161`
- 60d: hit_rate `0.8125`, avg `0.0509`, median `0.0738`, brier `0.1556`, calibration_gap `-0.0339`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.6500`, avg `0.0097`, median `0.0103`, brier `0.2302`, calibration_gap `-0.0307`
- 5d: hit_rate `0.6500`, avg `0.0169`, median `0.0134`, brier `0.2308`, calibration_gap `-0.0307`
- 10d: hit_rate `0.7000`, avg `0.0302`, median `0.0324`, brier `0.2208`, calibration_gap `-0.0807`
- 20d: hit_rate `0.7000`, avg `0.0353`, median `0.0298`, brier `0.2074`, calibration_gap `-0.0807`
- 60d: hit_rate `0.8000`, avg `0.0974`, median `0.1062`, brier `0.1988`, calibration_gap `-0.1807`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0124`, median `0.0137`, brier `0.2359`, calibration_gap `-0.0199`
- 5d: hit_rate `0.8125`, avg `0.0273`, median `0.0324`, brier `0.1924`, calibration_gap `-0.2074`
- 10d: hit_rate `0.8750`, avg `0.0465`, median `0.0533`, brier `0.1799`, calibration_gap `-0.2699`
- 20d: hit_rate `0.5625`, avg `0.0363`, median `0.0236`, brier `0.2473`, calibration_gap `0.0426`
- 60d: hit_rate `0.8750`, avg `0.1092`, median `0.1076`, brier `0.1820`, calibration_gap `-0.2699`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
