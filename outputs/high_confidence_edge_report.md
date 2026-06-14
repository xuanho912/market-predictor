# High Confidence Edge Report

Generated at: `2026-06-14T08:10:03.999633+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `0`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `0`, gate `insufficient`
- 5d: completed `0`, gate `insufficient`
- 10d: completed `0`, gate `insufficient`
- 20d: completed `0`, gate `insufficient`
- 60d: completed `0`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001175`, median `0.001558`, mae `0.013373`
- 5d: sample `80`, hit `0.5875`, avg `0.000734`, median `0.003005`, mae `0.01561`
- 10d: sample `80`, hit `0.4875`, avg `0.001104`, median `-0.0004`, mae `0.017979`
- 20d: sample `80`, hit `0.5875`, avg `0.002376`, median `0.009112`, mae `0.02924`
- 60d: sample `80`, hit `0.475`, avg `0.00681`, median `-0.003049`, mae `0.053208`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### NO_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### RISK_WARNING
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.002698`, median `0.003538`, mae `0.009556`
- 5d: sample `8`, hit `0.5`, avg `0.003863`, median `0.006133`, mae `0.009613`
- 10d: sample `8`, hit `0.625`, avg `0.004889`, median `0.00903`, mae `0.019592`
- 20d: sample `8`, hit `0.375`, avg `-0.021094`, median `-0.014517`, mae `0.028847`
- 60d: sample `8`, hit `0.75`, avg `0.035988`, median `0.069306`, mae `0.073304`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.008716`, median `-0.009383`, mae `0.013329`
- 5d: sample `8`, hit `0.375`, avg `-0.00719`, median `-0.004438`, mae `0.014041`
- 10d: sample `8`, hit `0.375`, avg `-0.001836`, median `-0.007011`, mae `0.016678`
- 20d: sample `8`, hit `0.625`, avg `0.003391`, median `0.020068`, mae `0.026589`
- 60d: sample `8`, hit `0.5`, avg `-0.006235`, median `0.012092`, mae `0.05141`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.001175, 'median_return': 0.001558, 'mean_absolute_return': 0.013373, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.000734, 'median_return': 0.003005, 'mean_absolute_return': 0.01561, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001104, 'median_return': -0.0004, 'mean_absolute_return': 0.017979, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.002376, 'median_return': 0.009112, 'mean_absolute_return': 0.02924, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.00681, 'median_return': -0.003049, 'mean_absolute_return': 0.053208, 'max_adverse_excursion': -0.178752, 'max_favorable_excursion': 0.121826}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008716, 'median_return': -0.009383, 'mean_absolute_return': 0.013329, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.00719, 'median_return': -0.004438, 'mean_absolute_return': 0.014041, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.001836, 'median_return': -0.007011, 'mean_absolute_return': 0.016678, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003391, 'median_return': 0.020068, 'mean_absolute_return': 0.026589, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.031196}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006235, 'median_return': 0.012092, 'mean_absolute_return': 0.05141, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.092646}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.002274, 'median_return': 0.00234, 'mean_absolute_return': 0.013377, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.001615, 'median_return': 0.003829, 'mean_absolute_return': 0.015784, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.001431, 'median_return': 0.000242, 'mean_absolute_return': 0.018124, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002263, 'median_return': 0.004543, 'mean_absolute_return': 0.029535, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.008259, 'median_return': -0.003049, 'mean_absolute_return': 0.053407, 'max_adverse_excursion': -0.178752, 'max_favorable_excursion': 0.121826}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.4875}, '20d': {'sample_size': 80, 'hit_rate': 0.5875}, '60d': {'sample_size': 80, 'hit_rate': 0.475}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.075, 'both_hit': 19, 'both_miss': 21}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.3625, 'primary_minus_secondary': 0.225, 'both_hit': 18, 'both_miss': 22}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.0, 'both_hit': 19, 'both_miss': 21}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.075, 'both_hit': 24, 'both_miss': 16}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.225, 'both_hit': 27, 'both_miss': 13}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.001175, 'median_return': 0.001558, 'mean_absolute_return': 0.013373, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.000734, 'median_return': 0.003005, 'mean_absolute_return': 0.01561, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001104, 'median_return': -0.0004, 'mean_absolute_return': 0.017979, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.002376, 'median_return': 0.009112, 'mean_absolute_return': 0.02924, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.00681, 'median_return': -0.003049, 'mean_absolute_return': 0.053208, 'max_adverse_excursion': -0.178752, 'max_favorable_excursion': 0.121826}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
