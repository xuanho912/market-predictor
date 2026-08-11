# High Confidence Edge Report

Generated at: `2026-08-11T13:48:21.125898+00:00`

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
- 3d: sample `80`, hit `0.625`, avg `0.002747`, median `0.005642`, mae `0.015198`
- 5d: sample `80`, hit `0.6625`, avg `0.004584`, median `0.005327`, mae `0.017837`
- 10d: sample `80`, hit `0.575`, avg `0.006678`, median `0.007467`, mae `0.024807`
- 20d: sample `80`, hit `0.6875`, avg `0.012965`, median `0.015261`, mae `0.040384`
- 60d: sample `80`, hit `0.6`, avg `0.030289`, median `0.046132`, mae `0.073509`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003813`, median `0.001448`, mae `0.013805`
- 5d: sample `8`, hit `0.75`, avg `0.000899`, median `0.004014`, mae `0.010054`
- 10d: sample `8`, hit `0.5`, avg `0.002265`, median `0.011426`, mae `0.018665`
- 20d: sample `8`, hit `0.625`, avg `0.009259`, median `0.020068`, mae `0.026767`
- 60d: sample `8`, hit `0.375`, avg `-0.012738`, median `-0.03081`, mae `0.04907`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.003813`, median `0.001448`, mae `0.013805`
- 5d: sample `8`, hit `0.75`, avg `0.000899`, median `0.004014`, mae `0.010054`
- 10d: sample `8`, hit `0.5`, avg `0.002265`, median `0.011426`, mae `0.018665`
- 20d: sample `8`, hit `0.625`, avg `0.009259`, median `0.020068`, mae `0.026767`
- 60d: sample `8`, hit `0.375`, avg `-0.012738`, median `-0.03081`, mae `0.04907`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.002747, 'median_return': 0.005642, 'mean_absolute_return': 0.015198, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': 0.004584, 'median_return': 0.005327, 'mean_absolute_return': 0.017837, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.006678, 'median_return': 0.007467, 'mean_absolute_return': 0.024807, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.012965, 'median_return': 0.015261, 'mean_absolute_return': 0.040384, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.030289, 'median_return': 0.046132, 'mean_absolute_return': 0.073509, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003813, 'median_return': 0.001448, 'mean_absolute_return': 0.013805, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.000899, 'median_return': 0.004014, 'mean_absolute_return': 0.010054, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002265, 'median_return': 0.011426, 'mean_absolute_return': 0.018665, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009259, 'median_return': 0.020068, 'mean_absolute_return': 0.026767, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012738, 'median_return': -0.03081, 'mean_absolute_return': 0.04907, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.003476, 'median_return': 0.006565, 'mean_absolute_return': 0.015353, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.004993, 'median_return': 0.006452, 'mean_absolute_return': 0.018702, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.007168, 'median_return': 0.007467, 'mean_absolute_return': 0.025489, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.013377, 'median_return': 0.015261, 'mean_absolute_return': 0.041897, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.035069, 'median_return': 0.055266, 'mean_absolute_return': 0.076224, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.6625}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': 0.0, 'both_hit': 53, 'both_miss': 27}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.0, 'both_hit': 46, 'both_miss': 34}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': 0.0, 'both_hit': 55, 'both_miss': 25}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.007955, 'median_return': 0.012091, 'mean_absolute_return': 0.019583, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.003606, 'median_return': 0.010281, 'mean_absolute_return': 0.025927, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.015564, 'median_return': 0.013022, 'mean_absolute_return': 0.036118, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.037269, 'median_return': 0.033791, 'mean_absolute_return': 0.052304, 'max_adverse_excursion': -0.080875, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.068731, 'median_return': 0.080433, 'mean_absolute_return': 0.098991, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.001011, 'median_return': 0.003538, 'mean_absolute_return': 0.013736, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.00491, 'median_return': 0.005327, 'mean_absolute_return': 0.015141, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.003716, 'median_return': 0.005616, 'mean_absolute_return': 0.021036, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.004864, 'median_return': 0.013178, 'mean_absolute_return': 0.03641, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.017474, 'median_return': 0.043546, 'mean_absolute_return': 0.065014, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.147541}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002537`, median `0.000201`, mae `0.01374`
- 5d: sample `40`, hit `0.675`, avg `0.003833`, median `0.004606`, mae `0.014068`
- 10d: sample `40`, hit `0.55`, avg `0.004229`, median `0.007467`, mae `0.018546`
- 20d: sample `40`, hit `0.675`, avg `0.007792`, median `0.013178`, mae `0.032242`
- 60d: sample `40`, hit `0.45`, avg `0.007279`, median `-0.004982`, mae `0.05452`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007955`, median `0.012091`, mae `0.019583`
- 5d: sample `20`, hit `0.6`, avg `0.003606`, median `0.010281`, mae `0.025927`
- 10d: sample `20`, hit `0.6`, avg `0.015564`, median `0.013022`, mae `0.036118`
- 20d: sample `20`, hit `0.75`, avg `0.037269`, median `0.033791`, mae `0.052304`
- 60d: sample `20`, hit `0.7`, avg `0.068731`, median `0.080433`, mae `0.098991`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002537`, median `0.000201`, mae `0.01374`
- 5d: sample `40`, hit `0.675`, avg `0.003833`, median `0.004606`, mae `0.014068`
- 10d: sample `40`, hit `0.55`, avg `0.004229`, median `0.007467`, mae `0.018546`
- 20d: sample `40`, hit `0.675`, avg `0.007792`, median `0.013178`, mae `0.032242`
- 60d: sample `40`, hit `0.45`, avg `0.007279`, median `-0.004982`, mae `0.05452`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.007955`, median `0.012091`, mae `0.019583`
- 5d: sample `20`, hit `0.6`, avg `0.003606`, median `0.010281`, mae `0.025927`
- 10d: sample `20`, hit `0.6`, avg `0.015564`, median `0.013022`, mae `0.036118`
- 20d: sample `20`, hit `0.75`, avg `0.037269`, median `0.033791`, mae `0.052304`
- 60d: sample `20`, hit `0.7`, avg `0.068731`, median `0.080433`, mae `0.098991`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001328`, median `0.006714`, mae `0.017911`
- 5d: sample `20`, hit `0.6`, avg `0.004001`, median `0.004014`, mae `0.017081`
- 10d: sample `20`, hit `0.55`, avg `0.005257`, median `0.010691`, mae `0.022407`
- 20d: sample `20`, hit `0.7`, avg `0.014227`, median `0.022652`, mae `0.03964`
- 60d: sample `20`, hit `0.5`, avg `0.01742`, median `0.012092`, mae `0.057918`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.002537`, median `0.000201`, mae `0.01374`
- 5d: sample `40`, hit `0.675`, avg `0.003833`, median `0.004606`, mae `0.014068`
- 10d: sample `40`, hit `0.55`, avg `0.004229`, median `0.007467`, mae `0.018546`
- 20d: sample `40`, hit `0.675`, avg `0.007792`, median `0.013178`, mae `0.032242`
- 60d: sample `40`, hit `0.45`, avg `0.007279`, median `-0.004982`, mae `0.05452`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.008031`, median `0.012091`, mae `0.016656`
- 5d: sample `40`, hit `0.65`, avg `0.005335`, median `0.010281`, mae `0.021607`
- 10d: sample `40`, hit `0.6`, avg `0.009126`, median `0.00903`, mae `0.031068`
- 20d: sample `40`, hit `0.7`, avg `0.018139`, median `0.01666`, mae `0.048525`
- 60d: sample `40`, hit `0.75`, avg `0.053299`, median `0.069146`, mae `0.092497`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001328`, median `0.006714`, mae `0.017911`
- 5d: sample `20`, hit `0.6`, avg `0.004001`, median `0.004014`, mae `0.017081`
- 10d: sample `20`, hit `0.55`, avg `0.005257`, median `0.010691`, mae `0.022407`
- 20d: sample `20`, hit `0.7`, avg `0.014227`, median `0.022652`, mae `0.03964`
- 60d: sample `20`, hit `0.5`, avg `0.01742`, median `0.012092`, mae `0.057918`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003745`, median `0.000145`, mae `0.009569`
- 5d: sample `20`, hit `0.75`, avg `0.003664`, median `0.005084`, mae `0.011054`
- 10d: sample `20`, hit `0.55`, avg `0.003202`, median `0.007467`, mae `0.014685`
- 20d: sample `20`, hit `0.65`, avg `0.001357`, median `0.012291`, mae `0.024844`
- 60d: sample `20`, hit `0.4`, avg `-0.002862`, median `-0.01711`, mae `0.051123`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.001328`, median `0.006714`, mae `0.017911`
- 5d: sample `20`, hit `0.6`, avg `0.004001`, median `0.004014`, mae `0.017081`
- 10d: sample `20`, hit `0.55`, avg `0.005257`, median `0.010691`, mae `0.022407`
- 20d: sample `20`, hit `0.7`, avg `0.014227`, median `0.022652`, mae `0.03964`
- 60d: sample `20`, hit `0.5`, avg `0.01742`, median `0.012092`, mae `0.057918`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.003745`, median `0.000145`, mae `0.009569`
- 5d: sample `20`, hit `0.75`, avg `0.003664`, median `0.005084`, mae `0.011054`
- 10d: sample `20`, hit `0.55`, avg `0.003202`, median `0.007467`, mae `0.014685`
- 20d: sample `20`, hit `0.65`, avg `0.001357`, median `0.012291`, mae `0.024844`
- 60d: sample `20`, hit `0.4`, avg `-0.002862`, median `-0.01711`, mae `0.051123`

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
