# High Confidence Edge Report

Generated at: `2026-07-06T14:44:23.219866+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.002275`, median `-0.000317`, mae `0.014801`
- 5d: sample `40`, hit `0.475`, avg `-0.004258`, median `-0.001324`, mae `0.016784`
- 10d: sample `40`, hit `0.45`, avg `0.003442`, median `-0.003071`, mae `0.019116`
- 20d: sample `40`, hit `0.625`, avg `0.011208`, median `0.012958`, mae `0.032905`
- 60d: sample `40`, hit `0.65`, avg `0.03519`, median `0.052998`, mae `0.067674`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002489`, median `-0.001166`, mae `0.007996`
- 5d: sample `20`, hit `0.7`, avg `0.002442`, median `0.003888`, mae `0.0102`
- 10d: sample `20`, hit `0.55`, avg `0.003657`, median `0.003491`, mae `0.011899`
- 20d: sample `20`, hit `0.7`, avg `0.00558`, median `0.012291`, mae `0.021801`
- 60d: sample `20`, hit `0.2`, avg `-0.038559`, median `-0.03635`, mae `0.052016`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002412`, median `0.006632`, mae `0.015396`
- 5d: sample `20`, hit `0.5`, avg `-0.001068`, median `0.004655`, mae `0.021072`
- 10d: sample `20`, hit `0.55`, avg `0.00019`, median `0.005417`, mae `0.024134`
- 20d: sample `20`, hit `0.75`, avg `-0.004591`, median `0.007366`, mae `0.028809`
- 60d: sample `20`, hit `0.35`, avg `-0.015059`, median `-0.01215`, mae `0.048646`

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
- 3d: sample `8`, hit `0.125`, avg `-0.013768`, median `-0.010033`, mae `0.015446`
- 5d: sample `8`, hit `0.375`, avg `-0.011794`, median `-0.004438`, mae `0.015076`
- 10d: sample `8`, hit `0.0`, avg `-0.01387`, median `-0.010456`, mae `0.01387`
- 20d: sample `8`, hit `0.625`, avg `0.016823`, median `0.029166`, mae `0.040022`
- 60d: sample `8`, hit `0.625`, avg `0.026683`, median `0.046132`, mae `0.079296`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.013768`, median `-0.010033`, mae `0.015446`
- 5d: sample `8`, hit `0.375`, avg `-0.011794`, median `-0.004438`, mae `0.015076`
- 10d: sample `8`, hit `0.0`, avg `-0.01387`, median `-0.010456`, mae `0.01387`
- 20d: sample `8`, hit `0.625`, avg `0.016823`, median `0.029166`, mae `0.040022`
- 60d: sample `8`, hit `0.625`, avg `0.026683`, median `0.046132`, mae `0.079296`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.002275, 'median_return': -0.000317, 'mean_absolute_return': 0.014801, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.004258, 'median_return': -0.001324, 'mean_absolute_return': 0.016784, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.03091}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.003442, 'median_return': -0.003071, 'mean_absolute_return': 0.019116, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.011208, 'median_return': 0.012958, 'mean_absolute_return': 0.032905, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.03519, 'median_return': 0.052998, 'mean_absolute_return': 0.067674, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.002489, 'median_return': -0.001166, 'mean_absolute_return': 0.007996, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.011957}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.002442, 'median_return': 0.003888, 'mean_absolute_return': 0.0102, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.003657, 'median_return': 0.003491, 'mean_absolute_return': 0.011899, 'max_adverse_excursion': -0.017864, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.00558, 'median_return': 0.012291, 'mean_absolute_return': 0.021801, 'max_adverse_excursion': -0.050277, 'max_favorable_excursion': 0.043353}, '60d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.038559, 'median_return': -0.03635, 'mean_absolute_return': 0.052016, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.048421}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.013768, 'median_return': -0.010033, 'mean_absolute_return': 0.015446, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.011794, 'median_return': -0.004438, 'mean_absolute_return': 0.015076, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.01387, 'median_return': -0.010456, 'mean_absolute_return': 0.01387, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016823, 'median_return': 0.029166, 'mean_absolute_return': 0.040022, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.026683, 'median_return': 0.046132, 'mean_absolute_return': 0.079296, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.000245, 'median_return': 0.001558, 'mean_absolute_return': 0.013004, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.000673, 'median_return': 0.003197, 'mean_absolute_return': 0.016336, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.004522, 'median_return': 0.003262, 'mean_absolute_return': 0.019088, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.004632, 'median_return': 0.010653, 'mean_absolute_return': 0.027892, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': 0.001691, 'median_return': -0.009954, 'mean_absolute_return': 0.056748, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.130806}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.5}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.4625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.05, 'both_hit': 28, 'both_miss': 32}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.0, 'both_hit': 33, 'both_miss': 27}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.025, 'both_hit': 29, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.125, 'both_hit': 39, 'both_miss': 21}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 30, 'both_miss': 30}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.001157, 'median_return': 0.000145, 'mean_absolute_return': 0.013248, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': -0.001785, 'median_return': 0.002694, 'mean_absolute_return': 0.01621, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.034374}, '10d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': 0.002683, 'median_return': 0.000242, 'mean_absolute_return': 0.018566, 'max_adverse_excursion': -0.039317, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.005851, 'median_return': 0.010788, 'mean_absolute_return': 0.029105, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.083836}, '60d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': 0.00419, 'median_return': -0.005523, 'mean_absolute_return': 0.059003, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001157`, median `0.000145`, mae `0.013248`
- 5d: sample `80`, hit `0.5375`, avg `-0.001785`, median `0.002694`, mae `0.01621`
- 10d: sample `80`, hit `0.5`, avg `0.002683`, median `0.000242`, mae `0.018566`
- 20d: sample `80`, hit `0.675`, avg `0.005851`, median `0.010788`, mae `0.029105`
- 60d: sample `80`, hit `0.4625`, avg `0.00419`, median `-0.005523`, mae `0.059003`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001157`, median `0.000145`, mae `0.013248`
- 5d: sample `80`, hit `0.5375`, avg `-0.001785`, median `0.002694`, mae `0.01621`
- 10d: sample `80`, hit `0.5`, avg `0.002683`, median `0.000242`, mae `0.018566`
- 20d: sample `80`, hit `0.675`, avg `0.005851`, median `0.010788`, mae `0.029105`
- 60d: sample `80`, hit `0.4625`, avg `0.00419`, median `-0.005523`, mae `0.059003`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.000713`, median `0.000453`, mae `0.014999`
- 5d: sample `60`, hit `0.4833`, avg `-0.003194`, median `-0.001324`, mae `0.018213`
- 10d: sample `60`, hit `0.4833`, avg `0.002358`, median `-0.0004`, mae `0.020789`
- 20d: sample `60`, hit `0.6667`, avg `0.005942`, median `0.009812`, mae `0.03154`
- 60d: sample `60`, hit `0.55`, avg `0.01844`, median `0.019715`, mae `0.061332`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.001157`, median `0.000145`, mae `0.013248`
- 5d: sample `80`, hit `0.5375`, avg `-0.001785`, median `0.002694`, mae `0.01621`
- 10d: sample `80`, hit `0.5`, avg `0.002683`, median `0.000242`, mae `0.018566`
- 20d: sample `80`, hit `0.675`, avg `0.005851`, median `0.010788`, mae `0.029105`
- 60d: sample `80`, hit `0.4625`, avg `0.00419`, median `-0.005523`, mae `0.059003`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.000713`, median `0.000453`, mae `0.014999`
- 5d: sample `60`, hit `0.4833`, avg `-0.003194`, median `-0.001324`, mae `0.018213`
- 10d: sample `60`, hit `0.4833`, avg `0.002358`, median `-0.0004`, mae `0.020789`
- 20d: sample `60`, hit `0.6667`, avg `0.005942`, median `0.009812`, mae `0.03154`
- 60d: sample `60`, hit `0.55`, avg `0.01844`, median `0.019715`, mae `0.061332`

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
- 3d: sample `40`, hit `0.425`, avg `-0.005232`, median `-0.002654`, mae `0.01219`
- 5d: sample `40`, hit `0.55`, avg `-0.002978`, median `0.002694`, mae `0.01332`
- 10d: sample `40`, hit `0.4`, avg `-0.000767`, median `-0.003071`, mae `0.013694`
- 20d: sample `40`, hit `0.7`, avg `0.011891`, median `0.013178`, mae `0.026255`
- 60d: sample `40`, hit `0.425`, avg `-0.000449`, median `-0.01711`, mae `0.060577`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002918`, median `0.003538`, mae `0.014307`
- 5d: sample `40`, hit `0.525`, avg `-0.000592`, median `0.003197`, mae `0.0191`
- 10d: sample `40`, hit `0.6`, avg `0.006133`, median `0.005417`, mae `0.023438`
- 20d: sample `40`, hit `0.65`, avg `-0.000188`, median `0.007366`, mae `0.031955`
- 60d: sample `40`, hit `0.5`, avg `0.008829`, median `0.003923`, mae `0.057428`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.005232`, median `-0.002654`, mae `0.01219`
- 5d: sample `40`, hit `0.55`, avg `-0.002978`, median `0.002694`, mae `0.01332`
- 10d: sample `40`, hit `0.4`, avg `-0.000767`, median `-0.003071`, mae `0.013694`
- 20d: sample `40`, hit `0.7`, avg `0.011891`, median `0.013178`, mae `0.026255`
- 60d: sample `40`, hit `0.425`, avg `-0.000449`, median `-0.01711`, mae `0.060577`

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
