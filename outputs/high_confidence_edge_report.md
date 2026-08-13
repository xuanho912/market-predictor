# High Confidence Edge Report

Generated at: `2026-08-13T23:29:17.464420+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `20`
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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

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
- sample_size: `2`
- 3d: sample `2`, hit `1.0`, avg `0.018182`, median `0.022103`, mae `0.018182`
- 5d: sample `2`, hit `0.5`, avg `-0.00541`, median `0.000863`, mae `0.006274`
- 10d: sample `2`, hit `0.5`, avg `0.00239`, median `0.011168`, mae `0.008779`
- 20d: sample `2`, hit `0.0`, avg `-0.018135`, median `-0.003108`, mae `0.018135`
- 60d: sample `2`, hit `0.0`, avg `-0.053633`, median `-0.044207`, mae `0.053633`

### confidence_score top 10%
- sample_size: `2`
- 3d: sample `2`, hit `1.0`, avg `0.018182`, median `0.022103`, mae `0.018182`
- 5d: sample `2`, hit `0.5`, avg `-0.00541`, median `0.000863`, mae `0.006274`
- 10d: sample `2`, hit `0.5`, avg `0.00239`, median `0.011168`, mae `0.008779`
- 20d: sample `2`, hit `0.0`, avg `-0.018135`, median `-0.003108`, mae `0.018135`
- 60d: sample `2`, hit `0.0`, avg `-0.053633`, median `-0.044207`, mae `0.053633`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.008292, 'median_return': 0.010849, 'mean_absolute_return': 0.016473, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002088, 'median_return': 0.001654, 'mean_absolute_return': 0.021838, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007342, 'median_return': 0.011168, 'mean_absolute_return': 0.03467, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.017266, 'median_return': 0.010824, 'mean_absolute_return': 0.060433, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.052484, 'median_return': 0.065495, 'mean_absolute_return': 0.077384, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.171512}}}, 'confidence_top_10': {'sample_size': 2, 'by_horizon': {'3d': {'sample_size': 2, 'hit_rate': 1.0, 'avg_return': 0.018182, 'median_return': 0.022103, 'mean_absolute_return': 0.018182, 'max_adverse_excursion': 0.014261, 'max_favorable_excursion': 0.022103}, '5d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': -0.00541, 'median_return': 0.000863, 'mean_absolute_return': 0.006274, 'max_adverse_excursion': -0.011684, 'max_favorable_excursion': 0.000863}, '10d': {'sample_size': 2, 'hit_rate': 0.5, 'avg_return': 0.00239, 'median_return': 0.011168, 'mean_absolute_return': 0.008779, 'max_adverse_excursion': -0.006389, 'max_favorable_excursion': 0.011168}, '20d': {'sample_size': 2, 'hit_rate': 0.0, 'avg_return': -0.018135, 'median_return': -0.003108, 'mean_absolute_return': 0.018135, 'max_adverse_excursion': -0.033162, 'max_favorable_excursion': -0.003108}, '60d': {'sample_size': 2, 'hit_rate': 0.0, 'avg_return': -0.053633, 'median_return': -0.044207, 'mean_absolute_return': 0.053633, 'max_adverse_excursion': -0.063058, 'max_favorable_excursion': -0.044207}}}, 'ordinary_confidence': {'sample_size': 18, 'by_horizon': {'3d': {'sample_size': 18, 'hit_rate': 0.6111, 'avg_return': 0.007194, 'median_return': 0.009966, 'mean_absolute_return': 0.016284, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 18, 'hit_rate': 0.5556, 'avg_return': 0.002921, 'median_return': 0.007398, 'mean_absolute_return': 0.023568, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 18, 'hit_rate': 0.5556, 'avg_return': 0.007892, 'median_return': 0.01246, 'mean_absolute_return': 0.037547, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 18, 'hit_rate': 0.6667, 'avg_return': 0.0212, 'median_return': 0.015261, 'mean_absolute_return': 0.065133, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 18, 'hit_rate': 0.8889, 'avg_return': 0.064274, 'median_return': 0.065858, 'mean_absolute_return': 0.080024, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.171512}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 20, 'hit_rate': 0.65}, '5d': {'sample_size': 20, 'hit_rate': 0.55}, '10d': {'sample_size': 20, 'hit_rate': 0.55}, '20d': {'sample_size': 20, 'hit_rate': 0.6}, '60d': {'sample_size': 20, 'hit_rate': 0.8}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 20, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 20, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 11, 'both_miss': 9}, '10d': {'sample_size': 20, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 20, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 12, 'both_miss': 8}, '60d': {'sample_size': 20, 'primary_hit_rate': 0.8, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': 0.0, 'both_hit': 16, 'both_miss': 4}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.008292, 'median_return': 0.010849, 'mean_absolute_return': 0.016473, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002088, 'median_return': 0.001654, 'mean_absolute_return': 0.021838, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007342, 'median_return': 0.011168, 'mean_absolute_return': 0.03467, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.017266, 'median_return': 0.010824, 'mean_absolute_return': 0.060433, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.052484, 'median_return': 0.065495, 'mean_absolute_return': 0.077384, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.171512}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

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
