# High Confidence Edge Report

Generated at: `2026-08-15T02:22:24.760139+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `60`
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
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002108`, median `0.009229`, mae `0.015974`
- 5d: sample `20`, hit `0.6`, avg `0.006318`, median `0.005319`, mae `0.015168`
- 10d: sample `20`, hit `0.7`, avg `0.009379`, median `0.011426`, mae `0.019479`
- 20d: sample `20`, hit `0.85`, avg `0.024591`, median `0.027502`, mae `0.036417`
- 60d: sample `20`, hit `0.6`, avg `0.029623`, median `0.046132`, mae `0.062389`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002806`, median `0.000766`, mae `0.013081`
- 5d: sample `40`, hit `0.675`, avg `0.004293`, median `0.004606`, mae `0.017467`
- 10d: sample `40`, hit `0.5`, avg `0.006688`, median `0.007467`, mae `0.027361`
- 20d: sample `40`, hit `0.55`, avg `0.013111`, median `0.010656`, mae `0.044951`
- 60d: sample `40`, hit `0.575`, avg `0.029286`, median `0.020144`, mae `0.066634`

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
- sample_size: `6`
- 3d: sample `6`, hit `0.6667`, avg `0.004648`, median `0.009229`, mae `0.010618`
- 5d: sample `6`, hit `0.8333`, avg `0.007607`, median `0.010241`, mae `0.00927`
- 10d: sample `6`, hit `0.8333`, avg `0.011352`, median `0.021953`, mae `0.01706`
- 20d: sample `6`, hit `0.6667`, avg `0.016149`, median `0.022652`, mae `0.023721`
- 60d: sample `6`, hit `0.3333`, avg `0.004136`, median `-0.03081`, mae `0.053493`

### confidence_score top 10%
- sample_size: `6`
- 3d: sample `6`, hit `0.6667`, avg `0.004648`, median `0.009229`, mae `0.010618`
- 5d: sample `6`, hit `0.8333`, avg `0.007607`, median `0.010241`, mae `0.00927`
- 10d: sample `6`, hit `0.8333`, avg `0.011352`, median `0.021953`, mae `0.01706`
- 20d: sample `6`, hit `0.6667`, avg `0.016149`, median `0.022652`, mae `0.023721`
- 60d: sample `6`, hit `0.3333`, avg `0.004136`, median `-0.03081`, mae `0.053493`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.002108, 'median_return': 0.009229, 'mean_absolute_return': 0.015974, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006318, 'median_return': 0.005319, 'mean_absolute_return': 0.015168, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.009379, 'median_return': 0.011426, 'mean_absolute_return': 0.019479, 'max_adverse_excursion': -0.033507, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.024591, 'median_return': 0.027502, 'mean_absolute_return': 0.036417, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.029623, 'median_return': 0.046132, 'mean_absolute_return': 0.062389, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.102896}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002806, 'median_return': 0.000766, 'mean_absolute_return': 0.013081, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.004293, 'median_return': 0.004606, 'mean_absolute_return': 0.017467, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.006688, 'median_return': 0.007467, 'mean_absolute_return': 0.027361, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.013111, 'median_return': 0.010656, 'mean_absolute_return': 0.044951, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.029286, 'median_return': 0.020144, 'mean_absolute_return': 0.066634, 'max_adverse_excursion': -0.088557, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 6, 'by_horizon': {'3d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.004648, 'median_return': 0.009229, 'mean_absolute_return': 0.010618, 'max_adverse_excursion': -0.012068, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 6, 'hit_rate': 0.8333, 'avg_return': 0.007607, 'median_return': 0.010241, 'mean_absolute_return': 0.00927, 'max_adverse_excursion': -0.004989, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 6, 'hit_rate': 0.8333, 'avg_return': 0.011352, 'median_return': 0.021953, 'mean_absolute_return': 0.01706, 'max_adverse_excursion': -0.017124, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.016149, 'median_return': 0.022652, 'mean_absolute_return': 0.023721, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 6, 'hit_rate': 0.3333, 'avg_return': 0.004136, 'median_return': -0.03081, 'mean_absolute_return': 0.053493, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 54, 'by_horizon': {'3d': {'sample_size': 54, 'hit_rate': 0.5741, 'avg_return': 0.002343, 'median_return': 0.002329, 'mean_absolute_return': 0.014426, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 54, 'hit_rate': 0.6296, 'avg_return': 0.004675, 'median_return': 0.003005, 'mean_absolute_return': 0.017526, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 54, 'hit_rate': 0.537, 'avg_return': 0.007166, 'median_return': 0.007467, 'mean_absolute_return': 0.025587, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 54, 'hit_rate': 0.6481, 'avg_return': 0.017025, 'median_return': 0.015261, 'mean_absolute_return': 0.044149, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 54, 'hit_rate': 0.6111, 'avg_return': 0.032205, 'median_return': 0.030553, 'mean_absolute_return': 0.066522, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 60, 'hit_rate': 0.5833}, '5d': {'sample_size': 60, 'hit_rate': 0.65}, '10d': {'sample_size': 60, 'hit_rate': 0.5667}, '20d': {'sample_size': 60, 'hit_rate': 0.65}, '60d': {'sample_size': 60, 'hit_rate': 0.5833}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 60, 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.5833, 'primary_minus_secondary': 0.0, 'both_hit': 35, 'both_miss': 25}, '5d': {'sample_size': 60, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 21}, '10d': {'sample_size': 60, 'primary_hit_rate': 0.5667, 'secondary_hit_rate': 0.5667, 'primary_minus_secondary': 0.0, 'both_hit': 34, 'both_miss': 26}, '20d': {'sample_size': 60, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 21}, '60d': {'sample_size': 60, 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.5833, 'primary_minus_secondary': 0.0, 'both_hit': 35, 'both_miss': 25}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.009257, 'median_return': 0.010891, 'mean_absolute_return': 0.01706, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.006839, 'median_return': 0.009721, 'mean_absolute_return': 0.02368, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.018491, 'median_return': 0.016536, 'mean_absolute_return': 0.038402, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.034864, 'median_return': 0.029018, 'mean_absolute_return': 0.063565, 'max_adverse_excursion': -0.136294, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.074228, 'median_return': 0.071905, 'mean_absolute_return': 0.086328, 'max_adverse_excursion': -0.063058, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.000768, 'median_return': 0.000201, 'mean_absolute_return': 0.012538, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.004032, 'median_return': 0.004606, 'mean_absolute_return': 0.013211, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.002132, 'median_return': 0.002739, 'mean_absolute_return': 0.0179, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.007974, 'median_return': 0.012291, 'mean_absolute_return': 0.031378, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.45, 'avg_return': 0.006984, 'median_return': -0.004982, 'mean_absolute_return': 0.054665, 'max_adverse_excursion': -0.1263, 'max_favorable_excursion': 0.102896}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.000768`, median `0.000201`, mae `0.012538`
- 5d: sample `40`, hit `0.675`, avg `0.004032`, median `0.004606`, mae `0.013211`
- 10d: sample `40`, hit `0.525`, avg `0.002132`, median `0.002739`, mae `0.0179`
- 20d: sample `40`, hit `0.65`, avg `0.007974`, median `0.012291`, mae `0.031378`
- 60d: sample `40`, hit `0.45`, avg `0.006984`, median `-0.004982`, mae `0.054665`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.000768`, median `0.000201`, mae `0.012538`
- 5d: sample `40`, hit `0.675`, avg `0.004032`, median `0.004606`, mae `0.013211`
- 10d: sample `40`, hit `0.525`, avg `0.002132`, median `0.002739`, mae `0.0179`
- 20d: sample `40`, hit `0.65`, avg `0.007974`, median `0.012291`, mae `0.031378`
- 60d: sample `40`, hit `0.45`, avg `0.006984`, median `-0.004982`, mae `0.054665`

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
- 3d: sample `40`, hit `0.525`, avg `-0.000768`, median `0.000201`, mae `0.012538`
- 5d: sample `40`, hit `0.675`, avg `0.004032`, median `0.004606`, mae `0.013211`
- 10d: sample `40`, hit `0.525`, avg `0.002132`, median `0.002739`, mae `0.0179`
- 20d: sample `40`, hit `0.65`, avg `0.007974`, median `0.012291`, mae `0.031378`
- 60d: sample `40`, hit `0.45`, avg `0.006984`, median `-0.004982`, mae `0.054665`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003645`, median `-0.001166`, mae `0.009102`
- 5d: sample `20`, hit `0.75`, avg `0.001747`, median `0.004606`, mae `0.011254`
- 10d: sample `20`, hit `0.35`, avg `-0.005115`, median `-0.007117`, mae `0.01632`
- 20d: sample `20`, hit `0.45`, avg `-0.008642`, median `-0.001203`, mae `0.026338`
- 60d: sample `20`, hit `0.3`, avg `-0.015656`, median `-0.018455`, mae `0.046941`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002108`, median `0.009229`, mae `0.015974`
- 5d: sample `20`, hit `0.6`, avg `0.006318`, median `0.005319`, mae `0.015168`
- 10d: sample `20`, hit `0.7`, avg `0.009379`, median `0.011426`, mae `0.019479`
- 20d: sample `20`, hit `0.85`, avg `0.024591`, median `0.027502`, mae `0.036417`
- 60d: sample `20`, hit `0.6`, avg `0.029623`, median `0.046132`, mae `0.062389`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.009257`, median `0.010891`, mae `0.01706`
- 5d: sample `20`, hit `0.6`, avg `0.006839`, median `0.009721`, mae `0.02368`
- 10d: sample `20`, hit `0.65`, avg `0.018491`, median `0.016536`, mae `0.038402`
- 20d: sample `20`, hit `0.65`, avg `0.034864`, median `0.029018`, mae `0.063565`
- 60d: sample `20`, hit `0.85`, avg `0.074228`, median `0.071905`, mae `0.086328`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.003645`, median `-0.001166`, mae `0.009102`
- 5d: sample `20`, hit `0.75`, avg `0.001747`, median `0.004606`, mae `0.011254`
- 10d: sample `20`, hit `0.35`, avg `-0.005115`, median `-0.007117`, mae `0.01632`
- 20d: sample `20`, hit `0.45`, avg `-0.008642`, median `-0.001203`, mae `0.026338`
- 60d: sample `20`, hit `0.3`, avg `-0.015656`, median `-0.018455`, mae `0.046941`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002573`, median `0.002329`, mae `0.014045`
- 5d: sample `60`, hit `0.65`, avg `0.004968`, median `0.004606`, mae `0.016701`
- 10d: sample `60`, hit `0.5667`, avg `0.007585`, median `0.010691`, mae `0.024734`
- 20d: sample `60`, hit `0.65`, avg `0.016938`, median `0.015261`, mae `0.042107`
- 60d: sample `60`, hit `0.5833`, avg `0.029398`, median `0.026139`, mae `0.065219`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002573`, median `0.002329`, mae `0.014045`
- 5d: sample `60`, hit `0.65`, avg `0.004968`, median `0.004606`, mae `0.016701`
- 10d: sample `60`, hit `0.5667`, avg `0.007585`, median `0.010691`, mae `0.024734`
- 20d: sample `60`, hit `0.65`, avg `0.016938`, median `0.015261`, mae `0.042107`
- 60d: sample `60`, hit `0.5833`, avg `0.029398`, median `0.026139`, mae `0.065219`

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
