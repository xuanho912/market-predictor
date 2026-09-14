# High Confidence Edge Report

Generated at: `2026-09-14T18:07:26.570512+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `16`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `16`, gate `insufficient`
- 5d: completed `16`, gate `insufficient`
- 10d: completed `16`, gate `insufficient`
- 20d: completed `16`, gate `insufficient`
- 60d: completed `16`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002092`, median `0.005296`, mae `0.01409`
- 5d: sample `80`, hit `0.55`, avg `-0.00116`, median `0.001303`, mae `0.0162`
- 10d: sample `80`, hit `0.425`, avg `-0.001312`, median `-0.006017`, mae `0.025695`
- 20d: sample `80`, hit `0.6375`, avg `0.014018`, median `0.020068`, mae `0.039654`
- 60d: sample `80`, hit `0.675`, avg `0.036356`, median `0.064104`, mae `0.083456`

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
- 3d: sample `8`, hit `0.625`, avg `0.001097`, median `0.003785`, mae `0.011645`
- 5d: sample `8`, hit `0.625`, avg `-0.00198`, median `0.003829`, mae `0.015516`
- 10d: sample `8`, hit `0.375`, avg `0.004504`, median `-0.0004`, mae `0.017422`
- 20d: sample `8`, hit `1.0`, avg `0.042901`, median `0.055822`, mae `0.042901`
- 60d: sample `8`, hit `1.0`, avg `0.091304`, median `0.120808`, mae `0.091304`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.001097`, median `0.003785`, mae `0.011645`
- 5d: sample `8`, hit `0.625`, avg `-0.00198`, median `0.003829`, mae `0.015516`
- 10d: sample `8`, hit `0.375`, avg `0.004504`, median `-0.0004`, mae `0.017422`
- 20d: sample `8`, hit `1.0`, avg `0.042901`, median `0.055822`, mae `0.042901`
- 60d: sample `8`, hit `1.0`, avg `0.091304`, median `0.120808`, mae `0.091304`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.001097, 'median_return': 0.003785, 'mean_absolute_return': 0.011645, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00198, 'median_return': 0.003829, 'mean_absolute_return': 0.015516, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.004504, 'median_return': -0.0004, 'mean_absolute_return': 0.017422, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.042901, 'median_return': 0.055822, 'mean_absolute_return': 0.042901, 'max_adverse_excursion': 0.000213, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.091304, 'median_return': 0.120808, 'mean_absolute_return': 0.091304, 'max_adverse_excursion': 0.012092, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.002202, 'median_return': 0.00531, 'mean_absolute_return': 0.014362, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.035961}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.001069, 'median_return': 0.001087, 'mean_absolute_return': 0.016276, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.001959, 'median_return': -0.006389, 'mean_absolute_return': 0.026614, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.010808, 'median_return': 0.010824, 'mean_absolute_return': 0.039293, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.03025, 'median_return': 0.061042, 'mean_absolute_return': 0.082584, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.3875}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.3625}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.275, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.002092, 'median_return': 0.005296, 'mean_absolute_return': 0.01409, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.035961}, '5d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': -0.00116, 'median_return': 0.001303, 'mean_absolute_return': 0.0162, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 80, 'hit_rate': 0.425, 'avg_return': -0.001312, 'median_return': -0.006017, 'mean_absolute_return': 0.025695, 'max_adverse_excursion': -0.073108, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.014018, 'median_return': 0.020068, 'mean_absolute_return': 0.039654, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.036356, 'median_return': 0.064104, 'mean_absolute_return': 0.083456, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.192595}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002092`, median `0.005296`, mae `0.01409`
- 5d: sample `80`, hit `0.55`, avg `-0.00116`, median `0.001303`, mae `0.0162`
- 10d: sample `80`, hit `0.425`, avg `-0.001312`, median `-0.006017`, mae `0.025695`
- 20d: sample `80`, hit `0.6375`, avg `0.014018`, median `0.020068`, mae `0.039654`
- 60d: sample `80`, hit `0.675`, avg `0.036356`, median `0.064104`, mae `0.083456`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002092`, median `0.005296`, mae `0.01409`
- 5d: sample `80`, hit `0.55`, avg `-0.00116`, median `0.001303`, mae `0.0162`
- 10d: sample `80`, hit `0.425`, avg `-0.001312`, median `-0.006017`, mae `0.025695`
- 20d: sample `80`, hit `0.6375`, avg `0.014018`, median `0.020068`, mae `0.039654`
- 60d: sample `80`, hit `0.675`, avg `0.036356`, median `0.064104`, mae `0.083456`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### mixed_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.002092`, median `0.005296`, mae `0.01409`
- 5d: sample `80`, hit `0.55`, avg `-0.00116`, median `0.001303`, mae `0.0162`
- 10d: sample `80`, hit `0.425`, avg `-0.001312`, median `-0.006017`, mae `0.025695`
- 20d: sample `80`, hit `0.6375`, avg `0.014018`, median `0.020068`, mae `0.039654`
- 60d: sample `80`, hit `0.675`, avg `0.036356`, median `0.064104`, mae `0.083456`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### risk_path_with_flow_conflict
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
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
