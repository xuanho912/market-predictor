# High Confidence Edge Report

Generated at: `2026-09-10T23:23:19.834175+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `8`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `8`, gate `insufficient`
- 5d: completed `8`, gate `insufficient`
- 10d: completed `8`, gate `insufficient`
- 20d: completed `8`, gate `insufficient`
- 60d: completed `8`, gate `insufficient`

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
- 3d: sample `80`, hit `0.5875`, avg `0.000354`, median `0.003785`, mae `0.014851`
- 5d: sample `80`, hit `0.575`, avg `-0.002314`, median `0.001971`, mae `0.017228`
- 10d: sample `80`, hit `0.425`, avg `-0.003483`, median `-0.006017`, mae `0.02531`
- 20d: sample `80`, hit `0.5625`, avg `0.006527`, median `0.00745`, mae `0.037231`
- 60d: sample `80`, hit `0.625`, avg `0.027297`, median `0.053301`, mae `0.080616`

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
- 3d: sample `8`, hit `0.625`, avg `-0.001516`, median `0.007289`, mae `0.018284`
- 5d: sample `8`, hit `0.625`, avg `-0.011121`, median `0.001087`, mae `0.015744`
- 10d: sample `8`, hit `0.125`, avg `-0.014794`, median `-0.01796`, mae `0.023768`
- 20d: sample `8`, hit `0.75`, avg `0.018164`, median `0.029166`, mae `0.033657`
- 60d: sample `8`, hit `0.625`, avg `0.035099`, median `0.059495`, mae `0.078831`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.001516`, median `0.007289`, mae `0.018284`
- 5d: sample `8`, hit `0.625`, avg `-0.011121`, median `0.001087`, mae `0.015744`
- 10d: sample `8`, hit `0.125`, avg `-0.014794`, median `-0.01796`, mae `0.023768`
- 20d: sample `8`, hit `0.75`, avg `0.018164`, median `0.029166`, mae `0.033657`
- 60d: sample `8`, hit `0.625`, avg `0.035099`, median `0.059495`, mae `0.078831`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001516, 'median_return': 0.007289, 'mean_absolute_return': 0.018284, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.011121, 'median_return': 0.001087, 'mean_absolute_return': 0.015744, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.014794, 'median_return': -0.01796, 'mean_absolute_return': 0.023768, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.018164, 'median_return': 0.029166, 'mean_absolute_return': 0.033657, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.035099, 'median_return': 0.059495, 'mean_absolute_return': 0.078831, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.000562, 'median_return': 0.003785, 'mean_absolute_return': 0.014469, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': -0.001335, 'median_return': 0.002453, 'mean_absolute_return': 0.017393, 'max_adverse_excursion': -0.079529, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.002227, 'median_return': -0.00367, 'mean_absolute_return': 0.025481, 'max_adverse_excursion': -0.087659, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.005234, 'median_return': 0.00745, 'mean_absolute_return': 0.037629, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.02643, 'median_return': 0.053301, 'mean_absolute_return': 0.080815, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4125}, '5d': {'sample_size': 80, 'hit_rate': 0.425}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.000872, 'median_return': 0.006714, 'mean_absolute_return': 0.018048, 'max_adverse_excursion': -0.052779, 'max_favorable_excursion': 0.03592}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.004091, 'median_return': 0.0019, 'mean_absolute_return': 0.019131, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.044767}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': 0.001481, 'median_return': -0.00367, 'mean_absolute_return': 0.022016, 'max_adverse_excursion': -0.044039, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.017279, 'median_return': 0.015444, 'mean_absolute_return': 0.031803, 'max_adverse_excursion': -0.056353, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.039296, 'median_return': 0.054268, 'mean_absolute_return': 0.081371, 'max_adverse_excursion': -0.12745, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.00158, 'median_return': 0.002067, 'mean_absolute_return': 0.011654, 'max_adverse_excursion': -0.044671, 'max_favorable_excursion': 0.025832}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': -0.000537, 'median_return': 0.002774, 'mean_absolute_return': 0.015325, 'max_adverse_excursion': -0.079529, 'max_favorable_excursion': 0.038591}, '10d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.008448, 'median_return': -0.007491, 'mean_absolute_return': 0.028603, 'max_adverse_excursion': -0.087659, 'max_favorable_excursion': 0.049674}, '20d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.004225, 'median_return': -0.001941, 'mean_absolute_return': 0.04266, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.073928}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.015299, 'median_return': 0.049411, 'mean_absolute_return': 0.079862, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.1448}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.000354`, median `0.003785`, mae `0.014851`
- 5d: sample `80`, hit `0.575`, avg `-0.002314`, median `0.001971`, mae `0.017228`
- 10d: sample `80`, hit `0.425`, avg `-0.003483`, median `-0.006017`, mae `0.02531`
- 20d: sample `80`, hit `0.5625`, avg `0.006527`, median `0.00745`, mae `0.037231`
- 60d: sample `80`, hit `0.625`, avg `0.027297`, median `0.053301`, mae `0.080616`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.000354`, median `0.003785`, mae `0.014851`
- 5d: sample `80`, hit `0.575`, avg `-0.002314`, median `0.001971`, mae `0.017228`
- 10d: sample `80`, hit `0.425`, avg `-0.003483`, median `-0.006017`, mae `0.02531`
- 20d: sample `80`, hit `0.5625`, avg `0.006527`, median `0.00745`, mae `0.037231`
- 60d: sample `80`, hit `0.625`, avg `0.027297`, median `0.053301`, mae `0.080616`

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
- 3d: sample `80`, hit `0.5875`, avg `0.000354`, median `0.003785`, mae `0.014851`
- 5d: sample `80`, hit `0.575`, avg `-0.002314`, median `0.001971`, mae `0.017228`
- 10d: sample `80`, hit `0.425`, avg `-0.003483`, median `-0.006017`, mae `0.02531`
- 20d: sample `80`, hit `0.5625`, avg `0.006527`, median `0.00745`, mae `0.037231`
- 60d: sample `80`, hit `0.625`, avg `0.027297`, median `0.053301`, mae `0.080616`

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
