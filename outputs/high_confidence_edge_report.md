# High Confidence Edge Report

Generated at: `2026-07-31T14:38:27.792187+00:00`

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
- 3d: sample `20`, hit `0.45`, avg `-0.007641`, median `-0.001658`, mae `0.019996`
- 5d: sample `20`, hit `0.4`, avg `-0.014181`, median `-0.004438`, mae `0.022684`
- 10d: sample `20`, hit `0.25`, avg `-0.005124`, median `-0.007755`, mae `0.017258`
- 20d: sample `20`, hit `0.6`, avg `0.011254`, median `0.020068`, mae `0.037711`
- 60d: sample `20`, hit `0.65`, avg `0.030096`, median `0.046132`, mae `0.071813`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.000452`, median `0.000766`, mae `0.016858`
- 5d: sample `60`, hit `0.4833`, avg `-0.001185`, median `-0.000513`, mae `0.020736`
- 10d: sample `60`, hit `0.5667`, avg `0.005339`, median `0.013774`, mae `0.031645`
- 20d: sample `60`, hit `0.5833`, avg `0.008653`, median `0.015416`, mae `0.049624`
- 60d: sample `60`, hit `0.4833`, avg `-0.005771`, median `-0.003034`, mae `0.088677`

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
- 3d: sample `8`, hit `0.25`, avg `-0.019064`, median `-0.026364`, mae `0.025746`
- 5d: sample `8`, hit `0.25`, avg `-0.026817`, median `-0.026253`, mae `0.028836`
- 10d: sample `8`, hit `0.125`, avg `-0.012517`, median `-0.007755`, mae `0.015616`
- 20d: sample `8`, hit `0.5`, avg `0.009732`, median `0.020068`, mae `0.032514`
- 60d: sample `8`, hit `0.625`, avg `0.027859`, median `0.037425`, mae `0.05702`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.019064`, median `-0.026364`, mae `0.025746`
- 5d: sample `8`, hit `0.25`, avg `-0.026817`, median `-0.026253`, mae `0.028836`
- 10d: sample `8`, hit `0.125`, avg `-0.012517`, median `-0.007755`, mae `0.015616`
- 20d: sample `8`, hit `0.5`, avg `0.009732`, median `0.020068`, mae `0.032514`
- 60d: sample `8`, hit `0.625`, avg `0.027859`, median `0.037425`, mae `0.05702`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.007641, 'median_return': -0.001658, 'mean_absolute_return': 0.019996, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.026729}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.014181, 'median_return': -0.004438, 'mean_absolute_return': 0.022684, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 20, 'hit_rate': 0.25, 'avg_return': -0.005124, 'median_return': -0.007755, 'mean_absolute_return': 0.017258, 'max_adverse_excursion': -0.035191, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.011254, 'median_return': 0.020068, 'mean_absolute_return': 0.037711, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.030096, 'median_return': 0.046132, 'mean_absolute_return': 0.071813, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.019064, 'median_return': -0.026364, 'mean_absolute_return': 0.025746, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.026817, 'median_return': -0.026253, 'mean_absolute_return': 0.028836, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.005072}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.012517, 'median_return': -0.007755, 'mean_absolute_return': 0.015616, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.012396}, '20d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.009732, 'median_return': 0.020068, 'mean_absolute_return': 0.032514, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.027859, 'median_return': 0.037425, 'mean_absolute_return': 0.05702, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.000372, 'median_return': 0.001139, 'mean_absolute_return': 0.016742, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.040779}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.001947, 'median_return': -0.000513, 'mean_absolute_return': 0.020377, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.004416, 'median_return': 0.005691, 'mean_absolute_return': 0.029429, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.009256, 'median_return': 0.015444, 'mean_absolute_return': 0.048216, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.000455, 'median_return': 0.006294, 'mean_absolute_return': 0.08751, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21366}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.45}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.3875}, '20d': {'sample_size': 80, 'hit_rate': 0.4625}, '60d': {'sample_size': 80, 'hit_rate': 0.55}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': -0.000532, 'median_return': 0.001199, 'mean_absolute_return': 0.018015, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.040779}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.001862, 'median_return': 0.000762, 'mean_absolute_return': 0.020696, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.057302}, '10d': {'sample_size': 60, 'hit_rate': 0.4667, 'avg_return': 0.005299, 'median_return': -0.0004, 'mean_absolute_return': 0.025954, 'max_adverse_excursion': -0.068474, 'max_favorable_excursion': 0.080212}, '20d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.016957, 'median_return': 0.016745, 'mean_absolute_return': 0.043422, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.129427}, '60d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.023764, 'median_return': 0.032982, 'mean_absolute_return': 0.074714, 'max_adverse_excursion': -0.177732, 'max_favorable_excursion': 0.21366}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.004691, 'median_return': -0.001058, 'mean_absolute_return': 0.016525, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.039325}, '5d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.012151, 'median_return': -0.010857, 'mean_absolute_return': 0.022801, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.005005, 'median_return': 0.013774, 'mean_absolute_return': 0.034331, 'max_adverse_excursion': -0.080816, 'max_favorable_excursion': 0.065408}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.013657, 'median_return': 0.011139, 'mean_absolute_return': 0.056315, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.05851, 'median_return': -0.058227, 'mean_absolute_return': 0.1137, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.114377}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.004618`, median `0.000201`, mae `0.015727`
- 5d: sample `40`, hit `0.45`, avg `-0.009167`, median `-0.001429`, mae `0.016927`
- 10d: sample `40`, hit `0.275`, avg `-0.00743`, median `-0.009882`, mae `0.01649`
- 20d: sample `40`, hit `0.425`, avg `-0.000452`, median `-0.001941`, mae `0.032377`
- 60d: sample `40`, hit `0.525`, avg `0.014418`, median `0.006294`, mae `0.055789`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001475`, median `0.006247`, mae `0.019558`
- 5d: sample `40`, hit `0.475`, avg `0.000298`, median `-0.001129`, mae `0.025519`
- 10d: sample `40`, hit `0.7`, avg `0.012876`, median `0.023905`, mae `0.039605`
- 20d: sample `40`, hit `0.75`, avg `0.019059`, median `0.032252`, mae `0.060914`
- 60d: sample `40`, hit `0.525`, avg `-0.008027`, median `0.027637`, mae `0.113132`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.007641`, median `-0.001658`, mae `0.019996`
- 5d: sample `20`, hit `0.4`, avg `-0.014181`, median `-0.004438`, mae `0.022684`
- 10d: sample `20`, hit `0.25`, avg `-0.005124`, median `-0.007755`, mae `0.017258`
- 20d: sample `20`, hit `0.6`, avg `0.011254`, median `0.020068`, mae `0.037711`
- 60d: sample `20`, hit `0.65`, avg `0.030096`, median `0.046132`, mae `0.071813`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.007641`, median `-0.001658`, mae `0.019996`
- 5d: sample `20`, hit `0.4`, avg `-0.014181`, median `-0.004438`, mae `0.022684`
- 10d: sample `20`, hit `0.25`, avg `-0.005124`, median `-0.007755`, mae `0.017258`
- 20d: sample `20`, hit `0.6`, avg `0.011254`, median `0.020068`, mae `0.037711`
- 60d: sample `20`, hit `0.65`, avg `0.030096`, median `0.046132`, mae `0.071813`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.007641`, median `-0.001658`, mae `0.019996`
- 5d: sample `20`, hit `0.4`, avg `-0.014181`, median `-0.004438`, mae `0.022684`
- 10d: sample `20`, hit `0.25`, avg `-0.005124`, median `-0.007755`, mae `0.017258`
- 20d: sample `20`, hit `0.6`, avg `0.011254`, median `0.020068`, mae `0.037711`
- 60d: sample `20`, hit `0.65`, avg `0.030096`, median `0.046132`, mae `0.071813`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.007641`, median `-0.001658`, mae `0.019996`
- 5d: sample `20`, hit `0.4`, avg `-0.014181`, median `-0.004438`, mae `0.022684`
- 10d: sample `20`, hit `0.25`, avg `-0.005124`, median `-0.007755`, mae `0.017258`
- 20d: sample `20`, hit `0.6`, avg `0.011254`, median `0.020068`, mae `0.037711`
- 60d: sample `20`, hit `0.65`, avg `0.030096`, median `0.046132`, mae `0.071813`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001475`, median `0.006247`, mae `0.019558`
- 5d: sample `40`, hit `0.475`, avg `0.000298`, median `-0.001129`, mae `0.025519`
- 10d: sample `40`, hit `0.7`, avg `0.012876`, median `0.023905`, mae `0.039605`
- 20d: sample `40`, hit `0.75`, avg `0.019059`, median `0.032252`, mae `0.060914`
- 60d: sample `40`, hit `0.525`, avg `-0.008027`, median `0.027637`, mae `0.113132`

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
- 3d: sample `80`, hit `0.525`, avg `-0.001571`, median `0.000707`, mae `0.017643`
- 5d: sample `80`, hit `0.4625`, avg `-0.004434`, median `-0.001429`, mae `0.021223`
- 10d: sample `80`, hit `0.4875`, avg `0.002723`, median `-0.000231`, mae `0.028048`
- 20d: sample `80`, hit `0.5875`, avg `0.009304`, median `0.015444`, mae `0.046646`
- 60d: sample `80`, hit `0.525`, avg `0.003195`, median `0.012092`, mae `0.084461`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.007641`, median `-0.001658`, mae `0.019996`
- 5d: sample `20`, hit `0.4`, avg `-0.014181`, median `-0.004438`, mae `0.022684`
- 10d: sample `20`, hit `0.25`, avg `-0.005124`, median `-0.007755`, mae `0.017258`
- 20d: sample `20`, hit `0.6`, avg `0.011254`, median `0.020068`, mae `0.037711`
- 60d: sample `20`, hit `0.65`, avg `0.030096`, median `0.046132`, mae `0.071813`

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
