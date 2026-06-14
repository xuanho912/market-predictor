# High Confidence Edge Report

Generated at: `2026-06-14T10:12:16.541003+00:00`

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
- 3d: sample `8`, hit `0.375`, avg `-0.008716`, median `-0.009383`, mae `0.013329`
- 5d: sample `8`, hit `0.375`, avg `-0.00719`, median `-0.004438`, mae `0.014041`
- 10d: sample `8`, hit `0.375`, avg `-0.001836`, median `-0.007011`, mae `0.016678`
- 20d: sample `8`, hit `0.625`, avg `0.003391`, median `0.020068`, mae `0.026589`
- 60d: sample `8`, hit `0.5`, avg `-0.006235`, median `0.012092`, mae `0.05141`

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
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.125, 'both_hit': 27, 'both_miss': 33}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.125, 'both_hit': 32, 'both_miss': 28}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.05, 'both_hit': 27, 'both_miss': 33}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.025, 'both_hit': 36, 'both_miss': 24}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.1, 'both_hit': 32, 'both_miss': 28}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': 0.001175, 'median_return': 0.001558, 'mean_absolute_return': 0.013373, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.000734, 'median_return': 0.003005, 'mean_absolute_return': 0.01561, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001104, 'median_return': -0.0004, 'mean_absolute_return': 0.017979, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.002376, 'median_return': 0.009112, 'mean_absolute_return': 0.02924, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.00681, 'median_return': -0.003049, 'mean_absolute_return': 0.053208, 'max_adverse_excursion': -0.178752, 'max_favorable_excursion': 0.121826}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001175`, median `0.001558`, mae `0.013373`
- 5d: sample `80`, hit `0.5875`, avg `0.000734`, median `0.003005`, mae `0.01561`
- 10d: sample `80`, hit `0.4875`, avg `0.001104`, median `-0.0004`, mae `0.017979`
- 20d: sample `80`, hit `0.5875`, avg `0.002376`, median `0.009112`, mae `0.02924`
- 60d: sample `80`, hit `0.475`, avg `0.00681`, median `-0.003049`, mae `0.053208`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001175`, median `0.001558`, mae `0.013373`
- 5d: sample `80`, hit `0.5875`, avg `0.000734`, median `0.003005`, mae `0.01561`
- 10d: sample `80`, hit `0.4875`, avg `0.001104`, median `-0.0004`, mae `0.017979`
- 20d: sample `80`, hit `0.5875`, avg `0.002376`, median `0.009112`, mae `0.02924`
- 60d: sample `80`, hit `0.475`, avg `0.00681`, median `-0.003049`, mae `0.053208`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.006693`, median `-0.009383`, mae `0.014506`
- 5d: sample `20`, hit `0.35`, avg `-0.009981`, median `-0.006798`, mae `0.014545`
- 10d: sample `20`, hit `0.4`, avg `-0.00085`, median `-0.001222`, mae `0.013253`
- 20d: sample `20`, hit `0.8`, avg `0.020009`, median `0.029166`, mae `0.031437`
- 60d: sample `20`, hit `0.75`, avg `0.042877`, median `0.065295`, mae `0.069044`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.003777`, median `-0.005417`, mae `0.013197`
- 5d: sample `40`, hit `0.525`, avg `-0.003334`, median `0.000415`, mae `0.013661`
- 10d: sample `40`, hit `0.4`, avg `-0.000313`, median `-0.001932`, mae `0.014763`
- 20d: sample `40`, hit `0.7`, avg `0.011927`, median `0.020068`, mae `0.030814`
- 60d: sample `40`, hit `0.5`, avg `0.010918`, median `0.012092`, mae `0.058741`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.006127`, median `0.006895`, mae `0.013548`
- 5d: sample `40`, hit `0.65`, avg `0.004803`, median `0.008121`, mae `0.017559`
- 10d: sample `40`, hit `0.575`, avg `0.002522`, median `0.005417`, mae `0.021195`
- 20d: sample `40`, hit `0.475`, avg `-0.007175`, median `-0.001638`, mae `0.027666`
- 60d: sample `40`, hit `0.45`, avg `0.002701`, median `-0.003136`, mae `0.047674`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.003777`, median `-0.005417`, mae `0.013197`
- 5d: sample `40`, hit `0.525`, avg `-0.003334`, median `0.000415`, mae `0.013661`
- 10d: sample `40`, hit `0.4`, avg `-0.000313`, median `-0.001932`, mae `0.014763`
- 20d: sample `40`, hit `0.7`, avg `0.011927`, median `0.020068`, mae `0.030814`
- 60d: sample `40`, hit `0.5`, avg `0.010918`, median `0.012092`, mae `0.058741`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
