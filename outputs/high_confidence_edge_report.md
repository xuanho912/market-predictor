# High Confidence Edge Report

Generated at: `2026-09-05T05:48:47.260674+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.5125`, avg `-0.001891`, median `0.000603`, mae `0.013142`
- 5d: sample `80`, hit `0.5375`, avg `-1e-06`, median `0.000762`, mae `0.015917`
- 10d: sample `80`, hit `0.4125`, avg `0.001741`, median `-0.007117`, mae `0.02556`
- 20d: sample `80`, hit `0.6625`, avg `0.008537`, median `0.023289`, mae `0.038443`
- 60d: sample `80`, hit `0.6625`, avg `0.029108`, median `0.057625`, mae `0.076846`

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
- 3d: sample `8`, hit `0.75`, avg `0.005498`, median `0.013911`, mae `0.013634`
- 5d: sample `8`, hit `0.875`, avg `0.015418`, median `0.019001`, mae `0.018612`
- 10d: sample `8`, hit `0.5`, avg `0.006302`, median `0.014312`, mae `0.028561`
- 20d: sample `8`, hit `0.75`, avg `0.011006`, median `0.046529`, mae `0.040175`
- 60d: sample `8`, hit `0.75`, avg `0.025361`, median `0.070559`, mae `0.08093`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.009071`, median `0.001558`, mae `0.01267`
- 5d: sample `8`, hit `0.375`, avg `-0.013834`, median `-0.012956`, mae `0.01797`
- 10d: sample `8`, hit `0.375`, avg `-0.003721`, median `-0.0004`, mae `0.015659`
- 20d: sample `8`, hit `0.875`, avg `0.016337`, median `0.029166`, mae `0.030162`
- 60d: sample `8`, hit `0.875`, avg `0.050804`, median `0.059495`, mae `0.065022`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.009071, 'median_return': 0.001558, 'mean_absolute_return': 0.01267, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.006714}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.013834, 'median_return': -0.012956, 'mean_absolute_return': 0.01797, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.009709}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.003721, 'median_return': -0.0004, 'mean_absolute_return': 0.015659, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.020918}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.016337, 'median_return': 0.029166, 'mean_absolute_return': 0.030162, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.058396}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.050804, 'median_return': 0.059495, 'mean_absolute_return': 0.065022, 'max_adverse_excursion': -0.056873, 'max_favorable_excursion': 0.121826}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.001094, 'median_return': 0.000603, 'mean_absolute_return': 0.013195, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001536, 'median_return': 0.000873, 'mean_absolute_return': 0.015689, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 72, 'hit_rate': 0.4167, 'avg_return': 0.002347, 'median_return': -0.007491, 'mean_absolute_return': 0.02666, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.007671, 'median_return': 0.023289, 'mean_absolute_return': 0.039363, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.026697, 'median_return': 0.057625, 'mean_absolute_return': 0.07816, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.4625}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.3375}, '60d': {'sample_size': 80, 'hit_rate': 0.3375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': -0.025, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.075, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3375, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': -0.325, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.00185, 'median_return': 0.001558, 'mean_absolute_return': 0.013404, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.000675, 'median_return': 0.003005, 'mean_absolute_return': 0.016801, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.003408, 'median_return': -0.001222, 'mean_absolute_return': 0.025434, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.062181}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.01643, 'median_return': 0.031658, 'mean_absolute_return': 0.041806, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.030156, 'median_return': 0.070559, 'mean_absolute_return': 0.087216, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.144029}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': -0.001932, 'median_return': -0.001641, 'mean_absolute_return': 0.01288, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.000677, 'median_return': 0.000688, 'mean_absolute_return': 0.015032, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.04629}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': 7.4e-05, 'median_return': -0.010413, 'mean_absolute_return': 0.025686, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.000645, 'median_return': 0.007004, 'mean_absolute_return': 0.035081, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.02806, 'median_return': 0.049712, 'mean_absolute_return': 0.066476, 'max_adverse_excursion': -0.118336, 'max_favorable_excursion': 0.19145}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.002666`, median `-0.001658`, mae `0.013209`
- 5d: sample `60`, hit `0.4833`, avg `-0.002773`, median `-0.00244`, mae `0.015293`
- 10d: sample `60`, hit `0.3833`, avg `0.000557`, median `-0.007117`, mae `0.023335`
- 20d: sample `60`, hit `0.6333`, avg `0.00806`, median `0.02086`, mae `0.035954`
- 60d: sample `60`, hit `0.6833`, avg `0.035648`, median `0.057625`, mae `0.07084`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `-0.001522`, median `-0.001658`, mae `0.015101`
- 5d: sample `40`, hit `0.45`, avg `-0.002235`, median `-0.005477`, mae `0.017979`
- 10d: sample `40`, hit `0.5`, avg `0.007414`, median `0.000937`, mae `0.024143`
- 20d: sample `40`, hit `0.775`, avg `0.022962`, median `0.028804`, mae `0.033678`
- 60d: sample `40`, hit `0.825`, avg `0.056437`, median `0.073517`, mae `0.078478`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.002666`, median `-0.001658`, mae `0.013209`
- 5d: sample `60`, hit `0.4833`, avg `-0.002773`, median `-0.00244`, mae `0.015293`
- 10d: sample `60`, hit `0.3833`, avg `0.000557`, median `-0.007117`, mae `0.023335`
- 20d: sample `60`, hit `0.6333`, avg `0.00806`, median `0.02086`, mae `0.035954`
- 60d: sample `60`, hit `0.6833`, avg `0.035648`, median `0.057625`, mae `0.07084`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.001891`, median `0.000603`, mae `0.013142`
- 5d: sample `80`, hit `0.5375`, avg `-1e-06`, median `0.000762`, mae `0.015917`
- 10d: sample `80`, hit `0.4125`, avg `0.001741`, median `-0.007117`, mae `0.02556`
- 20d: sample `80`, hit `0.6625`, avg `0.008537`, median `0.023289`, mae `0.038443`
- 60d: sample `80`, hit `0.6625`, avg `0.029108`, median `0.057625`, mae `0.076846`

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
