# High Confidence Edge Report

Generated at: `2026-10-06T18:25:45.657398+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `80`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `80`, gate `moderate_evidence`
- 5d: completed `80`, gate `moderate_evidence`
- 10d: completed `80`, gate `moderate_evidence`
- 20d: completed `80`, gate `moderate_evidence`
- 60d: completed `80`, gate `moderate_evidence`

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
- 3d: sample `60`, hit `0.3`, avg `-0.010518`, median `-0.009843`, mae `0.018125`
- 5d: sample `60`, hit `0.3667`, avg `-0.014409`, median `-0.009444`, mae `0.02361`
- 10d: sample `60`, hit `0.4167`, avg `-0.010682`, median `-0.011432`, mae `0.03222`
- 20d: sample `60`, hit `0.5667`, avg `-0.003345`, median `0.013156`, mae `0.046344`
- 60d: sample `60`, hit `0.65`, avg `0.012429`, median `0.041902`, mae `0.081822`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.005261`, median `-0.003413`, mae `0.016186`
- 5d: sample `20`, hit `0.4`, avg `-0.010225`, median `-0.013499`, mae `0.022518`
- 10d: sample `20`, hit `0.45`, avg `-0.016454`, median `-0.009882`, mae `0.028381`
- 20d: sample `20`, hit `0.45`, avg `-0.007376`, median `-0.001813`, mae `0.02876`
- 60d: sample `20`, hit `0.75`, avg `0.033348`, median `0.046407`, mae `0.055498`

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
- 3d: sample `8`, hit `0.625`, avg `-0.000663`, median `0.00752`, mae `0.012485`
- 5d: sample `8`, hit `0.625`, avg `0.000394`, median `0.003238`, mae `0.008865`
- 10d: sample `8`, hit `0.625`, avg `0.010591`, median `0.018745`, mae `0.025568`
- 20d: sample `8`, hit `0.875`, avg `0.019356`, median `0.034024`, mae `0.040194`
- 60d: sample `8`, hit `0.875`, avg `0.03672`, median `0.044683`, mae `0.050331`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.25`, avg `-0.018053`, median `-0.012933`, mae `0.023208`
- 5d: sample `8`, hit `0.375`, avg `-0.019869`, median `-0.026253`, mae `0.033488`
- 10d: sample `8`, hit `0.25`, avg `-0.026419`, median `-0.030486`, mae `0.034201`
- 20d: sample `8`, hit `0.375`, avg `-0.040108`, median `-0.010854`, mae `0.058629`
- 60d: sample `8`, hit `0.25`, avg `-0.091117`, median `-0.134617`, mae `0.12761`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3, 'avg_return': -0.010518, 'median_return': -0.009843, 'mean_absolute_return': 0.018125, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.014409, 'median_return': -0.009444, 'mean_absolute_return': 0.02361, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.010682, 'median_return': -0.011432, 'mean_absolute_return': 0.03222, 'max_adverse_excursion': -0.105849, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': -0.003345, 'median_return': 0.013156, 'mean_absolute_return': 0.046344, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.012429, 'median_return': 0.041902, 'mean_absolute_return': 0.081822, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154804}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.018053, 'median_return': -0.012933, 'mean_absolute_return': 0.023208, 'max_adverse_excursion': -0.042693, 'max_favorable_excursion': 0.013727}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.019869, 'median_return': -0.026253, 'mean_absolute_return': 0.033488, 'max_adverse_excursion': -0.065028, 'max_favorable_excursion': 0.026602}, '10d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.026419, 'median_return': -0.030486, 'mean_absolute_return': 0.034201, 'max_adverse_excursion': -0.064399, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.040108, 'median_return': -0.010854, 'mean_absolute_return': 0.058629, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.043456}, '60d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.091117, 'median_return': -0.134617, 'mean_absolute_return': 0.12761, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.099838}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.3333, 'avg_return': -0.00822, 'median_return': -0.004907, 'mean_absolute_return': 0.017022, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 72, 'hit_rate': 0.375, 'avg_return': -0.01264, 'median_return': -0.009659, 'mean_absolute_return': 0.022209, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.010537, 'median_return': -0.00952, 'mean_absolute_return': 0.030933, 'max_adverse_excursion': -0.105849, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.00038, 'median_return': 0.003675, 'mean_absolute_return': 0.040094, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.029745, 'median_return': 0.044367, 'mean_absolute_return': 0.069422, 'max_adverse_excursion': -0.158935, 'max_favorable_excursion': 0.154804}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.475}, '20d': {'sample_size': 80, 'hit_rate': 0.4375}, '60d': {'sample_size': 80, 'hit_rate': 0.325}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.475, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.05, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.125, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.325, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.35, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.3, 'avg_return': -0.010518, 'median_return': -0.009843, 'mean_absolute_return': 0.018125, 'max_adverse_excursion': -0.055386, 'max_favorable_excursion': 0.041771}, '5d': {'sample_size': 60, 'hit_rate': 0.3667, 'avg_return': -0.014409, 'median_return': -0.009444, 'mean_absolute_return': 0.02361, 'max_adverse_excursion': -0.081558, 'max_favorable_excursion': 0.038052}, '10d': {'sample_size': 60, 'hit_rate': 0.4167, 'avg_return': -0.010682, 'median_return': -0.011432, 'mean_absolute_return': 0.03222, 'max_adverse_excursion': -0.105849, 'max_favorable_excursion': 0.066884}, '20d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': -0.003345, 'median_return': 0.013156, 'mean_absolute_return': 0.046344, 'max_adverse_excursion': -0.128948, 'max_favorable_excursion': 0.11977}, '60d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.012429, 'median_return': 0.041902, 'mean_absolute_return': 0.081822, 'max_adverse_excursion': -0.184479, 'max_favorable_excursion': 0.154804}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.005261, 'median_return': -0.003413, 'mean_absolute_return': 0.016186, 'max_adverse_excursion': -0.03466, 'max_favorable_excursion': 0.026049}, '5d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.010225, 'median_return': -0.013499, 'mean_absolute_return': 0.022518, 'max_adverse_excursion': -0.049407, 'max_favorable_excursion': 0.031487}, '10d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.016454, 'median_return': -0.009882, 'mean_absolute_return': 0.028381, 'max_adverse_excursion': -0.081978, 'max_favorable_excursion': 0.035149}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.007376, 'median_return': -0.001813, 'mean_absolute_return': 0.02876, 'max_adverse_excursion': -0.090946, 'max_favorable_excursion': 0.053054}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.033348, 'median_return': 0.046407, 'mean_absolute_return': 0.055498, 'max_adverse_excursion': -0.089779, 'max_favorable_excursion': 0.142584}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.35`, avg `-0.00774`, median `-0.004296`, mae `0.016395`
- 5d: sample `60`, hit `0.3833`, avg `-0.012254`, median `-0.009659`, mae `0.02226`
- 10d: sample `60`, hit `0.4667`, avg `-0.008521`, median `-0.006389`, mae `0.031331`
- 20d: sample `60`, hit `0.5667`, avg `0.002089`, median `0.003675`, mae `0.040607`
- 60d: sample `60`, hit `0.7333`, avg `0.036177`, median `0.044683`, mae `0.069202`

### breadth_confirmed_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000133`, median `0.003898`, mae `0.009427`
- 5d: sample `20`, hit `0.55`, avg `-0.00292`, median `0.001479`, mae `0.011505`
- 10d: sample `20`, hit `0.55`, avg `0.006968`, median `0.011168`, mae `0.020796`
- 20d: sample `20`, hit `0.75`, avg `0.012731`, median `0.025198`, mae `0.031527`
- 60d: sample `20`, hit `0.8`, avg `0.023246`, median `0.041902`, mae `0.045439`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.013594`, median `-0.012933`, mae `0.021377`
- 5d: sample `20`, hit `0.35`, avg `-0.01669`, median `-0.016421`, mae `0.026566`
- 10d: sample `20`, hit `0.3`, avg `-0.022936`, median `-0.01796`, mae `0.031049`
- 20d: sample `20`, hit `0.45`, avg `-0.02368`, median `-0.001666`, mae `0.045972`
- 60d: sample `20`, hit `0.5`, avg `-0.037895`, median `0.025283`, mae `0.093358`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.35`, avg `-0.00774`, median `-0.004296`, mae `0.016395`
- 5d: sample `60`, hit `0.3833`, avg `-0.012254`, median `-0.009659`, mae `0.02226`
- 10d: sample `60`, hit `0.4667`, avg `-0.008521`, median `-0.006389`, mae `0.031331`
- 20d: sample `60`, hit `0.5667`, avg `0.002089`, median `0.003675`, mae `0.040607`
- 60d: sample `60`, hit `0.7333`, avg `0.036177`, median `0.044683`, mae `0.069202`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

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
- 3d: sample `80`, hit `0.325`, avg `-0.009204`, median `-0.007923`, mae `0.017641`
- 5d: sample `80`, hit `0.375`, avg `-0.013363`, median `-0.011684`, mae `0.023337`
- 10d: sample `80`, hit `0.425`, avg `-0.012125`, median `-0.011432`, mae `0.03126`
- 20d: sample `80`, hit `0.5375`, avg `-0.004353`, median `0.002605`, mae `0.041948`
- 60d: sample `80`, hit `0.675`, avg `0.017659`, median `0.041902`, mae `0.075241`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.013594`, median `-0.012933`, mae `0.021377`
- 5d: sample `20`, hit `0.35`, avg `-0.01669`, median `-0.016421`, mae `0.026566`
- 10d: sample `20`, hit `0.3`, avg `-0.022936`, median `-0.01796`, mae `0.031049`
- 20d: sample `20`, hit `0.45`, avg `-0.02368`, median `-0.001666`, mae `0.045972`
- 60d: sample `20`, hit `0.5`, avg `-0.037895`, median `0.025283`, mae `0.093358`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.325`, avg `-0.009204`, median `-0.007923`, mae `0.017641`
- 5d: sample `80`, hit `0.375`, avg `-0.013363`, median `-0.011684`, mae `0.023337`
- 10d: sample `80`, hit `0.425`, avg `-0.012125`, median `-0.011432`, mae `0.03126`
- 20d: sample `80`, hit `0.5375`, avg `-0.004353`, median `0.002605`, mae `0.041948`
- 60d: sample `80`, hit `0.675`, avg `0.017659`, median `0.041902`, mae `0.075241`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.25`, avg `-0.013594`, median `-0.012933`, mae `0.021377`
- 5d: sample `20`, hit `0.35`, avg `-0.01669`, median `-0.016421`, mae `0.026566`
- 10d: sample `20`, hit `0.3`, avg `-0.022936`, median `-0.01796`, mae `0.031049`
- 20d: sample `20`, hit `0.45`, avg `-0.02368`, median `-0.001666`, mae `0.045972`
- 60d: sample `20`, hit `0.5`, avg `-0.037895`, median `0.025283`, mae `0.093358`

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
