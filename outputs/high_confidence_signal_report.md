# High Confidence Signal Report

Generated at: `2026-10-07T18:59:35.611240+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `0.0005`, median `0.0031`, brier `0.2674`, calibration_gap `0.1906`
- 5d: hit_rate `0.6250`, avg `-0.0013`, median `0.0056`, brier `0.2674`, calibration_gap `0.1906`
- 10d: hit_rate `0.5000`, avg `-0.0035`, median `-0.0047`, brier `0.3541`, calibration_gap `0.3156`
- 20d: hit_rate `0.7500`, avg `0.0196`, median `0.0173`, brier `0.1970`, calibration_gap `0.0656`
- 60d: hit_rate `1.0000`, avg `0.0443`, median `0.0415`, brier `0.0341`, calibration_gap `-0.1844`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0031`, median `-0.0009`, brier `0.3367`, calibration_gap `0.3029`
- 5d: hit_rate `0.4375`, avg `-0.0077`, median `-0.0134`, brier `0.3726`, calibration_gap `0.3654`
- 10d: hit_rate `0.4375`, avg `-0.0152`, median `-0.0116`, brier `0.3794`, calibration_gap `0.3654`
- 20d: hit_rate `0.5625`, avg `-0.0022`, median `0.0009`, brier `0.3014`, calibration_gap `0.2404`
- 60d: hit_rate `0.9375`, avg `0.0530`, median `0.0571`, brier `0.0754`, calibration_gap `-0.1346`

### strong_signal_only
- sample_size: `20`
- 3d: hit_rate `0.5500`, avg `0.0006`, median `0.0030`, brier `0.2621`, calibration_gap `0.0993`
- 5d: hit_rate `0.6000`, avg `-0.0011`, median `0.0024`, brier `0.2473`, calibration_gap `0.0493`
- 10d: hit_rate `0.6000`, avg `0.0081`, median `0.0097`, brier `0.2483`, calibration_gap `0.0493`
- 20d: hit_rate `0.7000`, avg `0.0125`, median `0.0206`, brier `0.2064`, calibration_gap `-0.0507`
- 60d: hit_rate `0.8000`, avg `0.0215`, median `0.0344`, brier `0.1764`, calibration_gap `-0.1507`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `0.0007`, median `0.0004`, brier `0.2754`, calibration_gap `0.1422`
- 5d: hit_rate `0.5625`, avg `-0.0018`, median `0.0021`, brier `0.2569`, calibration_gap `0.0797`
- 10d: hit_rate `0.6250`, avg `0.0087`, median `0.0097`, brier `0.2372`, calibration_gap `0.0172`
- 20d: hit_rate `0.6250`, avg `0.0072`, median `0.0120`, brier `0.2320`, calibration_gap `0.0172`
- 60d: hit_rate `0.7500`, avg `0.0141`, median `0.0306`, brier `0.1945`, calibration_gap `-0.1078`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
