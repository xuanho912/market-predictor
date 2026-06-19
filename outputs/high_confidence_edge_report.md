# High Confidence Edge Report

Generated at: `2026-06-19T23:43:29.402639+00:00`

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
- 3d: sample `60`, hit `0.55`, avg `0.005615`, median `0.003538`, mae `0.01507`
- 5d: sample `60`, hit `0.6833`, avg `0.0065`, median `0.005327`, mae `0.017305`
- 10d: sample `60`, hit `0.55`, avg `0.007311`, median `0.007467`, mae `0.023618`
- 20d: sample `60`, hit `0.6`, avg `0.008106`, median `0.015404`, mae `0.031116`
- 60d: sample `60`, hit `0.5667`, avg `0.020298`, median `0.032982`, mae `0.057206`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.004904`, median `0.008941`, mae `0.013975`
- 5d: sample `20`, hit `0.75`, avg `0.00659`, median `0.01152`, mae `0.018011`
- 10d: sample `20`, hit `0.6`, avg `-0.000412`, median `0.006378`, mae `0.021162`
- 20d: sample `20`, hit `0.55`, avg `-0.009702`, median `0.002988`, mae `0.030808`
- 60d: sample `20`, hit `0.3`, avg `-0.016939`, median `-0.009954`, mae `0.040891`

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
- 3d: sample `8`, hit `0.5`, avg `0.002698`, median `0.003538`, mae `0.009556`
- 5d: sample `8`, hit `0.5`, avg `0.003863`, median `0.006133`, mae `0.009613`
- 10d: sample `8`, hit `0.625`, avg `0.004889`, median `0.00903`, mae `0.019592`
- 20d: sample `8`, hit `0.375`, avg `-0.021094`, median `-0.014517`, mae `0.028847`
- 60d: sample `8`, hit `0.75`, avg `0.035988`, median `0.069306`, mae `0.073304`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.003857`, median `-0.002654`, mae `0.006673`
- 5d: sample `8`, hit `0.75`, avg `0.001521`, median `0.004606`, mae `0.011542`
- 10d: sample `8`, hit `0.5`, avg `0.001197`, median `0.003491`, mae `0.011805`
- 20d: sample `8`, hit `0.625`, avg `-0.005241`, median `0.011728`, mae `0.023884`
- 60d: sample `8`, hit `0.125`, avg `-0.05063`, median `-0.069824`, mae `0.061565`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.005615, 'median_return': 0.003538, 'mean_absolute_return': 0.01507, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.0065, 'median_return': 0.005327, 'mean_absolute_return': 0.017305, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.007311, 'median_return': 0.007467, 'mean_absolute_return': 0.023618, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.008106, 'median_return': 0.015404, 'mean_absolute_return': 0.031116, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.020298, 'median_return': 0.032982, 'mean_absolute_return': 0.057206, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.130806}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.003857, 'median_return': -0.002654, 'mean_absolute_return': 0.006673, 'max_adverse_excursion': -0.014409, 'max_favorable_excursion': 0.006722}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.001521, 'median_return': 0.004606, 'mean_absolute_return': 0.011542, 'max_adverse_excursion': -0.021762, 'max_favorable_excursion': 0.019686}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001197, 'median_return': 0.003491, 'mean_absolute_return': 0.011805, 'max_adverse_excursion': -0.017864, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.005241, 'median_return': 0.011728, 'mean_absolute_return': 0.023884, 'max_adverse_excursion': -0.050277, 'max_favorable_excursion': 0.033597}, '60d': {'sample_size': 8, 'hit_rate': 0.125, 'avg_return': -0.05063, 'median_return': -0.069824, 'mean_absolute_return': 0.061565, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.043741}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.00647, 'median_return': 0.00696, 'mean_absolute_return': 0.015699, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.007078, 'median_return': 0.007324, 'mean_absolute_return': 0.018142, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.005845, 'median_return': 0.008102, 'mean_absolute_return': 0.024248, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.004642, 'median_return': 0.009812, 'mean_absolute_return': 0.031834, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.017835, 'median_return': 0.012273, 'mean_absolute_return': 0.052189, 'max_adverse_excursion': -0.178752, 'max_favorable_excursion': 0.130806}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.475}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.5625}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.1, 'both_hit': 12, 'both_miss': 8}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.125, 'both_hit': 11, 'both_miss': 9}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.0, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.3875, 'primary_minus_secondary': 0.175, 'both_hit': 8, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.15, 'both_hit': 12, 'both_miss': 8}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.010354, 'median_return': 0.018606, 'mean_absolute_return': 0.020201, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.037129}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.013172, 'median_return': 0.015202, 'mean_absolute_return': 0.022032, 'max_adverse_excursion': -0.0363, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.016253, 'median_return': 0.032575, 'mean_absolute_return': 0.033353, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.054673}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.025121, 'median_return': 0.031464, 'mean_absolute_return': 0.038632, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.06925}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.059594, 'median_return': 0.065766, 'mean_absolute_return': 0.068722, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.003798, 'median_return': 0.003218, 'mean_absolute_return': 0.012995, 'max_adverse_excursion': -0.043682, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.004306, 'median_return': 0.005327, 'mean_absolute_return': 0.015965, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.042123}, '10d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.001756, 'median_return': 0.001785, 'mean_absolute_return': 0.019554, 'max_adverse_excursion': -0.059374, 'max_favorable_excursion': 0.065859}, '20d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': -0.003502, 'median_return': 0.002616, 'mean_absolute_return': 0.028508, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.005213, 'median_return': -0.012181, 'mean_absolute_return': 0.047929, 'max_adverse_excursion': -0.178752, 'max_favorable_excursion': 0.114016}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.003245`, median `0.000201`, mae `0.012504`
- 5d: sample `40`, hit `0.625`, avg `0.003164`, median `0.003714`, mae `0.014942`
- 10d: sample `40`, hit `0.475`, avg `0.00284`, median `-0.001676`, mae `0.018751`
- 20d: sample `40`, hit `0.5`, avg `-0.000401`, median `0.001555`, mae `0.027358`
- 60d: sample `40`, hit `0.425`, avg `0.00065`, median `-0.012792`, mae `0.051447`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.007629`, median `0.012584`, mae `0.017088`
- 5d: sample `40`, hit `0.775`, avg `0.009881`, median `0.01152`, mae `0.020021`
- 10d: sample `40`, hit `0.65`, avg `0.007921`, median `0.01246`, mae `0.027257`
- 20d: sample `40`, hit `0.675`, avg `0.00771`, median `0.017149`, mae `0.03472`
- 60d: sample `40`, hit `0.575`, avg `0.021327`, median `0.022865`, mae `0.054807`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.003245`, median `0.000201`, mae `0.012504`
- 5d: sample `40`, hit `0.625`, avg `0.003164`, median `0.003714`, mae `0.014942`
- 10d: sample `40`, hit `0.475`, avg `0.00284`, median `-0.001676`, mae `0.018751`
- 20d: sample `40`, hit `0.5`, avg `-0.000401`, median `0.001555`, mae `0.027358`
- 60d: sample `40`, hit `0.425`, avg `0.00065`, median `-0.012792`, mae `0.051447`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.010354`, median `0.018606`, mae `0.020201`
- 5d: sample `20`, hit `0.8`, avg `0.013172`, median `0.015202`, mae `0.022032`
- 10d: sample `20`, hit `0.7`, avg `0.016253`, median `0.032575`, mae `0.033353`
- 20d: sample `20`, hit `0.8`, avg `0.025121`, median `0.031464`, mae `0.038632`
- 60d: sample `20`, hit `0.85`, avg `0.059594`, median `0.065766`, mae `0.068722`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.010354`, median `0.018606`, mae `0.020201`
- 5d: sample `20`, hit `0.8`, avg `0.013172`, median `0.015202`, mae `0.022032`
- 10d: sample `20`, hit `0.7`, avg `0.016253`, median `0.032575`, mae `0.033353`
- 20d: sample `20`, hit `0.8`, avg `0.025121`, median `0.031464`, mae `0.038632`
- 60d: sample `20`, hit `0.85`, avg `0.059594`, median `0.065766`, mae `0.068722`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `0.003245`, median `0.000201`, mae `0.012504`
- 5d: sample `40`, hit `0.625`, avg `0.003164`, median `0.003714`, mae `0.014942`
- 10d: sample `40`, hit `0.475`, avg `0.00284`, median `-0.001676`, mae `0.018751`
- 20d: sample `40`, hit `0.5`, avg `-0.000401`, median `0.001555`, mae `0.027358`
- 60d: sample `40`, hit `0.425`, avg `0.00065`, median `-0.012792`, mae `0.051447`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.010354`, median `0.018606`, mae `0.020201`
- 5d: sample `20`, hit `0.8`, avg `0.013172`, median `0.015202`, mae `0.022032`
- 10d: sample `20`, hit `0.7`, avg `0.016253`, median `0.032575`, mae `0.033353`
- 20d: sample `20`, hit `0.8`, avg `0.025121`, median `0.031464`, mae `0.038632`
- 60d: sample `20`, hit `0.85`, avg `0.059594`, median `0.065766`, mae `0.068722`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.004904`, median `0.008941`, mae `0.013975`
- 5d: sample `20`, hit `0.75`, avg `0.00659`, median `0.01152`, mae `0.018011`
- 10d: sample `20`, hit `0.6`, avg `-0.000412`, median `0.006378`, mae `0.021162`
- 20d: sample `20`, hit `0.55`, avg `-0.009702`, median `0.002988`, mae `0.030808`
- 60d: sample `20`, hit `0.3`, avg `-0.016939`, median `-0.009954`, mae `0.040891`

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
- 3d: sample `40`, hit `0.5`, avg `0.003245`, median `0.000201`, mae `0.012504`
- 5d: sample `40`, hit `0.625`, avg `0.003164`, median `0.003714`, mae `0.014942`
- 10d: sample `40`, hit `0.475`, avg `0.00284`, median `-0.001676`, mae `0.018751`
- 20d: sample `40`, hit `0.5`, avg `-0.000401`, median `0.001555`, mae `0.027358`
- 60d: sample `40`, hit `0.425`, avg `0.00065`, median `-0.012792`, mae `0.051447`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.007629`, median `0.012584`, mae `0.017088`
- 5d: sample `40`, hit `0.775`, avg `0.009881`, median `0.01152`, mae `0.020021`
- 10d: sample `40`, hit `0.65`, avg `0.007921`, median `0.01246`, mae `0.027257`
- 20d: sample `40`, hit `0.675`, avg `0.00771`, median `0.017149`, mae `0.03472`
- 60d: sample `40`, hit `0.575`, avg `0.021327`, median `0.022865`, mae `0.054807`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.010354`, median `0.018606`, mae `0.020201`
- 5d: sample `20`, hit `0.8`, avg `0.013172`, median `0.015202`, mae `0.022032`
- 10d: sample `20`, hit `0.7`, avg `0.016253`, median `0.032575`, mae `0.033353`
- 20d: sample `20`, hit `0.8`, avg `0.025121`, median `0.031464`, mae `0.038632`
- 60d: sample `20`, hit `0.85`, avg `0.059594`, median `0.065766`, mae `0.068722`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.005437`, median `0.004569`, mae `0.014796`
- 5d: sample `80`, hit `0.7`, avg `0.006523`, median `0.006133`, mae `0.017482`
- 10d: sample `80`, hit `0.5625`, avg `0.00538`, median `0.006378`, mae `0.023004`
- 20d: sample `80`, hit `0.5875`, avg `0.003654`, median `0.009812`, mae `0.031039`
- 60d: sample `80`, hit `0.5`, avg `0.010989`, median `0.003923`, mae `0.053127`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.55`, avg `0.005615`, median `0.003538`, mae `0.01507`
- 5d: sample `60`, hit `0.6833`, avg `0.0065`, median `0.005327`, mae `0.017305`
- 10d: sample `60`, hit `0.55`, avg `0.007311`, median `0.007467`, mae `0.023618`
- 20d: sample `60`, hit `0.6`, avg `0.008106`, median `0.015404`, mae `0.031116`
- 60d: sample `60`, hit `0.5667`, avg `0.020298`, median `0.032982`, mae `0.057206`

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
