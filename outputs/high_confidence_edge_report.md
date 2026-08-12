# High Confidence Edge Report

Generated at: `2026-08-12T13:50:02.999121+00:00`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.003858`, median `0.006565`, mae `0.014705`
- 5d: sample `40`, hit `0.625`, avg `0.005176`, median `0.005319`, mae `0.01517`
- 10d: sample `40`, hit `0.6`, avg `0.005529`, median `0.00903`, mae `0.024971`
- 20d: sample `40`, hit `0.7`, avg `0.010064`, median `0.021844`, mae `0.044108`
- 60d: sample `40`, hit `0.65`, avg `0.027204`, median `0.052998`, mae `0.082299`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008567`, median `0.010849`, mae `0.015282`
- 5d: sample `20`, hit `0.65`, avg `0.006005`, median `0.010281`, mae `0.021769`
- 10d: sample `20`, hit `0.6`, avg `0.011234`, median `0.01246`, mae `0.031921`
- 20d: sample `20`, hit `0.65`, avg `0.018705`, median `0.015261`, mae `0.053719`
- 60d: sample `20`, hit `0.65`, avg `0.036803`, median `0.02283`, mae `0.076003`

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
- 3d: sample `6`, hit `0.6667`, avg `0.000538`, median `0.009229`, mae `0.014727`
- 5d: sample `6`, hit `0.6667`, avg `0.001449`, median `0.010241`, mae `0.013655`
- 10d: sample `6`, hit `0.6667`, avg `0.006454`, median `0.021953`, mae `0.018149`
- 20d: sample `6`, hit `0.6667`, avg `0.019467`, median `0.024743`, mae `0.027039`
- 60d: sample `6`, hit `0.5`, avg `0.017417`, median `0.046132`, mae `0.055589`

### confidence_score top 10%
- sample_size: `6`
- 3d: sample `6`, hit `0.6667`, avg `0.000538`, median `0.009229`, mae `0.014727`
- 5d: sample `6`, hit `0.6667`, avg `0.001449`, median `0.010241`, mae `0.013655`
- 10d: sample `6`, hit `0.6667`, avg `0.006454`, median `0.021953`, mae `0.018149`
- 20d: sample `6`, hit `0.6667`, avg `0.019467`, median `0.024743`, mae `0.027039`
- 60d: sample `6`, hit `0.5`, avg `0.017417`, median `0.046132`, mae `0.055589`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.003858, 'median_return': 0.006565, 'mean_absolute_return': 0.014705, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.005176, 'median_return': 0.005319, 'mean_absolute_return': 0.01517, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.005529, 'median_return': 0.00903, 'mean_absolute_return': 0.024971, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.010064, 'median_return': 0.021844, 'mean_absolute_return': 0.044108, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.027204, 'median_return': 0.052998, 'mean_absolute_return': 0.082299, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008567, 'median_return': 0.010849, 'mean_absolute_return': 0.015282, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006005, 'median_return': 0.010281, 'mean_absolute_return': 0.021769, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.011234, 'median_return': 0.01246, 'mean_absolute_return': 0.031921, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.018705, 'median_return': 0.015261, 'mean_absolute_return': 0.053719, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.036803, 'median_return': 0.02283, 'mean_absolute_return': 0.076003, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 6, 'by_horizon': {'3d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.000538, 'median_return': 0.009229, 'mean_absolute_return': 0.014727, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.001449, 'median_return': 0.010241, 'mean_absolute_return': 0.013655, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.006454, 'median_return': 0.021953, 'mean_absolute_return': 0.018149, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 6, 'hit_rate': 0.6667, 'avg_return': 0.019467, 'median_return': 0.024743, 'mean_absolute_return': 0.027039, 'max_adverse_excursion': -0.015135, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 6, 'hit_rate': 0.5, 'avg_return': 0.017417, 'median_return': 0.046132, 'mean_absolute_return': 0.055589, 'max_adverse_excursion': -0.045404, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 54, 'by_horizon': {'3d': {'sample_size': 54, 'hit_rate': 0.6667, 'avg_return': 0.005971, 'median_return': 0.009585, 'mean_absolute_return': 0.014916, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 54, 'hit_rate': 0.6296, 'avg_return': 0.005897, 'median_return': 0.005327, 'mean_absolute_return': 0.017783, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 54, 'hit_rate': 0.5926, 'avg_return': 0.00754, 'median_return': 0.010691, 'mean_absolute_return': 0.028303, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 54, 'hit_rate': 0.6852, 'avg_return': 0.01222, 'median_return': 0.015661, 'mean_absolute_return': 0.049564, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 54, 'hit_rate': 0.6667, 'avg_return': 0.031847, 'median_return': 0.052998, 'mean_absolute_return': 0.082935, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 60, 'hit_rate': 0.6667}, '5d': {'sample_size': 60, 'hit_rate': 0.6333}, '10d': {'sample_size': 60, 'hit_rate': 0.6}, '20d': {'sample_size': 60, 'hit_rate': 0.6833}, '60d': {'sample_size': 60, 'hit_rate': 0.65}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 60, 'primary_hit_rate': 0.6667, 'secondary_hit_rate': 0.6667, 'primary_minus_secondary': 0.0, 'both_hit': 40, 'both_miss': 20}, '5d': {'sample_size': 60, 'primary_hit_rate': 0.6333, 'secondary_hit_rate': 0.6333, 'primary_minus_secondary': 0.0, 'both_hit': 38, 'both_miss': 22}, '10d': {'sample_size': 60, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.0, 'both_hit': 36, 'both_miss': 24}, '20d': {'sample_size': 60, 'primary_hit_rate': 0.6833, 'secondary_hit_rate': 0.6833, 'primary_minus_secondary': 0.0, 'both_hit': 41, 'both_miss': 19}, '60d': {'sample_size': 60, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.65, 'primary_minus_secondary': 0.0, 'both_hit': 39, 'both_miss': 21}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008567, 'median_return': 0.010849, 'mean_absolute_return': 0.015282, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.006005, 'median_return': 0.010281, 'mean_absolute_return': 0.021769, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.011234, 'median_return': 0.01246, 'mean_absolute_return': 0.031921, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.018705, 'median_return': 0.015261, 'mean_absolute_return': 0.053719, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.036803, 'median_return': 0.02283, 'mean_absolute_return': 0.076003, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.003858, 'median_return': 0.006565, 'mean_absolute_return': 0.014705, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.005176, 'median_return': 0.005319, 'mean_absolute_return': 0.01517, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.005529, 'median_return': 0.00903, 'mean_absolute_return': 0.024971, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.063488}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.010064, 'median_return': 0.021844, 'mean_absolute_return': 0.044108, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.107803}, '60d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.027204, 'median_return': 0.052998, 'mean_absolute_return': 0.082299, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.322945}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000364`, median `0.006714`, mae `0.016436`
- 5d: sample `20`, hit `0.6`, avg `0.005321`, median `0.004014`, mae `0.014172`
- 10d: sample `20`, hit `0.65`, avg `0.007504`, median `0.010691`, mae `0.019955`
- 20d: sample `20`, hit `0.8`, avg `0.020502`, median `0.024743`, mae `0.03706`
- 60d: sample `20`, hit `0.55`, avg `0.02044`, median `0.030553`, mae `0.063122`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008567`, median `0.010849`, mae `0.015282`
- 5d: sample `20`, hit `0.65`, avg `0.006005`, median `0.010281`, mae `0.021769`
- 10d: sample `20`, hit `0.6`, avg `0.011234`, median `0.01246`, mae `0.031921`
- 20d: sample `20`, hit `0.65`, avg `0.018705`, median `0.015261`, mae `0.053719`
- 60d: sample `20`, hit `0.65`, avg `0.036803`, median `0.02283`, mae `0.076003`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000364`, median `0.006714`, mae `0.016436`
- 5d: sample `20`, hit `0.6`, avg `0.005321`, median `0.004014`, mae `0.014172`
- 10d: sample `20`, hit `0.65`, avg `0.007504`, median `0.010691`, mae `0.019955`
- 20d: sample `20`, hit `0.8`, avg `0.020502`, median `0.024743`, mae `0.03706`
- 60d: sample `20`, hit `0.55`, avg `0.02044`, median `0.030553`, mae `0.063122`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008567`, median `0.010849`, mae `0.015282`
- 5d: sample `20`, hit `0.65`, avg `0.006005`, median `0.010281`, mae `0.021769`
- 10d: sample `20`, hit `0.6`, avg `0.011234`, median `0.01246`, mae `0.031921`
- 20d: sample `20`, hit `0.65`, avg `0.018705`, median `0.015261`, mae `0.053719`
- 60d: sample `20`, hit `0.65`, avg `0.036803`, median `0.02283`, mae `0.076003`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000364`, median `0.006714`, mae `0.016436`
- 5d: sample `20`, hit `0.6`, avg `0.005321`, median `0.004014`, mae `0.014172`
- 10d: sample `20`, hit `0.65`, avg `0.007504`, median `0.010691`, mae `0.019955`
- 20d: sample `20`, hit `0.8`, avg `0.020502`, median `0.024743`, mae `0.03706`
- 60d: sample `20`, hit `0.55`, avg `0.02044`, median `0.030553`, mae `0.063122`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.725`, avg `0.007959`, median `0.009966`, mae `0.014127`
- 5d: sample `40`, hit `0.65`, avg `0.005518`, median `0.009721`, mae `0.018969`
- 10d: sample `40`, hit `0.575`, avg `0.007394`, median `0.011168`, mae `0.030954`
- 20d: sample `40`, hit `0.625`, avg `0.009166`, median `0.015261`, mae `0.052438`
- 60d: sample `40`, hit `0.7`, avg `0.035386`, median `0.056189`, mae `0.08874`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000364`, median `0.006714`, mae `0.016436`
- 5d: sample `20`, hit `0.6`, avg `0.005321`, median `0.004014`, mae `0.014172`
- 10d: sample `20`, hit `0.65`, avg `0.007504`, median `0.010691`, mae `0.019955`
- 20d: sample `20`, hit `0.8`, avg `0.020502`, median `0.024743`, mae `0.03706`
- 60d: sample `20`, hit `0.55`, avg `0.02044`, median `0.030553`, mae `0.063122`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008567`, median `0.010849`, mae `0.015282`
- 5d: sample `20`, hit `0.65`, avg `0.006005`, median `0.010281`, mae `0.021769`
- 10d: sample `20`, hit `0.6`, avg `0.011234`, median `0.01246`, mae `0.031921`
- 20d: sample `20`, hit `0.65`, avg `0.018705`, median `0.015261`, mae `0.053719`
- 60d: sample `20`, hit `0.65`, avg `0.036803`, median `0.02283`, mae `0.076003`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008567`, median `0.010849`, mae `0.015282`
- 5d: sample `20`, hit `0.65`, avg `0.006005`, median `0.010281`, mae `0.021769`
- 10d: sample `20`, hit `0.6`, avg `0.011234`, median `0.01246`, mae `0.031921`
- 20d: sample `20`, hit `0.65`, avg `0.018705`, median `0.015261`, mae `0.053719`
- 60d: sample `20`, hit `0.65`, avg `0.036803`, median `0.02283`, mae `0.076003`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005427`, median `0.009349`, mae `0.014897`
- 5d: sample `60`, hit `0.6333`, avg `0.005452`, median `0.005327`, mae `0.01737`
- 10d: sample `60`, hit `0.6`, avg `0.007431`, median `0.010691`, mae `0.027287`
- 20d: sample `60`, hit `0.6833`, avg `0.012944`, median `0.01666`, mae `0.047312`
- 60d: sample `60`, hit `0.65`, avg `0.030404`, median `0.046677`, mae `0.0802`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6667`, avg `0.005427`, median `0.009349`, mae `0.014897`
- 5d: sample `60`, hit `0.6333`, avg `0.005452`, median `0.005327`, mae `0.01737`
- 10d: sample `60`, hit `0.6`, avg `0.007431`, median `0.010691`, mae `0.027287`
- 20d: sample `60`, hit `0.6833`, avg `0.012944`, median `0.01666`, mae `0.047312`
- 60d: sample `60`, hit `0.65`, avg `0.030404`, median `0.046677`, mae `0.0802`

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
