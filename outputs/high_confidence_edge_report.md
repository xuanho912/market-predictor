# High Confidence Edge Report

Generated at: `2026-07-22T14:24:59.452863+00:00`

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
- 3d: sample `20`, hit `0.35`, avg `-0.011343`, median `-0.010033`, mae `0.021393`
- 5d: sample `20`, hit `0.4`, avg `-0.011905`, median `-0.004438`, mae `0.02292`
- 10d: sample `20`, hit `0.35`, avg `-0.003471`, median `-0.007011`, mae `0.020373`
- 20d: sample `20`, hit `0.65`, avg `0.01147`, median `0.021759`, mae `0.042657`
- 60d: sample `20`, hit `0.7`, avg `0.036482`, median `0.059131`, mae `0.074207`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.003811`, median `-0.001617`, mae `0.01371`
- 5d: sample `60`, hit `0.4167`, avg `-0.004541`, median `-0.003609`, mae `0.015494`
- 10d: sample `60`, hit `0.4333`, avg `-0.003817`, median `-0.007117`, mae `0.024268`
- 20d: sample `60`, hit `0.6333`, avg `-0.000163`, median `0.007748`, mae `0.039072`
- 60d: sample `60`, hit `0.4667`, avg `-0.008793`, median `-0.003049`, mae `0.076117`

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
- 3d: sample `8`, hit `0.375`, avg `-0.020804`, median `-0.030499`, mae `0.024014`
- 5d: sample `8`, hit `0.25`, avg `-0.028823`, median `-0.026253`, mae `0.030532`
- 10d: sample `8`, hit `0.125`, avg `-0.016415`, median `-0.01796`, mae `0.021223`
- 20d: sample `8`, hit `0.625`, avg `-0.00875`, median `0.020068`, mae `0.040476`
- 60d: sample `8`, hit `0.625`, avg `0.011496`, median `0.046132`, mae `0.068214`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.020804`, median `-0.030499`, mae `0.024014`
- 5d: sample `8`, hit `0.25`, avg `-0.028823`, median `-0.026253`, mae `0.030532`
- 10d: sample `8`, hit `0.125`, avg `-0.016415`, median `-0.01796`, mae `0.021223`
- 20d: sample `8`, hit `0.625`, avg `-0.00875`, median `0.020068`, mae `0.040476`
- 60d: sample `8`, hit `0.625`, avg `0.011496`, median `0.046132`, mae `0.068214`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.011343, 'median_return': -0.010033, 'mean_absolute_return': 0.021393, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.029522}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.011905, 'median_return': -0.004438, 'mean_absolute_return': 0.02292, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.003471, 'median_return': -0.007011, 'mean_absolute_return': 0.020373, 'max_adverse_excursion': -0.037842, 'max_favorable_excursion': 0.043492}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.01147, 'median_return': 0.021759, 'mean_absolute_return': 0.042657, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.036482, 'median_return': 0.059131, 'mean_absolute_return': 0.074207, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.020804, 'median_return': -0.030499, 'mean_absolute_return': 0.024014, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.028823, 'median_return': -0.026253, 'mean_absolute_return': 0.030532, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.003829}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.016415, 'median_return': -0.01796, 'mean_absolute_return': 0.021223, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.00875, 'median_return': 0.020068, 'mean_absolute_return': 0.040476, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.011496, 'median_return': 0.046132, 'mean_absolute_return': 0.068214, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.004015, 'median_return': -0.002441, 'mean_absolute_return': 0.014699, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.003889, 'median_return': -0.002855, 'mean_absolute_return': 0.015886, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.002321, 'median_return': -0.006017, 'mean_absolute_return': 0.023524, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.004022, 'median_return': 0.015444, 'mean_absolute_return': 0.039912, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.001529, 'median_return': 0.006294, 'mean_absolute_return': 0.076465, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.144029}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.575}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.00981, 'median_return': -0.009085, 'mean_absolute_return': 0.017366, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.029522}, '5d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.01046, 'median_return': -0.004438, 'mean_absolute_return': 0.019169, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.046339}, '10d': {'sample_size': 40, 'hit_rate': 0.3, 'avg_return': -0.008048, 'median_return': -0.01051, 'mean_absolute_return': 0.020991, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.043492}, '20d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.001684, 'median_return': 0.000213, 'mean_absolute_return': 0.036798, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.086905}, '60d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.017319, 'median_return': 0.024156, 'mean_absolute_return': 0.059414, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.001578, 'median_return': -0.0002, 'mean_absolute_return': 0.013895, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.002304, 'median_return': -0.003609, 'mean_absolute_return': 0.015531, 'max_adverse_excursion': -0.056697, 'max_favorable_excursion': 0.039173}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.000588, 'median_return': 0.006208, 'mean_absolute_return': 0.025597, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.007174, 'median_return': 0.018939, 'mean_absolute_return': 0.043139, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.012268, 'median_return': 0.00483, 'mean_absolute_return': 0.091865, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.141614}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.375`, avg `-0.00981`, median `-0.009085`, mae `0.017366`
- 5d: sample `40`, hit `0.425`, avg `-0.01046`, median `-0.004438`, mae `0.019169`
- 10d: sample `40`, hit `0.3`, avg `-0.008048`, median `-0.01051`, mae `0.020991`
- 20d: sample `40`, hit `0.5`, avg `-0.001684`, median `0.000213`, mae `0.036798`
- 60d: sample `40`, hit `0.55`, avg `0.017319`, median `0.024156`, mae `0.059414`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002054`, median `0.006513`, mae `0.018236`
- 5d: sample `20`, hit `0.4`, avg `-0.002018`, median `-0.007381`, mae `0.019446`
- 10d: sample `20`, hit `0.65`, avg `0.012609`, median `0.01795`, mae `0.026162`
- 20d: sample `20`, hit `0.9`, avg `0.025881`, median `0.03392`, mae `0.034477`
- 60d: sample `20`, hit `0.6`, avg `0.013798`, median `0.043615`, mae `0.080662`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011343`, median `-0.010033`, mae `0.021393`
- 5d: sample `20`, hit `0.4`, avg `-0.011905`, median `-0.004438`, mae `0.02292`
- 10d: sample `20`, hit `0.35`, avg `-0.003471`, median `-0.007011`, mae `0.020373`
- 20d: sample `20`, hit `0.65`, avg `0.01147`, median `0.021759`, mae `0.042657`
- 60d: sample `20`, hit `0.7`, avg `0.036482`, median `0.059131`, mae `0.074207`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011343`, median `-0.010033`, mae `0.021393`
- 5d: sample `20`, hit `0.4`, avg `-0.011905`, median `-0.004438`, mae `0.02292`
- 10d: sample `20`, hit `0.35`, avg `-0.003471`, median `-0.007011`, mae `0.020373`
- 20d: sample `20`, hit `0.65`, avg `0.01147`, median `0.021759`, mae `0.042657`
- 60d: sample `20`, hit `0.7`, avg `0.036482`, median `0.059131`, mae `0.074207`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002054`, median `0.006513`, mae `0.018236`
- 5d: sample `20`, hit `0.4`, avg `-0.002018`, median `-0.007381`, mae `0.019446`
- 10d: sample `20`, hit `0.65`, avg `0.012609`, median `0.01795`, mae `0.026162`
- 20d: sample `20`, hit `0.9`, avg `0.025881`, median `0.03392`, mae `0.034477`
- 60d: sample `20`, hit `0.6`, avg `0.013798`, median `0.043615`, mae `0.080662`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011343`, median `-0.010033`, mae `0.021393`
- 5d: sample `20`, hit `0.4`, avg `-0.011905`, median `-0.004438`, mae `0.02292`
- 10d: sample `20`, hit `0.35`, avg `-0.003471`, median `-0.007011`, mae `0.020373`
- 20d: sample `20`, hit `0.65`, avg `0.01147`, median `0.021759`, mae `0.042657`
- 60d: sample `20`, hit `0.7`, avg `0.036482`, median `0.059131`, mae `0.074207`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011343`, median `-0.010033`, mae `0.021393`
- 5d: sample `20`, hit `0.4`, avg `-0.011905`, median `-0.004438`, mae `0.02292`
- 10d: sample `20`, hit `0.35`, avg `-0.003471`, median `-0.007011`, mae `0.020373`
- 20d: sample `20`, hit `0.65`, avg `0.01147`, median `0.021759`, mae `0.042657`
- 60d: sample `20`, hit `0.7`, avg `0.036482`, median `0.059131`, mae `0.074207`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002054`, median `0.006513`, mae `0.018236`
- 5d: sample `20`, hit `0.4`, avg `-0.002018`, median `-0.007381`, mae `0.019446`
- 10d: sample `20`, hit `0.65`, avg `0.012609`, median `0.01795`, mae `0.026162`
- 20d: sample `20`, hit `0.9`, avg `0.025881`, median `0.03392`, mae `0.034477`
- 60d: sample `20`, hit `0.6`, avg `0.013798`, median `0.043615`, mae `0.080662`

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
- 3d: sample `80`, hit `0.425`, avg `-0.005694`, median `-0.003723`, mae `0.01563`
- 5d: sample `80`, hit `0.4125`, avg `-0.006382`, median `-0.004438`, mae `0.01735`
- 10d: sample `80`, hit `0.4125`, avg `-0.00373`, median `-0.007117`, mae `0.023294`
- 20d: sample `80`, hit `0.6375`, avg `0.002745`, median `0.015444`, mae `0.039968`
- 60d: sample `80`, hit `0.525`, avg `0.002526`, median `0.010234`, mae `0.07564`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.011343`, median `-0.010033`, mae `0.021393`
- 5d: sample `20`, hit `0.4`, avg `-0.011905`, median `-0.004438`, mae `0.02292`
- 10d: sample `20`, hit `0.35`, avg `-0.003471`, median `-0.007011`, mae `0.020373`
- 20d: sample `20`, hit `0.65`, avg `0.01147`, median `0.021759`, mae `0.042657`
- 60d: sample `20`, hit `0.7`, avg `0.036482`, median `0.059131`, mae `0.074207`

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
