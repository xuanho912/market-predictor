# High Confidence Edge Report

Generated at: `2026-09-10T00:42:46.688080+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `4`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `4`, gate `insufficient`
- 5d: completed `4`, gate `insufficient`
- 10d: completed `4`, gate `insufficient`
- 20d: completed `4`, gate `insufficient`
- 60d: completed `4`, gate `insufficient`

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
- 3d: sample `80`, hit `0.675`, avg `0.006341`, median `0.012272`, mae `0.020218`
- 5d: sample `80`, hit `0.7`, avg `0.009805`, median `0.014114`, mae `0.0241`
- 10d: sample `80`, hit `0.6125`, avg `0.007855`, median `0.016142`, mae `0.037499`
- 20d: sample `80`, hit `0.6875`, avg `0.022117`, median `0.029348`, mae `0.048796`
- 60d: sample `80`, hit `0.7875`, avg `0.059372`, median `0.067625`, mae `0.077239`

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
- 3d: sample `8`, hit `0.5`, avg `0.002422`, median `0.012272`, mae `0.017125`
- 5d: sample `8`, hit `0.625`, avg `0.002383`, median `0.009709`, mae `0.019793`
- 10d: sample `8`, hit `0.5`, avg `0.001255`, median `0.011031`, mae `0.024852`
- 20d: sample `8`, hit `0.875`, avg `0.045109`, median `0.058396`, mae `0.052788`
- 60d: sample `8`, hit `0.875`, avg `0.098577`, median `0.121826`, mae `0.101115`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.002422`, median `0.012272`, mae `0.017125`
- 5d: sample `8`, hit `0.625`, avg `0.002383`, median `0.009709`, mae `0.019793`
- 10d: sample `8`, hit `0.5`, avg `0.001255`, median `0.011031`, mae `0.024852`
- 20d: sample `8`, hit `0.875`, avg `0.045109`, median `0.058396`, mae `0.052788`
- 60d: sample `8`, hit `0.875`, avg `0.098577`, median `0.121826`, mae `0.101115`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002422, 'median_return': 0.012272, 'mean_absolute_return': 0.017125, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022637}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002383, 'median_return': 0.009709, 'mean_absolute_return': 0.019793, 'max_adverse_excursion': -0.026253, 'max_favorable_excursion': 0.030736}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001255, 'median_return': 0.011031, 'mean_absolute_return': 0.024852, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.036012}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.045109, 'median_return': 0.058396, 'mean_absolute_return': 0.052788, 'max_adverse_excursion': -0.030715, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.098577, 'median_return': 0.121826, 'mean_absolute_return': 0.101115, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.006776, 'median_return': 0.012525, 'mean_absolute_return': 0.020562, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.01063, 'median_return': 0.014937, 'mean_absolute_return': 0.024579, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.008589, 'median_return': 0.017429, 'mean_absolute_return': 0.038905, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.019562, 'median_return': 0.028859, 'mean_absolute_return': 0.048353, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.055016, 'median_return': 0.064286, 'mean_absolute_return': 0.074586, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.325}, '5d': {'sample_size': 80, 'hit_rate': 0.3}, '10d': {'sample_size': 80, 'hit_rate': 0.3875}, '20d': {'sample_size': 80, 'hit_rate': 0.3125}, '60d': {'sample_size': 80, 'hit_rate': 0.2125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.3, 'secondary_hit_rate': 0.7, 'primary_minus_secondary': -0.4, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.3125, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.375, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.2125, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.575, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.006341, 'median_return': 0.012272, 'mean_absolute_return': 0.020218, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.7, 'avg_return': 0.009805, 'median_return': 0.014114, 'mean_absolute_return': 0.0241, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.007855, 'median_return': 0.016142, 'mean_absolute_return': 0.037499, 'max_adverse_excursion': -0.158305, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.022117, 'median_return': 0.029348, 'mean_absolute_return': 0.048796, 'max_adverse_excursion': -0.122656, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.7875, 'avg_return': 0.059372, 'median_return': 0.067625, 'mean_absolute_return': 0.077239, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

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
- 3d: sample `80`, hit `0.675`, avg `0.006341`, median `0.012272`, mae `0.020218`
- 5d: sample `80`, hit `0.7`, avg `0.009805`, median `0.014114`, mae `0.0241`
- 10d: sample `80`, hit `0.6125`, avg `0.007855`, median `0.016142`, mae `0.037499`
- 20d: sample `80`, hit `0.6875`, avg `0.022117`, median `0.029348`, mae `0.048796`
- 60d: sample `80`, hit `0.7875`, avg `0.059372`, median `0.067625`, mae `0.077239`

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
- 3d: sample `40`, hit `0.75`, avg `0.011851`, median `0.018458`, mae `0.02091`
- 5d: sample `40`, hit `0.825`, avg `0.01836`, median `0.022634`, mae `0.026634`
- 10d: sample `40`, hit `0.725`, avg `0.021588`, median `0.024811`, mae `0.039594`
- 20d: sample `40`, hit `0.8`, avg `0.040549`, median `0.03791`, mae `0.056924`
- 60d: sample `40`, hit `0.875`, avg `0.087262`, median `0.095628`, mae `0.092174`

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
- 3d: sample `80`, hit `0.675`, avg `0.006341`, median `0.012272`, mae `0.020218`
- 5d: sample `80`, hit `0.7`, avg `0.009805`, median `0.014114`, mae `0.0241`
- 10d: sample `80`, hit `0.6125`, avg `0.007855`, median `0.016142`, mae `0.037499`
- 20d: sample `80`, hit `0.6875`, avg `0.022117`, median `0.029348`, mae `0.048796`
- 60d: sample `80`, hit `0.7875`, avg `0.059372`, median `0.067625`, mae `0.077239`

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
- 3d: sample `80`, hit `0.675`, avg `0.006341`, median `0.012272`, mae `0.020218`
- 5d: sample `80`, hit `0.7`, avg `0.009805`, median `0.014114`, mae `0.0241`
- 10d: sample `80`, hit `0.6125`, avg `0.007855`, median `0.016142`, mae `0.037499`
- 20d: sample `80`, hit `0.6875`, avg `0.022117`, median `0.029348`, mae `0.048796`
- 60d: sample `80`, hit `0.7875`, avg `0.059372`, median `0.067625`, mae `0.077239`

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
