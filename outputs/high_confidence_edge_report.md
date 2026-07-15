# High Confidence Edge Report

Generated at: `2026-07-15T22:35:54.828328+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003782`, median `0.003952`, mae `0.00888`
- 5d: sample `20`, hit `0.55`, avg `0.006578`, median `0.006133`, mae `0.013782`
- 10d: sample `20`, hit `0.55`, avg `0.003347`, median `0.005616`, mae `0.023341`
- 20d: sample `20`, hit `0.65`, avg `0.001503`, median `0.01011`, mae `0.031703`
- 60d: sample `20`, hit `0.6`, avg `0.017648`, median `0.048484`, mae `0.070844`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.001943`, median `0.000201`, mae `0.013141`
- 5d: sample `60`, hit `0.6167`, avg `-0.001008`, median `0.003714`, mae `0.015504`
- 10d: sample `60`, hit `0.4833`, avg `-0.000457`, median `-0.000214`, mae `0.018921`
- 20d: sample `60`, hit `0.6167`, avg `0.000949`, median `0.004241`, mae `0.030648`
- 60d: sample `60`, hit `0.4333`, avg `-0.006409`, median `-0.005523`, mae `0.061286`

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
- 3d: sample `8`, hit `0.75`, avg `0.005437`, median `0.004667`, mae `0.00776`
- 5d: sample `8`, hit `0.5`, avg `0.003605`, median `0.006133`, mae `0.01084`
- 10d: sample `8`, hit `0.5`, avg `-0.007875`, median `0.000242`, mae `0.02628`
- 20d: sample `8`, hit `0.5`, avg `-0.005878`, median `0.007748`, mae `0.035688`
- 60d: sample `8`, hit `0.625`, avg `0.01802`, median `0.064286`, mae `0.080676`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.005437`, median `0.004667`, mae `0.00776`
- 5d: sample `8`, hit `0.5`, avg `0.003605`, median `0.006133`, mae `0.01084`
- 10d: sample `8`, hit `0.5`, avg `-0.007875`, median `0.000242`, mae `0.02628`
- 20d: sample `8`, hit `0.5`, avg `-0.005878`, median `0.007748`, mae `0.035688`
- 60d: sample `8`, hit `0.625`, avg `0.01802`, median `0.064286`, mae `0.080676`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.003782, 'median_return': 0.003952, 'mean_absolute_return': 0.00888, 'max_adverse_excursion': -0.018644, 'max_favorable_excursion': 0.025242}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.006578, 'median_return': 0.006133, 'mean_absolute_return': 0.013782, 'max_adverse_excursion': -0.033213, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003347, 'median_return': 0.005616, 'mean_absolute_return': 0.023341, 'max_adverse_excursion': -0.039512, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.001503, 'median_return': 0.01011, 'mean_absolute_return': 0.031703, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.017648, 'median_return': 0.048484, 'mean_absolute_return': 0.070844, 'max_adverse_excursion': -0.10388, 'max_favorable_excursion': 0.112436}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005437, 'median_return': 0.004667, 'mean_absolute_return': 0.00776, 'max_adverse_excursion': -0.005568, 'max_favorable_excursion': 0.025242}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.003605, 'median_return': 0.006133, 'mean_absolute_return': 0.01084, 'max_adverse_excursion': -0.013784, 'max_favorable_excursion': 0.021374}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.007875, 'median_return': 0.000242, 'mean_absolute_return': 0.02628, 'max_adverse_excursion': -0.039512, 'max_favorable_excursion': 0.039489}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.005878, 'median_return': 0.007748, 'mean_absolute_return': 0.035688, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.01802, 'median_return': 0.064286, 'mean_absolute_return': 0.080676, 'max_adverse_excursion': -0.10388, 'max_favorable_excursion': 0.11101}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001173, 'median_return': 0.000201, 'mean_absolute_return': 0.012555, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.000587, 'median_return': 0.003888, 'mean_absolute_return': 0.015544, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.001424, 'median_return': 0.000197, 'mean_absolute_return': 0.019331, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.001861, 'median_return': 0.009259, 'mean_absolute_return': 0.030381, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.002441, 'median_return': -0.004982, 'mean_absolute_return': 0.061787, 'max_adverse_excursion': -0.158935, 'max_favorable_excursion': 0.145114}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.425}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.575}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.0, 'both_hit': 12, 'both_miss': 8}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.175, 'both_hit': 11, 'both_miss': 9}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.025, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.175, 'both_hit': 13, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.1, 'both_hit': 12, 'both_miss': 8}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.003457, 'median_return': 0.006214, 'mean_absolute_return': 0.011592, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.032615}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002489, 'median_return': 0.00596, 'mean_absolute_return': 0.016008, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.034232}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.003459, 'median_return': 0.005417, 'mean_absolute_return': 0.023635, 'max_adverse_excursion': -0.039512, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.000905, 'median_return': 0.007748, 'mean_absolute_return': 0.032538, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.012697, 'median_return': 0.019715, 'mean_absolute_return': 0.062032, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.112436}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.004481, 'median_return': -0.002654, 'mean_absolute_return': 0.01256, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': -0.000712, 'median_return': 0.003714, 'mean_absolute_return': 0.014139, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.025923}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.00247, 'median_return': -0.001676, 'mean_absolute_return': 0.016418, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.00127, 'median_return': 0.009259, 'mean_absolute_return': 0.029286, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.013486, 'median_return': -0.03023, 'mean_absolute_return': 0.065319, 'max_adverse_excursion': -0.158935, 'max_favorable_excursion': 0.145114}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.003457`, median `0.006214`, mae `0.011592`
- 5d: sample `40`, hit `0.55`, avg `0.002489`, median `0.00596`, mae `0.016008`
- 10d: sample `40`, hit `0.55`, avg `0.003459`, median `0.005417`, mae `0.023635`
- 20d: sample `40`, hit `0.675`, avg `0.000905`, median `0.007748`, mae `0.032538`
- 60d: sample `40`, hit `0.575`, avg `0.012697`, median `0.019715`, mae `0.062032`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.001943`, median `0.000201`, mae `0.013141`
- 5d: sample `60`, hit `0.6167`, avg `-0.001008`, median `0.003714`, mae `0.015504`
- 10d: sample `60`, hit `0.4833`, avg `-0.000457`, median `-0.000214`, mae `0.018921`
- 20d: sample `60`, hit `0.6167`, avg `0.000949`, median `0.004241`, mae `0.030648`
- 60d: sample `60`, hit `0.4333`, avg `-0.006409`, median `-0.005523`, mae `0.061286`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003782`, median `0.003952`, mae `0.00888`
- 5d: sample `20`, hit `0.55`, avg `0.006578`, median `0.006133`, mae `0.013782`
- 10d: sample `20`, hit `0.55`, avg `0.003347`, median `0.005616`, mae `0.023341`
- 20d: sample `20`, hit `0.65`, avg `0.001503`, median `0.01011`, mae `0.031703`
- 60d: sample `20`, hit `0.6`, avg `0.017648`, median `0.048484`, mae `0.070844`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003132`, median `0.009966`, mae `0.014304`
- 5d: sample `20`, hit `0.55`, avg `-0.0016`, median `0.004655`, mae `0.018235`
- 10d: sample `20`, hit `0.55`, avg `0.00357`, median `0.005417`, mae `0.023928`
- 20d: sample `20`, hit `0.7`, avg `0.000306`, median `0.003662`, mae `0.033372`
- 60d: sample `20`, hit `0.55`, avg `0.007745`, median `0.012273`, mae `0.053221`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003132`, median `0.009966`, mae `0.014304`
- 5d: sample `20`, hit `0.55`, avg `-0.0016`, median `0.004655`, mae `0.018235`
- 10d: sample `20`, hit `0.55`, avg `0.00357`, median `0.005417`, mae `0.023928`
- 20d: sample `20`, hit `0.7`, avg `0.000306`, median `0.003662`, mae `0.033372`
- 60d: sample `20`, hit `0.55`, avg `0.007745`, median `0.012273`, mae `0.053221`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003782`, median `0.003952`, mae `0.00888`
- 5d: sample `20`, hit `0.55`, avg `0.006578`, median `0.006133`, mae `0.013782`
- 10d: sample `20`, hit `0.55`, avg `0.003347`, median `0.005616`, mae `0.023341`
- 20d: sample `20`, hit `0.65`, avg `0.001503`, median `0.01011`, mae `0.031703`
- 60d: sample `20`, hit `0.6`, avg `0.017648`, median `0.048484`, mae `0.070844`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.003132`, median `0.009966`, mae `0.014304`
- 5d: sample `20`, hit `0.55`, avg `-0.0016`, median `0.004655`, mae `0.018235`
- 10d: sample `20`, hit `0.55`, avg `0.00357`, median `0.005417`, mae `0.023928`
- 20d: sample `20`, hit `0.7`, avg `0.000306`, median `0.003662`, mae `0.033372`
- 60d: sample `20`, hit `0.55`, avg `0.007745`, median `0.012273`, mae `0.053221`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.001943`, median `0.000201`, mae `0.013141`
- 5d: sample `60`, hit `0.6167`, avg `-0.001008`, median `0.003714`, mae `0.015504`
- 10d: sample `60`, hit `0.4833`, avg `-0.000457`, median `-0.000214`, mae `0.018921`
- 20d: sample `60`, hit `0.6167`, avg `0.000949`, median `0.004241`, mae `0.030648`
- 60d: sample `60`, hit `0.4333`, avg `-0.006409`, median `-0.005523`, mae `0.061286`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.001943`, median `0.000201`, mae `0.013141`
- 5d: sample `60`, hit `0.6167`, avg `-0.001008`, median `0.003714`, mae `0.015504`
- 10d: sample `60`, hit `0.4833`, avg `-0.000457`, median `-0.000214`, mae `0.018921`
- 20d: sample `60`, hit `0.6167`, avg `0.000949`, median `0.004241`, mae `0.030648`
- 60d: sample `60`, hit `0.4333`, avg `-0.006409`, median `-0.005523`, mae `0.061286`

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
