# High Confidence Edge Report

Generated at: `2026-08-14T23:10:36.065844+00:00`

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
- 3d: sample `40`, hit `0.55`, avg `0.002163`, median `0.002887`, mae `0.013039`
- 5d: sample `40`, hit `0.55`, avg `0.000621`, median `0.003209`, mae `0.015837`
- 10d: sample `40`, hit `0.625`, avg `0.006408`, median `0.00903`, mae `0.021902`
- 20d: sample `40`, hit `0.675`, avg `0.012552`, median `0.024743`, mae `0.044146`
- 60d: sample `40`, hit `0.575`, avg `0.021288`, median `0.045044`, mae `0.0862`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.002829`, median `0.002997`, mae `0.011524`
- 5d: sample `40`, hit `0.625`, avg `0.001797`, median `0.002694`, mae `0.01432`
- 10d: sample `40`, hit `0.5`, avg `0.003219`, median `0.007467`, mae `0.025077`
- 20d: sample `40`, hit `0.6`, avg `0.005894`, median `0.013156`, mae `0.043237`
- 60d: sample `40`, hit `0.6`, avg `0.016682`, median `0.018072`, mae `0.057245`

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
- 3d: sample `8`, hit `0.625`, avg `-0.001413`, median `0.009229`, mae `0.015951`
- 5d: sample `8`, hit `0.625`, avg `0.002386`, median `0.005319`, mae `0.010272`
- 10d: sample `8`, hit `0.75`, avg `0.004849`, median `0.011426`, mae `0.017507`
- 20d: sample `8`, hit `0.625`, avg `0.003606`, median `0.022652`, mae `0.033172`
- 60d: sample `8`, hit `0.5`, avg `0.017202`, median `0.030553`, mae `0.05422`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.001413`, median `0.009229`, mae `0.015951`
- 5d: sample `8`, hit `0.625`, avg `0.002386`, median `0.005319`, mae `0.010272`
- 10d: sample `8`, hit `0.75`, avg `0.004849`, median `0.011426`, mae `0.017507`
- 20d: sample `8`, hit `0.625`, avg `0.003606`, median `0.022652`, mae `0.033172`
- 60d: sample `8`, hit `0.5`, avg `0.017202`, median `0.030553`, mae `0.05422`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.002163, 'median_return': 0.002887, 'mean_absolute_return': 0.013039, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.000621, 'median_return': 0.003209, 'mean_absolute_return': 0.015837, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.006408, 'median_return': 0.00903, 'mean_absolute_return': 0.021902, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.012552, 'median_return': 0.024743, 'mean_absolute_return': 0.044146, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.021288, 'median_return': 0.045044, 'mean_absolute_return': 0.0862, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.002829, 'median_return': 0.002997, 'mean_absolute_return': 0.011524, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.001797, 'median_return': 0.002694, 'mean_absolute_return': 0.01432, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.003219, 'median_return': 0.007467, 'mean_absolute_return': 0.025077, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.005894, 'median_return': 0.013156, 'mean_absolute_return': 0.043237, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.016682, 'median_return': 0.018072, 'mean_absolute_return': 0.057245, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.171512}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.001413, 'median_return': 0.009229, 'mean_absolute_return': 0.015951, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.002386, 'median_return': 0.005319, 'mean_absolute_return': 0.010272, 'max_adverse_excursion': -0.018503, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.004849, 'median_return': 0.011426, 'mean_absolute_return': 0.017507, 'max_adverse_excursion': -0.033507, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003606, 'median_return': 0.022652, 'mean_absolute_return': 0.033172, 'max_adverse_excursion': -0.095545, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.017202, 'median_return': 0.030553, 'mean_absolute_return': 0.05422, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002931, 'median_return': 0.002887, 'mean_absolute_return': 0.011874, 'max_adverse_excursion': -0.045596, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.001078, 'median_return': 0.002694, 'mean_absolute_return': 0.015612, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.00481, 'median_return': 0.007467, 'mean_absolute_return': 0.024154, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.009847, 'median_return': 0.016027, 'mean_absolute_return': 0.04486, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.019183, 'median_return': 0.02999, 'mean_absolute_return': 0.073667, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.575}, '5d': {'sample_size': 80, 'hit_rate': 0.5875}, '10d': {'sample_size': 80, 'hit_rate': 0.5625}, '20d': {'sample_size': 80, 'hit_rate': 0.6375}, '60d': {'sample_size': 80, 'hit_rate': 0.5875}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.0, 'both_hit': 46, 'both_miss': 34}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.0, 'both_hit': 45, 'both_miss': 35}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.0, 'both_hit': 51, 'both_miss': 29}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 47, 'both_miss': 33}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.009026, 'median_return': 0.009966, 'mean_absolute_return': 0.01331, 'max_adverse_excursion': -0.013716, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.002715, 'median_return': 0.001654, 'mean_absolute_return': 0.016819, 'max_adverse_excursion': -0.034174, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.007718, 'median_return': 0.01246, 'mean_absolute_return': 0.033349, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.015628, 'median_return': 0.016027, 'mean_absolute_return': 0.058795, 'max_adverse_excursion': -0.144666, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.033762, 'median_return': 0.026139, 'mean_absolute_return': 0.06395, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.171512}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.00032, 'median_return': 0.000603, 'mean_absolute_return': 0.011938, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 60, 'hit_rate': 0.6, 'avg_return': 0.000707, 'median_return': 0.003209, 'mean_absolute_return': 0.014498, 'max_adverse_excursion': -0.040484, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.003846, 'median_return': 0.004187, 'mean_absolute_return': 0.020203, 'max_adverse_excursion': -0.059371, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.007088, 'median_return': 0.019193, 'mean_absolute_return': 0.038657, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.014059, 'median_return': 0.030786, 'mean_absolute_return': 0.074313, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001689`, median `0.000201`, mae `0.01265`
- 5d: sample `40`, hit `0.6`, avg `0.001572`, median `0.004014`, mae `0.014237`
- 10d: sample `40`, hit `0.55`, avg `0.001533`, median `0.004187`, mae `0.019921`
- 20d: sample `40`, hit `0.675`, avg `0.004453`, median `0.013178`, mae `0.034264`
- 60d: sample `40`, hit `0.475`, avg `0.005486`, median `-0.003049`, mae `0.059842`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.009026`, median `0.009966`, mae `0.01331`
- 5d: sample `20`, hit `0.55`, avg `0.002715`, median `0.001654`, mae `0.016819`
- 10d: sample `20`, hit `0.55`, avg `0.007718`, median `0.01246`, mae `0.033349`
- 20d: sample `20`, hit `0.6`, avg `0.015628`, median `0.016027`, mae `0.058795`
- 60d: sample `20`, hit `0.75`, avg `0.033762`, median `0.026139`, mae `0.06395`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001689`, median `0.000201`, mae `0.01265`
- 5d: sample `40`, hit `0.6`, avg `0.001572`, median `0.004014`, mae `0.014237`
- 10d: sample `40`, hit `0.55`, avg `0.001533`, median `0.004187`, mae `0.019921`
- 20d: sample `40`, hit `0.675`, avg `0.004453`, median `0.013178`, mae `0.034264`
- 60d: sample `40`, hit `0.475`, avg `0.005486`, median `-0.003049`, mae `0.059842`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.009026`, median `0.009966`, mae `0.01331`
- 5d: sample `20`, hit `0.55`, avg `0.002715`, median `0.001654`, mae `0.016819`
- 10d: sample `20`, hit `0.55`, avg `0.007718`, median `0.01246`, mae `0.033349`
- 20d: sample `20`, hit `0.6`, avg `0.015628`, median `0.016027`, mae `0.058795`
- 60d: sample `20`, hit `0.75`, avg `0.033762`, median `0.026139`, mae `0.06395`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `-0.001689`, median `0.000201`, mae `0.01265`
- 5d: sample `40`, hit `0.6`, avg `0.001572`, median `0.004014`, mae `0.014237`
- 10d: sample `40`, hit `0.55`, avg `0.001533`, median `0.004187`, mae `0.019921`
- 20d: sample `40`, hit `0.675`, avg `0.004453`, median `0.013178`, mae `0.034264`
- 60d: sample `40`, hit `0.475`, avg `0.005486`, median `-0.003049`, mae `0.059842`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.006681`, median `0.005642`, mae `0.011913`
- 5d: sample `40`, hit `0.575`, avg `0.000846`, median `0.003197`, mae `0.01592`
- 10d: sample `40`, hit `0.575`, avg `0.008094`, median `0.011168`, mae `0.027059`
- 20d: sample `40`, hit `0.6`, avg `0.013992`, median `0.023384`, mae `0.053118`
- 60d: sample `40`, hit `0.7`, avg `0.032484`, median `0.031273`, mae `0.083604`

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
- 3d: sample `20`, hit `0.55`, avg `-0.003367`, median `0.000201`, mae `0.009738`
- 5d: sample `20`, hit `0.7`, avg `0.000878`, median `0.005084`, mae `0.011821`
- 10d: sample `20`, hit `0.45`, avg `-0.001279`, median `-0.000214`, mae `0.016805`
- 20d: sample `20`, hit `0.6`, avg `-0.00384`, median `0.012291`, mae `0.02768`
- 60d: sample `20`, hit `0.45`, avg `-0.000398`, median `-0.003049`, mae `0.050539`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-1.1e-05`, median `0.001448`, mae `0.015562`
- 5d: sample `20`, hit `0.5`, avg `0.002265`, median `0.004014`, mae `0.016652`
- 10d: sample `20`, hit `0.65`, avg `0.004346`, median `0.010691`, mae `0.023037`
- 20d: sample `20`, hit `0.75`, avg `0.012746`, median `0.024743`, mae `0.040849`
- 60d: sample `20`, hit `0.5`, avg `0.01137`, median `0.030553`, mae `0.069144`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.009026`, median `0.009966`, mae `0.01331`
- 5d: sample `20`, hit `0.55`, avg `0.002715`, median `0.001654`, mae `0.016819`
- 10d: sample `20`, hit `0.55`, avg `0.007718`, median `0.01246`, mae `0.033349`
- 20d: sample `20`, hit `0.6`, avg `0.015628`, median `0.016027`, mae `0.058795`
- 60d: sample `20`, hit `0.75`, avg `0.033762`, median `0.026139`, mae `0.06395`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.003367`, median `0.000201`, mae `0.009738`
- 5d: sample `20`, hit `0.7`, avg `0.000878`, median `0.005084`, mae `0.011821`
- 10d: sample `20`, hit `0.45`, avg `-0.001279`, median `-0.000214`, mae `0.016805`
- 20d: sample `20`, hit `0.6`, avg `-0.00384`, median `0.012291`, mae `0.02768`
- 60d: sample `20`, hit `0.45`, avg `-0.000398`, median `-0.003049`, mae `0.050539`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.009026`, median `0.009966`, mae `0.01331`
- 5d: sample `20`, hit `0.55`, avg `0.002715`, median `0.001654`, mae `0.016819`
- 10d: sample `20`, hit `0.55`, avg `0.007718`, median `0.01246`, mae `0.033349`
- 20d: sample `20`, hit `0.6`, avg `0.015628`, median `0.016027`, mae `0.058795`
- 60d: sample `20`, hit `0.75`, avg `0.033762`, median `0.026139`, mae `0.06395`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.002496`, median `0.002887`, mae `0.012281`
- 5d: sample `80`, hit `0.5875`, avg `0.001209`, median `0.003197`, mae `0.015078`
- 10d: sample `80`, hit `0.5625`, avg `0.004814`, median `0.007467`, mae `0.02349`
- 20d: sample `80`, hit `0.6375`, avg `0.009223`, median `0.016027`, mae `0.043691`
- 60d: sample `80`, hit `0.5875`, avg `0.018985`, median `0.02999`, mae `0.071723`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.002496`, median `0.002887`, mae `0.012281`
- 5d: sample `80`, hit `0.5875`, avg `0.001209`, median `0.003197`, mae `0.015078`
- 10d: sample `80`, hit `0.5625`, avg `0.004814`, median `0.007467`, mae `0.02349`
- 20d: sample `80`, hit `0.6375`, avg `0.009223`, median `0.016027`, mae `0.043691`
- 60d: sample `80`, hit `0.5875`, avg `0.018985`, median `0.02999`, mae `0.071723`

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
