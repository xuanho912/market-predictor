# High Confidence Edge Report

Generated at: `2026-08-26T13:20:35.133369+00:00`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.002664`, median `0.006228`, mae `0.016526`
- 5d: sample `60`, hit `0.55`, avg `0.002362`, median `0.003829`, mae `0.020653`
- 10d: sample `60`, hit `0.5667`, avg `0.005656`, median `0.0076`, mae `0.028086`
- 20d: sample `60`, hit `0.6833`, avg `0.008017`, median `0.024844`, mae `0.038705`
- 60d: sample `60`, hit `0.6667`, avg `0.025339`, median `0.029917`, mae `0.063037`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001171`, median `0.000603`, mae `0.009017`
- 5d: sample `20`, hit `0.6`, avg `-0.002599`, median `0.000873`, mae `0.009711`
- 10d: sample `20`, hit `0.25`, avg `-0.01227`, median `-0.014239`, mae `0.022339`
- 20d: sample `20`, hit `0.4`, avg `-0.020576`, median `-0.00751`, mae `0.041371`
- 60d: sample `20`, hit `0.4`, avg `-0.003977`, median `-0.018455`, mae `0.060691`

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
- 3d: sample `8`, hit `0.625`, avg `-0.008017`, median `0.00234`, mae `0.01479`
- 5d: sample `8`, hit `0.5`, avg `-0.008603`, median `0.000415`, mae `0.019962`
- 10d: sample `8`, hit `0.5`, avg `-0.001747`, median `0.0076`, mae `0.021656`
- 20d: sample `8`, hit `0.625`, avg `-0.000917`, median `0.012958`, mae `0.026633`
- 60d: sample `8`, hit `0.5`, avg `0.002785`, median `0.029831`, mae `0.0564`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.008017`, median `0.00234`, mae `0.01479`
- 5d: sample `8`, hit `0.5`, avg `-0.008603`, median `0.000415`, mae `0.019962`
- 10d: sample `8`, hit `0.5`, avg `-0.001747`, median `0.0076`, mae `0.021656`
- 20d: sample `8`, hit `0.625`, avg `-0.000917`, median `0.012958`, mae `0.026633`
- 60d: sample `8`, hit `0.5`, avg `0.002785`, median `0.029831`, mae `0.0564`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.002664, 'median_return': 0.006228, 'mean_absolute_return': 0.016526, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.040299}, '5d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.002362, 'median_return': 0.003829, 'mean_absolute_return': 0.020653, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049196}, '10d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.005656, 'median_return': 0.0076, 'mean_absolute_return': 0.028086, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.008017, 'median_return': 0.024844, 'mean_absolute_return': 0.038705, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 60, 'hit_rate': 0.6667, 'avg_return': 0.025339, 'median_return': 0.029917, 'mean_absolute_return': 0.063037, 'max_adverse_excursion': -0.15362, 'max_favorable_excursion': 0.19145}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.008017, 'median_return': 0.00234, 'mean_absolute_return': 0.01479, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.008603, 'median_return': 0.000415, 'mean_absolute_return': 0.019962, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001747, 'median_return': 0.0076, 'mean_absolute_return': 0.021656, 'max_adverse_excursion': -0.031869, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000917, 'median_return': 0.012958, 'mean_absolute_return': 0.026633, 'max_adverse_excursion': -0.055302, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002785, 'median_return': 0.029831, 'mean_absolute_return': 0.0564, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.002786, 'median_return': 0.003952, 'mean_absolute_return': 0.014633, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.040299}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002202, 'median_return': 0.002786, 'mean_absolute_return': 0.01769, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049196}, '10d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': 0.001499, 'median_return': -0.000629, 'mean_absolute_return': 0.027204, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.001067, 'median_return': 0.018868, 'mean_absolute_return': 0.040787, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.019701, 'median_return': 0.028986, 'mean_absolute_return': 0.063123, 'max_adverse_excursion': -0.15362, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.5125}, '10d': {'sample_size': 80, 'hit_rate': 0.6125}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.65}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5125, 'primary_minus_secondary': 0.075, 'both_hit': 24, 'both_miss': 16}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 20, 'both_miss': 20}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4625, 'primary_minus_secondary': 0.15, 'both_hit': 23, 'both_miss': 17}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.125, 'both_hit': 28, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.65, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.075, 'both_hit': 29, 'both_miss': 11}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.001705, 'median_return': 0.003026, 'mean_absolute_return': 0.014649, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.040299}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.001122, 'median_return': 0.001303, 'mean_absolute_return': 0.017917, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.049196}, '10d': {'sample_size': 80, 'hit_rate': 0.4875, 'avg_return': 0.001174, 'median_return': -0.000629, 'mean_absolute_return': 0.026649, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.6125, 'avg_return': 0.000869, 'median_return': 0.017881, 'mean_absolute_return': 0.039371, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.089282}, '60d': {'sample_size': 80, 'hit_rate': 0.6, 'avg_return': 0.01801, 'median_return': 0.028986, 'mean_absolute_return': 0.06245, 'max_adverse_excursion': -0.15362, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00385`, median `0.001558`, mae `0.013793`
- 5d: sample `20`, hit `0.5`, avg `-0.004014`, median `0.000415`, mae `0.015909`
- 10d: sample `20`, hit `0.6`, avg `0.007073`, median `0.012964`, mae `0.021088`
- 20d: sample `20`, hit `0.7`, avg `0.0152`, median `0.029166`, mae `0.033269`
- 60d: sample `20`, hit `0.65`, avg `0.022341`, median `0.03283`, mae `0.063814`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.002849`, median `0.005581`, mae `0.014651`
- 5d: sample `40`, hit `0.55`, avg `0.000706`, median `0.000873`, mae `0.017095`
- 10d: sample `40`, hit `0.4`, avg `-0.003605`, median `-0.007491`, mae `0.027198`
- 20d: sample `40`, hit `0.55`, avg `-0.005839`, median `0.012337`, mae `0.042122`
- 60d: sample `40`, hit `0.6`, avg `0.024621`, median `0.032982`, mae `0.06818`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00385`, median `0.001558`, mae `0.013793`
- 5d: sample `20`, hit `0.5`, avg `-0.004014`, median `0.000415`, mae `0.015909`
- 10d: sample `20`, hit `0.6`, avg `0.007073`, median `0.012964`, mae `0.021088`
- 20d: sample `20`, hit `0.7`, avg `0.0152`, median `0.029166`, mae `0.033269`
- 60d: sample `20`, hit `0.65`, avg `0.022341`, median `0.03283`, mae `0.063814`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006869`, median `0.010849`, mae `0.020285`
- 5d: sample `20`, hit `0.5`, avg `0.004011`, median `0.007909`, mae `0.024479`
- 10d: sample `20`, hit `0.55`, avg `0.005059`, median `0.001935`, mae `0.032058`
- 20d: sample `20`, hit `0.7`, avg `0.008899`, median `0.028049`, mae `0.042872`
- 60d: sample `20`, hit `0.8`, avg `0.05322`, median `0.053301`, mae `0.075669`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00385`, median `0.001558`, mae `0.013793`
- 5d: sample `20`, hit `0.5`, avg `-0.004014`, median `0.000415`, mae `0.015909`
- 10d: sample `20`, hit `0.6`, avg `0.007073`, median `0.012964`, mae `0.021088`
- 20d: sample `20`, hit `0.7`, avg `0.0152`, median `0.029166`, mae `0.033269`
- 60d: sample `20`, hit `0.65`, avg `0.022341`, median `0.03283`, mae `0.063814`

### breadth_conflicted_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.7`, avg `0.006869`, median `0.010849`, mae `0.020285`
- 5d: sample `20`, hit `0.5`, avg `0.004011`, median `0.007909`, mae `0.024479`
- 10d: sample `20`, hit `0.55`, avg `0.005059`, median `0.001935`, mae `0.032058`
- 20d: sample `20`, hit `0.7`, avg `0.008899`, median `0.028049`, mae `0.042872`
- 60d: sample `20`, hit `0.8`, avg `0.05322`, median `0.053301`, mae `0.075669`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00385`, median `0.001558`, mae `0.013793`
- 5d: sample `20`, hit `0.5`, avg `-0.004014`, median `0.000415`, mae `0.015909`
- 10d: sample `20`, hit `0.6`, avg `0.007073`, median `0.012964`, mae `0.021088`
- 20d: sample `20`, hit `0.7`, avg `0.0152`, median `0.029166`, mae `0.033269`
- 60d: sample `20`, hit `0.65`, avg `0.022341`, median `0.03283`, mae `0.063814`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.005921`, median `0.009204`, mae `0.017893`
- 5d: sample `40`, hit `0.575`, avg `0.00555`, median `0.006838`, mae `0.023025`
- 10d: sample `40`, hit `0.55`, avg `0.004948`, median `0.004304`, mae `0.031584`
- 20d: sample `40`, hit `0.675`, avg `0.004426`, median `0.023289`, mae `0.041422`
- 60d: sample `40`, hit `0.675`, avg `0.026837`, median `0.028986`, mae `0.062649`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.00385`, median `0.001558`, mae `0.013793`
- 5d: sample `20`, hit `0.5`, avg `-0.004014`, median `0.000415`, mae `0.015909`
- 10d: sample `20`, hit `0.6`, avg `0.007073`, median `0.012964`, mae `0.021088`
- 20d: sample `20`, hit `0.7`, avg `0.0152`, median `0.029166`, mae `0.033269`
- 60d: sample `20`, hit `0.65`, avg `0.022341`, median `0.03283`, mae `0.063814`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.001171`, median `0.000603`, mae `0.009017`
- 5d: sample `20`, hit `0.6`, avg `-0.002599`, median `0.000873`, mae `0.009711`
- 10d: sample `20`, hit `0.25`, avg `-0.01227`, median `-0.014239`, mae `0.022339`
- 20d: sample `20`, hit `0.4`, avg `-0.020576`, median `-0.00751`, mae `0.041371`
- 60d: sample `20`, hit `0.4`, avg `-0.003977`, median `-0.018455`, mae `0.060691`

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
- 3d: sample `80`, hit `0.5875`, avg `0.001705`, median `0.003026`, mae `0.014649`
- 5d: sample `80`, hit `0.5625`, avg `0.001122`, median `0.001303`, mae `0.017917`
- 10d: sample `80`, hit `0.4875`, avg `0.001174`, median `-0.000629`, mae `0.026649`
- 20d: sample `80`, hit `0.6125`, avg `0.000869`, median `0.017881`, mae `0.039371`
- 60d: sample `80`, hit `0.6`, avg `0.01801`, median `0.028986`, mae `0.06245`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.002664`, median `0.006228`, mae `0.016526`
- 5d: sample `60`, hit `0.55`, avg `0.002362`, median `0.003829`, mae `0.020653`
- 10d: sample `60`, hit `0.5667`, avg `0.005656`, median `0.0076`, mae `0.028086`
- 20d: sample `60`, hit `0.6833`, avg `0.008017`, median `0.024844`, mae `0.038705`
- 60d: sample `60`, hit `0.6667`, avg `0.025339`, median `0.029917`, mae `0.063037`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.001705`, median `0.003026`, mae `0.014649`
- 5d: sample `80`, hit `0.5625`, avg `0.001122`, median `0.001303`, mae `0.017917`
- 10d: sample `80`, hit `0.4875`, avg `0.001174`, median `-0.000629`, mae `0.026649`
- 20d: sample `80`, hit `0.6125`, avg `0.000869`, median `0.017881`, mae `0.039371`
- 60d: sample `80`, hit `0.6`, avg `0.01801`, median `0.028986`, mae `0.06245`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.002664`, median `0.006228`, mae `0.016526`
- 5d: sample `60`, hit `0.55`, avg `0.002362`, median `0.003829`, mae `0.020653`
- 10d: sample `60`, hit `0.5667`, avg `0.005656`, median `0.0076`, mae `0.028086`
- 20d: sample `60`, hit `0.6833`, avg `0.008017`, median `0.024844`, mae `0.038705`
- 60d: sample `60`, hit `0.6667`, avg `0.025339`, median `0.029917`, mae `0.063037`

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
