# High Confidence Edge Report

Generated at: `2026-07-29T00:10:44.142574+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `-0.001325`, median `0.001199`, mae `0.019968`
- 5d: sample `60`, hit `0.5667`, avg `-0.000159`, median `0.003005`, mae `0.022136`
- 10d: sample `60`, hit `0.5167`, avg `0.008086`, median `0.001574`, mae `0.026765`
- 20d: sample `60`, hit `0.65`, avg `0.023888`, median `0.026113`, mae `0.04449`
- 60d: sample `60`, hit `0.7167`, avg `0.047853`, median `0.059131`, mae `0.077788`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.004033`, median `-0.0002`, mae `0.017636`
- 5d: sample `20`, hit `0.45`, avg `-0.007026`, median `-0.000413`, mae `0.027112`
- 10d: sample `20`, hit `0.55`, avg `-0.003205`, median `0.011411`, mae `0.037074`
- 20d: sample `20`, hit `0.55`, avg `-0.007088`, median `0.017237`, mae `0.062225`
- 60d: sample `20`, hit `0.45`, avg `-0.028388`, median `-0.00384`, mae `0.097194`

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
- 3d: sample `8`, hit `0.125`, avg `-0.021369`, median `-0.030499`, mae `0.026372`
- 5d: sample `8`, hit `0.25`, avg `-0.028609`, median `-0.026253`, mae `0.032304`
- 10d: sample `8`, hit `0.0`, avg `-0.017639`, median `-0.011432`, mae `0.017639`
- 20d: sample `8`, hit `0.5`, avg `0.001093`, median `0.029166`, mae `0.050735`
- 60d: sample `8`, hit `0.625`, avg `0.027797`, median `0.046132`, mae `0.084515`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.125`, avg `-0.021369`, median `-0.030499`, mae `0.026372`
- 5d: sample `8`, hit `0.25`, avg `-0.028609`, median `-0.026253`, mae `0.032304`
- 10d: sample `8`, hit `0.0`, avg `-0.017639`, median `-0.011432`, mae `0.017639`
- 20d: sample `8`, hit `0.5`, avg `0.001093`, median `0.029166`, mae `0.050735`
- 60d: sample `8`, hit `0.625`, avg `0.027797`, median `0.046132`, mae `0.084515`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.001325, 'median_return': 0.001199, 'mean_absolute_return': 0.019968, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': -0.000159, 'median_return': 0.003005, 'mean_absolute_return': 0.022136, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.057302}, '10d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.008086, 'median_return': 0.001574, 'mean_absolute_return': 0.026765, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.023888, 'median_return': 0.026113, 'mean_absolute_return': 0.04449, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.047853, 'median_return': 0.059131, 'mean_absolute_return': 0.077788, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.21366}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.021369, 'median_return': -0.030499, 'mean_absolute_return': 0.026372, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.028609, 'median_return': -0.026253, 'mean_absolute_return': 0.032304, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.017639, 'median_return': -0.011432, 'mean_absolute_return': 0.017639, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001093, 'median_return': 0.029166, 'mean_absolute_return': 0.050735, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.027797, 'median_return': 0.046132, 'mean_absolute_return': 0.084515, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.00015, 'median_return': 0.001199, 'mean_absolute_return': 0.018608, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.001095, 'median_return': 0.003005, 'mean_absolute_return': 0.022389, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.007808, 'median_return': 0.012396, 'mean_absolute_return': 0.030643, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.017817, 'median_return': 0.021759, 'mean_absolute_return': 0.048722, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.028904, 'median_return': 0.055167, 'mean_absolute_return': 0.082431, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.3}, '20d': {'sample_size': 80, 'hit_rate': 0.45}, '60d': {'sample_size': 80, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.075, 'both_hit': 9, 'both_miss': 11}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.125, 'both_hit': 8, 'both_miss': 12}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.3, 'both_hit': 6, 'both_miss': 14}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': -0.2, 'both_hit': 14, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.125, 'both_hit': 15, 'both_miss': 5}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': -0.001325, 'median_return': 0.001199, 'mean_absolute_return': 0.019968, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.044434}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': -0.000159, 'median_return': 0.003005, 'mean_absolute_return': 0.022136, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.057302}, '10d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.008086, 'median_return': 0.001574, 'mean_absolute_return': 0.026765, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.023888, 'median_return': 0.026113, 'mean_absolute_return': 0.04449, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.047853, 'median_return': 0.059131, 'mean_absolute_return': 0.077788, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.21366}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.004033, 'median_return': -0.0002, 'mean_absolute_return': 0.017636, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.007026, 'median_return': -0.000413, 'mean_absolute_return': 0.027112, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.003205, 'median_return': 0.011411, 'mean_absolute_return': 0.037074, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.007088, 'median_return': 0.017237, 'mean_absolute_return': 0.062225, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.028388, 'median_return': -0.00384, 'mean_absolute_return': 0.097194, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.129489}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.00713`, median `-0.000285`, mae `0.016578`
- 5d: sample `40`, hit `0.45`, avg `-0.009525`, median `-0.001429`, mae `0.018018`
- 10d: sample `40`, hit `0.325`, avg `-0.006099`, median `-0.007755`, mae `0.017061`
- 20d: sample `40`, hit `0.575`, avg `0.008687`, median `0.016745`, mae `0.031656`
- 60d: sample `40`, hit `0.65`, avg `0.030218`, median `0.046132`, mae `0.05846`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.003126`, median `0.004667`, mae `0.022191`
- 5d: sample `40`, hit `0.625`, avg `0.005775`, median `0.010083`, mae `0.028742`
- 10d: sample `40`, hit `0.725`, avg `0.016625`, median `0.027869`, mae `0.041623`
- 20d: sample `40`, hit `0.675`, avg `0.023602`, median `0.046831`, mae `0.066191`
- 60d: sample `40`, hit `0.65`, avg `0.027368`, median `0.072268`, mae `0.106818`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.00713`, median `-0.000285`, mae `0.016578`
- 5d: sample `40`, hit `0.45`, avg `-0.009525`, median `-0.001429`, mae `0.018018`
- 10d: sample `40`, hit `0.325`, avg `-0.006099`, median `-0.007755`, mae `0.017061`
- 20d: sample `40`, hit `0.575`, avg `0.008687`, median `0.016745`, mae `0.031656`
- 60d: sample `40`, hit `0.65`, avg `0.030218`, median `0.046132`, mae `0.05846`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.009167`, median `-0.001658`, mae `0.020077`
- 5d: sample `20`, hit `0.4`, avg `-0.014375`, median `-0.016062`, mae `0.022151`
- 10d: sample `20`, hit `0.3`, avg `-0.004863`, median `-0.007011`, mae `0.016136`
- 20d: sample `20`, hit `0.7`, avg `0.016938`, median `0.026113`, mae `0.039158`
- 60d: sample `20`, hit `0.75`, avg `0.047276`, median `0.059495`, mae `0.078633`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.010286`, median `0.013951`, mae `0.026746`
- 5d: sample `20`, hit `0.8`, avg `0.018575`, median `0.028258`, mae `0.030373`
- 10d: sample `20`, hit `0.9`, avg `0.036454`, median `0.039397`, mae `0.046173`
- 20d: sample `20`, hit `0.8`, avg `0.054291`, median `0.063669`, mae `0.070157`
- 60d: sample `20`, hit `0.85`, avg `0.083124`, median `0.106076`, mae `0.116442`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.00713`, median `-0.000285`, mae `0.016578`
- 5d: sample `40`, hit `0.45`, avg `-0.009525`, median `-0.001429`, mae `0.018018`
- 10d: sample `40`, hit `0.325`, avg `-0.006099`, median `-0.007755`, mae `0.017061`
- 20d: sample `40`, hit `0.575`, avg `0.008687`, median `0.016745`, mae `0.031656`
- 60d: sample `40`, hit `0.65`, avg `0.030218`, median `0.046132`, mae `0.05846`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.009167`, median `-0.001658`, mae `0.020077`
- 5d: sample `20`, hit `0.4`, avg `-0.014375`, median `-0.016062`, mae `0.022151`
- 10d: sample `20`, hit `0.3`, avg `-0.004863`, median `-0.007011`, mae `0.016136`
- 20d: sample `20`, hit `0.7`, avg `0.016938`, median `0.026113`, mae `0.039158`
- 60d: sample `20`, hit `0.75`, avg `0.047276`, median `0.059495`, mae `0.078633`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.003126`, median `0.004667`, mae `0.022191`
- 5d: sample `40`, hit `0.625`, avg `0.005775`, median `0.010083`, mae `0.028742`
- 10d: sample `40`, hit `0.725`, avg `0.016625`, median `0.027869`, mae `0.041623`
- 20d: sample `40`, hit `0.675`, avg `0.023602`, median `0.046831`, mae `0.066191`
- 60d: sample `40`, hit `0.65`, avg `0.027368`, median `0.072268`, mae `0.106818`

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
- 3d: sample `80`, hit `0.525`, avg `-0.002002`, median `0.000707`, mae `0.019385`
- 5d: sample `80`, hit `0.5375`, avg `-0.001875`, median `0.001695`, mae `0.02338`
- 10d: sample `80`, hit `0.525`, avg `0.005263`, median `0.001607`, mae `0.029342`
- 20d: sample `80`, hit `0.625`, avg `0.016144`, median `0.021759`, mae `0.048923`
- 60d: sample `80`, hit `0.65`, avg `0.028793`, median `0.053855`, mae `0.082639`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.00713`, median `-0.000285`, mae `0.016578`
- 5d: sample `40`, hit `0.45`, avg `-0.009525`, median `-0.001429`, mae `0.018018`
- 10d: sample `40`, hit `0.325`, avg `-0.006099`, median `-0.007755`, mae `0.017061`
- 20d: sample `40`, hit `0.575`, avg `0.008687`, median `0.016745`, mae `0.031656`
- 60d: sample `40`, hit `0.65`, avg `0.030218`, median `0.046132`, mae `0.05846`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.002597`, median `0.002067`, mae `0.019913`
- 5d: sample `40`, hit `0.65`, avg `0.00695`, median `0.006452`, mae `0.022129`
- 10d: sample `40`, hit `0.625`, avg `0.01456`, median `0.017778`, mae `0.032079`
- 20d: sample `40`, hit `0.625`, avg `0.027364`, median `0.02865`, mae `0.047155`
- 60d: sample `40`, hit `0.7`, avg `0.048142`, median `0.058473`, mae `0.077365`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.005092`, median `0.000201`, mae `0.01308`
- 5d: sample `20`, hit `0.5`, avg `-0.004676`, median `0.000688`, mae `0.013886`
- 10d: sample `20`, hit `0.35`, avg `-0.007334`, median `-0.009882`, mae `0.017986`
- 20d: sample `20`, hit `0.45`, avg `0.000436`, median `-0.001203`, mae `0.024154`
- 60d: sample `20`, hit `0.55`, avg `0.013159`, median `0.006294`, mae `0.038288`

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
