# High Confidence Edge Report

Generated at: `2026-10-29T18:31:31.158015+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `148`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `148`, gate `stronger_evidence`
- 5d: completed `148`, gate `stronger_evidence`
- 10d: completed `148`, gate `stronger_evidence`
- 20d: completed `148`, gate `stronger_evidence`
- 60d: completed `148`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.6667`, avg `0.005792`, median `0.006372`, mae `0.014774`
- 5d: sample `60`, hit `0.5667`, avg `0.006677`, median `0.006712`, mae `0.020234`
- 10d: sample `60`, hit `0.7333`, avg `0.015895`, median `0.018086`, mae `0.030022`
- 20d: sample `60`, hit `0.8`, avg `0.025893`, median `0.028859`, mae `0.036499`
- 60d: sample `60`, hit `0.7667`, avg `0.043497`, median `0.055822`, mae `0.062705`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000372`, median `-0.00723`, mae `0.0228`
- 5d: sample `20`, hit `0.55`, avg `-0.001354`, median `0.004752`, mae `0.023721`
- 10d: sample `20`, hit `0.65`, avg `0.015147`, median `0.010559`, mae `0.029187`
- 20d: sample `20`, hit `0.75`, avg `0.025074`, median `0.029038`, mae `0.037371`
- 60d: sample `20`, hit `0.95`, avg `0.070339`, median `0.062764`, mae `0.0714`

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
- 3d: sample `8`, hit `0.625`, avg `0.003864`, median `0.004243`, mae `0.015101`
- 5d: sample `8`, hit `0.5`, avg `0.008008`, median `0.013109`, mae `0.020881`
- 10d: sample `8`, hit `0.75`, avg `0.019334`, median `0.023979`, mae `0.02779`
- 20d: sample `8`, hit `0.875`, avg `0.033152`, median `0.031196`, mae `0.035534`
- 60d: sample `8`, hit `0.875`, avg `0.061844`, median `0.073586`, mae `0.066877`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.003864`, median `0.004243`, mae `0.015101`
- 5d: sample `8`, hit `0.5`, avg `0.008008`, median `0.013109`, mae `0.020881`
- 10d: sample `8`, hit `0.75`, avg `0.019334`, median `0.023979`, mae `0.02779`
- 20d: sample `8`, hit `0.875`, avg `0.033152`, median `0.031196`, mae `0.035534`
- 60d: sample `8`, hit `0.875`, avg `0.061844`, median `0.073586`, mae `0.066877`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.005792, 'median_return': 0.006372, 'mean_absolute_return': 0.014774, 'max_adverse_excursion': -0.028651, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.006677, 'median_return': 0.006712, 'mean_absolute_return': 0.020234, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.015895, 'median_return': 0.018086, 'mean_absolute_return': 0.030022, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.025893, 'median_return': 0.028859, 'mean_absolute_return': 0.036499, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.7667, 'avg_return': 0.043497, 'median_return': 0.055822, 'mean_absolute_return': 0.062705, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.139575}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003864, 'median_return': 0.004243, 'mean_absolute_return': 0.015101, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.008008, 'median_return': 0.013109, 'mean_absolute_return': 0.020881, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.019334, 'median_return': 0.023979, 'mean_absolute_return': 0.02779, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.033152, 'median_return': 0.031196, 'mean_absolute_return': 0.035534, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.061844, 'median_return': 0.073586, 'mean_absolute_return': 0.066877, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.101208}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.004294, 'median_return': 0.006372, 'mean_absolute_return': 0.016967, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.004298, 'median_return': 0.006018, 'mean_absolute_return': 0.021131, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.015305, 'median_return': 0.014227, 'mean_absolute_return': 0.030038, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.024859, 'median_return': 0.028859, 'mean_absolute_return': 0.036848, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 72, 'hit_rate': 0.8056, 'avg_return': 0.048914, 'median_return': 0.055515, 'mean_absolute_return': 0.064657, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6375}, '5d': {'sample_size': 80, 'hit_rate': 0.5375}, '10d': {'sample_size': 80, 'hit_rate': 0.6375}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.025, 'both_hit': 40, 'both_miss': 20}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.025, 'both_hit': 34, 'both_miss': 26}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.075, 'both_hit': 44, 'both_miss': 16}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7875, 'primary_minus_secondary': -0.125, 'both_hit': 48, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.8125, 'primary_minus_secondary': -0.225, 'both_hit': 46, 'both_miss': 14}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003781, 'median_return': 0.009859, 'mean_absolute_return': 0.020075, 'max_adverse_excursion': -0.075785, 'max_favorable_excursion': 0.041595}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.007852, 'median_return': 0.012136, 'mean_absolute_return': 0.025155, 'max_adverse_excursion': -0.077059, 'max_favorable_excursion': 0.050402}, '10d': {'sample_size': 40, 'hit_rate': 0.75, 'avg_return': 0.021861, 'median_return': 0.033298, 'mean_absolute_return': 0.033782, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.030169, 'median_return': 0.043233, 'mean_absolute_return': 0.041332, 'max_adverse_excursion': -0.068819, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 40, 'hit_rate': 0.85, 'avg_return': 0.063142, 'median_return': 0.064194, 'mean_absolute_return': 0.071189, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.188184}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.004721, 'median_return': 0.004391, 'mean_absolute_return': 0.013486, 'max_adverse_excursion': -0.028191, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.001486, 'median_return': -0.001796, 'mean_absolute_return': 0.017056, 'max_adverse_excursion': -0.033198, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.009555, 'median_return': 0.012215, 'mean_absolute_return': 0.025845, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.060273}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.021208, 'median_return': 0.027343, 'mean_absolute_return': 0.032102, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.037273, 'median_return': 0.052632, 'mean_absolute_return': 0.058569, 'max_adverse_excursion': -0.07448, 'max_favorable_excursion': 0.10846}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005792`, median `0.006372`, mae `0.014774`
- 5d: sample `60`, hit `0.5667`, avg `0.006677`, median `0.006712`, mae `0.020234`
- 10d: sample `60`, hit `0.7333`, avg `0.015895`, median `0.018086`, mae `0.030022`
- 20d: sample `60`, hit `0.8`, avg `0.025893`, median `0.028859`, mae `0.036499`
- 60d: sample `60`, hit `0.7667`, avg `0.043497`, median `0.055822`, mae `0.062705`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000372`, median `-0.00723`, mae `0.0228`
- 5d: sample `20`, hit `0.55`, avg `-0.001354`, median `0.004752`, mae `0.023721`
- 10d: sample `20`, hit `0.65`, avg `0.015147`, median `0.010559`, mae `0.029187`
- 20d: sample `20`, hit `0.75`, avg `0.025074`, median `0.029038`, mae `0.037371`
- 60d: sample `20`, hit `0.95`, avg `0.070339`, median `0.062764`, mae `0.0714`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005792`, median `0.006372`, mae `0.014774`
- 5d: sample `60`, hit `0.5667`, avg `0.006677`, median `0.006712`, mae `0.020234`
- 10d: sample `60`, hit `0.7333`, avg `0.015895`, median `0.018086`, mae `0.030022`
- 20d: sample `60`, hit `0.8`, avg `0.025893`, median `0.028859`, mae `0.036499`
- 60d: sample `60`, hit `0.7667`, avg `0.043497`, median `0.055822`, mae `0.062705`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001192`, median `0.003072`, mae `0.010293`
- 5d: sample `20`, hit `0.45`, avg `-0.001862`, median `-0.001796`, mae `0.015238`
- 10d: sample `20`, hit `0.7`, avg `0.001858`, median `0.009675`, mae `0.02504`
- 20d: sample `20`, hit `0.75`, avg `0.012737`, median `0.018139`, mae `0.026169`
- 60d: sample `20`, hit `0.7`, avg `0.021521`, median `0.024785`, mae `0.04882`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005792`, median `0.006372`, mae `0.014774`
- 5d: sample `60`, hit `0.5667`, avg `0.006677`, median `0.006712`, mae `0.020234`
- 10d: sample `60`, hit `0.7333`, avg `0.015895`, median `0.018086`, mae `0.030022`
- 20d: sample `60`, hit `0.8`, avg `0.025893`, median `0.028859`, mae `0.036499`
- 60d: sample `60`, hit `0.7667`, avg `0.043497`, median `0.055822`, mae `0.062705`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001192`, median `0.003072`, mae `0.010293`
- 5d: sample `20`, hit `0.45`, avg `-0.001862`, median `-0.001796`, mae `0.015238`
- 10d: sample `20`, hit `0.7`, avg `0.001858`, median `0.009675`, mae `0.02504`
- 20d: sample `20`, hit `0.75`, avg `0.012737`, median `0.018139`, mae `0.026169`
- 60d: sample `20`, hit `0.7`, avg `0.021521`, median `0.024785`, mae `0.04882`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000372`, median `-0.00723`, mae `0.0228`
- 5d: sample `20`, hit `0.55`, avg `-0.001354`, median `0.004752`, mae `0.023721`
- 10d: sample `20`, hit `0.65`, avg `0.015147`, median `0.010559`, mae `0.029187`
- 20d: sample `20`, hit `0.75`, avg `0.025074`, median `0.029038`, mae `0.037371`
- 60d: sample `20`, hit `0.95`, avg `0.070339`, median `0.062764`, mae `0.0714`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004721`, median `0.004391`, mae `0.013486`
- 5d: sample `40`, hit `0.475`, avg `0.001486`, median `-0.001796`, mae `0.017056`
- 10d: sample `40`, hit `0.675`, avg `0.009555`, median `0.012215`, mae `0.025845`
- 20d: sample `40`, hit `0.8`, avg `0.021208`, median `0.027343`, mae `0.032102`
- 60d: sample `40`, hit `0.775`, avg `0.037273`, median `0.052632`, mae `0.058569`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.007933`, median `0.010582`, mae `0.01735`
- 5d: sample `20`, hit `0.75`, avg `0.017058`, median `0.021829`, mae `0.02659`
- 10d: sample `20`, hit `0.85`, avg `0.028575`, median `0.037056`, mae `0.038377`
- 20d: sample `20`, hit `0.8`, avg `0.035263`, median `0.045928`, mae `0.045293`
- 60d: sample `20`, hit `0.75`, avg `0.055945`, median `0.066636`, mae `0.070978`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000372`, median `-0.00723`, mae `0.0228`
- 5d: sample `20`, hit `0.55`, avg `-0.001354`, median `0.004752`, mae `0.023721`
- 10d: sample `20`, hit `0.65`, avg `0.015147`, median `0.010559`, mae `0.029187`
- 20d: sample `20`, hit `0.75`, avg `0.025074`, median `0.029038`, mae `0.037371`
- 60d: sample `20`, hit `0.95`, avg `0.070339`, median `0.062764`, mae `0.0714`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.004721`, median `0.004391`, mae `0.013486`
- 5d: sample `40`, hit `0.475`, avg `0.001486`, median `-0.001796`, mae `0.017056`
- 10d: sample `40`, hit `0.675`, avg `0.009555`, median `0.012215`, mae `0.025845`
- 20d: sample `40`, hit `0.8`, avg `0.021208`, median `0.027343`, mae `0.032102`
- 60d: sample `40`, hit `0.775`, avg `0.037273`, median `0.052632`, mae `0.058569`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.005271`, median `0.009859`, mae `0.018943`
- 5d: sample `60`, hit `0.6`, avg `0.006846`, median `0.011074`, mae `0.023062`
- 10d: sample `60`, hit `0.7167`, avg `0.020325`, median `0.023979`, mae `0.031404`
- 20d: sample `60`, hit `0.8`, avg `0.030005`, median `0.031658`, mae `0.040233`
- 60d: sample `60`, hit `0.85`, avg `0.05977`, median `0.065766`, mae `0.070232`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.004251`, median `0.006274`, mae `0.01678`
- 5d: sample `80`, hit `0.5625`, avg `0.004669`, median `0.006018`, mae `0.021106`
- 10d: sample `80`, hit `0.7125`, avg `0.015708`, median `0.014845`, mae `0.029813`
- 20d: sample `80`, hit `0.7875`, avg `0.025688`, median `0.028859`, mae `0.036717`
- 60d: sample `80`, hit `0.8125`, avg `0.050207`, median `0.055822`, mae `0.064879`

### bounce_with_flow_support
- sample_size: `40`
- 3d: sample `40`, hit `0.7`, avg `0.008092`, median `0.01018`, mae `0.017014`
- 5d: sample `40`, hit `0.625`, avg `0.010946`, median `0.013109`, mae `0.022733`
- 10d: sample `40`, hit `0.75`, avg `0.022913`, median `0.025759`, mae `0.032513`
- 20d: sample `40`, hit `0.825`, avg `0.032471`, median `0.040311`, mae `0.041664`
- 60d: sample `40`, hit `0.8`, avg `0.054485`, median `0.066636`, mae `0.069648`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005792`, median `0.006372`, mae `0.014774`
- 5d: sample `60`, hit `0.5667`, avg `0.006677`, median `0.006712`, mae `0.020234`
- 10d: sample `60`, hit `0.7333`, avg `0.015895`, median `0.018086`, mae `0.030022`
- 20d: sample `60`, hit `0.8`, avg `0.025893`, median `0.028859`, mae `0.036499`
- 60d: sample `60`, hit `0.7667`, avg `0.043497`, median `0.055822`, mae `0.062705`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000372`, median `-0.00723`, mae `0.0228`
- 5d: sample `20`, hit `0.55`, avg `-0.001354`, median `0.004752`, mae `0.023721`
- 10d: sample `20`, hit `0.65`, avg `0.015147`, median `0.010559`, mae `0.029187`
- 20d: sample `20`, hit `0.75`, avg `0.025074`, median `0.029038`, mae `0.037371`
- 60d: sample `20`, hit `0.95`, avg `0.070339`, median `0.062764`, mae `0.0714`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
