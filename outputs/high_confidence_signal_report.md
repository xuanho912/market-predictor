# High Confidence Signal Report

Generated at: `2026-09-01T16:43:19.548429+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0013`, median `0.0014`, brier `0.2618`, calibration_gap `0.1860`
- 5d: hit_rate `0.5000`, avg `-0.0030`, median `-0.0009`, brier `0.3410`, calibration_gap `0.3110`
- 10d: hit_rate `0.1250`, avg `-0.0155`, median `-0.0204`, brier `0.5849`, calibration_gap `0.6860`
- 20d: hit_rate `0.3750`, avg `-0.0119`, median `-0.0055`, brier `0.4233`, calibration_gap `0.4360`
- 60d: hit_rate `0.6250`, avg `0.0223`, median `0.0453`, brier `0.2619`, calibration_gap `0.1860`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0023`, median `-0.0004`, brier `0.3299`, calibration_gap `0.2955`
- 5d: hit_rate `0.5000`, avg `-0.0046`, median `-0.0009`, brier `0.3353`, calibration_gap `0.2955`
- 10d: hit_rate `0.3750`, avg `-0.0046`, median `-0.0127`, brier `0.4217`, calibration_gap `0.4205`
- 20d: hit_rate `0.6250`, avg `0.0026`, median `0.0205`, brier `0.2702`, calibration_gap `0.1705`
- 60d: hit_rate `0.7500`, avg `0.0413`, median `0.0597`, brier `0.1895`, calibration_gap `0.0455`

### strong_signal_only
- sample_size: `60`
- 3d: hit_rate `0.4833`, avg `-0.0006`, median `-0.0015`, brier `0.3256`, calibration_gap `0.2745`
- 5d: hit_rate `0.4833`, avg `-0.0034`, median `-0.0034`, brier `0.3281`, calibration_gap `0.2745`
- 10d: hit_rate `0.4667`, avg `0.0031`, median `-0.0024`, brier `0.3427`, calibration_gap `0.2911`
- 20d: hit_rate `0.7167`, avg `0.0181`, median `0.0247`, brier `0.2110`, calibration_gap `0.0411`
- 60d: hit_rate `0.8000`, avg `0.0539`, median `0.0655`, brier `0.1665`, calibration_gap `-0.0422`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6875`, avg `0.0044`, median `0.0042`, brier `0.2154`, calibration_gap `0.0220`
- 5d: hit_rate `0.6250`, avg `0.0069`, median `0.0052`, brier `0.2427`, calibration_gap `0.0845`
- 10d: hit_rate `0.3750`, avg `-0.0036`, median `-0.0162`, brier `0.3457`, calibration_gap `0.3345`
- 20d: hit_rate `0.5000`, avg `0.0010`, median `0.0128`, brier `0.2932`, calibration_gap `0.2095`
- 60d: hit_rate `0.6875`, avg `0.0173`, median `0.0526`, brier `0.2164`, calibration_gap `0.0220`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
