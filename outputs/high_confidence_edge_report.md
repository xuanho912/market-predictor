# High Confidence Edge Report

Generated at: `2026-07-10T22:37:32.692849+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002925`, median `0.004569`, mae `0.012365`
- 5d: sample `20`, hit `0.6`, avg `0.002748`, median `0.008121`, mae `0.017763`
- 10d: sample `20`, hit `0.75`, avg `0.015747`, median `0.00903`, mae `0.022768`
- 20d: sample `20`, hit `0.6`, avg `0.006217`, median `0.009812`, mae `0.037302`
- 60d: sample `20`, hit `0.65`, avg `0.020311`, median `0.055266`, mae `0.07734`

### MODERATE_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.003708`, median `-0.001227`, mae `0.011523`
- 5d: sample `60`, hit `0.4833`, avg `-0.00525`, median `-0.001796`, mae `0.015366`
- 10d: sample `60`, hit `0.45`, avg `-0.00509`, median `-0.003071`, mae `0.020499`
- 20d: sample `60`, hit `0.6833`, avg `-0.004303`, median `0.012291`, mae `0.033167`
- 60d: sample `60`, hit `0.45`, avg `-0.00751`, median `-0.005997`, mae `0.054988`

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
- 3d: sample `8`, hit `0.5`, avg `-0.008752`, median `0.001448`, mae `0.014948`
- 5d: sample `8`, hit `0.25`, avg `-0.00855`, median `-0.004989`, mae `0.013855`
- 10d: sample `8`, hit `0.375`, avg `-0.003031`, median `-0.003071`, mae `0.019711`
- 20d: sample `8`, hit `0.75`, avg `0.018499`, median `0.029166`, mae `0.024178`
- 60d: sample `8`, hit `0.5`, avg `0.028022`, median `0.046132`, mae `0.057897`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.002073`, median `0.004542`, mae `0.006066`
- 5d: sample `8`, hit `0.75`, avg `0.006075`, median `0.007324`, mae `0.011104`
- 10d: sample `8`, hit `0.625`, avg `0.006747`, median `0.007467`, mae `0.011354`
- 20d: sample `8`, hit `0.75`, avg `0.008852`, median `0.012291`, mae `0.018053`
- 60d: sample `8`, hit `0.25`, avg `-0.032855`, median `-0.03635`, mae `0.055895`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002925, 'median_return': 0.004569, 'mean_absolute_return': 0.012365, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002748, 'median_return': 0.008121, 'mean_absolute_return': 0.017763, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.015747, 'median_return': 0.00903, 'mean_absolute_return': 0.022768, 'max_adverse_excursion': -0.024582, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006217, 'median_return': 0.009812, 'mean_absolute_return': 0.037302, 'max_adverse_excursion': -0.086744, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.020311, 'median_return': 0.055266, 'mean_absolute_return': 0.07734, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.137137}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': -0.003708, 'median_return': -0.001227, 'mean_absolute_return': 0.011523, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': -0.00525, 'median_return': -0.001796, 'mean_absolute_return': 0.015366, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.032674}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.00509, 'median_return': -0.003071, 'mean_absolute_return': 0.020499, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.041955}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': -0.004303, 'median_return': 0.012291, 'mean_absolute_return': 0.033167, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.062475}, '60d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.00751, 'median_return': -0.005997, 'mean_absolute_return': 0.054988, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.145114}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002073, 'median_return': 0.004542, 'mean_absolute_return': 0.006066, 'max_adverse_excursion': -0.006734, 'max_favorable_excursion': 0.011957}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.006075, 'median_return': 0.007324, 'mean_absolute_return': 0.011104, 'max_adverse_excursion': -0.018322, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006747, 'median_return': 0.007467, 'mean_absolute_return': 0.011354, 'max_adverse_excursion': -0.016537, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.008852, 'median_return': 0.012291, 'mean_absolute_return': 0.018053, 'max_adverse_excursion': -0.021537, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.032855, 'median_return': -0.03635, 'mean_absolute_return': 0.055895, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.048421}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.002508, 'median_return': 0.000145, 'mean_absolute_return': 0.012363, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.004287, 'median_return': -0.001324, 'mean_absolute_return': 0.016505, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.000617, 'median_return': 0.001517, 'mean_absolute_return': 0.022146, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': -0.002843, 'median_return': 0.009812, 'mean_absolute_return': 0.035995, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.003034, 'median_return': 0.012273, 'mean_absolute_return': 0.061096, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.145114}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.025, 'both_hit': 31, 'both_miss': 29}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 32, 'both_miss': 28}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.075, 'both_hit': 35, 'both_miss': 25}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.05, 'both_hit': 41, 'both_miss': 19}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.025, 'both_hit': 31, 'both_miss': 29}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001288, 'median_return': 0.001999, 'mean_absolute_return': 0.011022, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.001124, 'median_return': 0.003197, 'mean_absolute_return': 0.017008, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002421, 'median_return': 0.002896, 'mean_absolute_return': 0.024167, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': -0.007187, 'median_return': 0.00514, 'mean_absolute_return': 0.039243, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.003106, 'median_return': 0.017077, 'mean_absolute_return': 0.062116, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.137137}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.005388, 'median_return': -0.001166, 'mean_absolute_return': 0.012444, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.01781}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.005378, 'median_return': 0.000415, 'mean_absolute_return': 0.014922, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.025291}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002183, 'median_return': 0.001517, 'mean_absolute_return': 0.017966, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.003841, 'median_return': 0.015404, 'mean_absolute_return': 0.029158, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.058602}, '60d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.004216, 'median_return': -0.005523, 'mean_absolute_return': 0.059036, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.145114}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.003708`, median `-0.001227`, mae `0.011523`
- 5d: sample `60`, hit `0.4833`, avg `-0.00525`, median `-0.001796`, mae `0.015366`
- 10d: sample `60`, hit `0.45`, avg `-0.00509`, median `-0.003071`, mae `0.020499`
- 20d: sample `60`, hit `0.6833`, avg `-0.004303`, median `0.012291`, mae `0.033167`
- 60d: sample `60`, hit `0.45`, avg `-0.00751`, median `-0.005997`, mae `0.054988`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000348`, median `-0.001227`, mae `0.00968`
- 5d: sample `20`, hit `0.45`, avg `-0.004995`, median `-0.004461`, mae `0.016254`
- 10d: sample `20`, hit `0.35`, avg `-0.010905`, median `-0.01411`, mae `0.025566`
- 20d: sample `20`, hit `0.6`, avg `-0.020592`, median `0.003662`, mae `0.041184`
- 60d: sample `20`, hit `0.45`, avg `-0.014098`, median `-0.005997`, mae `0.046892`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.003708`, median `-0.001227`, mae `0.011523`
- 5d: sample `60`, hit `0.4833`, avg `-0.00525`, median `-0.001796`, mae `0.015366`
- 10d: sample `60`, hit `0.45`, avg `-0.00509`, median `-0.003071`, mae `0.020499`
- 20d: sample `60`, hit `0.6833`, avg `-0.004303`, median `0.012291`, mae `0.033167`
- 60d: sample `60`, hit `0.45`, avg `-0.00751`, median `-0.005997`, mae `0.054988`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000348`, median `-0.001227`, mae `0.00968`
- 5d: sample `20`, hit `0.45`, avg `-0.004995`, median `-0.004461`, mae `0.016254`
- 10d: sample `20`, hit `0.35`, avg `-0.010905`, median `-0.01411`, mae `0.025566`
- 20d: sample `20`, hit `0.6`, avg `-0.020592`, median `0.003662`, mae `0.041184`
- 60d: sample `20`, hit `0.45`, avg `-0.014098`, median `-0.005997`, mae `0.046892`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.003708`, median `-0.001227`, mae `0.011523`
- 5d: sample `60`, hit `0.4833`, avg `-0.00525`, median `-0.001796`, mae `0.015366`
- 10d: sample `60`, hit `0.45`, avg `-0.00509`, median `-0.003071`, mae `0.020499`
- 20d: sample `60`, hit `0.6833`, avg `-0.004303`, median `0.012291`, mae `0.033167`
- 60d: sample `60`, hit `0.45`, avg `-0.00751`, median `-0.005997`, mae `0.054988`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002925`, median `0.004569`, mae `0.012365`
- 5d: sample `20`, hit `0.6`, avg `0.002748`, median `0.008121`, mae `0.017763`
- 10d: sample `20`, hit `0.75`, avg `0.015747`, median `0.00903`, mae `0.022768`
- 20d: sample `20`, hit `0.6`, avg `0.006217`, median `0.009812`, mae `0.037302`
- 60d: sample `20`, hit `0.65`, avg `0.020311`, median `0.055266`, mae `0.07734`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001985`, median `-0.001166`, mae `0.008853`
- 5d: sample `20`, hit `0.6`, avg `-0.00139`, median `0.003714`, mae `0.01168`
- 10d: sample `20`, hit `0.65`, avg `0.003961`, median `0.007467`, mae `0.01422`
- 20d: sample `20`, hit `0.8`, avg `0.009545`, median `0.015404`, mae `0.022895`
- 60d: sample `20`, hit `0.4`, avg `-0.016391`, median `-0.01711`, mae `0.051162`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.008791`, median `0.001448`, mae `0.016036`
- 5d: sample `20`, hit `0.4`, avg `-0.009366`, median `-0.004438`, mae `0.018165`
- 10d: sample `20`, hit `0.35`, avg `-0.008327`, median `-0.015123`, mae `0.021712`
- 20d: sample `20`, hit `0.65`, avg `-0.001863`, median `0.020068`, mae `0.035422`
- 60d: sample `20`, hit `0.5`, avg `0.007958`, median `0.012092`, mae `0.06691`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000348`, median `-0.001227`, mae `0.00968`
- 5d: sample `20`, hit `0.45`, avg `-0.004995`, median `-0.004461`, mae `0.016254`
- 10d: sample `20`, hit `0.35`, avg `-0.010905`, median `-0.01411`, mae `0.025566`
- 20d: sample `20`, hit `0.6`, avg `-0.020592`, median `0.003662`, mae `0.041184`
- 60d: sample `20`, hit `0.45`, avg `-0.014098`, median `-0.005997`, mae `0.046892`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001985`, median `-0.001166`, mae `0.008853`
- 5d: sample `20`, hit `0.6`, avg `-0.00139`, median `0.003714`, mae `0.01168`
- 10d: sample `20`, hit `0.65`, avg `0.003961`, median `0.007467`, mae `0.01422`
- 20d: sample `20`, hit `0.8`, avg `0.009545`, median `0.015404`, mae `0.022895`
- 60d: sample `20`, hit `0.4`, avg `-0.016391`, median `-0.01711`, mae `0.051162`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000348`, median `-0.001227`, mae `0.00968`
- 5d: sample `20`, hit `0.45`, avg `-0.004995`, median `-0.004461`, mae `0.016254`
- 10d: sample `20`, hit `0.35`, avg `-0.010905`, median `-0.01411`, mae `0.025566`
- 20d: sample `20`, hit `0.6`, avg `-0.020592`, median `0.003662`, mae `0.041184`
- 60d: sample `20`, hit `0.45`, avg `-0.014098`, median `-0.005997`, mae `0.046892`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.00205`, median `0.000145`, mae `0.011733`
- 5d: sample `80`, hit `0.5125`, avg `-0.003251`, median `0.001259`, mae `0.015965`
- 10d: sample `80`, hit `0.525`, avg `0.000119`, median `0.002362`, mae `0.021066`
- 20d: sample `80`, hit `0.6625`, avg `-0.001673`, median `0.01011`, mae `0.034201`
- 60d: sample `80`, hit `0.5`, avg `-0.000555`, median `0.003923`, mae `0.060576`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.00205`, median `0.000145`, mae `0.011733`
- 5d: sample `80`, hit `0.5125`, avg `-0.003251`, median `0.001259`, mae `0.015965`
- 10d: sample `80`, hit `0.525`, avg `0.000119`, median `0.002362`, mae `0.021066`
- 20d: sample `80`, hit `0.6625`, avg `-0.001673`, median `0.01011`, mae `0.034201`
- 60d: sample `80`, hit `0.5`, avg `-0.000555`, median `0.003923`, mae `0.060576`

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
