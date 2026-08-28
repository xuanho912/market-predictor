# High Confidence Edge Report

Generated at: `2026-08-28T15:41:45.819501+00:00`

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
- 3d: sample `80`, hit `0.5`, avg `-0.002025`, median `0.000603`, mae `0.015652`
- 5d: sample `80`, hit `0.5125`, avg `-0.002038`, median `0.000548`, mae `0.019724`
- 10d: sample `80`, hit `0.5125`, avg `0.003322`, median `0.001935`, mae `0.025959`
- 20d: sample `80`, hit `0.675`, avg `0.009759`, median `0.015261`, mae `0.033954`
- 60d: sample `80`, hit `0.675`, avg `0.033174`, median `0.039879`, mae `0.06468`

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
- 3d: sample `8`, hit `0.5`, avg `-0.004471`, median `0.001558`, mae `0.010659`
- 5d: sample `8`, hit `0.25`, avg `-0.006804`, median `-0.012956`, mae `0.017102`
- 10d: sample `8`, hit `0.75`, avg `0.011181`, median `0.020918`, mae `0.019952`
- 20d: sample `8`, hit `0.875`, avg `0.022572`, median `0.029166`, mae `0.024468`
- 60d: sample `8`, hit `0.625`, avg `0.034462`, median `0.046132`, mae `0.056772`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004471`, median `0.001558`, mae `0.010659`
- 5d: sample `8`, hit `0.25`, avg `-0.006804`, median `-0.012956`, mae `0.017102`
- 10d: sample `8`, hit `0.75`, avg `0.011181`, median `0.020918`, mae `0.019952`
- 20d: sample `8`, hit `0.875`, avg `0.022572`, median `0.029166`, mae `0.024468`
- 60d: sample `8`, hit `0.625`, avg `0.034462`, median `0.046132`, mae `0.056772`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.002025, 'median_return': 0.000603, 'mean_absolute_return': 0.015652, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.002038, 'median_return': 0.000548, 'mean_absolute_return': 0.019724, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.003322, 'median_return': 0.001935, 'mean_absolute_return': 0.025959, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.009759, 'median_return': 0.015261, 'mean_absolute_return': 0.033954, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.033174, 'median_return': 0.039879, 'mean_absolute_return': 0.06468, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004471, 'median_return': 0.001558, 'mean_absolute_return': 0.010659, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.006804, 'median_return': -0.012956, 'mean_absolute_return': 0.017102, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.011181, 'median_return': 0.020918, 'mean_absolute_return': 0.019952, 'max_adverse_excursion': -0.01796, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.022572, 'median_return': 0.029166, 'mean_absolute_return': 0.024468, 'max_adverse_excursion': -0.007581, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.034462, 'median_return': 0.046132, 'mean_absolute_return': 0.056772, 'max_adverse_excursion': -0.038302, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.001753, 'median_return': 0.000603, 'mean_absolute_return': 0.016206, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': -0.001508, 'median_return': 0.000873, 'mean_absolute_return': 0.020015, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.002449, 'median_return': -0.001932, 'mean_absolute_return': 0.026627, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.008335, 'median_return': 0.013877, 'mean_absolute_return': 0.035008, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.03303, 'median_return': 0.039879, 'mean_absolute_return': 0.065559, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.675}, '60d': {'sample_size': 80, 'hit_rate': 0.675}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.05, 'both_hit': 32, 'both_miss': 28}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 32, 'both_miss': 28}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.1, 'both_hit': 35, 'both_miss': 25}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.05, 'both_hit': 42, 'both_miss': 18}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': 0.075, 'both_hit': 41, 'both_miss': 19}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5, 'avg_return': -0.002025, 'median_return': 0.000603, 'mean_absolute_return': 0.015652, 'max_adverse_excursion': -0.062191, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.002038, 'median_return': 0.000548, 'mean_absolute_return': 0.019724, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.003322, 'median_return': 0.001935, 'mean_absolute_return': 0.025959, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.009759, 'median_return': 0.015261, 'mean_absolute_return': 0.033954, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.033174, 'median_return': 0.039879, 'mean_absolute_return': 0.06468, 'max_adverse_excursion': -0.129489, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.00045`, median `0.000766`, mae `0.014403`
- 5d: sample `60`, hit `0.5167`, avg `-0.001867`, median `0.000688`, mae `0.018984`
- 10d: sample `60`, hit `0.55`, avg `0.006068`, median `0.009031`, mae `0.025485`
- 20d: sample `60`, hit `0.7`, avg `0.012329`, median `0.018139`, mae `0.033649`
- 60d: sample `60`, hit `0.7`, avg `0.042263`, median `0.059495`, mae `0.070939`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5167`, avg `-0.00045`, median `0.000766`, mae `0.014403`
- 5d: sample `60`, hit `0.5167`, avg `-0.001867`, median `0.000688`, mae `0.018984`
- 10d: sample `60`, hit `0.55`, avg `0.006068`, median `0.009031`, mae `0.025485`
- 20d: sample `60`, hit `0.7`, avg `0.012329`, median `0.018139`, mae `0.033649`
- 60d: sample `60`, hit `0.7`, avg `0.042263`, median `0.059495`, mae `0.070939`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.0032`, median `0.001448`, mae `0.014371`
- 5d: sample `20`, hit `0.45`, avg `-0.004924`, median `-0.004438`, mae `0.017247`
- 10d: sample `20`, hit `0.6`, avg `0.008693`, median `0.019233`, mae `0.022148`
- 20d: sample `20`, hit `0.7`, avg `0.015368`, median `0.026531`, mae `0.03172`
- 60d: sample `20`, hit `0.6`, avg `0.028324`, median `0.059495`, mae `0.070227`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002025`, median `0.000603`, mae `0.015652`
- 5d: sample `80`, hit `0.5125`, avg `-0.002038`, median `0.000548`, mae `0.019724`
- 10d: sample `80`, hit `0.5125`, avg `0.003322`, median `0.001935`, mae `0.025959`
- 20d: sample `80`, hit `0.675`, avg `0.009759`, median `0.015261`, mae `0.033954`
- 60d: sample `80`, hit `0.675`, avg `0.033174`, median `0.039879`, mae `0.06468`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### surface_only_strength
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002025`, median `0.000603`, mae `0.015652`
- 5d: sample `80`, hit `0.5125`, avg `-0.002038`, median `0.000548`, mae `0.019724`
- 10d: sample `80`, hit `0.5125`, avg `0.003322`, median `0.001935`, mae `0.025959`
- 20d: sample `80`, hit `0.675`, avg `0.009759`, median `0.015261`, mae `0.033954`
- 60d: sample `80`, hit `0.675`, avg `0.033174`, median `0.039879`, mae `0.06468`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002025`, median `0.000603`, mae `0.015652`
- 5d: sample `80`, hit `0.5125`, avg `-0.002038`, median `0.000548`, mae `0.019724`
- 10d: sample `80`, hit `0.5125`, avg `0.003322`, median `0.001935`, mae `0.025959`
- 20d: sample `80`, hit `0.675`, avg `0.009759`, median `0.015261`, mae `0.033954`
- 60d: sample `80`, hit `0.675`, avg `0.033174`, median `0.039879`, mae `0.06468`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002025`, median `0.000603`, mae `0.015652`
- 5d: sample `80`, hit `0.5125`, avg `-0.002038`, median `0.000548`, mae `0.019724`
- 10d: sample `80`, hit `0.5125`, avg `0.003322`, median `0.001935`, mae `0.025959`
- 20d: sample `80`, hit `0.675`, avg `0.009759`, median `0.015261`, mae `0.033954`
- 60d: sample `80`, hit `0.675`, avg `0.033174`, median `0.039879`, mae `0.06468`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002025`, median `0.000603`, mae `0.015652`
- 5d: sample `80`, hit `0.5125`, avg `-0.002038`, median `0.000548`, mae `0.019724`
- 10d: sample `80`, hit `0.5125`, avg `0.003322`, median `0.001935`, mae `0.025959`
- 20d: sample `80`, hit `0.675`, avg `0.009759`, median `0.015261`, mae `0.033954`
- 60d: sample `80`, hit `0.675`, avg `0.033174`, median `0.039879`, mae `0.06468`

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
