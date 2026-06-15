# High Confidence Signal Report

Generated at: `2026-06-15T13:55:23.101243+00:00`

This report does not confirm alpha. It checks whether higher-confidence historical analog candidates look better than lower-confidence candidates.

Status: `historical_proxy_only_not_forward_confirmed`
Sample size: `80`
Conclusion: `confidence_not_yet_validated`

## Bucket Metrics

### top_10_confidence_signals
- sample_size: `8`
- 3d: hit_rate `0.6250`, avg `-0.0026`, median `0.0031`, brier `0.2414`, calibration_gap `0.0890`
- 5d: hit_rate `0.3750`, avg `-0.0075`, median `-0.0157`, brier `0.3471`, calibration_gap `0.3390`
- 10d: hit_rate `0.8750`, avg `0.0117`, median `0.0135`, brier `0.1373`, calibration_gap `-0.1610`
- 20d: hit_rate `0.7500`, avg `0.0097`, median `0.0142`, brier `0.1842`, calibration_gap `-0.0360`
- 60d: hit_rate `0.3750`, avg `-0.0092`, median `-0.0282`, brier `0.3517`, calibration_gap `0.3390`

### top_20_confidence_signals
- sample_size: `16`
- 3d: hit_rate `0.5000`, avg `-0.0024`, median `0.0002`, brier `0.2875`, calibration_gap `0.2015`
- 5d: hit_rate `0.3125`, avg `-0.0067`, median `-0.0075`, brier `0.3629`, calibration_gap `0.3890`
- 10d: hit_rate `0.7500`, avg `0.0074`, median `0.0075`, brier `0.1875`, calibration_gap `-0.0485`
- 20d: hit_rate `0.8125`, avg `0.0122`, median `0.0210`, brier `0.1640`, calibration_gap `-0.1110`
- 60d: hit_rate `0.5000`, avg `0.0102`, median `0.0064`, brier `0.2954`, calibration_gap `0.2015`

### strong_signal_only
- sample_size: `80`
- 3d: hit_rate `0.6125`, avg `0.0036`, median `0.0046`, brier `0.2443`, calibration_gap `0.0489`
- 5d: hit_rate `0.6125`, avg `0.0044`, median `0.0046`, brier `0.2480`, calibration_gap `0.0489`
- 10d: hit_rate `0.5875`, avg `0.0067`, median `0.0072`, brier `0.2472`, calibration_gap `0.0739`
- 20d: hit_rate `0.6875`, avg `0.0093`, median `0.0171`, brier `0.2115`, calibration_gap `-0.0261`
- 60d: hit_rate `0.5875`, avg `0.0258`, median `0.0314`, brier `0.2503`, calibration_gap `0.0739`

### low_confidence_reference
- sample_size: `16`
- 3d: hit_rate `0.6250`, avg `0.0044`, median `0.0043`, brier `0.2348`, calibration_gap `0.0021`
- 5d: hit_rate `0.6875`, avg `0.0097`, median `0.0086`, brier `0.2195`, calibration_gap `-0.0604`
- 10d: hit_rate `0.6250`, avg `0.0070`, median `0.0166`, brier `0.2349`, calibration_gap `0.0021`
- 20d: hit_rate `0.5625`, avg `0.0056`, median `0.0136`, brier `0.2499`, calibration_gap `0.0646`
- 60d: hit_rate `0.5000`, avg `0.0211`, median `0.0046`, brier `0.2665`, calibration_gap `0.1271`

## Interpretation

- If high-confidence buckets do not beat low-confidence buckets, confidence is not yet usable.
- Forward-only validation still matters more than this historical proxy report.
- Alpha v1 remains RESEARCH ALPHA CANDIDATE.
