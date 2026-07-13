# High Confidence Edge Report

Generated at: `2026-07-13T15:14:46.204900+00:00`

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
- 3d: sample `60`, hit `0.5333`, avg `-0.002175`, median `0.000603`, mae `0.012159`
- 5d: sample `60`, hit `0.5167`, avg `-0.00205`, median `0.001303`, mae `0.015392`
- 10d: sample `60`, hit `0.5333`, avg `0.000681`, median `0.002362`, mae `0.023715`
- 20d: sample `60`, hit `0.7333`, avg `0.011576`, median `0.012291`, mae `0.032473`
- 60d: sample `60`, hit `0.5667`, avg `0.012568`, median `0.024329`, mae `0.07255`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009029`, median `-0.010033`, mae `0.019108`
- 5d: sample `20`, hit `0.4`, avg `-0.013146`, median `-0.008162`, mae `0.020267`
- 10d: sample `20`, hit `0.25`, avg `-0.010676`, median `-0.011432`, mae `0.019503`
- 20d: sample `20`, hit `0.75`, avg `0.012488`, median `0.021759`, mae `0.03757`
- 60d: sample `20`, hit `0.75`, avg `0.039467`, median `0.059131`, mae `0.078587`

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
- 3d: sample `8`, hit `0.375`, avg `-0.001674`, median `-0.002441`, mae `0.013671`
- 5d: sample `8`, hit `0.25`, avg `-0.004666`, median `-0.0129`, mae `0.019416`
- 10d: sample `8`, hit `0.625`, avg `0.004835`, median `0.013648`, mae `0.027498`
- 20d: sample `8`, hit `1.0`, avg `0.025259`, median `0.014918`, mae `0.025259`
- 60d: sample `8`, hit `0.25`, avg `-0.006529`, median `-0.01215`, mae `0.044033`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.00654`, median `0.009937`, mae `0.010834`
- 5d: sample `8`, hit `0.5`, avg `0.005081`, median `0.007332`, mae `0.009625`
- 10d: sample `8`, hit `0.375`, avg `-0.008264`, median `-0.003263`, mae `0.017683`
- 20d: sample `8`, hit `0.875`, avg `0.019375`, median `0.031909`, mae `0.031278`
- 60d: sample `8`, hit `0.625`, avg `0.019746`, median `0.048484`, mae `0.06455`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.002175, 'median_return': 0.000603, 'mean_absolute_return': 0.012159, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.022897}, '5d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.00205, 'median_return': 0.001303, 'mean_absolute_return': 0.015392, 'max_adverse_excursion': -0.053416, 'max_favorable_excursion': 0.032674}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.000681, 'median_return': 0.002362, 'mean_absolute_return': 0.023715, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.011576, 'median_return': 0.012291, 'mean_absolute_return': 0.032473, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.012568, 'median_return': 0.024329, 'mean_absolute_return': 0.07255, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.19082}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.00654, 'median_return': 0.009937, 'mean_absolute_return': 0.010834, 'max_adverse_excursion': -0.01345, 'max_favorable_excursion': 0.022026}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.005081, 'median_return': 0.007332, 'mean_absolute_return': 0.009625, 'max_adverse_excursion': -0.013784, 'max_favorable_excursion': 0.020575}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008264, 'median_return': -0.003263, 'mean_absolute_return': 0.017683, 'max_adverse_excursion': -0.036679, 'max_favorable_excursion': 0.015162}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.019375, 'median_return': 0.031909, 'mean_absolute_return': 0.031278, 'max_adverse_excursion': -0.047612, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.019746, 'median_return': 0.048484, 'mean_absolute_return': 0.06455, 'max_adverse_excursion': -0.093084, 'max_favorable_excursion': 0.116132}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.005048, 'median_return': -0.001166, 'mean_absolute_return': 0.014236, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.005925, 'median_return': -0.001796, 'mean_absolute_return': 0.017387, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.032674}, '10d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': -0.00148, 'median_return': -0.0004, 'mean_absolute_return': 0.023215, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.010963, 'median_return': 0.019193, 'mean_absolute_return': 0.034022, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.019243, 'median_return': 0.037425, 'mean_absolute_return': 0.075116, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.5875}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.4875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.05, 'both_hit': 12, 'both_miss': 8}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 10, 'both_miss': 10}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.4125, 'primary_minus_secondary': 0.175, 'both_hit': 10, 'both_miss': 10}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.1, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 13, 'both_miss': 7}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.003889, 'median_return': 0.000324, 'mean_absolute_return': 0.013896, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.024649}, '5d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': -0.004824, 'median_return': -0.000371, 'mean_absolute_return': 0.016611, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.032674}, '10d': {'sample_size': 80, 'hit_rate': 0.4625, 'avg_return': -0.002159, 'median_return': -0.001676, 'mean_absolute_return': 0.022662, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 80, 'hit_rate': 0.7375, 'avg_return': 0.011804, 'median_return': 0.019193, 'mean_absolute_return': 0.033748, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.019293, 'median_return': 0.037425, 'mean_absolute_return': 0.074059, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.19082}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002826`, median `0.000324`, mae `0.012398`
- 5d: sample `40`, hit `0.525`, avg `-0.003007`, median `0.001303`, mae `0.016565`
- 10d: sample `40`, hit `0.55`, avg `0.002221`, median `0.003262`, mae `0.02402`
- 20d: sample `40`, hit `0.725`, avg `0.009034`, median `0.01128`, mae `0.030007`
- 60d: sample `40`, hit `0.525`, avg `0.006889`, median `0.019715`, mae `0.068784`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.004893`, median `-0.001658`, mae `0.014635`
- 5d: sample `60`, hit `0.4833`, avg `-0.006387`, median `-0.001796`, mae `0.017799`
- 10d: sample `60`, hit `0.45`, avg `-0.002078`, median `-0.001676`, mae `0.022514`
- 20d: sample `60`, hit `0.7333`, avg `0.010185`, median `0.016745`, mae `0.032528`
- 60d: sample `60`, hit `0.6`, avg `0.017749`, median `0.037425`, mae `0.072052`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002826`, median `0.000324`, mae `0.012398`
- 5d: sample `40`, hit `0.525`, avg `-0.003007`, median `0.001303`, mae `0.016565`
- 10d: sample `40`, hit `0.55`, avg `0.002221`, median `0.003262`, mae `0.02402`
- 20d: sample `40`, hit `0.725`, avg `0.009034`, median `0.01128`, mae `0.030007`
- 60d: sample `40`, hit `0.525`, avg `0.006889`, median `0.019715`, mae `0.068784`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002826`, median `0.000324`, mae `0.012398`
- 5d: sample `40`, hit `0.525`, avg `-0.003007`, median `0.001303`, mae `0.016565`
- 10d: sample `40`, hit `0.55`, avg `0.002221`, median `0.003262`, mae `0.02402`
- 20d: sample `40`, hit `0.725`, avg `0.009034`, median `0.01128`, mae `0.030007`
- 60d: sample `40`, hit `0.525`, avg `0.006889`, median `0.019715`, mae `0.068784`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003602`, median `0.000324`, mae `0.015192`
- 5d: sample `20`, hit `0.5`, avg `-0.003442`, median `0.001104`, mae `0.019126`
- 10d: sample `20`, hit `0.6`, avg `0.008891`, median `0.013648`, mae `0.030208`
- 20d: sample `20`, hit `0.75`, avg `0.016046`, median `0.01128`, mae `0.035227`
- 60d: sample `20`, hit `0.6`, avg `0.032796`, median `0.044771`, mae `0.075364`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.45`, avg `-0.006315`, median `-0.002441`, mae `0.01715`
- 5d: sample `40`, hit `0.45`, avg `-0.008294`, median `-0.007381`, mae `0.019696`
- 10d: sample `40`, hit `0.425`, avg `-0.000893`, median `-0.007011`, mae `0.024856`
- 20d: sample `40`, hit `0.75`, avg `0.014267`, median `0.01983`, mae `0.036399`
- 60d: sample `40`, hit `0.675`, avg `0.036132`, median `0.050438`, mae `0.076976`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002826`, median `0.000324`, mae `0.012398`
- 5d: sample `40`, hit `0.525`, avg `-0.003007`, median `0.001303`, mae `0.016565`
- 10d: sample `40`, hit `0.55`, avg `0.002221`, median `0.003262`, mae `0.02402`
- 20d: sample `40`, hit `0.725`, avg `0.009034`, median `0.01128`, mae `0.030007`
- 60d: sample `40`, hit `0.525`, avg `0.006889`, median `0.019715`, mae `0.068784`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `-0.000875`, median `0.003026`, mae `0.01168`
- 5d: sample `20`, hit `0.5`, avg `-0.000137`, median `0.001737`, mae `0.013046`
- 10d: sample `20`, hit `0.5`, avg `-0.002401`, median `0.000242`, mae `0.023105`
- 20d: sample `20`, hit `0.75`, avg `0.016661`, median `0.029125`, mae `0.037406`
- 60d: sample `20`, hit `0.65`, avg `0.023926`, median `0.048484`, mae `0.080081`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003602`, median `0.000324`, mae `0.015192`
- 5d: sample `20`, hit `0.5`, avg `-0.003442`, median `0.001104`, mae `0.019126`
- 10d: sample `20`, hit `0.6`, avg `0.008891`, median `0.013648`, mae `0.030208`
- 20d: sample `20`, hit `0.75`, avg `0.016046`, median `0.01128`, mae `0.035227`
- 60d: sample `20`, hit `0.6`, avg `0.032796`, median `0.044771`, mae `0.075364`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009029`, median `-0.010033`, mae `0.019108`
- 5d: sample `20`, hit `0.4`, avg `-0.013146`, median `-0.008162`, mae `0.020267`
- 10d: sample `20`, hit `0.25`, avg `-0.010676`, median `-0.011432`, mae `0.019503`
- 20d: sample `20`, hit `0.75`, avg `0.012488`, median `0.021759`, mae `0.03757`
- 60d: sample `20`, hit `0.75`, avg `0.039467`, median `0.059131`, mae `0.078587`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002049`, median `0.000603`, mae `0.009604`
- 5d: sample `20`, hit `0.55`, avg `-0.002572`, median `0.003888`, mae `0.014005`
- 10d: sample `20`, hit `0.5`, avg `-0.004448`, median `0.002362`, mae `0.017831`
- 20d: sample `20`, hit `0.7`, avg `0.002021`, median `0.012291`, mae `0.024787`
- 60d: sample `20`, hit `0.45`, avg `-0.019017`, median `-0.015418`, mae `0.062205`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.009029`, median `-0.010033`, mae `0.019108`
- 5d: sample `20`, hit `0.4`, avg `-0.013146`, median `-0.008162`, mae `0.020267`
- 10d: sample `20`, hit `0.25`, avg `-0.010676`, median `-0.011432`, mae `0.019503`
- 20d: sample `20`, hit `0.75`, avg `0.012488`, median `0.021759`, mae `0.03757`
- 60d: sample `20`, hit `0.75`, avg `0.039467`, median `0.059131`, mae `0.078587`

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
