# High Confidence Edge Report

Generated at: `2026-08-16T13:03:53.446333+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.003222`, median `0.005642`, mae `0.013245`
- 5d: sample `40`, hit `0.6`, avg `0.002647`, median `0.004014`, mae `0.015095`
- 10d: sample `40`, hit `0.65`, avg `0.008925`, median `0.010691`, mae `0.020124`
- 20d: sample `40`, hit `0.725`, avg `0.018474`, median `0.027502`, mae `0.04193`
- 60d: sample `40`, hit `0.625`, avg `0.030414`, median `0.046132`, mae `0.082823`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.002973`, median `0.004004`, mae `0.013332`
- 5d: sample `40`, hit `0.675`, avg `0.004872`, median `0.005084`, mae `0.016987`
- 10d: sample `40`, hit `0.55`, avg `0.009477`, median `0.012215`, mae `0.026732`
- 20d: sample `40`, hit `0.625`, avg `0.015977`, median `0.013178`, mae `0.045158`
- 60d: sample `40`, hit `0.625`, avg `0.034703`, median `0.032982`, mae `0.067764`

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
- 3d: sample `8`, hit `0.5`, avg `-0.000728`, median `0.001448`, mae `0.012178`
- 5d: sample `8`, hit `0.625`, avg `0.000875`, median `0.005319`, mae `0.011784`
- 10d: sample `8`, hit `0.75`, avg `0.007606`, median `0.011426`, mae `0.016377`
- 20d: sample `8`, hit `0.75`, avg `0.01684`, median `0.022652`, mae `0.022519`
- 60d: sample `8`, hit `0.375`, avg `0.006335`, median `-0.020268`, mae `0.04842`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.000728`, median `0.001448`, mae `0.012178`
- 5d: sample `8`, hit `0.625`, avg `0.000875`, median `0.005319`, mae `0.011784`
- 10d: sample `8`, hit `0.75`, avg `0.007606`, median `0.011426`, mae `0.016377`
- 20d: sample `8`, hit `0.75`, avg `0.01684`, median `0.022652`, mae `0.022519`
- 60d: sample `8`, hit `0.375`, avg `0.006335`, median `-0.020268`, mae `0.04842`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.003222, 'median_return': 0.005642, 'mean_absolute_return': 0.013245, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002647, 'median_return': 0.004014, 'mean_absolute_return': 0.015095, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.008925, 'median_return': 0.010691, 'mean_absolute_return': 0.020124, 'max_adverse_excursion': -0.033507, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.018474, 'median_return': 0.027502, 'mean_absolute_return': 0.04193, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.030414, 'median_return': 0.046132, 'mean_absolute_return': 0.082823, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002973, 'median_return': 0.004004, 'mean_absolute_return': 0.013332, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.004872, 'median_return': 0.005084, 'mean_absolute_return': 0.016987, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.009477, 'median_return': 0.012215, 'mean_absolute_return': 0.026732, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.015977, 'median_return': 0.013178, 'mean_absolute_return': 0.045158, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.034703, 'median_return': 0.032982, 'mean_absolute_return': 0.067764, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000728, 'median_return': 0.001448, 'mean_absolute_return': 0.012178, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.000875, 'median_return': 0.005319, 'mean_absolute_return': 0.011784, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007606, 'median_return': 0.011426, 'mean_absolute_return': 0.016377, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.01684, 'median_return': 0.022652, 'mean_absolute_return': 0.022519, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.006335, 'median_return': -0.020268, 'mean_absolute_return': 0.04842, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003523, 'median_return': 0.004569, 'mean_absolute_return': 0.013412, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.00408, 'median_return': 0.004606, 'mean_absolute_return': 0.016514, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.009378, 'median_return': 0.011168, 'mean_absolute_return': 0.024211, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.017268, 'median_return': 0.020226, 'mean_absolute_return': 0.04588, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.035472, 'median_return': 0.043741, 'mean_absolute_return': 0.07828, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 32}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': 0.0, 'both_hit': 54, 'both_miss': 26}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.009257, 'median_return': 0.010891, 'mean_absolute_return': 0.01706, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006839, 'median_return': 0.009721, 'mean_absolute_return': 0.02368, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.018491, 'median_return': 0.016536, 'mean_absolute_return': 0.038402, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.034864, 'median_return': 0.029018, 'mean_absolute_return': 0.063565, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.074228, 'median_return': 0.071905, 'mean_absolute_return': 0.086328, 'max_adverse_excursion': -0.063058, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.001045, 'median_return': 0.001448, 'mean_absolute_return': 0.012031, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.002733, 'median_return': 0.004606, 'mean_absolute_return': 0.013495, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.006104, 'median_return': 0.007467, 'mean_absolute_return': 0.018437, 'max_adverse_excursion': -0.033507, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.011346, 'median_return': 0.020226, 'mean_absolute_return': 0.03687, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.018669, 'median_return': 0.030786, 'mean_absolute_return': 0.071616, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.000601`, median `0.000603`, mae `0.012789`
- 5d: sample `40`, hit `0.675`, avg `0.004611`, median `0.005084`, mae `0.012731`
- 10d: sample `40`, hit `0.575`, avg `0.004921`, median `0.007467`, mae `0.017271`
- 20d: sample `40`, hit `0.725`, avg `0.01084`, median `0.020068`, mae `0.031584`
- 60d: sample `40`, hit `0.5`, avg `0.012401`, median `0.012092`, mae `0.055795`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.000601`, median `0.000603`, mae `0.012789`
- 5d: sample `40`, hit `0.675`, avg `0.004611`, median `0.005084`, mae `0.012731`
- 10d: sample `40`, hit `0.575`, avg `0.004921`, median `0.007467`, mae `0.017271`
- 20d: sample `40`, hit `0.725`, avg `0.01084`, median `0.020068`, mae `0.031584`
- 60d: sample `40`, hit `0.5`, avg `0.012401`, median `0.012092`, mae `0.055795`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.000601`, median `0.000603`, mae `0.012789`
- 5d: sample `40`, hit `0.675`, avg `0.004611`, median `0.005084`, mae `0.012731`
- 10d: sample `40`, hit `0.575`, avg `0.004921`, median `0.007467`, mae `0.017271`
- 20d: sample `40`, hit `0.725`, avg `0.01084`, median `0.020068`, mae `0.031584`
- 60d: sample `40`, hit `0.5`, avg `0.012401`, median `0.012092`, mae `0.055795`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.65`, avg `0.006797`, median `0.006443`, mae `0.013788`
- 5d: sample `40`, hit `0.6`, avg `0.002908`, median `0.003209`, mae `0.019351`
- 10d: sample `40`, hit `0.625`, avg `0.013481`, median `0.01246`, mae `0.029585`
- 20d: sample `40`, hit `0.625`, avg `0.023611`, median `0.029018`, mae `0.055503`
- 60d: sample `40`, hit `0.75`, avg `0.052717`, median `0.057531`, mae `0.094792`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `-0.000601`, median `0.000603`, mae `0.012789`
- 5d: sample `40`, hit `0.675`, avg `0.004611`, median `0.005084`, mae `0.012731`
- 10d: sample `40`, hit `0.575`, avg `0.004921`, median `0.007467`, mae `0.017271`
- 20d: sample `40`, hit `0.725`, avg `0.01084`, median `0.020068`, mae `0.031584`
- 60d: sample `40`, hit `0.5`, avg `0.012401`, median `0.012092`, mae `0.055795`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.003098`, median `0.004542`, mae `0.013288`
- 5d: sample `80`, hit `0.6375`, avg `0.003759`, median `0.004606`, mae `0.016041`
- 10d: sample `80`, hit `0.6`, avg `0.009201`, median `0.011168`, mae `0.023428`
- 20d: sample `80`, hit `0.675`, avg `0.017225`, median `0.020226`, mae `0.043544`
- 60d: sample `80`, hit `0.625`, avg `0.032559`, median `0.043546`, mae `0.075294`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6`, avg `0.003098`, median `0.004542`, mae `0.013288`
- 5d: sample `80`, hit `0.6375`, avg `0.003759`, median `0.004606`, mae `0.016041`
- 10d: sample `80`, hit `0.6`, avg `0.009201`, median `0.011168`, mae `0.023428`
- 20d: sample `80`, hit `0.675`, avg `0.017225`, median `0.020226`, mae `0.043544`
- 60d: sample `80`, hit `0.625`, avg `0.032559`, median `0.043546`, mae `0.075294`

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
