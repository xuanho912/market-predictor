# High Confidence Edge Report

Generated at: `2026-09-03T01:07:41.845008+00:00`

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
- 3d: sample `40`, hit `0.675`, avg `0.004951`, median `0.010897`, mae `0.015126`
- 5d: sample `40`, hit `0.7`, avg `0.009326`, median `0.012091`, mae `0.018877`
- 10d: sample `40`, hit `0.725`, avg `0.011982`, median `0.017201`, mae `0.023026`
- 20d: sample `40`, hit `0.85`, avg `0.035189`, median `0.033597`, mae `0.041155`
- 60d: sample `40`, hit `0.85`, avg `0.067281`, median `0.084597`, mae `0.07811`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.005862`, median `0.012584`, mae `0.022332`
- 5d: sample `40`, hit `0.6`, avg `0.007569`, median `0.014114`, mae `0.027633`
- 10d: sample `40`, hit `0.65`, avg `0.020356`, median `0.02569`, mae `0.040093`
- 20d: sample `40`, hit `0.85`, avg `0.033539`, median `0.034158`, mae `0.044077`
- 60d: sample `40`, hit `0.6`, avg `0.036679`, median `0.064124`, mae `0.087184`

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
- 3d: sample `8`, hit `0.5`, avg `0.001549`, median `0.012272`, mae `0.017688`
- 5d: sample `8`, hit `0.75`, avg `0.005751`, median `0.009709`, mae `0.017887`
- 10d: sample `8`, hit `0.625`, avg `0.012164`, median `0.023826`, mae `0.02139`
- 20d: sample `8`, hit `1.0`, avg `0.058072`, median `0.062955`, mae `0.058072`
- 60d: sample `8`, hit `1.0`, avg `0.104031`, median `0.121826`, mae `0.104031`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.001549`, median `0.012272`, mae `0.017688`
- 5d: sample `8`, hit `0.75`, avg `0.005751`, median `0.009709`, mae `0.017887`
- 10d: sample `8`, hit `0.625`, avg `0.012164`, median `0.023826`, mae `0.02139`
- 20d: sample `8`, hit `1.0`, avg `0.058072`, median `0.062955`, mae `0.058072`
- 60d: sample `8`, hit `1.0`, avg `0.104031`, median `0.121826`, mae `0.104031`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.004951, 'median_return': 0.010897, 'mean_absolute_return': 0.015126, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.031839}, '5d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.009326, 'median_return': 0.012091, 'mean_absolute_return': 0.018877, 'max_adverse_excursion': -0.029469, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.011982, 'median_return': 0.017201, 'mean_absolute_return': 0.023026, 'max_adverse_excursion': -0.047482, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.035189, 'median_return': 0.033597, 'mean_absolute_return': 0.041155, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.067281, 'median_return': 0.084597, 'mean_absolute_return': 0.07811, 'max_adverse_excursion': -0.04694, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001549, 'median_return': 0.012272, 'mean_absolute_return': 0.017688, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.005751, 'median_return': 0.009709, 'mean_absolute_return': 0.017887, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.03199}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.012164, 'median_return': 0.023826, 'mean_absolute_return': 0.02139, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.041976}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.058072, 'median_return': 0.062955, 'mean_absolute_return': 0.058072, 'max_adverse_excursion': 0.01983, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.104031, 'median_return': 0.121826, 'mean_absolute_return': 0.104031, 'max_adverse_excursion': 0.024156, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.005835, 'median_return': 0.011414, 'mean_absolute_return': 0.018845, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.047995}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.008747, 'median_return': 0.013411, 'mean_absolute_return': 0.023852, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.016614, 'median_return': 0.018412, 'mean_absolute_return': 0.03269, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.03173, 'median_return': 0.032954, 'mean_absolute_return': 0.040899, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.046196, 'median_return': 0.065995, 'mean_absolute_return': 0.080271, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.220253}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.5}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.375, 'primary_minus_secondary': 0.25, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.005406, 'median_return': 0.011414, 'mean_absolute_return': 0.018729, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.047995}, '5d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.008448, 'median_return': 0.012604, 'mean_absolute_return': 0.023255, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.062217}, '10d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.016169, 'median_return': 0.018412, 'mean_absolute_return': 0.03156, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.098213}, '20d': {'sample_size': 80, 'hit_rate': 0.85, 'avg_return': 0.034364, 'median_return': 0.033791, 'mean_absolute_return': 0.042616, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.05198, 'median_return': 0.0765, 'mean_absolute_return': 0.082647, 'max_adverse_excursion': -0.171649, 'max_favorable_excursion': 0.220253}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.65`, avg `0.005406`, median `0.011414`, mae `0.018729`
- 5d: sample `80`, hit `0.65`, avg `0.008448`, median `0.012604`, mae `0.023255`
- 10d: sample `80`, hit `0.6875`, avg `0.016169`, median `0.018412`, mae `0.03156`
- 20d: sample `80`, hit `0.85`, avg `0.034364`, median `0.033791`, mae `0.042616`
- 60d: sample `80`, hit `0.725`, avg `0.05198`, median `0.0765`, mae `0.082647`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004951`, median `0.010897`, mae `0.015126`
- 5d: sample `40`, hit `0.7`, avg `0.009326`, median `0.012091`, mae `0.018877`
- 10d: sample `40`, hit `0.725`, avg `0.011982`, median `0.017201`, mae `0.023026`
- 20d: sample `40`, hit `0.85`, avg `0.035189`, median `0.033597`, mae `0.041155`
- 60d: sample `40`, hit `0.85`, avg `0.067281`, median `0.084597`, mae `0.07811`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.65`, avg `0.006996`, median `0.013598`, mae `0.020763`
- 5d: sample `60`, hit `0.6667`, avg `0.009957`, median `0.014114`, mae `0.025452`
- 10d: sample `60`, hit `0.6833`, avg `0.019995`, median `0.023826`, mae `0.035243`
- 20d: sample `60`, hit `0.8667`, avg `0.037448`, median `0.034726`, mae `0.044806`
- 60d: sample `60`, hit `0.7`, avg `0.052172`, median `0.085781`, mae `0.088939`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004951`, median `0.010897`, mae `0.015126`
- 5d: sample `40`, hit `0.7`, avg `0.009326`, median `0.012091`, mae `0.018877`
- 10d: sample `40`, hit `0.725`, avg `0.011982`, median `0.017201`, mae `0.023026`
- 20d: sample `40`, hit `0.85`, avg `0.035189`, median `0.033597`, mae `0.041155`
- 60d: sample `40`, hit `0.85`, avg `0.067281`, median `0.084597`, mae `0.07811`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.005862`, median `0.012584`, mae `0.022332`
- 5d: sample `40`, hit `0.6`, avg `0.007569`, median `0.014114`, mae `0.027633`
- 10d: sample `40`, hit `0.65`, avg `0.020356`, median `0.02569`, mae `0.040093`
- 20d: sample `40`, hit `0.85`, avg `0.033539`, median `0.034158`, mae `0.044077`
- 60d: sample `40`, hit `0.6`, avg `0.036679`, median `0.064124`, mae `0.087184`

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
- 3d: sample `80`, hit `0.65`, avg `0.005406`, median `0.011414`, mae `0.018729`
- 5d: sample `80`, hit `0.65`, avg `0.008448`, median `0.012604`, mae `0.023255`
- 10d: sample `80`, hit `0.6875`, avg `0.016169`, median `0.018412`, mae `0.03156`
- 20d: sample `80`, hit `0.85`, avg `0.034364`, median `0.033791`, mae `0.042616`
- 60d: sample `80`, hit `0.725`, avg `0.05198`, median `0.0765`, mae `0.082647`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004951`, median `0.010897`, mae `0.015126`
- 5d: sample `40`, hit `0.7`, avg `0.009326`, median `0.012091`, mae `0.018877`
- 10d: sample `40`, hit `0.725`, avg `0.011982`, median `0.017201`, mae `0.023026`
- 20d: sample `40`, hit `0.85`, avg `0.035189`, median `0.033597`, mae `0.041155`
- 60d: sample `40`, hit `0.85`, avg `0.067281`, median `0.084597`, mae `0.07811`

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
