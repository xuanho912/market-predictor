# High Confidence Edge Report

Generated at: `2026-09-23T01:10:42.747537+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `40`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `40`, gate `early_evidence`
- 5d: completed `40`, gate `early_evidence`
- 10d: completed `40`, gate `early_evidence`
- 20d: completed `40`, gate `early_evidence`
- 60d: completed `40`, gate `early_evidence`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004166`, median `0.010773`, mae `0.018304`
- 5d: sample `80`, hit `0.625`, avg `0.004877`, median `0.010061`, mae `0.021863`
- 10d: sample `80`, hit `0.6375`, avg `0.009102`, median `0.011031`, mae `0.030401`
- 20d: sample `80`, hit `0.8375`, avg `0.032772`, median `0.030922`, mae `0.044576`
- 60d: sample `80`, hit `0.85`, avg `0.066426`, median `0.082988`, mae `0.084036`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004166, 'median_return': 0.010773, 'mean_absolute_return': 0.018304, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.004877, 'median_return': 0.010061, 'mean_absolute_return': 0.021863, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.009102, 'median_return': 0.011031, 'mean_absolute_return': 0.030401, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.8375, 'avg_return': 0.032772, 'median_return': 0.030922, 'mean_absolute_return': 0.044576, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.85, 'avg_return': 0.066426, 'median_return': 0.082988, 'mean_absolute_return': 0.084036, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011441, 'median_return': 0.0214, 'mean_absolute_return': 0.020136, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013802, 'median_return': 0.013852, 'mean_absolute_return': 0.021604, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016973, 'median_return': 0.024811, 'mean_absolute_return': 0.02576, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.061725, 'median_return': 0.062955, 'mean_absolute_return': 0.061725, 'max_adverse_excursion': 0.031464, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.085751, 'median_return': 0.099719, 'mean_absolute_return': 0.097241, 'max_adverse_excursion': -0.045961, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.003358, 'median_return': 0.00745, 'mean_absolute_return': 0.0181, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003886, 'median_return': 0.010061, 'mean_absolute_return': 0.021891, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.008228, 'median_return': 0.008908, 'mean_absolute_return': 0.030917, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.8194, 'avg_return': 0.029555, 'median_return': 0.027502, 'mean_absolute_return': 0.04267, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.8472, 'avg_return': 0.064279, 'median_return': 0.077143, 'mean_absolute_return': 0.082569, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.625}, '10d': {'sample_size': 80, 'hit_rate': 0.6375}, '20d': {'sample_size': 80, 'hit_rate': 0.8375}, '60d': {'sample_size': 80, 'hit_rate': 0.85}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.8375, 'secondary_hit_rate': 0.8375, 'primary_minus_secondary': 0.0, 'both_hit': 67, 'both_miss': 13}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.85, 'secondary_hit_rate': 0.85, 'primary_minus_secondary': 0.0, 'both_hit': 68, 'both_miss': 12}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.004166, 'median_return': 0.010773, 'mean_absolute_return': 0.018304, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.004877, 'median_return': 0.010061, 'mean_absolute_return': 0.021863, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6375, 'avg_return': 0.009102, 'median_return': 0.011031, 'mean_absolute_return': 0.030401, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.8375, 'avg_return': 0.032772, 'median_return': 0.030922, 'mean_absolute_return': 0.044576, 'max_adverse_excursion': -0.084015, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.85, 'avg_return': 0.066426, 'median_return': 0.082988, 'mean_absolute_return': 0.084036, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00496`, median `0.010897`, mae `0.012858`
- 5d: sample `20`, hit `0.65`, avg `0.004889`, median `0.012091`, mae `0.01553`
- 10d: sample `20`, hit `0.8`, avg `0.007392`, median `0.011619`, mae `0.018729`
- 20d: sample `20`, hit `0.85`, avg `0.026815`, median `0.032299`, mae `0.034262`
- 60d: sample `20`, hit `0.95`, avg `0.084077`, median `0.084216`, mae `0.086159`

### breadth_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004166`, median `0.010773`, mae `0.018304`
- 5d: sample `80`, hit `0.625`, avg `0.004877`, median `0.010061`, mae `0.021863`
- 10d: sample `80`, hit `0.6375`, avg `0.009102`, median `0.011031`, mae `0.030401`
- 20d: sample `80`, hit `0.8375`, avg `0.032772`, median `0.030922`, mae `0.044576`
- 60d: sample `80`, hit `0.85`, avg `0.066426`, median `0.082988`, mae `0.084036`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00496`, median `0.010897`, mae `0.012858`
- 5d: sample `20`, hit `0.65`, avg `0.004889`, median `0.012091`, mae `0.01553`
- 10d: sample `20`, hit `0.8`, avg `0.007392`, median `0.011619`, mae `0.018729`
- 20d: sample `20`, hit `0.85`, avg `0.026815`, median `0.032299`, mae `0.034262`
- 60d: sample `20`, hit `0.95`, avg `0.084077`, median `0.084216`, mae `0.086159`

### breadth_conflicted_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004166`, median `0.010773`, mae `0.018304`
- 5d: sample `80`, hit `0.625`, avg `0.004877`, median `0.010061`, mae `0.021863`
- 10d: sample `80`, hit `0.6375`, avg `0.009102`, median `0.011031`, mae `0.030401`
- 20d: sample `80`, hit `0.8375`, avg `0.032772`, median `0.030922`, mae `0.044576`
- 60d: sample `80`, hit `0.85`, avg `0.066426`, median `0.082988`, mae `0.084036`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003901`, median `0.010773`, mae `0.02012`
- 5d: sample `60`, hit `0.6167`, avg `0.004874`, median `0.010061`, mae `0.023974`
- 10d: sample `60`, hit `0.5833`, avg `0.009672`, median `0.011031`, mae `0.034292`
- 20d: sample `60`, hit `0.8333`, avg `0.034757`, median `0.030922`, mae `0.048013`
- 60d: sample `60`, hit `0.8167`, avg `0.060542`, median `0.082251`, mae `0.083329`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.00496`, median `0.010897`, mae `0.012858`
- 5d: sample `20`, hit `0.65`, avg `0.004889`, median `0.012091`, mae `0.01553`
- 10d: sample `20`, hit `0.8`, avg `0.007392`, median `0.011619`, mae `0.018729`
- 20d: sample `20`, hit `0.85`, avg `0.026815`, median `0.032299`, mae `0.034262`
- 60d: sample `20`, hit `0.95`, avg `0.084077`, median `0.084216`, mae `0.086159`

### bounce_without_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003901`, median `0.010773`, mae `0.02012`
- 5d: sample `60`, hit `0.6167`, avg `0.004874`, median `0.010061`, mae `0.023974`
- 10d: sample `60`, hit `0.5833`, avg `0.009672`, median `0.011031`, mae `0.034292`
- 20d: sample `60`, hit `0.8333`, avg `0.034757`, median `0.030922`, mae `0.048013`
- 60d: sample `60`, hit `0.8167`, avg `0.060542`, median `0.082251`, mae `0.083329`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

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
- 3d: sample `80`, hit `0.6375`, avg `0.004166`, median `0.010773`, mae `0.018304`
- 5d: sample `80`, hit `0.625`, avg `0.004877`, median `0.010061`, mae `0.021863`
- 10d: sample `80`, hit `0.6375`, avg `0.009102`, median `0.011031`, mae `0.030401`
- 20d: sample `80`, hit `0.8375`, avg `0.032772`, median `0.030922`, mae `0.044576`
- 60d: sample `80`, hit `0.85`, avg `0.066426`, median `0.082988`, mae `0.084036`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004166`, median `0.010773`, mae `0.018304`
- 5d: sample `80`, hit `0.625`, avg `0.004877`, median `0.010061`, mae `0.021863`
- 10d: sample `80`, hit `0.6375`, avg `0.009102`, median `0.011031`, mae `0.030401`
- 20d: sample `80`, hit `0.8375`, avg `0.032772`, median `0.030922`, mae `0.044576`
- 60d: sample `80`, hit `0.85`, avg `0.066426`, median `0.082988`, mae `0.084036`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004166`, median `0.010773`, mae `0.018304`
- 5d: sample `80`, hit `0.625`, avg `0.004877`, median `0.010061`, mae `0.021863`
- 10d: sample `80`, hit `0.6375`, avg `0.009102`, median `0.011031`, mae `0.030401`
- 20d: sample `80`, hit `0.8375`, avg `0.032772`, median `0.030922`, mae `0.044576`
- 60d: sample `80`, hit `0.85`, avg `0.066426`, median `0.082988`, mae `0.084036`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6375`, avg `0.004166`, median `0.010773`, mae `0.018304`
- 5d: sample `80`, hit `0.625`, avg `0.004877`, median `0.010061`, mae `0.021863`
- 10d: sample `80`, hit `0.6375`, avg `0.009102`, median `0.011031`, mae `0.030401`
- 20d: sample `80`, hit `0.8375`, avg `0.032772`, median `0.030922`, mae `0.044576`
- 60d: sample `80`, hit `0.85`, avg `0.066426`, median `0.082988`, mae `0.084036`

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
