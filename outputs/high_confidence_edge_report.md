# High Confidence Edge Report

Generated at: `2026-08-20T20:54:09.784280+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.002641`, median `0.005431`, mae `0.016187`
- 5d: sample `40`, hit `0.575`, avg `0.004209`, median `0.003829`, mae `0.019131`
- 10d: sample `40`, hit `0.6`, avg `0.002873`, median `0.0076`, mae `0.026804`
- 20d: sample `40`, hit `0.7`, avg `0.009253`, median `0.014876`, mae `0.036854`
- 60d: sample `40`, hit `0.575`, avg `0.005748`, median `0.030553`, mae `0.075391`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.002844`, median `0.004569`, mae `0.013713`
- 5d: sample `40`, hit `0.5`, avg `-0.001677`, median `0.000579`, mae `0.017629`
- 10d: sample `40`, hit `0.5`, avg `0.001114`, median `0.002558`, mae `0.027223`
- 20d: sample `40`, hit `0.575`, avg `0.007056`, median `0.007988`, mae `0.044778`
- 60d: sample `40`, hit `0.6`, avg `0.031758`, median `0.032982`, mae `0.069715`

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
- 3d: sample `8`, hit `0.625`, avg `0.004174`, median `0.006565`, mae `0.014503`
- 5d: sample `8`, hit `0.5`, avg `-0.000584`, median `0.005327`, mae `0.021101`
- 10d: sample `8`, hit `0.375`, avg `-0.012003`, median `-0.010563`, mae `0.036962`
- 20d: sample `8`, hit `0.625`, avg `-0.007642`, median `0.021844`, mae `0.048635`
- 60d: sample `8`, hit `0.625`, avg `0.02301`, median `0.063119`, mae `0.073283`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001024`, median `0.001448`, mae `0.011883`
- 5d: sample `8`, hit `0.625`, avg `0.002593`, median `0.005319`, mae `0.013502`
- 10d: sample `8`, hit `0.75`, avg `0.011272`, median `0.021953`, mae `0.020043`
- 20d: sample `8`, hit `0.75`, avg `0.017063`, median `0.022652`, mae `0.022742`
- 60d: sample `8`, hit `0.25`, avg `-0.006904`, median `-0.020268`, mae `0.040213`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.002641, 'median_return': 0.005431, 'mean_absolute_return': 0.016187, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030961}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.004209, 'median_return': 0.003829, 'mean_absolute_return': 0.019131, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002873, 'median_return': 0.0076, 'mean_absolute_return': 0.026804, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.058745}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009253, 'median_return': 0.014876, 'mean_absolute_return': 0.036854, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.087524}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.005748, 'median_return': 0.030553, 'mean_absolute_return': 0.075391, 'max_adverse_excursion': -0.294669, 'max_favorable_excursion': 0.130669}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001024, 'median_return': 0.001448, 'mean_absolute_return': 0.011883, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002593, 'median_return': 0.005319, 'mean_absolute_return': 0.013502, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011272, 'median_return': 0.021953, 'mean_absolute_return': 0.020043, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.017063, 'median_return': 0.022652, 'mean_absolute_return': 0.022742, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.006904, 'median_return': -0.020268, 'mean_absolute_return': 0.040213, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.003161, 'median_return': 0.005431, 'mean_absolute_return': 0.015291, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.001119, 'median_return': 0.000688, 'mean_absolute_return': 0.018922, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5278, 'avg_return': 0.000963, 'median_return': 0.004807, 'mean_absolute_return': 0.027788, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.007165, 'median_return': 0.012958, 'mean_absolute_return': 0.042824, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.021604, 'median_return': 0.035245, 'mean_absolute_return': 0.076146, 'max_adverse_excursion': -0.294669, 'max_favorable_excursion': 0.171512}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4625}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.525}, '20d': {'sample_size': 80, 'hit_rate': 0.4875}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.175, 'both_hit': 14, 'both_miss': 6}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 12, 'both_miss': 8}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.025, 'both_hit': 13, 'both_miss': 7}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.15, 'both_hit': 15, 'both_miss': 5}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.075, 'both_hit': 14, 'both_miss': 6}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.002742, 'median_return': 0.004569, 'mean_absolute_return': 0.01495, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.5375, 'avg_return': 0.001266, 'median_return': 0.000863, 'mean_absolute_return': 0.01838, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': 0.001994, 'median_return': 0.006856, 'mean_absolute_return': 0.027014, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.008154, 'median_return': 0.012958, 'mean_absolute_return': 0.040816, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.018753, 'median_return': 0.032612, 'mean_absolute_return': 0.072553, 'max_adverse_excursion': -0.294669, 'max_favorable_excursion': 0.171512}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.000238`, median `0.00234`, mae `0.011825`
- 5d: sample `40`, hit `0.575`, avg `-0.000919`, median `0.000873`, mae `0.013233`
- 10d: sample `40`, hit `0.45`, avg `-0.004685`, median `-0.007117`, mae `0.021812`
- 20d: sample `40`, hit `0.525`, avg `-0.005228`, median `0.005803`, mae `0.033283`
- 60d: sample `40`, hit `0.425`, avg `-0.002358`, median `-0.018515`, mae `0.050546`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.000361`, median `0.002329`, mae `0.016893`
- 5d: sample `40`, hit `0.475`, avg `-0.001806`, median `-0.002418`, mae `0.021027`
- 10d: sample `40`, hit `0.6`, avg `0.005662`, median `0.009955`, mae `0.030342`
- 20d: sample `40`, hit `0.7`, avg `0.018377`, median `0.012958`, mae `0.044942`
- 60d: sample `40`, hit `0.625`, avg `0.039637`, median `0.035245`, mae `0.069565`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002244`, median `0.005458`, mae `0.018781`
- 5d: sample `20`, hit `0.4`, avg `-0.002564`, median `-0.009544`, mae `0.025424`
- 10d: sample `20`, hit `0.65`, avg `0.011461`, median `0.011168`, mae `0.035753`
- 20d: sample `20`, hit `0.75`, avg `0.030661`, median `0.029018`, mae `0.056436`
- 60d: sample `20`, hit `0.8`, avg `0.073754`, median `0.079128`, mae `0.088735`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008248`, median `0.013042`, mae `0.01737`
- 5d: sample `20`, hit `0.6`, avg `0.009466`, median `0.010393`, mae `0.02163`
- 10d: sample `20`, hit `0.65`, avg `0.005883`, median `0.012903`, mae `0.028677`
- 20d: sample `20`, hit `0.75`, avg `0.012413`, median `0.020008`, mae `0.040261`
- 60d: sample `20`, hit `0.7`, avg `0.005975`, median `0.05689`, mae `0.100386`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.000361`, median `0.002329`, mae `0.016893`
- 5d: sample `40`, hit `0.475`, avg `-0.001806`, median `-0.002418`, mae `0.021027`
- 10d: sample `40`, hit `0.6`, avg `0.005662`, median `0.009955`, mae `0.030342`
- 20d: sample `40`, hit `0.7`, avg `0.018377`, median `0.012958`, mae `0.044942`
- 60d: sample `40`, hit `0.625`, avg `0.039637`, median `0.035245`, mae `0.069565`

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
- 3d: sample `80`, hit `0.6375`, avg `0.002742`, median `0.004569`, mae `0.01495`
- 5d: sample `80`, hit `0.5375`, avg `0.001266`, median `0.000863`, mae `0.01838`
- 10d: sample `80`, hit `0.55`, avg `0.001994`, median `0.006856`, mae `0.027014`
- 20d: sample `80`, hit `0.6375`, avg `0.008154`, median `0.012958`, mae `0.040816`
- 60d: sample `80`, hit `0.5875`, avg `0.018753`, median `0.032612`, mae `0.072553`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008248`, median `0.013042`, mae `0.01737`
- 5d: sample `20`, hit `0.6`, avg `0.009466`, median `0.010393`, mae `0.02163`
- 10d: sample `20`, hit `0.65`, avg `0.005883`, median `0.012903`, mae `0.028677`
- 20d: sample `20`, hit `0.75`, avg `0.012413`, median `0.020008`, mae `0.040261`
- 60d: sample `20`, hit `0.7`, avg `0.005975`, median `0.05689`, mae `0.100386`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.002742`, median `0.004569`, mae `0.01495`
- 5d: sample `80`, hit `0.5375`, avg `0.001266`, median `0.000863`, mae `0.01838`
- 10d: sample `80`, hit `0.55`, avg `0.001994`, median `0.006856`, mae `0.027014`
- 20d: sample `80`, hit `0.6375`, avg `0.008154`, median `0.012958`, mae `0.040816`
- 60d: sample `80`, hit `0.5875`, avg `0.018753`, median `0.032612`, mae `0.072553`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.008248`, median `0.013042`, mae `0.01737`
- 5d: sample `20`, hit `0.6`, avg `0.009466`, median `0.010393`, mae `0.02163`
- 10d: sample `20`, hit `0.65`, avg `0.005883`, median `0.012903`, mae `0.028677`
- 20d: sample `20`, hit `0.75`, avg `0.012413`, median `0.020008`, mae `0.040261`
- 60d: sample `20`, hit `0.7`, avg `0.005975`, median `0.05689`, mae `0.100386`

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
