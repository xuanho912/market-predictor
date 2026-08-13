# High Confidence Edge Report

Generated at: `2026-08-13T23:54:10.898855+00:00`

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
- 3d: sample `20`, hit `0.65`, avg `0.008247`, median `0.01297`, mae `0.013959`
- 5d: sample `20`, hit `0.65`, avg `0.006714`, median `0.006133`, mae `0.019249`
- 10d: sample `20`, hit `0.6`, avg `0.010223`, median `0.00903`, mae `0.023061`
- 20d: sample `20`, hit `0.6`, avg `0.010053`, median `0.01666`, mae `0.040911`
- 60d: sample `20`, hit `0.75`, avg `0.030985`, median `0.063119`, mae `0.088334`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002944`, median `0.004569`, mae `0.013479`
- 5d: sample `40`, hit `0.675`, avg `0.004355`, median `0.006452`, mae `0.017187`
- 10d: sample `40`, hit `0.575`, avg `0.006356`, median `0.010495`, mae `0.024581`
- 20d: sample `40`, hit `0.675`, avg `0.011432`, median `0.012291`, mae `0.042589`
- 60d: sample `40`, hit `0.625`, avg `0.026895`, median `0.026139`, mae `0.065259`

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
- 3d: sample `6`, hit `1.0`, avg `0.017327`, median `0.014568`, mae `0.017327`
- 5d: sample `6`, hit `0.6667`, avg `0.004391`, median `0.010281`, mae `0.012806`
- 10d: sample `6`, hit `0.5`, avg `-0.005403`, median `0.011168`, mae `0.028631`
- 20d: sample `6`, hit `0.1667`, avg `-0.013283`, median `-0.004856`, mae `0.054984`
- 60d: sample `6`, hit `0.5`, avg `0.02782`, median `0.061844`, mae `0.068152`

### confidence_score top 10%
- sample_size: `6`
- 3d: sample `6`, hit `0.8333`, avg `0.00617`, median `0.004569`, mae `0.006559`
- 5d: sample `6`, hit `0.8333`, avg `0.006058`, median `0.010385`, mae `0.012165`
- 10d: sample `6`, hit `1.0`, avg `0.015476`, median `0.019702`, mae `0.015476`
- 20d: sample `6`, hit `0.6667`, avg `0.00191`, median `0.007988`, mae `0.014178`
- 60d: sample `6`, hit `0.1667`, avg `-0.019851`, median `-0.030864`, mae `0.047514`

### confidence validation
- `{'strong_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.008247, 'median_return': 0.01297, 'mean_absolute_return': 0.013959, 'max_adverse_excursion': -0.013716, 'max_favorable_excursion': 0.030961}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006714, 'median_return': 0.006133, 'mean_absolute_return': 0.019249, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.055415}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.010223, 'median_return': 0.00903, 'mean_absolute_return': 0.023061, 'max_adverse_excursion': -0.031038, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.010053, 'median_return': 0.01666, 'mean_absolute_return': 0.040911, 'max_adverse_excursion': -0.086744, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.030985, 'median_return': 0.063119, 'mean_absolute_return': 0.088334, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.147541}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002944, 'median_return': 0.004569, 'mean_absolute_return': 0.013479, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.004355, 'median_return': 0.006452, 'mean_absolute_return': 0.017187, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.006356, 'median_return': 0.010495, 'mean_absolute_return': 0.024581, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.011432, 'median_return': 0.012291, 'mean_absolute_return': 0.042589, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.026895, 'median_return': 0.026139, 'mean_absolute_return': 0.065259, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.171512}}}, 'confidence_top_10': {'sample_size': 6, 'by_horizon': {'3d': {'sample_size': 6, 'hit_rate': 0.8333, 'avg_return': 0.00617, 'median_return': 0.004569, 'mean_absolute_return': 0.006559, 'max_adverse_excursion': -0.001166, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 6, 'hit_rate': 0.8333, 'avg_return': 0.006058, 'median_return': 0.010385, 'mean_absolute_return': 0.012165, 'max_adverse_excursion': -0.018322, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 6, 'hit_rate': 1.0, 'avg_return': 0.015476, 'median_return': 0.019702, 'mean_absolute_return': 0.015476, 'max_adverse_excursion': 0.007467, 'max_favorable_excursion': 0.020167}, '20d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.00191, 'median_return': 0.007988, 'mean_absolute_return': 0.014178, 'max_adverse_excursion': -0.021537, 'max_favorable_excursion': 0.025541}, '60d': {'sample_size': 6, 'hit_rate': 0.1667, 'avg_return': -0.019851, 'median_return': -0.030864, 'mean_absolute_return': 0.047514, 'max_adverse_excursion': -0.07448, 'max_favorable_excursion': 0.082988}}}, 'ordinary_confidence': {'sample_size': 54, 'by_horizon': {'3d': {'sample_size': 54, 'hit_rate': 0.5741, 'avg_return': 0.00455, 'median_return': 0.00558, 'mean_absolute_return': 0.014426, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 54, 'hit_rate': 0.6481, 'avg_return': 0.00504, 'median_return': 0.005327, 'mean_absolute_return': 0.018509, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 54, 'hit_rate': 0.537, 'avg_return': 0.006775, 'median_return': 0.003491, 'mean_absolute_return': 0.02503, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 54, 'hit_rate': 0.6481, 'avg_return': 0.01198, 'median_return': 0.015261, 'mean_absolute_return': 0.045124, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 54, 'hit_rate': 0.7222, 'avg_return': 0.033604, 'median_return': 0.048421, 'mean_absolute_return': 0.075777, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.171512}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 60, 'hit_rate': 0.6}, '5d': {'sample_size': 60, 'hit_rate': 0.6667}, '10d': {'sample_size': 60, 'hit_rate': 0.5833}, '20d': {'sample_size': 60, 'hit_rate': 0.65}, '60d': {'sample_size': 60, 'hit_rate': 0.6667}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 60, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 36, 'both_miss': 24}, '5d': {'sample_size': 60, 'primary_hit_rate': 0.6667, 'secondary_hit_rate': 0.6667, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 20}, '10d': {'sample_size': 60, 'primary_hit_rate': 0.5833, 'secondary_hit_rate': 0.5833, 'primary_minus_secondary': 0.0, 'both_hit': 35, 'both_miss': 25}, '20d': {'sample_size': 60, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 21}, '60d': {'sample_size': 60, 'primary_hit_rate': 0.6667, 'secondary_hit_rate': 0.6667, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 20}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.00827, 'median_return': 0.010849, 'mean_absolute_return': 0.015216, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.004401, 'median_return': 0.005327, 'mean_absolute_return': 0.020544, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.008783, 'median_return': 0.00903, 'mean_absolute_return': 0.028865, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.01366, 'median_return': 0.014007, 'mean_absolute_return': 0.050672, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.041734, 'median_return': 0.063119, 'mean_absolute_return': 0.082859, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.171512}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.002404, 'median_return': 0.000145, 'mean_absolute_return': 0.010485, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.017982}, '5d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.006623, 'median_return': 0.007324, 'mean_absolute_return': 0.012536, 'max_adverse_excursion': -0.024669, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.00537, 'median_return': 0.010495, 'mean_absolute_return': 0.014492, 'max_adverse_excursion': -0.025012, 'max_favorable_excursion': 0.027042}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.005599, 'median_return': 0.013178, 'mean_absolute_return': 0.024745, 'max_adverse_excursion': -0.080367, 'max_favorable_excursion': 0.035222}, '60d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': 0.001306, 'median_return': -0.01711, 'mean_absolute_return': 0.053134, 'max_adverse_excursion': -0.088185, 'max_favorable_excursion': 0.096597}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002922`, median `0.004004`, mae `0.012222`
- 5d: sample `40`, hit `0.725`, avg `0.006668`, median `0.006452`, mae `0.015893`
- 10d: sample `40`, hit `0.6`, avg `0.007797`, median `0.00903`, mae `0.018776`
- 20d: sample `40`, hit `0.675`, avg `0.007826`, median `0.014007`, mae `0.032828`
- 60d: sample `40`, hit `0.6`, avg `0.016145`, median `0.04459`, mae `0.070734`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002922`, median `0.004004`, mae `0.012222`
- 5d: sample `40`, hit `0.725`, avg `0.006668`, median `0.006452`, mae `0.015893`
- 10d: sample `40`, hit `0.6`, avg `0.007797`, median `0.00903`, mae `0.018776`
- 20d: sample `40`, hit `0.675`, avg `0.007826`, median `0.014007`, mae `0.032828`
- 60d: sample `40`, hit `0.6`, avg `0.016145`, median `0.04459`, mae `0.070734`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002922`, median `0.004004`, mae `0.012222`
- 5d: sample `40`, hit `0.725`, avg `0.006668`, median `0.006452`, mae `0.015893`
- 10d: sample `40`, hit `0.6`, avg `0.007797`, median `0.00903`, mae `0.018776`
- 20d: sample `40`, hit `0.675`, avg `0.007826`, median `0.014007`, mae `0.032828`
- 60d: sample `40`, hit `0.6`, avg `0.016145`, median `0.04459`, mae `0.070734`

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
- 3d: sample `20`, hit `0.5`, avg `-0.002404`, median `0.000145`, mae `0.010485`
- 5d: sample `20`, hit `0.8`, avg `0.006623`, median `0.007324`, mae `0.012536`
- 10d: sample `20`, hit `0.6`, avg `0.00537`, median `0.010495`, mae `0.014492`
- 20d: sample `20`, hit `0.75`, avg `0.005599`, median `0.013178`, mae `0.024745`
- 60d: sample `20`, hit `0.45`, avg `0.001306`, median `-0.01711`, mae `0.053134`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008247`, median `0.01297`, mae `0.013959`
- 5d: sample `20`, hit `0.65`, avg `0.006714`, median `0.006133`, mae `0.019249`
- 10d: sample `20`, hit `0.6`, avg `0.010223`, median `0.00903`, mae `0.023061`
- 20d: sample `20`, hit `0.6`, avg `0.010053`, median `0.01666`, mae `0.040911`
- 60d: sample `20`, hit `0.75`, avg `0.030985`, median `0.063119`, mae `0.088334`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.008292`, median `0.010849`, mae `0.016473`
- 5d: sample `20`, hit `0.55`, avg `0.002088`, median `0.001654`, mae `0.021838`
- 10d: sample `20`, hit `0.55`, avg `0.007342`, median `0.011168`, mae `0.03467`
- 20d: sample `20`, hit `0.6`, avg `0.017266`, median `0.010824`, mae `0.060433`
- 60d: sample `20`, hit `0.8`, avg `0.052484`, median `0.065495`, mae `0.077384`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002404`, median `0.000145`, mae `0.010485`
- 5d: sample `20`, hit `0.8`, avg `0.006623`, median `0.007324`, mae `0.012536`
- 10d: sample `20`, hit `0.6`, avg `0.00537`, median `0.010495`, mae `0.014492`
- 20d: sample `20`, hit `0.75`, avg `0.005599`, median `0.013178`, mae `0.024745`
- 60d: sample `20`, hit `0.45`, avg `0.001306`, median `-0.01711`, mae `0.053134`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004712`, median `0.005458`, mae `0.013639`
- 5d: sample `60`, hit `0.6667`, avg `0.005142`, median `0.006133`, mae `0.017875`
- 10d: sample `60`, hit `0.5833`, avg `0.007645`, median `0.00903`, mae `0.024074`
- 20d: sample `60`, hit `0.65`, avg `0.010973`, median `0.013178`, mae `0.04203`
- 60d: sample `60`, hit `0.6667`, avg `0.028258`, median `0.045044`, mae `0.072951`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6`, avg `0.004712`, median `0.005458`, mae `0.013639`
- 5d: sample `60`, hit `0.6667`, avg `0.005142`, median `0.006133`, mae `0.017875`
- 10d: sample `60`, hit `0.5833`, avg `0.007645`, median `0.00903`, mae `0.024074`
- 20d: sample `60`, hit `0.65`, avg `0.010973`, median `0.013178`, mae `0.04203`
- 60d: sample `60`, hit `0.6667`, avg `0.028258`, median `0.045044`, mae `0.072951`

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
