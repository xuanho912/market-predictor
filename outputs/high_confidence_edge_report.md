# High Confidence Edge Report

Generated at: `2026-07-01T05:56:28.156737+00:00`

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
- 3d: sample `60`, hit `0.3833`, avg `-0.001582`, median `-0.002151`, mae `0.01595`
- 5d: sample `60`, hit `0.3667`, avg `-0.005453`, median `-0.007788`, mae `0.0204`
- 10d: sample `60`, hit `0.4833`, avg `0.001651`, median `-0.0004`, mae `0.021893`
- 20d: sample `60`, hit `0.7`, avg `0.02192`, median `0.028791`, mae `0.035472`
- 60d: sample `60`, hit `0.7333`, avg `0.052753`, median `0.067551`, mae `0.080259`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003795`, median `-0.002654`, mae `0.010955`
- 5d: sample `20`, hit `0.45`, avg `-0.005946`, median `-0.004389`, mae `0.01424`
- 10d: sample `20`, hit `0.4`, avg `-0.00758`, median `-0.007117`, mae `0.020134`
- 20d: sample `20`, hit `0.7`, avg `-0.003539`, median `0.015404`, mae `0.032139`
- 60d: sample `20`, hit `0.5`, avg `-0.002904`, median `0.031838`, mae `0.055533`

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
- 3d: sample `8`, hit `0.5`, avg `0.004016`, median `0.016671`, mae `0.017848`
- 5d: sample `8`, hit `0.25`, avg `-0.010099`, median `-0.00855`, mae `0.012901`
- 10d: sample `8`, hit `0.375`, avg `0.003671`, median `-0.001222`, mae `0.009067`
- 20d: sample `8`, hit `0.875`, avg `0.024906`, median `0.031196`, mae `0.027287`
- 60d: sample `8`, hit `1.0`, avg `0.081857`, median `0.092646`, mae `0.081857`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.004016`, median `0.016671`, mae `0.017848`
- 5d: sample `8`, hit `0.25`, avg `-0.010099`, median `-0.00855`, mae `0.012901`
- 10d: sample `8`, hit `0.375`, avg `0.003671`, median `-0.001222`, mae `0.009067`
- 20d: sample `8`, hit `0.875`, avg `0.024906`, median `0.031196`, mae `0.027287`
- 60d: sample `8`, hit `1.0`, avg `0.081857`, median `0.092646`, mae `0.081857`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.001582, 'median_return': -0.002151, 'mean_absolute_return': 0.01595, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.005453, 'median_return': -0.007788, 'mean_absolute_return': 0.0204, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 60, 'hit_rate': 0.4833, 'avg_return': 0.001651, 'median_return': -0.0004, 'mean_absolute_return': 0.021893, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.02192, 'median_return': 0.028791, 'mean_absolute_return': 0.035472, 'max_adverse_excursion': -0.070246, 'max_favorable_excursion': 0.100414}, '60d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.052753, 'median_return': 0.067551, 'mean_absolute_return': 0.080259, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.279401}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004016, 'median_return': 0.016671, 'mean_absolute_return': 0.017848, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.024354}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.010099, 'median_return': -0.00855, 'mean_absolute_return': 0.012901, 'max_adverse_excursion': -0.027126, 'max_favorable_excursion': 0.011002}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.003671, 'median_return': -0.001222, 'mean_absolute_return': 0.009067, 'max_adverse_excursion': -0.011849, 'max_favorable_excursion': 0.023979}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.024906, 'median_return': 0.031196, 'mean_absolute_return': 0.027287, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.041903}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.081857, 'median_return': 0.092646, 'mean_absolute_return': 0.081857, 'max_adverse_excursion': 0.025315, 'max_favorable_excursion': 0.117712}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.002818, 'median_return': -0.003036, 'mean_absolute_return': 0.014352, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': -0.005074, 'median_return': -0.006464, 'mean_absolute_return': 0.019522, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.001138, 'median_return': -0.001083, 'mean_absolute_return': 0.022829, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.014516, 'median_return': 0.018139, 'mean_absolute_return': 0.035456, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.100414}, '60d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.034059, 'median_return': 0.044344, 'mean_absolute_return': 0.073213, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.279401}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4375}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.6}, '60d': {'sample_size': 80, 'hit_rate': 0.675}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.075, 'both_hit': 18, 'both_miss': 22}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': -0.05, 'both_hit': 15, 'both_miss': 25}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.075, 'both_hit': 18, 'both_miss': 22}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.125, 'both_hit': 33, 'both_miss': 7}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.1, 'both_hit': 30, 'both_miss': 10}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 0, 'non_close_call_sample_size': 80, 'close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'non_close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.3875, 'avg_return': -0.002135, 'median_return': -0.002654, 'mean_absolute_return': 0.014701, 'max_adverse_excursion': -0.040381, 'max_favorable_excursion': 0.044644}, '5d': {'sample_size': 80, 'hit_rate': 0.3875, 'avg_return': -0.005576, 'median_return': -0.006798, 'mean_absolute_return': 0.01886, 'max_adverse_excursion': -0.052834, 'max_favorable_excursion': 0.037821}, '10d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.000657, 'median_return': -0.001222, 'mean_absolute_return': 0.021453, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.015555, 'median_return': 0.019987, 'mean_absolute_return': 0.034639, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.100414}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.038839, 'median_return': 0.050225, 'mean_absolute_return': 0.074077, 'max_adverse_excursion': -0.15215, 'max_favorable_excursion': 0.279401}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.001582`, median `-0.002151`, mae `0.01595`
- 5d: sample `60`, hit `0.3667`, avg `-0.005453`, median `-0.007788`, mae `0.0204`
- 10d: sample `60`, hit `0.4833`, avg `0.001651`, median `-0.0004`, mae `0.021893`
- 20d: sample `60`, hit `0.7`, avg `0.02192`, median `0.028791`, mae `0.035472`
- 60d: sample `60`, hit `0.7333`, avg `0.052753`, median `0.067551`, mae `0.080259`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003795`, median `-0.002654`, mae `0.010955`
- 5d: sample `20`, hit `0.45`, avg `-0.005946`, median `-0.004389`, mae `0.01424`
- 10d: sample `20`, hit `0.4`, avg `-0.00758`, median `-0.007117`, mae `0.020134`
- 20d: sample `20`, hit `0.7`, avg `-0.003539`, median `0.015404`, mae `0.032139`
- 60d: sample `20`, hit `0.5`, avg `-0.002904`, median `0.031838`, mae `0.055533`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.001582`, median `-0.002151`, mae `0.01595`
- 5d: sample `60`, hit `0.3667`, avg `-0.005453`, median `-0.007788`, mae `0.0204`
- 10d: sample `60`, hit `0.4833`, avg `0.001651`, median `-0.0004`, mae `0.021893`
- 20d: sample `60`, hit `0.7`, avg `0.02192`, median `0.028791`, mae `0.035472`
- 60d: sample `60`, hit `0.7333`, avg `0.052753`, median `0.067551`, mae `0.080259`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001898`, median `-0.001658`, mae `0.017159`
- 5d: sample `40`, hit `0.375`, avg `-0.006335`, median `-0.012956`, mae `0.021527`
- 10d: sample `40`, hit `0.45`, avg `0.000976`, median `-0.001083`, mae `0.021067`
- 20d: sample `40`, hit `0.825`, avg `0.025005`, median `0.029166`, mae `0.032761`
- 60d: sample `40`, hit `0.75`, avg `0.043066`, median `0.06458`, mae `0.068932`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.001582`, median `-0.002151`, mae `0.01595`
- 5d: sample `60`, hit `0.3667`, avg `-0.005453`, median `-0.007788`, mae `0.0204`
- 10d: sample `60`, hit `0.4833`, avg `0.001651`, median `-0.0004`, mae `0.021893`
- 20d: sample `60`, hit `0.7`, avg `0.02192`, median `0.028791`, mae `0.035472`
- 60d: sample `60`, hit `0.7333`, avg `0.052753`, median `0.067551`, mae `0.080259`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.001898`, median `-0.001658`, mae `0.017159`
- 5d: sample `40`, hit `0.375`, avg `-0.006335`, median `-0.012956`, mae `0.021527`
- 10d: sample `40`, hit `0.45`, avg `0.000976`, median `-0.001083`, mae `0.021067`
- 20d: sample `40`, hit `0.825`, avg `0.025005`, median `0.029166`, mae `0.032761`
- 60d: sample `40`, hit `0.75`, avg `0.043066`, median `0.06458`, mae `0.068932`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003795`, median `-0.002654`, mae `0.010955`
- 5d: sample `20`, hit `0.45`, avg `-0.005946`, median `-0.004389`, mae `0.01424`
- 10d: sample `20`, hit `0.4`, avg `-0.00758`, median `-0.007117`, mae `0.020134`
- 20d: sample `20`, hit `0.7`, avg `-0.003539`, median `0.015404`, mae `0.032139`
- 60d: sample `20`, hit `0.5`, avg `-0.002904`, median `0.031838`, mae `0.055533`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.001582`, median `-0.002151`, mae `0.01595`
- 5d: sample `60`, hit `0.3667`, avg `-0.005453`, median `-0.007788`, mae `0.0204`
- 10d: sample `60`, hit `0.4833`, avg `0.001651`, median `-0.0004`, mae `0.021893`
- 20d: sample `60`, hit `0.7`, avg `0.02192`, median `0.028791`, mae `0.035472`
- 60d: sample `60`, hit `0.7333`, avg `0.052753`, median `0.067551`, mae `0.080259`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.003795`, median `-0.002654`, mae `0.010955`
- 5d: sample `20`, hit `0.45`, avg `-0.005946`, median `-0.004389`, mae `0.01424`
- 10d: sample `20`, hit `0.4`, avg `-0.00758`, median `-0.007117`, mae `0.020134`
- 20d: sample `20`, hit `0.7`, avg `-0.003539`, median `0.015404`, mae `0.032139`
- 60d: sample `20`, hit `0.5`, avg `-0.002904`, median `0.031838`, mae `0.055533`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.3875`, avg `-0.002135`, median `-0.002654`, mae `0.014701`
- 5d: sample `80`, hit `0.3875`, avg `-0.005576`, median `-0.006798`, mae `0.01886`
- 10d: sample `80`, hit `0.4625`, avg `-0.000657`, median `-0.001222`, mae `0.021453`
- 20d: sample `80`, hit `0.7`, avg `0.015555`, median `0.019987`, mae `0.034639`
- 60d: sample `80`, hit `0.675`, avg `0.038839`, median `0.050225`, mae `0.074077`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.3833`, avg `-0.001582`, median `-0.002151`, mae `0.01595`
- 5d: sample `60`, hit `0.3667`, avg `-0.005453`, median `-0.007788`, mae `0.0204`
- 10d: sample `60`, hit `0.4833`, avg `0.001651`, median `-0.0004`, mae `0.021893`
- 20d: sample `60`, hit `0.7`, avg `0.02192`, median `0.028791`, mae `0.035472`
- 60d: sample `60`, hit `0.7333`, avg `0.052753`, median `0.067551`, mae `0.080259`

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
