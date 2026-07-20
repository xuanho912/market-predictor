# High Confidence Edge Report

Generated at: `2026-07-20T22:35:23.354735+00:00`

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
- 3d: sample `60`, hit `0.6167`, avg `-0.001269`, median `0.001139`, mae `0.012511`
- 5d: sample `60`, hit `0.5167`, avg `-0.002612`, median `0.000762`, mae `0.017812`
- 10d: sample `60`, hit `0.4`, avg `-0.002394`, median `-0.007117`, mae `0.023846`
- 20d: sample `60`, hit `0.6`, avg `0.011049`, median `0.020226`, mae `0.042385`
- 60d: sample `60`, hit `0.6167`, avg `0.026788`, median `0.053855`, mae `0.080184`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001845`, median `0.008009`, mae `0.022248`
- 5d: sample `20`, hit `0.65`, avg `0.008217`, median `0.016595`, mae `0.027389`
- 10d: sample `20`, hit `0.7`, avg `0.01401`, median `0.027869`, mae `0.041566`
- 20d: sample `20`, hit `0.75`, avg `0.02869`, median `0.046035`, mae `0.049512`
- 60d: sample `20`, hit `0.7`, avg `0.046322`, median `0.069439`, mae `0.097904`

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
- 3d: sample `8`, hit `0.75`, avg `0.002378`, median `0.002067`, mae `0.007354`
- 5d: sample `8`, hit `0.5`, avg `-0.001896`, median `0.000688`, mae `0.006605`
- 10d: sample `8`, hit `0.25`, avg `-0.009546`, median `-0.007491`, mae `0.022965`
- 20d: sample `8`, hit `0.5`, avg `0.002572`, median `0.020226`, mae `0.02809`
- 60d: sample `8`, hit `0.75`, avg `0.038862`, median `0.059948`, mae `0.059213`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.010615`, median `-0.001658`, mae `0.017881`
- 5d: sample `8`, hit `0.5`, avg `-0.014012`, median `0.003005`, mae `0.019416`
- 10d: sample `8`, hit `0.0`, avg `-0.015682`, median `-0.011432`, mae `0.015682`
- 20d: sample `8`, hit `0.75`, avg `0.021328`, median `0.029166`, mae `0.03557`
- 60d: sample `8`, hit `0.875`, avg `0.057995`, median `0.059495`, mae `0.072214`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': -0.001269, 'median_return': 0.001139, 'mean_absolute_return': 0.012511, 'max_adverse_excursion': -0.040548, 'max_favorable_excursion': 0.039325}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.002612, 'median_return': 0.000762, 'mean_absolute_return': 0.017812, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': -0.002394, 'median_return': -0.007117, 'mean_absolute_return': 0.023846, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.065408}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.011049, 'median_return': 0.020226, 'mean_absolute_return': 0.042385, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.026788, 'median_return': 0.053855, 'mean_absolute_return': 0.080184, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.1448}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.010615, 'median_return': -0.001658, 'mean_absolute_return': 0.017881, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.020012}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.014012, 'median_return': 0.003005, 'mean_absolute_return': 0.019416, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.0, 'avg_return': -0.015682, 'median_return': -0.011432, 'mean_absolute_return': 0.015682, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': -0.0004}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.021328, 'median_return': 0.029166, 'mean_absolute_return': 0.03557, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.057995, 'median_return': 0.059495, 'mean_absolute_return': 0.072214, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.000635, 'median_return': 0.001199, 'mean_absolute_return': 0.014619, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.039325}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001663, 'median_return': 0.002774, 'mean_absolute_return': 0.020294, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.003639, 'median_return': 0.005691, 'mean_absolute_return': 0.029675, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.065408}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.014807, 'median_return': 0.026005, 'mean_absolute_return': 0.045122, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.028747, 'median_return': 0.059104, 'mean_absolute_return': 0.085992, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21267}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.475}, '10d': {'sample_size': 80, 'hit_rate': 0.375}, '20d': {'sample_size': 80, 'hit_rate': 0.5125}, '60d': {'sample_size': 80, 'hit_rate': 0.5375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.075, 'both_hit': 23, 'both_miss': 17}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 20, 'both_miss': 20}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': -0.125, 'both_hit': 15, 'both_miss': 25}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.125, 'both_hit': 26, 'both_miss': 14}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.1, 'both_hit': 27, 'both_miss': 13}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': -0.00049, 'median_return': 0.001139, 'mean_absolute_return': 0.014945, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.039325}, '5d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 9.5e-05, 'median_return': 0.002774, 'mean_absolute_return': 0.020206, 'max_adverse_excursion': -0.068766, 'max_favorable_excursion': 0.069956}, '10d': {'sample_size': 80, 'hit_rate': 0.475, 'avg_return': 0.001707, 'median_return': -0.0004, 'mean_absolute_return': 0.028276, 'max_adverse_excursion': -0.06893, 'max_favorable_excursion': 0.065408}, '20d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.015459, 'median_return': 0.026005, 'mean_absolute_return': 0.044167, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.134212}, '60d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.031672, 'median_return': 0.059104, 'mean_absolute_return': 0.084614, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.21267}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.004837`, median `0.000766`, mae `0.013254`
- 5d: sample `40`, hit `0.475`, avg `-0.008458`, median `-0.001429`, mae `0.017774`
- 10d: sample `40`, hit `0.35`, avg `-0.005144`, median `-0.007117`, mae `0.019231`
- 20d: sample `40`, hit `0.55`, avg `0.006351`, median `0.017149`, mae `0.035855`
- 60d: sample `40`, hit `0.575`, avg `0.02343`, median `0.037425`, mae `0.063949`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001845`, median `0.008009`, mae `0.022248`
- 5d: sample `20`, hit `0.65`, avg `0.008217`, median `0.016595`, mae `0.027389`
- 10d: sample `20`, hit `0.7`, avg `0.01401`, median `0.027869`, mae `0.041566`
- 20d: sample `20`, hit `0.75`, avg `0.02869`, median `0.046035`, mae `0.049512`
- 60d: sample `20`, hit `0.7`, avg `0.046322`, median `0.069439`, mae `0.097904`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.004837`, median `0.000766`, mae `0.013254`
- 5d: sample `40`, hit `0.475`, avg `-0.008458`, median `-0.001429`, mae `0.017774`
- 10d: sample `40`, hit `0.35`, avg `-0.005144`, median `-0.007117`, mae `0.019231`
- 20d: sample `40`, hit `0.55`, avg `0.006351`, median `0.017149`, mae `0.035855`
- 60d: sample `40`, hit `0.575`, avg `0.02343`, median `0.037425`, mae `0.063949`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009254`, median `-0.001658`, mae `0.017698`
- 5d: sample `20`, hit `0.4`, avg `-0.013936`, median `-0.004438`, mae `0.022916`
- 10d: sample `20`, hit `0.25`, avg `-0.004054`, median `-0.007011`, mae `0.017535`
- 20d: sample `20`, hit `0.6`, avg `0.011941`, median `0.020068`, mae `0.039407`
- 60d: sample `20`, hit `0.65`, avg `0.034698`, median `0.046132`, mae `0.076434`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001845`, median `0.008009`, mae `0.022248`
- 5d: sample `20`, hit `0.65`, avg `0.008217`, median `0.016595`, mae `0.027389`
- 10d: sample `20`, hit `0.7`, avg `0.01401`, median `0.027869`, mae `0.041566`
- 20d: sample `20`, hit `0.75`, avg `0.02869`, median `0.046035`, mae `0.049512`
- 60d: sample `20`, hit `0.7`, avg `0.046322`, median `0.069439`, mae `0.097904`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.004837`, median `0.000766`, mae `0.013254`
- 5d: sample `40`, hit `0.475`, avg `-0.008458`, median `-0.001429`, mae `0.017774`
- 10d: sample `40`, hit `0.35`, avg `-0.005144`, median `-0.007117`, mae `0.019231`
- 20d: sample `40`, hit `0.55`, avg `0.006351`, median `0.017149`, mae `0.035855`
- 60d: sample `40`, hit `0.575`, avg `0.02343`, median `0.037425`, mae `0.063949`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.005867`, median `0.006983`, mae `0.011025`
- 5d: sample `20`, hit `0.6`, avg `0.009079`, median `0.012885`, mae `0.017887`
- 10d: sample `20`, hit `0.5`, avg `0.003107`, median `0.006208`, mae `0.033076`
- 20d: sample `20`, hit `0.7`, avg `0.020447`, median `0.042881`, mae `0.055445`
- 60d: sample `20`, hit `0.7`, avg `0.033503`, median `0.102417`, mae `0.112655`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009254`, median `-0.001658`, mae `0.017698`
- 5d: sample `20`, hit `0.4`, avg `-0.013936`, median `-0.004438`, mae `0.022916`
- 10d: sample `20`, hit `0.25`, avg `-0.004054`, median `-0.007011`, mae `0.017535`
- 20d: sample `20`, hit `0.6`, avg `0.011941`, median `0.020068`, mae `0.039407`
- 60d: sample `20`, hit `0.65`, avg `0.034698`, median `0.046132`, mae `0.076434`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001845`, median `0.008009`, mae `0.022248`
- 5d: sample `20`, hit `0.65`, avg `0.008217`, median `0.016595`, mae `0.027389`
- 10d: sample `20`, hit `0.7`, avg `0.01401`, median `0.027869`, mae `0.041566`
- 20d: sample `20`, hit `0.75`, avg `0.02869`, median `0.046035`, mae `0.049512`
- 60d: sample `20`, hit `0.7`, avg `0.046322`, median `0.069439`, mae `0.097904`

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
- 3d: sample `40`, hit `0.55`, avg `-0.004837`, median `0.000766`, mae `0.013254`
- 5d: sample `40`, hit `0.475`, avg `-0.008458`, median `-0.001429`, mae `0.017774`
- 10d: sample `40`, hit `0.35`, avg `-0.005144`, median `-0.007117`, mae `0.019231`
- 20d: sample `40`, hit `0.55`, avg `0.006351`, median `0.017149`, mae `0.035855`
- 60d: sample `40`, hit `0.575`, avg `0.02343`, median `0.037425`, mae `0.063949`

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
- 3d: sample `80`, hit `0.6`, avg `-0.00049`, median `0.001139`, mae `0.014945`
- 5d: sample `80`, hit `0.55`, avg `9.5e-05`, median `0.002774`, mae `0.020206`
- 10d: sample `80`, hit `0.475`, avg `0.001707`, median `-0.0004`, mae `0.028276`
- 20d: sample `80`, hit `0.6375`, avg `0.015459`, median `0.026005`, mae `0.044167`
- 60d: sample `80`, hit `0.6375`, avg `0.031672`, median `0.059104`, mae `0.084614`

### bounce_with_flow_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `-0.001269`, median `0.001139`, mae `0.012511`
- 5d: sample `60`, hit `0.5167`, avg `-0.002612`, median `0.000762`, mae `0.017812`
- 10d: sample `60`, hit `0.4`, avg `-0.002394`, median `-0.007117`, mae `0.023846`
- 20d: sample `60`, hit `0.6`, avg `0.011049`, median `0.020226`, mae `0.042385`
- 60d: sample `60`, hit `0.6167`, avg `0.026788`, median `0.053855`, mae `0.080184`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001845`, median `0.008009`, mae `0.022248`
- 5d: sample `20`, hit `0.65`, avg `0.008217`, median `0.016595`, mae `0.027389`
- 10d: sample `20`, hit `0.7`, avg `0.01401`, median `0.027869`, mae `0.041566`
- 20d: sample `20`, hit `0.75`, avg `0.02869`, median `0.046035`, mae `0.049512`
- 60d: sample `20`, hit `0.7`, avg `0.046322`, median `0.069439`, mae `0.097904`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
