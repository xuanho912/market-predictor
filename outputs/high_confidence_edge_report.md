# High Confidence Edge Report

Generated at: `2026-09-04T00:31:15.740212+00:00`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.6625`, avg `0.005226`, median `0.009349`, mae `0.01786`
- 5d: sample `80`, hit `0.675`, avg `0.008839`, median `0.012091`, mae `0.022419`
- 10d: sample `80`, hit `0.65`, avg `0.012478`, median `0.018412`, mae `0.031649`
- 20d: sample `80`, hit `0.8`, avg `0.025116`, median `0.029103`, mae `0.038888`
- 60d: sample `80`, hit `0.725`, avg `0.044394`, median `0.064124`, mae `0.075444`

### WEAK_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- 3d: sample `8`, hit `0.75`, avg `0.011441`, median `0.0214`, mae `0.020136`
- 5d: sample `8`, hit `0.75`, avg `0.013802`, median `0.013852`, mae `0.021604`
- 10d: sample `8`, hit `0.625`, avg `0.016973`, median `0.024811`, mae `0.02576`
- 20d: sample `8`, hit `1.0`, avg `0.061725`, median `0.062955`, mae `0.061725`
- 60d: sample `8`, hit `0.875`, avg `0.085751`, median `0.099719`, mae `0.097241`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.011441`, median `0.0214`, mae `0.020136`
- 5d: sample `8`, hit `0.75`, avg `0.013802`, median `0.013852`, mae `0.021604`
- 10d: sample `8`, hit `0.625`, avg `0.016973`, median `0.024811`, mae `0.02576`
- 20d: sample `8`, hit `1.0`, avg `0.061725`, median `0.062955`, mae `0.061725`
- 60d: sample `8`, hit `0.875`, avg `0.085751`, median `0.099719`, mae `0.097241`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.005226, 'median_return': 0.009349, 'mean_absolute_return': 0.01786, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.008839, 'median_return': 0.012091, 'mean_absolute_return': 0.022419, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.012478, 'median_return': 0.018412, 'mean_absolute_return': 0.031649, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.025116, 'median_return': 0.029103, 'mean_absolute_return': 0.038888, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.044394, 'median_return': 0.064124, 'mean_absolute_return': 0.075444, 'max_adverse_excursion': -0.15362, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011441, 'median_return': 0.0214, 'mean_absolute_return': 0.020136, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013802, 'median_return': 0.013852, 'mean_absolute_return': 0.021604, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016973, 'median_return': 0.024811, 'mean_absolute_return': 0.02576, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.061725, 'median_return': 0.062955, 'mean_absolute_return': 0.061725, 'max_adverse_excursion': 0.031464, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.085751, 'median_return': 0.099719, 'mean_absolute_return': 0.097241, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.004536, 'median_return': 0.008332, 'mean_absolute_return': 0.017607, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.008288, 'median_return': 0.012091, 'mean_absolute_return': 0.02251, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.011979, 'median_return': 0.018412, 'mean_absolute_return': 0.032303, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.021048, 'median_return': 0.026005, 'mean_absolute_return': 0.03635, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.039799, 'median_return': 0.059606, 'mean_absolute_return': 0.073022, 'max_adverse_excursion': -0.15362, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5375}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.6}, '60d': {'sample_size': 80, 'hit_rate': 0.725}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.075, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.275, 'primary_minus_secondary': 0.45, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.005226, 'median_return': 0.009349, 'mean_absolute_return': 0.01786, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.008839, 'median_return': 0.012091, 'mean_absolute_return': 0.022419, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.65, 'avg_return': 0.012478, 'median_return': 0.018412, 'mean_absolute_return': 0.031649, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.8, 'avg_return': 0.025116, 'median_return': 0.029103, 'mean_absolute_return': 0.038888, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.044394, 'median_return': 0.064124, 'mean_absolute_return': 0.075444, 'max_adverse_excursion': -0.15362, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `60`, hit `0.7167`, avg `0.007972`, median `0.012272`, mae `0.016678`
- 5d: sample `60`, hit `0.7`, avg `0.01108`, median `0.012091`, mae `0.021526`
- 10d: sample `60`, hit `0.6667`, avg `0.014231`, median `0.018352`, mae `0.029034`
- 20d: sample `60`, hit `0.8333`, avg `0.029487`, median `0.031464`, mae `0.039354`
- 60d: sample `60`, hit `0.7333`, avg `0.049507`, median `0.065995`, mae `0.07567`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.006316`, median `0.012217`, mae `0.015752`
- 5d: sample `40`, hit `0.725`, avg `0.010448`, median `0.011604`, mae `0.02009`
- 10d: sample `40`, hit `0.7`, avg `0.012372`, median `0.019171`, mae `0.028016`
- 20d: sample `40`, hit `0.8`, avg `0.026995`, median `0.031464`, mae `0.041449`
- 60d: sample `40`, hit `0.85`, avg `0.063027`, median `0.081441`, mae `0.071949`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.010964`, median `0.017193`, mae `0.018594`
- 5d: sample `40`, hit `0.725`, avg `0.014129`, median `0.018242`, mae `0.023886`
- 10d: sample `40`, hit `0.675`, avg `0.018867`, median `0.018412`, mae `0.03036`
- 20d: sample `40`, hit `0.9`, avg `0.038188`, median `0.033791`, mae `0.040458`
- 60d: sample `40`, hit `0.7`, avg `0.049646`, median `0.0765`, mae `0.082774`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.003207`, median `0.00745`, mae `0.017637`
- 5d: sample `60`, hit `0.6833`, avg `0.007671`, median `0.011604`, mae `0.02176`
- 10d: sample `60`, hit `0.6667`, avg `0.010655`, median `0.020119`, mae `0.031841`
- 20d: sample `60`, hit `0.7667`, avg `0.021998`, median `0.029103`, mae `0.040129`
- 60d: sample `60`, hit `0.8`, avg `0.051704`, median `0.069082`, mae `0.072888`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.011284`, median `0.014223`, mae `0.01853`
- 5d: sample `20`, hit `0.65`, avg `0.012343`, median `0.018242`, mae `0.024398`
- 10d: sample `20`, hit `0.6`, avg `0.017949`, median `0.01795`, mae `0.03107`
- 20d: sample `20`, hit `0.9`, avg `0.03447`, median `0.033791`, mae `0.035165`
- 60d: sample `20`, hit `0.5`, avg `0.022467`, median `0.003923`, mae `0.083111`

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
- 3d: sample `80`, hit `0.6625`, avg `0.005226`, median `0.009349`, mae `0.01786`
- 5d: sample `80`, hit `0.675`, avg `0.008839`, median `0.012091`, mae `0.022419`
- 10d: sample `80`, hit `0.65`, avg `0.012478`, median `0.018412`, mae `0.031649`
- 20d: sample `80`, hit `0.8`, avg `0.025116`, median `0.029103`, mae `0.038888`
- 60d: sample `80`, hit `0.725`, avg `0.044394`, median `0.064124`, mae `0.075444`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.003207`, median `0.00745`, mae `0.017637`
- 5d: sample `60`, hit `0.6833`, avg `0.007671`, median `0.011604`, mae `0.02176`
- 10d: sample `60`, hit `0.6667`, avg `0.010655`, median `0.020119`, mae `0.031841`
- 20d: sample `60`, hit `0.7667`, avg `0.021998`, median `0.029103`, mae `0.040129`
- 60d: sample `60`, hit `0.8`, avg `0.051704`, median `0.069082`, mae `0.072888`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `-0.000511`, median `0.004542`, mae `0.017126`
- 5d: sample `40`, hit `0.625`, avg `0.003549`, median `0.00972`, mae `0.020952`
- 10d: sample `40`, hit `0.625`, avg `0.006089`, median `0.019171`, mae `0.032937`
- 20d: sample `40`, hit `0.7`, avg `0.012044`, median `0.028859`, mae `0.037318`
- 60d: sample `40`, hit `0.75`, avg `0.039143`, median `0.062103`, mae `0.068114`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `-0.000511`, median `0.004542`, mae `0.017126`
- 5d: sample `40`, hit `0.625`, avg `0.003549`, median `0.00972`, mae `0.020952`
- 10d: sample `40`, hit `0.625`, avg `0.006089`, median `0.019171`, mae `0.032937`
- 20d: sample `40`, hit `0.7`, avg `0.012044`, median `0.028859`, mae `0.037318`
- 60d: sample `40`, hit `0.75`, avg `0.039143`, median `0.062103`, mae `0.068114`

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
