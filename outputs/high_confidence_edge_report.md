# High Confidence Edge Report

Generated at: `2026-08-29T07:56:29.712232+00:00`

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
- 3d: sample `80`, hit `0.7625`, avg `0.009631`, median `0.012525`, mae `0.018818`
- 5d: sample `80`, hit `0.75`, avg `0.014063`, median `0.017467`, mae `0.024784`
- 10d: sample `80`, hit `0.7`, avg `0.018469`, median `0.023034`, mae `0.03597`
- 20d: sample `80`, hit `0.8`, avg `0.033084`, median `0.032954`, mae `0.047304`
- 60d: sample `80`, hit `0.7875`, avg `0.063143`, median `0.082251`, mae `0.081068`

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
- 3d: sample `8`, hit `0.875`, avg `0.018743`, median `0.022579`, mae `0.019157`
- 5d: sample `8`, hit `0.875`, avg `0.024356`, median `0.03199`, mae `0.025596`
- 10d: sample `8`, hit `0.75`, avg `0.030415`, median `0.041976`, mae `0.031581`
- 20d: sample `8`, hit `1.0`, avg `0.06254`, median `0.075995`, mae `0.06254`
- 60d: sample `8`, hit `0.875`, avg `0.082138`, median `0.097048`, mae `0.093629`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.018743`, median `0.022579`, mae `0.019157`
- 5d: sample `8`, hit `0.875`, avg `0.024356`, median `0.03199`, mae `0.025596`
- 10d: sample `8`, hit `0.75`, avg `0.030415`, median `0.041976`, mae `0.031581`
- 20d: sample `8`, hit `1.0`, avg `0.06254`, median `0.075995`, mae `0.06254`
- 60d: sample `8`, hit `0.875`, avg `0.082138`, median `0.097048`, mae `0.093629`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.009631, 'median_return': 0.012525, 'mean_absolute_return': 0.018818, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.014063, 'median_return': 0.017467, 'mean_absolute_return': 0.024784, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.018469, 'median_return': 0.023034, 'mean_absolute_return': 0.03597, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.033084, 'median_return': 0.032954, 'mean_absolute_return': 0.047304, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.063143, 'median_return': 0.082251, 'mean_absolute_return': 0.081068, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.018743, 'median_return': 0.022579, 'mean_absolute_return': 0.019157, 'max_adverse_excursion': -0.001658, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.024356, 'median_return': 0.03199, 'mean_absolute_return': 0.025596, 'max_adverse_excursion': -0.004957, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.030415, 'median_return': 0.041976, 'mean_absolute_return': 0.031581, 'max_adverse_excursion': -0.004263, 'max_favorable_excursion': 0.05207}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.06254, 'median_return': 0.075995, 'mean_absolute_return': 0.06254, 'max_adverse_excursion': 0.02284, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.082138, 'median_return': 0.097048, 'mean_absolute_return': 0.093629, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.008619, 'median_return': 0.012272, 'mean_absolute_return': 0.01878, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.01292, 'median_return': 0.017411, 'mean_absolute_return': 0.024694, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.017142, 'median_return': 0.021169, 'mean_absolute_return': 0.036458, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.029811, 'median_return': 0.030922, 'mean_absolute_return': 0.045611, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.061033, 'median_return': 0.0765, 'mean_absolute_return': 0.079672, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.7625}, '5d': {'sample_size': 80, 'hit_rate': 0.75}, '10d': {'sample_size': 80, 'hit_rate': 0.7}, '20d': {'sample_size': 80, 'hit_rate': 0.8}, '60d': {'sample_size': 80, 'hit_rate': 0.7875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.7625, 'secondary_hit_rate': 0.7625, 'primary_minus_secondary': 0.0, 'both_hit': 61, 'both_miss': 19}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': 0.0, 'both_hit': 60, 'both_miss': 20}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': 0.0, 'both_hit': 56, 'both_miss': 24}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': 0.0, 'both_hit': 64, 'both_miss': 16}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.7875, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': 0.0, 'both_hit': 63, 'both_miss': 17}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.7625, 'avg_return': 0.009631, 'median_return': 0.012525, 'mean_absolute_return': 0.018818, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.014063, 'median_return': 0.017467, 'mean_absolute_return': 0.024784, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.018469, 'median_return': 0.023034, 'mean_absolute_return': 0.03597, 'max_adverse_excursion': -0.057499, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.033084, 'median_return': 0.032954, 'mean_absolute_return': 0.047304, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.063143, 'median_return': 0.082251, 'mean_absolute_return': 0.081068, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.7667`, avg `0.010661`, median `0.012542`, mae `0.017163`
- 5d: sample `60`, hit `0.75`, avg `0.014418`, median `0.015191`, mae `0.023536`
- 10d: sample `60`, hit `0.7`, avg `0.018283`, median `0.023034`, mae `0.034505`
- 20d: sample `60`, hit `0.8`, avg `0.034499`, median `0.032954`, mae `0.047602`
- 60d: sample `60`, hit `0.8`, avg `0.067902`, median `0.082988`, mae `0.078353`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.7667`, avg `0.010661`, median `0.012542`, mae `0.017163`
- 5d: sample `60`, hit `0.75`, avg `0.014418`, median `0.015191`, mae `0.023536`
- 10d: sample `60`, hit `0.7`, avg `0.018283`, median `0.023034`, mae `0.034505`
- 20d: sample `60`, hit `0.8`, avg `0.034499`, median `0.032954`, mae `0.047602`
- 60d: sample `60`, hit `0.8`, avg `0.067902`, median `0.082988`, mae `0.078353`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.009687`, median `0.009859`, mae `0.016014`
- 5d: sample `40`, hit `0.725`, avg `0.012729`, median `0.014937`, mae `0.023389`
- 10d: sample `40`, hit `0.65`, avg `0.01686`, median `0.021584`, mae `0.036563`
- 20d: sample `40`, hit `0.725`, avg `0.030925`, median `0.032954`, mae `0.049043`
- 60d: sample `40`, hit `0.75`, avg `0.064017`, median `0.0765`, mae `0.076888`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.7625`, avg `0.009631`, median `0.012525`, mae `0.018818`
- 5d: sample `80`, hit `0.75`, avg `0.014063`, median `0.017467`, mae `0.024784`
- 10d: sample `80`, hit `0.7`, avg `0.018469`, median `0.023034`, mae `0.03597`
- 20d: sample `80`, hit `0.8`, avg `0.033084`, median `0.032954`, mae `0.047304`
- 60d: sample `80`, hit `0.7875`, avg `0.063143`, median `0.082251`, mae `0.081068`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `80`, hit `0.7625`, avg `0.009631`, median `0.012525`, mae `0.018818`
- 5d: sample `80`, hit `0.75`, avg `0.014063`, median `0.017467`, mae `0.024784`
- 10d: sample `80`, hit `0.7`, avg `0.018469`, median `0.023034`, mae `0.03597`
- 20d: sample `80`, hit `0.8`, avg `0.033084`, median `0.032954`, mae `0.047304`
- 60d: sample `80`, hit `0.7875`, avg `0.063143`, median `0.082251`, mae `0.081068`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.7625`, avg `0.009631`, median `0.012525`, mae `0.018818`
- 5d: sample `80`, hit `0.75`, avg `0.014063`, median `0.017467`, mae `0.024784`
- 10d: sample `80`, hit `0.7`, avg `0.018469`, median `0.023034`, mae `0.03597`
- 20d: sample `80`, hit `0.8`, avg `0.033084`, median `0.032954`, mae `0.047304`
- 60d: sample `80`, hit `0.7875`, avg `0.063143`, median `0.082251`, mae `0.081068`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.7625`, avg `0.009631`, median `0.012525`, mae `0.018818`
- 5d: sample `80`, hit `0.75`, avg `0.014063`, median `0.017467`, mae `0.024784`
- 10d: sample `80`, hit `0.7`, avg `0.018469`, median `0.023034`, mae `0.03597`
- 20d: sample `80`, hit `0.8`, avg `0.033084`, median `0.032954`, mae `0.047304`
- 60d: sample `80`, hit `0.7875`, avg `0.063143`, median `0.082251`, mae `0.081068`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.7625`, avg `0.009631`, median `0.012525`, mae `0.018818`
- 5d: sample `80`, hit `0.75`, avg `0.014063`, median `0.017467`, mae `0.024784`
- 10d: sample `80`, hit `0.7`, avg `0.018469`, median `0.023034`, mae `0.03597`
- 20d: sample `80`, hit `0.8`, avg `0.033084`, median `0.032954`, mae `0.047304`
- 60d: sample `80`, hit `0.7875`, avg `0.063143`, median `0.082251`, mae `0.081068`

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
