# High Confidence Edge Report

Generated at: `2026-11-12T19:57:13.981640+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `188`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `historical_proxy_supports_higher_confidence_but_forward_validation_required`

## Forward Sample Gates

- 3d: completed `188`, gate `stronger_evidence`
- 5d: completed `188`, gate `stronger_evidence`
- 10d: completed `188`, gate `stronger_evidence`
- 20d: completed `188`, gate `stronger_evidence`
- 60d: completed `188`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002437`, median `0.003538`, mae `0.019717`
- 5d: sample `20`, hit `0.5`, avg `0.004647`, median `0.000519`, mae `0.021326`
- 10d: sample `20`, hit `0.6`, avg `0.011715`, median `0.006856`, mae `0.03184`
- 20d: sample `20`, hit `0.8`, avg `0.015921`, median `0.014567`, mae `0.033783`
- 60d: sample `20`, hit `0.5`, avg `0.004439`, median `0.044733`, mae `0.080461`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002214`, median `-0.005417`, mae `0.014807`
- 5d: sample `40`, hit `0.55`, avg `-0.000212`, median `0.001624`, mae `0.014649`
- 10d: sample `40`, hit `0.375`, avg `-0.000348`, median `-0.006017`, mae `0.017699`
- 20d: sample `40`, hit `0.575`, avg `0.009377`, median `0.012958`, mae `0.031174`
- 60d: sample `40`, hit `0.325`, avg `-0.011104`, median `-0.018455`, mae `0.053065`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

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
- 3d: sample `8`, hit `0.375`, avg `-0.008229`, median `-0.013814`, mae `0.024463`
- 5d: sample `8`, hit `0.375`, avg `-0.005724`, median `-0.005548`, mae `0.020332`
- 10d: sample `8`, hit `0.375`, avg `-0.007593`, median `-0.007535`, mae `0.022098`
- 20d: sample `8`, hit `0.75`, avg `-0.001571`, median `0.013823`, mae `0.031335`
- 60d: sample `8`, hit `0.25`, avg `-0.03188`, median `-0.031299`, mae `0.05688`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.375`, avg `-0.008229`, median `-0.013814`, mae `0.024463`
- 5d: sample `8`, hit `0.375`, avg `-0.005724`, median `-0.005548`, mae `0.020332`
- 10d: sample `8`, hit `0.375`, avg `-0.007593`, median `-0.007535`, mae `0.022098`
- 20d: sample `8`, hit `0.75`, avg `-0.001571`, median `0.013823`, mae `0.031335`
- 60d: sample `8`, hit `0.25`, avg `-0.03188`, median `-0.031299`, mae `0.05688`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002437, 'median_return': 0.003538, 'mean_absolute_return': 0.019717, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.004647, 'median_return': 0.000519, 'mean_absolute_return': 0.021326, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.011715, 'median_return': 0.006856, 'mean_absolute_return': 0.03184, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.015921, 'median_return': 0.014567, 'mean_absolute_return': 0.033783, 'max_adverse_excursion': -0.085064, 'max_favorable_excursion': 0.101125}, '60d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': 0.004439, 'median_return': 0.044733, 'mean_absolute_return': 0.080461, 'max_adverse_excursion': -0.294669, 'max_favorable_excursion': 0.186083}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.002214, 'median_return': -0.005417, 'mean_absolute_return': 0.014807, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.038451}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': -0.000212, 'median_return': 0.001624, 'mean_absolute_return': 0.014649, 'max_adverse_excursion': -0.040544, 'max_favorable_excursion': 0.049393}, '10d': {'sample_size': 40, 'hit_rate': 0.375, 'avg_return': -0.000348, 'median_return': -0.006017, 'mean_absolute_return': 0.017699, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.075562}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.009377, 'median_return': 0.012958, 'mean_absolute_return': 0.031174, 'max_adverse_excursion': -0.051042, 'max_favorable_excursion': 0.089661}, '60d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.011104, 'median_return': -0.018455, 'mean_absolute_return': 0.053065, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.008229, 'median_return': -0.013814, 'mean_absolute_return': 0.024463, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.029672}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.005724, 'median_return': -0.005548, 'mean_absolute_return': 0.020332, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.035985}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.007593, 'median_return': -0.007535, 'mean_absolute_return': 0.022098, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.050956}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': -0.001571, 'median_return': 0.013823, 'mean_absolute_return': 0.031335, 'max_adverse_excursion': -0.085064, 'max_favorable_excursion': 0.050144}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.03188, 'median_return': -0.031299, 'mean_absolute_return': 0.05688, 'max_adverse_excursion': -0.182805, 'max_favorable_excursion': 0.055266}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.003102, 'median_return': 0.002046, 'mean_absolute_return': 0.016584, 'max_adverse_excursion': -0.04969, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.00533, 'median_return': 0.004408, 'mean_absolute_return': 0.017661, 'max_adverse_excursion': -0.04207, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': 0.005912, 'median_return': 0.000197, 'mean_absolute_return': 0.027815, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.018668, 'median_return': 0.017416, 'mean_absolute_return': 0.03606, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.152433}, '60d': {'sample_size': 72, 'hit_rate': 0.4722, 'avg_return': 0.005368, 'median_return': -0.003049, 'mean_absolute_return': 0.07121, 'max_adverse_excursion': -0.316659, 'max_favorable_excursion': 0.258847}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4}, '5d': {'sample_size': 80, 'hit_rate': 0.45}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.55}, '60d': {'sample_size': 80, 'hit_rate': 0.375}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.225, 'both_hit': 11, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 10, 'both_miss': 10}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.175, 'both_hit': 12, 'both_miss': 8}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.05, 'both_hit': 16, 'both_miss': 4}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 10, 'both_miss': 10}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.009868, 'median_return': 0.012584, 'mean_absolute_return': 0.020157, 'max_adverse_excursion': -0.04969, 'max_favorable_excursion': 0.036856}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.012674, 'median_return': 0.012634, 'mean_absolute_return': 0.021089, 'max_adverse_excursion': -0.04207, 'max_favorable_excursion': 0.049091}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.007226, 'median_return': 0.018412, 'mean_absolute_return': 0.041737, 'max_adverse_excursion': -0.156852, 'max_favorable_excursion': 0.109183}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.031904, 'median_return': 0.036446, 'mean_absolute_return': 0.046219, 'max_adverse_excursion': -0.078831, 'max_favorable_excursion': 0.152433}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.024342, 'median_return': 0.045321, 'mean_absolute_return': 0.092516, 'max_adverse_excursion': -0.316659, 'max_favorable_excursion': 0.258847}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.000664, 'median_return': -0.002654, 'mean_absolute_return': 0.016443, 'max_adverse_excursion': -0.040531, 'max_favorable_excursion': 0.049303}, '5d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.001408, 'median_return': 0.000762, 'mean_absolute_return': 0.016874, 'max_adverse_excursion': -0.050569, 'max_favorable_excursion': 0.061998}, '10d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': 0.003673, 'median_return': -0.004918, 'mean_absolute_return': 0.022412, 'max_adverse_excursion': -0.05959, 'max_favorable_excursion': 0.099025}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.011558, 'median_return': 0.013823, 'mean_absolute_return': 0.032044, 'max_adverse_excursion': -0.085064, 'max_favorable_excursion': 0.101125}, '60d': {'sample_size': 60, 'hit_rate': 0.3833, 'avg_return': -0.005923, 'median_return': -0.018455, 'mean_absolute_return': 0.062197, 'max_adverse_excursion': -0.294669, 'max_favorable_excursion': 0.186083}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000664`, median `-0.002654`, mae `0.016443`
- 5d: sample `60`, hit `0.5333`, avg `0.001408`, median `0.000762`, mae `0.016874`
- 10d: sample `60`, hit `0.45`, avg `0.003673`, median `-0.004918`, mae `0.022412`
- 20d: sample `60`, hit `0.65`, avg `0.011558`, median `0.013823`, mae `0.032044`
- 60d: sample `60`, hit `0.3833`, avg `-0.005923`, median `-0.018455`, mae `0.062197`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000664`, median `-0.002654`, mae `0.016443`
- 5d: sample `60`, hit `0.5333`, avg `0.001408`, median `0.000762`, mae `0.016874`
- 10d: sample `60`, hit `0.45`, avg `0.003673`, median `-0.004918`, mae `0.022412`
- 20d: sample `60`, hit `0.65`, avg `0.011558`, median `0.013823`, mae `0.032044`
- 60d: sample `60`, hit `0.3833`, avg `-0.005923`, median `-0.018455`, mae `0.062197`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000664`, median `-0.002654`, mae `0.016443`
- 5d: sample `60`, hit `0.5333`, avg `0.001408`, median `0.000762`, mae `0.016874`
- 10d: sample `60`, hit `0.45`, avg `0.003673`, median `-0.004918`, mae `0.022412`
- 20d: sample `60`, hit `0.65`, avg `0.011558`, median `0.013823`, mae `0.032044`
- 60d: sample `60`, hit `0.3833`, avg `-0.005923`, median `-0.018455`, mae `0.062197`

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
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002214`, median `-0.005417`, mae `0.014807`
- 5d: sample `40`, hit `0.55`, avg `-0.000212`, median `0.001624`, mae `0.014649`
- 10d: sample `40`, hit `0.375`, avg `-0.000348`, median `-0.006017`, mae `0.017699`
- 20d: sample `40`, hit `0.575`, avg `0.009377`, median `0.012958`, mae `0.031174`
- 60d: sample `40`, hit `0.325`, avg `-0.011104`, median `-0.018455`, mae `0.053065`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002437`, median `0.003538`, mae `0.019717`
- 5d: sample `20`, hit `0.5`, avg `0.004647`, median `0.000519`, mae `0.021326`
- 10d: sample `20`, hit `0.6`, avg `0.011715`, median `0.006856`, mae `0.03184`
- 20d: sample `20`, hit `0.8`, avg `0.015921`, median `0.014567`, mae `0.033783`
- 60d: sample `20`, hit `0.5`, avg `0.004439`, median `0.044733`, mae `0.080461`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.002214`, median `-0.005417`, mae `0.014807`
- 5d: sample `40`, hit `0.55`, avg `-0.000212`, median `0.001624`, mae `0.014649`
- 10d: sample `40`, hit `0.375`, avg `-0.000348`, median `-0.006017`, mae `0.017699`
- 20d: sample `40`, hit `0.575`, avg `0.009377`, median `0.012958`, mae `0.031174`
- 60d: sample `40`, hit `0.325`, avg `-0.011104`, median `-0.018455`, mae `0.053065`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001969`, median `0.001999`, mae `0.017372`
- 5d: sample `80`, hit `0.6`, avg `0.004224`, median `0.003714`, mae `0.017928`
- 10d: sample `80`, hit `0.4875`, avg `0.004561`, median `-0.001676`, mae `0.027244`
- 20d: sample `80`, hit `0.675`, avg `0.016645`, median `0.015661`, mae `0.035588`
- 60d: sample `80`, hit `0.45`, avg `0.001643`, median `-0.005523`, mae `0.069777`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `0.001969`, median `0.001999`, mae `0.017372`
- 5d: sample `80`, hit `0.6`, avg `0.004224`, median `0.003714`, mae `0.017928`
- 10d: sample `80`, hit `0.4875`, avg `0.004561`, median `-0.001676`, mae `0.027244`
- 20d: sample `80`, hit `0.675`, avg `0.016645`, median `0.015661`, mae `0.035588`
- 60d: sample `80`, hit `0.45`, avg `0.001643`, median `-0.005523`, mae `0.069777`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000664`, median `-0.002654`, mae `0.016443`
- 5d: sample `60`, hit `0.5333`, avg `0.001408`, median `0.000762`, mae `0.016874`
- 10d: sample `60`, hit `0.45`, avg `0.003673`, median `-0.004918`, mae `0.022412`
- 20d: sample `60`, hit `0.65`, avg `0.011558`, median `0.013823`, mae `0.032044`
- 60d: sample `60`, hit `0.3833`, avg `-0.005923`, median `-0.018455`, mae `0.062197`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000664`, median `-0.002654`, mae `0.016443`
- 5d: sample `60`, hit `0.5333`, avg `0.001408`, median `0.000762`, mae `0.016874`
- 10d: sample `60`, hit `0.45`, avg `0.003673`, median `-0.004918`, mae `0.022412`
- 20d: sample `60`, hit `0.65`, avg `0.011558`, median `0.013823`, mae `0.032044`
- 60d: sample `60`, hit `0.3833`, avg `-0.005923`, median `-0.018455`, mae `0.062197`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.009868`, median `0.012584`, mae `0.020157`
- 5d: sample `20`, hit `0.8`, avg `0.012674`, median `0.012634`, mae `0.021089`
- 10d: sample `20`, hit `0.6`, avg `0.007226`, median `0.018412`, mae `0.041737`
- 20d: sample `20`, hit `0.75`, avg `0.031904`, median `0.036446`, mae `0.046219`
- 60d: sample `20`, hit `0.65`, avg `0.024342`, median `0.045321`, mae `0.092516`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
