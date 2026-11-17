# High Confidence Edge Report

Generated at: `2026-11-17T20:58:31.439514+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `200`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `200`, gate `stronger_evidence`
- 5d: completed `200`, gate `stronger_evidence`
- 10d: completed `200`, gate `stronger_evidence`
- 20d: completed `200`, gate `stronger_evidence`
- 60d: completed `200`, gate `stronger_evidence`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.006423`, median `0.008733`, mae `0.022031`
- 5d: sample `80`, hit `0.675`, avg `0.010781`, median `0.010832`, mae `0.024354`
- 10d: sample `80`, hit `0.675`, avg `0.021136`, median `0.015974`, mae `0.033513`
- 20d: sample `80`, hit `0.725`, avg `0.031709`, median `0.037433`, mae `0.048123`
- 60d: sample `80`, hit `0.6125`, avg `0.048638`, median `0.054472`, mae `0.085341`

## Top Confirmation / Confidence Buckets

### signal_confirmation_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.010561`, median `0.017427`, mae `0.019502`
- 5d: sample `8`, hit `0.875`, avg `0.010055`, median `0.011143`, mae `0.015391`
- 10d: sample `8`, hit `0.5`, avg `0.007601`, median `0.005519`, mae `0.030241`
- 20d: sample `8`, hit `0.625`, avg `0.016553`, median `0.030297`, mae `0.027174`
- 60d: sample `8`, hit `0.5`, avg `0.019755`, median `0.048963`, mae `0.06089`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.75`, avg `0.010561`, median `0.017427`, mae `0.019502`
- 5d: sample `8`, hit `0.875`, avg `0.010055`, median `0.011143`, mae `0.015391`
- 10d: sample `8`, hit `0.5`, avg `0.007601`, median `0.005519`, mae `0.030241`
- 20d: sample `8`, hit `0.625`, avg `0.016553`, median `0.030297`, mae `0.027174`
- 60d: sample `8`, hit `0.5`, avg `0.019755`, median `0.048963`, mae `0.06089`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.010561, 'median_return': 0.017427, 'mean_absolute_return': 0.019502, 'max_adverse_excursion': -0.030262, 'max_favorable_excursion': 0.034466}, '5d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.010055, 'median_return': 0.011143, 'mean_absolute_return': 0.015391, 'max_adverse_excursion': -0.021344, 'max_favorable_excursion': 0.047293}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.007601, 'median_return': 0.005519, 'mean_absolute_return': 0.030241, 'max_adverse_excursion': -0.038485, 'max_favorable_excursion': 0.059136}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.016553, 'median_return': 0.030297, 'mean_absolute_return': 0.027174, 'max_adverse_excursion': -0.034684, 'max_favorable_excursion': 0.055822}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.019755, 'median_return': 0.048963, 'mean_absolute_return': 0.06089, 'max_adverse_excursion': -0.061859, 'max_favorable_excursion': 0.120808}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.005964, 'median_return': 0.007812, 'mean_absolute_return': 0.022312, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.010861, 'median_return': 0.010832, 'mean_absolute_return': 0.02535, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.02264, 'median_return': 0.01609, 'mean_absolute_return': 0.033877, 'max_adverse_excursion': -0.04664, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.033393, 'median_return': 0.038387, 'mean_absolute_return': 0.05045, 'max_adverse_excursion': -0.081434, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.051847, 'median_return': 0.061042, 'mean_absolute_return': 0.088058, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.247486}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4125}, '5d': {'sample_size': 80, 'hit_rate': 0.325}, '10d': {'sample_size': 80, 'hit_rate': 0.325}, '20d': {'sample_size': 80, 'hit_rate': 0.275}, '60d': {'sample_size': 80, 'hit_rate': 0.3875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.3875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.225, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.005262, 'median_return': 0.00531, 'mean_absolute_return': 0.015323, 'max_adverse_excursion': -0.023634, 'max_favorable_excursion': 0.037878}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.006955, 'median_return': 0.010394, 'mean_absolute_return': 0.016395, 'max_adverse_excursion': -0.024873, 'max_favorable_excursion': 0.040946}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.010243, 'median_return': 0.008464, 'mean_absolute_return': 0.023545, 'max_adverse_excursion': -0.034603, 'max_favorable_excursion': 0.065706}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.023983, 'median_return': 0.036447, 'mean_absolute_return': 0.031361, 'max_adverse_excursion': -0.02849, 'max_favorable_excursion': 0.072836}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.031276, 'median_return': 0.049411, 'mean_absolute_return': 0.055547, 'max_adverse_excursion': -0.053675, 'max_favorable_excursion': 0.117852}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.006811, 'median_return': 0.009959, 'mean_absolute_return': 0.024267, 'max_adverse_excursion': -0.064397, 'max_favorable_excursion': 0.058752}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.012056, 'median_return': 0.0127, 'mean_absolute_return': 0.027007, 'max_adverse_excursion': -0.05312, 'max_favorable_excursion': 0.115863}, '10d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.024768, 'median_return': 0.018992, 'mean_absolute_return': 0.036836, 'max_adverse_excursion': -0.04664, 'max_favorable_excursion': 0.137031}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.034285, 'median_return': 0.039227, 'mean_absolute_return': 0.05371, 'max_adverse_excursion': -0.081434, 'max_favorable_excursion': 0.162865}, '60d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.054425, 'median_return': 0.067551, 'mean_absolute_return': 0.095272, 'max_adverse_excursion': -0.147091, 'max_favorable_excursion': 0.247486}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.009124`, median `0.009123`, mae `0.019687`
- 5d: sample `60`, hit `0.6667`, avg `0.010067`, median `0.010394`, mae `0.021266`
- 10d: sample `60`, hit `0.65`, avg `0.018173`, median `0.011855`, mae `0.031565`
- 20d: sample `60`, hit `0.7833`, avg `0.03659`, median `0.037433`, mae `0.043567`
- 60d: sample `60`, hit `0.6833`, avg `0.060156`, median `0.067623`, mae `0.084121`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001677`, median `0.005908`, mae `0.029063`
- 5d: sample `20`, hit `0.7`, avg `0.01292`, median `0.019502`, mae `0.033619`
- 10d: sample `20`, hit `0.75`, avg `0.030027`, median `0.029161`, mae `0.039358`
- 20d: sample `20`, hit `0.55`, avg `0.017067`, median `0.053984`, mae `0.061788`
- 60d: sample `20`, hit `0.4`, avg `0.014082`, median `-0.00906`, mae `0.089`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001677`, median `0.005908`, mae `0.029063`
- 5d: sample `20`, hit `0.7`, avg `0.01292`, median `0.019502`, mae `0.033619`
- 10d: sample `20`, hit `0.75`, avg `0.030027`, median `0.029161`, mae `0.039358`
- 20d: sample `20`, hit `0.55`, avg `0.017067`, median `0.053984`, mae `0.061788`
- 60d: sample `20`, hit `0.4`, avg `0.014082`, median `-0.00906`, mae `0.089`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.004807`, median `0.006898`, mae `0.016171`
- 5d: sample `40`, hit `0.65`, avg `0.004292`, median `0.004641`, mae `0.015562`
- 10d: sample `40`, hit `0.575`, avg `0.007374`, median `0.005519`, mae `0.02341`
- 20d: sample `40`, hit `0.7`, avg `0.024383`, median `0.030606`, mae `0.034708`
- 60d: sample `40`, hit `0.6`, avg `0.033372`, median `0.049411`, mae `0.0659`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.004351`, median `0.007289`, mae `0.017018`
- 5d: sample `20`, hit `0.6`, avg `0.00163`, median `0.002223`, mae `0.01473`
- 10d: sample `20`, hit `0.45`, avg `0.004505`, median `-0.001222`, mae `0.023276`
- 20d: sample `20`, hit `0.65`, avg `0.024782`, median `0.030606`, mae `0.038056`
- 60d: sample `20`, hit `0.55`, avg `0.035468`, median `0.052255`, mae `0.076252`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.006423`, median `0.008733`, mae `0.022031`
- 5d: sample `80`, hit `0.675`, avg `0.010781`, median `0.010832`, mae `0.024354`
- 10d: sample `80`, hit `0.675`, avg `0.021136`, median `0.015974`, mae `0.033513`
- 20d: sample `80`, hit `0.725`, avg `0.031709`, median `0.037433`, mae `0.048123`
- 60d: sample `80`, hit `0.6125`, avg `0.048638`, median `0.054472`, mae `0.085341`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.006423`, median `0.008733`, mae `0.022031`
- 5d: sample `80`, hit `0.675`, avg `0.010781`, median `0.010832`, mae `0.024354`
- 10d: sample `80`, hit `0.675`, avg `0.021136`, median `0.015974`, mae `0.033513`
- 20d: sample `80`, hit `0.725`, avg `0.031709`, median `0.037433`, mae `0.048123`
- 60d: sample `80`, hit `0.6125`, avg `0.048638`, median `0.054472`, mae `0.085341`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
