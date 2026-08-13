# High Confidence Edge Report

Generated at: `2026-08-13T13:50:48.671063+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003316`, median `0.004004`, mae `0.012609`
- 5d: sample `60`, hit `0.6667`, avg `0.00602`, median `0.006133`, mae `0.016019`
- 10d: sample `60`, hit `0.6333`, avg `0.008198`, median `0.010691`, mae `0.01938`
- 20d: sample `60`, hit `0.7167`, avg `0.013493`, median `0.020226`, mae `0.033709`
- 60d: sample `60`, hit `0.5833`, avg `0.018784`, median `0.045044`, mae `0.070533`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

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
- `{'strong_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.003316, 'median_return': 0.004004, 'mean_absolute_return': 0.012609, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030961}, '5d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.00602, 'median_return': 0.006133, 'mean_absolute_return': 0.016019, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.008198, 'median_return': 0.010691, 'mean_absolute_return': 0.01938, 'max_adverse_excursion': -0.033551, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.013493, 'median_return': 0.020226, 'mean_absolute_return': 0.033709, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.018784, 'median_return': 0.045044, 'mean_absolute_return': 0.070533, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.147541}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.008292, 'median_return': 0.010849, 'mean_absolute_return': 0.016473, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002088, 'median_return': 0.001654, 'mean_absolute_return': 0.021838, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007342, 'median_return': 0.011168, 'mean_absolute_return': 0.03467, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.017266, 'median_return': 0.010824, 'mean_absolute_return': 0.060433, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.052484, 'median_return': 0.065495, 'mean_absolute_return': 0.077384, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.171512}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.000728, 'median_return': 0.001448, 'mean_absolute_return': 0.012178, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.000875, 'median_return': 0.005319, 'mean_absolute_return': 0.011784, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.007606, 'median_return': 0.011426, 'mean_absolute_return': 0.016377, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.01684, 'median_return': 0.022652, 'mean_absolute_return': 0.022519, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.006335, 'median_return': -0.020268, 'mean_absolute_return': 0.04842, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.625, 'avg_return': 0.005148, 'median_return': 0.00558, 'mean_absolute_return': 0.013731, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.005499, 'median_return': 0.006133, 'mean_absolute_return': 0.018106, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.008026, 'median_return': 0.00903, 'mean_absolute_return': 0.023961, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.01417, 'median_return': 0.016027, 'mean_absolute_return': 0.042376, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.029528, 'median_return': 0.048421, 'mean_absolute_return': 0.074893, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.171512}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.6125}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.6875}, '60d': {'sample_size': 80, 'hit_rate': 0.6375}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': 0.0, 'both_hit': 49, 'both_miss': 31}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': 0.0, 'both_hit': 55, 'both_miss': 25}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.00827, 'median_return': 0.010849, 'mean_absolute_return': 0.015216, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.004401, 'median_return': 0.005327, 'mean_absolute_return': 0.020544, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.008783, 'median_return': 0.00903, 'mean_absolute_return': 0.028865, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.01366, 'median_return': 0.014007, 'mean_absolute_return': 0.050672, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.041734, 'median_return': 0.063119, 'mean_absolute_return': 0.082859, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.171512}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.000851, 'median_return': 0.001448, 'mean_absolute_return': 0.011935, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.005673, 'median_return': 0.006452, 'mean_absolute_return': 0.014403, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.007186, 'median_return': 0.011426, 'mean_absolute_return': 0.017539, 'max_adverse_excursion': -0.033551, 'max_favorable_excursion': 0.050746}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.015213, 'median_return': 0.02086, 'mean_absolute_return': 0.030108, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.085597}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.012684, 'median_return': 0.018072, 'mean_absolute_return': 0.061632, 'max_adverse_excursion': -0.152845, 'max_favorable_excursion': 0.102896}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003316`, median `0.004004`, mae `0.012609`
- 5d: sample `60`, hit `0.6667`, avg `0.00602`, median `0.006133`, mae `0.016019`
- 10d: sample `60`, hit `0.6333`, avg `0.008198`, median `0.010691`, mae `0.01938`
- 20d: sample `60`, hit `0.7167`, avg `0.013493`, median `0.020226`, mae `0.033709`
- 60d: sample `60`, hit `0.5833`, avg `0.018784`, median `0.045044`, mae `0.070533`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003316`, median `0.004004`, mae `0.012609`
- 5d: sample `60`, hit `0.6667`, avg `0.00602`, median `0.006133`, mae `0.016019`
- 10d: sample `60`, hit `0.6333`, avg `0.008198`, median `0.010691`, mae `0.01938`
- 20d: sample `60`, hit `0.7167`, avg `0.013493`, median `0.020226`, mae `0.033709`
- 60d: sample `60`, hit `0.5833`, avg `0.018784`, median `0.045044`, mae `0.070533`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008247`, median `0.01297`, mae `0.013959`
- 5d: sample `20`, hit `0.65`, avg `0.006714`, median `0.006133`, mae `0.019249`
- 10d: sample `20`, hit `0.6`, avg `0.010223`, median `0.00903`, mae `0.023061`
- 20d: sample `20`, hit `0.6`, avg `0.010053`, median `0.01666`, mae `0.040911`
- 60d: sample `20`, hit `0.75`, avg `0.030985`, median `0.063119`, mae `0.088334`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.003316`, median `0.004004`, mae `0.012609`
- 5d: sample `60`, hit `0.6667`, avg `0.00602`, median `0.006133`, mae `0.016019`
- 10d: sample `60`, hit `0.6333`, avg `0.008198`, median `0.010691`, mae `0.01938`
- 20d: sample `60`, hit `0.7167`, avg `0.013493`, median `0.020226`, mae `0.033709`
- 60d: sample `60`, hit `0.5833`, avg `0.018784`, median `0.045044`, mae `0.070533`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008247`, median `0.01297`, mae `0.013959`
- 5d: sample `20`, hit `0.65`, avg `0.006714`, median `0.006133`, mae `0.019249`
- 10d: sample `20`, hit `0.6`, avg `0.010223`, median `0.00903`, mae `0.023061`
- 20d: sample `20`, hit `0.6`, avg `0.010053`, median `0.01666`, mae `0.040911`
- 60d: sample `20`, hit `0.75`, avg `0.030985`, median `0.063119`, mae `0.088334`

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
- 3d: sample `20`, hit `0.6`, avg `0.000137`, median `0.000603`, mae `0.008024`
- 5d: sample `20`, hit `0.8`, avg `0.006506`, median `0.007324`, mae `0.012461`
- 10d: sample `20`, hit `0.6`, avg `0.006319`, median `0.012215`, mae `0.014271`
- 20d: sample `20`, hit `0.75`, avg `0.010206`, median `0.019193`, mae `0.021436`
- 60d: sample `20`, hit `0.45`, avg `0.003991`, median `-0.003049`, mae `0.053837`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001565`, median `0.009229`, mae `0.015845`
- 5d: sample `20`, hit `0.55`, avg `0.00484`, median `0.005319`, mae `0.016345`
- 10d: sample `20`, hit `0.7`, avg `0.008052`, median `0.011426`, mae `0.020806`
- 20d: sample `20`, hit `0.8`, avg `0.020221`, median `0.027502`, mae `0.038781`
- 60d: sample `20`, hit `0.55`, avg `0.021376`, median `0.046132`, mae `0.069427`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.000137`, median `0.000603`, mae `0.008024`
- 5d: sample `20`, hit `0.8`, avg `0.006506`, median `0.007324`, mae `0.012461`
- 10d: sample `20`, hit `0.6`, avg `0.006319`, median `0.012215`, mae `0.014271`
- 20d: sample `20`, hit `0.75`, avg `0.010206`, median `0.019193`, mae `0.021436`
- 60d: sample `20`, hit `0.45`, avg `0.003991`, median `-0.003049`, mae `0.053837`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.00456`, median `0.005458`, mae `0.013575`
- 5d: sample `80`, hit `0.6375`, avg `0.005037`, median `0.005327`, mae `0.017474`
- 10d: sample `80`, hit `0.6125`, avg `0.007984`, median `0.010691`, mae `0.023202`
- 20d: sample `80`, hit `0.6875`, avg `0.014437`, median `0.016027`, mae `0.04039`
- 60d: sample `80`, hit `0.6375`, avg `0.027209`, median `0.046132`, mae `0.072246`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.00456`, median `0.005458`, mae `0.013575`
- 5d: sample `80`, hit `0.6375`, avg `0.005037`, median `0.005327`, mae `0.017474`
- 10d: sample `80`, hit `0.6125`, avg `0.007984`, median `0.010691`, mae `0.023202`
- 20d: sample `80`, hit `0.6875`, avg `0.014437`, median `0.016027`, mae `0.04039`
- 60d: sample `80`, hit `0.6375`, avg `0.027209`, median `0.046132`, mae `0.072246`

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
