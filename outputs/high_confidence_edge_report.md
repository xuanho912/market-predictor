# High Confidence Edge Report

Generated at: `2026-09-09T01:14:10.907566+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.004095`, median `0.012083`, mae `0.025454`
- 5d: sample `20`, hit `0.7`, avg `0.006971`, median `0.01713`, mae `0.027009`
- 10d: sample `20`, hit `0.65`, avg `0.012123`, median `0.02569`, mae `0.039591`
- 20d: sample `20`, hit `0.7`, avg `0.015158`, median `0.020431`, mae `0.037842`
- 60d: sample `20`, hit `0.7`, avg `0.033659`, median `0.064286`, mae `0.07937`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.7667`, avg `0.011172`, median `0.013568`, mae `0.017356`
- 5d: sample `60`, hit `0.7667`, avg `0.014206`, median `0.014937`, mae `0.022436`
- 10d: sample `60`, hit `0.6667`, avg `0.015512`, median `0.021169`, mae `0.035112`
- 20d: sample `60`, hit `0.7333`, avg `0.0318`, median `0.032954`, mae `0.050337`
- 60d: sample `60`, hit `0.8`, avg `0.070115`, median `0.081441`, mae `0.080344`

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
- 3d: sample `8`, hit `0.5`, avg `-0.007348`, median `0.012525`, mae `0.033597`
- 5d: sample `8`, hit `0.5`, avg `-0.003974`, median `0.000548`, mae `0.033259`
- 10d: sample `8`, hit `0.5`, avg `0.001997`, median `9.9e-05`, mae `0.041165`
- 20d: sample `8`, hit `0.625`, avg `0.008006`, median `0.009812`, mae `0.034372`
- 60d: sample `8`, hit `0.375`, avg `-0.030549`, median `-0.003135`, mae `0.070316`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.013326`, median `0.0214`, mae `0.01724`
- 5d: sample `8`, hit `0.875`, avg `0.016571`, median `0.026456`, mae `0.021844`
- 10d: sample `8`, hit `0.75`, avg `0.016362`, median `0.032575`, mae `0.030832`
- 20d: sample `8`, hit `0.875`, avg `0.049332`, median `0.062955`, mae `0.057011`
- 60d: sample `8`, hit `0.875`, avg `0.092512`, median `0.099719`, mae `0.09505`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004095, 'median_return': 0.012083, 'mean_absolute_return': 0.025454, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.006971, 'median_return': 0.01713, 'mean_absolute_return': 0.027009, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.012123, 'median_return': 0.02569, 'mean_absolute_return': 0.039591, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.078607}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.015158, 'median_return': 0.020431, 'mean_absolute_return': 0.037842, 'max_adverse_excursion': -0.065027, 'max_favorable_excursion': 0.081382}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.033659, 'median_return': 0.064286, 'mean_absolute_return': 0.07937, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.139575}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.013326, 'median_return': 0.0214, 'mean_absolute_return': 0.01724, 'max_adverse_excursion': -0.013999, 'max_favorable_excursion': 0.022679}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.016571, 'median_return': 0.026456, 'mean_absolute_return': 0.021844, 'max_adverse_excursion': -0.021092, 'max_favorable_excursion': 0.032969}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016362, 'median_return': 0.032575, 'mean_absolute_return': 0.030832, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.04237}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.049332, 'median_return': 0.062955, 'mean_absolute_return': 0.057011, 'max_adverse_excursion': -0.030715, 'max_favorable_excursion': 0.07754}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.092512, 'median_return': 0.099719, 'mean_absolute_return': 0.09505, 'max_adverse_excursion': -0.010153, 'max_favorable_excursion': 0.130806}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.008967, 'median_return': 0.012525, 'mean_absolute_return': 0.019618, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.011933, 'median_return': 0.014937, 'mean_absolute_return': 0.023772, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.014477, 'median_return': 0.020503, 'mean_absolute_return': 0.036832, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.025229, 'median_return': 0.029103, 'mean_absolute_return': 0.046125, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.7639, 'avg_return': 0.0575, 'median_return': 0.065995, 'mean_absolute_return': 0.07844, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.7375}, '5d': {'sample_size': 80, 'hit_rate': 0.75}, '10d': {'sample_size': 80, 'hit_rate': 0.6625}, '20d': {'sample_size': 80, 'hit_rate': 0.725}, '60d': {'sample_size': 80, 'hit_rate': 0.775}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.7375, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.275, 'both_hit': 28, 'both_miss': 12}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.75, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.25, 'both_hit': 30, 'both_miss': 10}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.15, 'both_hit': 27, 'both_miss': 13}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.175, 'both_hit': 31, 'both_miss': 9}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.775, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': 0.25, 'both_hit': 32, 'both_miss': 8}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.7375, 'avg_return': 0.009403, 'median_return': 0.012584, 'mean_absolute_return': 0.019381, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.049473}, '5d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.012397, 'median_return': 0.014937, 'mean_absolute_return': 0.023579, 'max_adverse_excursion': -0.055579, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.014665, 'median_return': 0.021169, 'mean_absolute_return': 0.036232, 'max_adverse_excursion': -0.058014, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.725, 'avg_return': 0.027639, 'median_return': 0.03107, 'mean_absolute_return': 0.047213, 'max_adverse_excursion': -0.078156, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.775, 'avg_return': 0.061001, 'median_return': 0.069875, 'mean_absolute_return': 0.080101, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002976`, median `0.007259`, mae `0.0115`
- 5d: sample `20`, hit `0.55`, avg `0.001476`, median `0.006712`, mae `0.0161`
- 10d: sample `20`, hit `0.45`, avg `-0.009403`, median `-0.007491`, mae `0.031144`
- 20d: sample `20`, hit `0.5`, avg `-0.001329`, median `0.025541`, mae `0.037975`
- 60d: sample `20`, hit `0.65`, avg `0.030834`, median `0.043741`, mae `0.051698`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.825`, avg `0.01527`, median `0.018606`, mae `0.020284`
- 5d: sample `40`, hit `0.875`, avg `0.020571`, median `0.025024`, mae `0.025603`
- 10d: sample `40`, hit `0.775`, avg `0.02797`, median `0.036012`, mae `0.037097`
- 20d: sample `40`, hit `0.85`, avg `0.048364`, median `0.048969`, mae `0.056519`
- 60d: sample `40`, hit `0.875`, avg `0.089755`, median `0.098961`, mae `0.094667`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002976`, median `0.007259`, mae `0.0115`
- 5d: sample `20`, hit `0.55`, avg `0.001476`, median `0.006712`, mae `0.0161`
- 10d: sample `20`, hit `0.45`, avg `-0.009403`, median `-0.007491`, mae `0.031144`
- 20d: sample `20`, hit `0.5`, avg `-0.001329`, median `0.025541`, mae `0.037975`
- 60d: sample `20`, hit `0.65`, avg `0.030834`, median `0.043741`, mae `0.051698`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.011908`, median `0.018606`, mae `0.019764`
- 5d: sample `20`, hit `0.8`, avg `0.015282`, median `0.017411`, mae `0.022742`
- 10d: sample `20`, hit `0.7`, avg `0.017215`, median `0.024811`, mae `0.032171`
- 20d: sample `20`, hit `0.85`, avg `0.037731`, median `0.043456`, mae `0.048486`
- 60d: sample `20`, hit `0.9`, avg `0.076898`, median `0.090399`, mae `0.08251`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.825`, avg `0.01527`, median `0.018606`, mae `0.020284`
- 5d: sample `40`, hit `0.875`, avg `0.020571`, median `0.025024`, mae `0.025603`
- 10d: sample `40`, hit `0.775`, avg `0.02797`, median `0.036012`, mae `0.037097`
- 20d: sample `40`, hit `0.85`, avg `0.048364`, median `0.048969`, mae `0.056519`
- 60d: sample `40`, hit `0.875`, avg `0.089755`, median `0.098961`, mae `0.094667`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.002976`, median `0.007259`, mae `0.0115`
- 5d: sample `20`, hit `0.55`, avg `0.001476`, median `0.006712`, mae `0.0161`
- 10d: sample `20`, hit `0.45`, avg `-0.009403`, median `-0.007491`, mae `0.031144`
- 20d: sample `20`, hit `0.5`, avg `-0.001329`, median `0.025541`, mae `0.037975`
- 60d: sample `20`, hit `0.65`, avg `0.030834`, median `0.043741`, mae `0.051698`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.008002`, median `0.017193`, mae `0.022609`
- 5d: sample `40`, hit `0.75`, avg `0.011127`, median `0.01713`, mae `0.024876`
- 10d: sample `40`, hit `0.675`, avg `0.014669`, median `0.024811`, mae `0.035881`
- 20d: sample `40`, hit `0.775`, avg `0.026444`, median `0.030922`, mae `0.043164`
- 60d: sample `40`, hit `0.8`, avg `0.055279`, median `0.069875`, mae `0.08094`

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
- 3d: sample `80`, hit `0.7375`, avg `0.009403`, median `0.012584`, mae `0.019381`
- 5d: sample `80`, hit `0.75`, avg `0.012397`, median `0.014937`, mae `0.023579`
- 10d: sample `80`, hit `0.6625`, avg `0.014665`, median `0.021169`, mae `0.036232`
- 20d: sample `80`, hit `0.725`, avg `0.027639`, median `0.03107`, mae `0.047213`
- 60d: sample `80`, hit `0.775`, avg `0.061001`, median `0.069875`, mae `0.080101`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.6833`, avg `0.006326`, median `0.012272`, mae `0.018906`
- 5d: sample `60`, hit `0.6833`, avg `0.00791`, median `0.012091`, mae `0.021951`
- 10d: sample `60`, hit `0.6`, avg `0.006645`, median `0.017636`, mae `0.034302`
- 20d: sample `60`, hit `0.6833`, avg `0.017186`, median `0.028859`, mae `0.041434`
- 60d: sample `60`, hit `0.75`, avg `0.04713`, median `0.065766`, mae `0.071193`

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
