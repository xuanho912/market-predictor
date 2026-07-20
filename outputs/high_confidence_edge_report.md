# High Confidence Edge Report

Generated at: `2026-07-20T14:36:49.190328+00:00`

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
- 3d: sample `20`, hit `0.4`, avg `-0.010277`, median `-0.009383`, mae `0.018722`
- 5d: sample `20`, hit `0.4`, avg `-0.015047`, median `-0.004438`, mae `0.021805`
- 10d: sample `20`, hit `0.2`, avg `-0.007033`, median `-0.007755`, mae `0.016906`
- 20d: sample `20`, hit `0.55`, avg `0.008718`, median `0.020068`, mae `0.040916`
- 60d: sample `20`, hit `0.6`, avg `0.028015`, median `0.046132`, mae `0.079667`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.001703`, median `0.002067`, mae `0.012057`
- 5d: sample `60`, hit `0.6167`, avg `0.004053`, median `0.003476`, mae `0.01548`
- 10d: sample `60`, hit `0.5167`, avg `0.001576`, median `0.000397`, mae `0.027719`
- 20d: sample `60`, hit `0.6667`, avg `0.013694`, median `0.020226`, mae `0.040002`
- 60d: sample `60`, hit `0.6`, avg `0.028996`, median `0.057625`, mae `0.083874`

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
- 3d: sample `8`, hit `0.375`, avg `-0.012643`, median `-0.001658`, mae `0.015853`
- 5d: sample `8`, hit `0.375`, avg `-0.016654`, median `-0.016062`, mae `0.02079`
- 10d: sample `8`, hit `0.125`, avg `-0.011849`, median `-0.007011`, mae `0.016657`
- 20d: sample `8`, hit `0.875`, avg `0.025786`, median `0.033999`, mae `0.039612`
- 60d: sample `8`, hit `0.875`, avg `0.065978`, median `0.099838`, mae `0.080196`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.012643`, median `-0.001658`, mae `0.015853`
- 5d: sample `8`, hit `0.375`, avg `-0.016654`, median `-0.016062`, mae `0.02079`
- 10d: sample `8`, hit `0.125`, avg `-0.011849`, median `-0.007011`, mae `0.016657`
- 20d: sample `8`, hit `0.875`, avg `0.025786`, median `0.033999`, mae `0.039612`
- 60d: sample `8`, hit `0.875`, avg `0.065978`, median `0.099838`, mae `0.080196`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010277, 'median_return': -0.009383, 'mean_absolute_return': 0.018722, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.0207}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.015047, 'median_return': -0.004438, 'mean_absolute_return': 0.021805, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.2, 'avg_return': -0.007033, 'median_return': -0.007755, 'mean_absolute_return': 0.016906, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.008718, 'median_return': 0.020068, 'mean_absolute_return': 0.040916, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.028015, 'median_return': 0.046132, 'mean_absolute_return': 0.079667, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012643, 'median_return': -0.001658, 'mean_absolute_return': 0.015853, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.016654, 'median_return': -0.016062, 'mean_absolute_return': 0.02079, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.011849, 'median_return': -0.007011, 'mean_absolute_return': 0.016657, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.019233}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.025786, 'median_return': 0.033999, 'mean_absolute_return': 0.039612, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.065978, 'median_return': 0.099838, 'mean_absolute_return': 0.080196, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': -3.1e-05, 'median_return': 0.001199, 'mean_absolute_return': 0.013487, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.001048, 'median_return': 0.002453, 'mean_absolute_return': 0.016647, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.000676, 'median_return': -0.00367, 'mean_absolute_return': 0.025945, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.010969, 'median_return': 0.012025, 'mean_absolute_return': 0.040299, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.024614, 'median_return': 0.053855, 'mean_absolute_return': 0.083114, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5125}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.3875}, '20d': {'sample_size': 80, 'hit_rate': 0.4625}, '60d': {'sample_size': 80, 'hit_rate': 0.525}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': -0.001292, 'median_return': 0.001122, 'mean_absolute_return': 0.013723, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': -0.000722, 'median_return': 0.001695, 'mean_absolute_return': 0.017061, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.04835}, '10d': {'sample_size': 80, 'hit_rate': 0.4375, 'avg_return': -0.000576, 'median_return': -0.006017, 'mean_absolute_return': 0.025016, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.01245, 'median_return': 0.020068, 'mean_absolute_return': 0.04023, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.086756}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.028751, 'median_return': 0.055167, 'mean_absolute_return': 0.082822, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.005974`, median `0.000201`, mae `0.014065`
- 5d: sample `40`, hit `0.5`, avg `-0.009056`, median `0.000415`, mae `0.016757`
- 10d: sample `40`, hit `0.3`, avg `-0.007064`, median `-0.007755`, mae `0.01759`
- 20d: sample `40`, hit `0.5`, avg `0.004665`, median `0.000213`, mae `0.035251`
- 60d: sample `40`, hit `0.525`, avg `0.01962`, median `0.032982`, mae `0.063714`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001454`, median `0.006632`, mae `0.017684`
- 5d: sample `20`, hit `0.6`, avg `0.007364`, median `0.009517`, mae `0.021306`
- 10d: sample `20`, hit `0.7`, avg `0.015053`, median `0.022558`, mae `0.036241`
- 20d: sample `20`, hit `0.9`, avg `0.03449`, median `0.046035`, mae `0.040362`
- 60d: sample `20`, hit `0.7`, avg `0.054457`, median `0.068712`, mae `0.088816`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.010277`, median `-0.009383`, mae `0.018722`
- 5d: sample `20`, hit `0.4`, avg `-0.015047`, median `-0.004438`, mae `0.021805`
- 10d: sample `20`, hit `0.2`, avg `-0.007033`, median `-0.007755`, mae `0.016906`
- 20d: sample `20`, hit `0.55`, avg `0.008718`, median `0.020068`, mae `0.040916`
- 60d: sample `20`, hit `0.6`, avg `0.028015`, median `0.046132`, mae `0.079667`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.010277`, median `-0.009383`, mae `0.018722`
- 5d: sample `20`, hit `0.4`, avg `-0.015047`, median `-0.004438`, mae `0.021805`
- 10d: sample `20`, hit `0.2`, avg `-0.007033`, median `-0.007755`, mae `0.016906`
- 20d: sample `20`, hit `0.55`, avg `0.008718`, median `0.020068`, mae `0.040916`
- 60d: sample `20`, hit `0.6`, avg `0.028015`, median `0.046132`, mae `0.079667`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001454`, median `0.006632`, mae `0.017684`
- 5d: sample `20`, hit `0.6`, avg `0.007364`, median `0.009517`, mae `0.021306`
- 10d: sample `20`, hit `0.7`, avg `0.015053`, median `0.022558`, mae `0.036241`
- 20d: sample `20`, hit `0.9`, avg `0.03449`, median `0.046035`, mae `0.040362`
- 60d: sample `20`, hit `0.7`, avg `0.054457`, median `0.068712`, mae `0.088816`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.010277`, median `-0.009383`, mae `0.018722`
- 5d: sample `20`, hit `0.4`, avg `-0.015047`, median `-0.004438`, mae `0.021805`
- 10d: sample `20`, hit `0.2`, avg `-0.007033`, median `-0.007755`, mae `0.016906`
- 20d: sample `20`, hit `0.55`, avg `0.008718`, median `0.020068`, mae `0.040916`
- 60d: sample `20`, hit `0.6`, avg `0.028015`, median `0.046132`, mae `0.079667`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.005325`, median `0.006983`, mae `0.009081`
- 5d: sample `20`, hit `0.65`, avg `0.00786`, median `0.011917`, mae `0.013425`
- 10d: sample `20`, hit `0.45`, avg `-0.003231`, median `-0.013321`, mae `0.028643`
- 20d: sample `20`, hit `0.65`, avg `0.005983`, median `0.026005`, mae `0.050057`
- 60d: sample `20`, hit `0.65`, avg `0.021304`, median `0.099631`, mae `0.115047`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.010277`, median `-0.009383`, mae `0.018722`
- 5d: sample `20`, hit `0.4`, avg `-0.015047`, median `-0.004438`, mae `0.021805`
- 10d: sample `20`, hit `0.2`, avg `-0.007033`, median `-0.007755`, mae `0.016906`
- 20d: sample `20`, hit `0.55`, avg `0.008718`, median `0.020068`, mae `0.040916`
- 60d: sample `20`, hit `0.6`, avg `0.028015`, median `0.046132`, mae `0.079667`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001454`, median `0.006632`, mae `0.017684`
- 5d: sample `20`, hit `0.6`, avg `0.007364`, median `0.009517`, mae `0.021306`
- 10d: sample `20`, hit `0.7`, avg `0.015053`, median `0.022558`, mae `0.036241`
- 20d: sample `20`, hit `0.9`, avg `0.03449`, median `0.046035`, mae `0.040362`
- 60d: sample `20`, hit `0.7`, avg `0.054457`, median `0.068712`, mae `0.088816`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.005974`, median `0.000201`, mae `0.014065`
- 5d: sample `40`, hit `0.5`, avg `-0.009056`, median `0.000415`, mae `0.016757`
- 10d: sample `40`, hit `0.3`, avg `-0.007064`, median `-0.007755`, mae `0.01759`
- 20d: sample `40`, hit `0.5`, avg `0.004665`, median `0.000213`, mae `0.035251`
- 60d: sample `40`, hit `0.525`, avg `0.01962`, median `0.032982`, mae `0.063714`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `-0.001292`, median `0.001122`, mae `0.013723`
- 5d: sample `80`, hit `0.5625`, avg `-0.000722`, median `0.001695`, mae `0.017061`
- 10d: sample `80`, hit `0.4375`, avg `-0.000576`, median `-0.006017`, mae `0.025016`
- 20d: sample `80`, hit `0.6375`, avg `0.01245`, median `0.020068`, mae `0.04023`
- 60d: sample `80`, hit `0.6`, avg `0.028751`, median `0.055167`, mae `0.082822`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `-0.002476`, median `0.001199`, mae `0.013901`
- 5d: sample `40`, hit `0.525`, avg `-0.003593`, median `0.001239`, mae `0.017615`
- 10d: sample `40`, hit `0.325`, avg `-0.005132`, median `-0.010456`, mae `0.022775`
- 20d: sample `40`, hit `0.6`, avg `0.00735`, median `0.020068`, mae `0.045487`
- 60d: sample `40`, hit `0.625`, avg `0.02466`, median `0.078322`, mae `0.097357`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.000108`, median `0.001122`, mae `0.013546`
- 5d: sample `40`, hit `0.6`, avg `0.002149`, median `0.002774`, mae `0.016507`
- 10d: sample `40`, hit `0.55`, avg `0.003979`, median `0.003262`, mae `0.027257`
- 20d: sample `40`, hit `0.675`, avg `0.01755`, median `0.020226`, mae `0.034974`
- 60d: sample `40`, hit `0.575`, avg `0.032842`, median `0.053855`, mae `0.068288`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
