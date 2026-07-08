# High Confidence Edge Report

Generated at: `2026-07-08T14:43:43.188804+00:00`

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
- 3d: sample `60`, hit `0.5333`, avg `-0.001052`, median `0.001558`, mae `0.015835`
- 5d: sample `60`, hit `0.45`, avg `-0.003113`, median `-0.001324`, mae `0.019707`
- 10d: sample `60`, hit `0.5`, avg `0.001792`, median `0.000242`, mae `0.020927`
- 20d: sample `60`, hit `0.8`, avg `0.017502`, median `0.021759`, mae `0.031184`
- 60d: sample `60`, hit `0.6333`, avg `0.028911`, median `0.046132`, mae `0.066611`

### MODERATE_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.004469`, median `-0.002654`, mae `0.008423`
- 5d: sample `20`, hit `0.6`, avg `-0.002489`, median `0.001303`, mae `0.01107`
- 10d: sample `20`, hit `0.3`, avg `-0.009484`, median `-0.010413`, mae `0.016723`
- 20d: sample `20`, hit `0.5`, avg `-0.00884`, median `0.001555`, mae `0.028986`
- 60d: sample `20`, hit `0.35`, avg `-0.019681`, median `-0.020815`, mae `0.055269`

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
- 3d: sample `8`, hit `0.5`, avg `-0.006276`, median `0.001558`, mae `0.012553`
- 5d: sample `8`, hit `0.375`, avg `-0.010574`, median `-0.013034`, mae `0.016744`
- 10d: sample `8`, hit `0.375`, avg `-0.001552`, median `-0.0004`, mae `0.017234`
- 20d: sample `8`, hit `1.0`, avg `0.038788`, median `0.043456`, mae `0.038788`
- 60d: sample `8`, hit `1.0`, avg `0.090405`, median `0.101282`, mae `0.090405`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.006276`, median `0.001558`, mae `0.012553`
- 5d: sample `8`, hit `0.375`, avg `-0.010574`, median `-0.013034`, mae `0.016744`
- 10d: sample `8`, hit `0.375`, avg `-0.001552`, median `-0.0004`, mae `0.017234`
- 20d: sample `8`, hit `1.0`, avg `0.038788`, median `0.043456`, mae `0.038788`
- 60d: sample `8`, hit `1.0`, avg `0.090405`, median `0.101282`, mae `0.090405`

### confidence validation
- `{'strong_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': -0.001052, 'median_return': 0.001558, 'mean_absolute_return': 0.015835, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 60, 'hit_rate': 0.45, 'avg_return': -0.003113, 'median_return': -0.001324, 'mean_absolute_return': 0.019707, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.001792, 'median_return': 0.000242, 'mean_absolute_return': 0.020927, 'max_adverse_excursion': -0.047759, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 60, 'hit_rate': 0.8, 'avg_return': 0.017502, 'median_return': 0.021759, 'mean_absolute_return': 0.031184, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.028911, 'median_return': 0.046132, 'mean_absolute_return': 0.066611, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.144029}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.004469, 'median_return': -0.002654, 'mean_absolute_return': 0.008423, 'max_adverse_excursion': -0.029603, 'max_favorable_excursion': 0.011487}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': -0.002489, 'median_return': 0.001303, 'mean_absolute_return': 0.01107, 'max_adverse_excursion': -0.035525, 'max_favorable_excursion': 0.022174}, '10d': {'sample_size': 20, 'hit_rate': 0.3, 'avg_return': -0.009484, 'median_return': -0.010413, 'mean_absolute_return': 0.016723, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.021584}, '20d': {'sample_size': 20, 'hit_rate': 0.5, 'avg_return': -0.00884, 'median_return': 0.001555, 'mean_absolute_return': 0.028986, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.039296}, '60d': {'sample_size': 20, 'hit_rate': 0.35, 'avg_return': -0.019681, 'median_return': -0.020815, 'mean_absolute_return': 0.055269, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.077439}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.006276, 'median_return': 0.001558, 'mean_absolute_return': 0.012553, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.017427}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.010574, 'median_return': -0.013034, 'mean_absolute_return': 0.016744, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.001552, 'median_return': -0.0004, 'mean_absolute_return': 0.017234, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.038788, 'median_return': 0.043456, 'mean_absolute_return': 0.038788, 'max_adverse_excursion': 0.000213, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.090405, 'median_return': 0.101282, 'mean_absolute_return': 0.090405, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.144029}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4861, 'avg_return': -0.001421, 'median_return': -0.000722, 'mean_absolute_return': 0.014141, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.002111, 'median_return': 0.000208, 'mean_absolute_return': 0.017637, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 72, 'hit_rate': 0.4583, 'avg_return': -0.000969, 'median_return': -0.003263, 'mean_absolute_return': 0.020169, 'max_adverse_excursion': -0.047759, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.00782, 'median_return': 0.012291, 'mean_absolute_return': 0.029729, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 0.00858, 'median_return': 0.010234, 'mean_absolute_return': 0.060817, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.130806}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.4875}, '10d': {'sample_size': 80, 'hit_rate': 0.45}, '20d': {'sample_size': 80, 'hit_rate': 0.725}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': -0.075, 'both_hit': 32, 'both_miss': 28}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.4375, 'primary_minus_secondary': 0.05, 'both_hit': 27, 'both_miss': 33}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.45, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1, 'both_hit': 30, 'both_miss': 30}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.725, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': 0.0, 'both_hit': 48, 'both_miss': 12}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': -0.075, 'both_hit': 38, 'both_miss': 22}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.001442, 'median_return': 0.001999, 'mean_absolute_return': 0.015097, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.037412}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.001912, 'median_return': 0.00596, 'mean_absolute_return': 0.019761, 'max_adverse_excursion': -0.053416, 'max_favorable_excursion': 0.045689}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003297, 'median_return': 0.004067, 'mean_absolute_return': 0.023218, 'max_adverse_excursion': -0.047759, 'max_favorable_excursion': 0.057326}, '20d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.013873, 'median_return': 0.014918, 'mean_absolute_return': 0.029405, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.012483, 'median_return': 0.014933, 'mean_absolute_return': 0.059441, 'max_adverse_excursion': -0.15079, 'max_favorable_excursion': 0.116132}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.005254, 'median_return': -0.001811, 'mean_absolute_return': 0.012867, 'max_adverse_excursion': -0.039566, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': -0.007826, 'median_return': -0.001796, 'mean_absolute_return': 0.015334, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.026456}, '10d': {'sample_size': 40, 'hit_rate': 0.325, 'avg_return': -0.005352, 'median_return': -0.007117, 'mean_absolute_return': 0.016533, 'max_adverse_excursion': -0.043454, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.00796, 'median_return': 0.012958, 'mean_absolute_return': 0.031864, 'max_adverse_excursion': -0.10356, 'max_favorable_excursion': 0.076296}, '60d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.021043, 'median_return': 0.037425, 'mean_absolute_return': 0.068111, 'max_adverse_excursion': -0.123535, 'max_favorable_excursion': 0.144029}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.001906`, median `-0.000722`, mae `0.013982`
- 5d: sample `80`, hit `0.4875`, avg `-0.002957`, median `-0.000371`, mae `0.017548`
- 10d: sample `80`, hit `0.45`, avg `-0.001027`, median `-0.003263`, mae `0.019876`
- 20d: sample `80`, hit `0.725`, avg `0.010917`, median `0.013877`, mae `0.030635`
- 60d: sample `80`, hit `0.5625`, avg `0.016763`, median `0.029831`, mae `0.063776`

### breadth_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_bounce_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.001906`, median `-0.000722`, mae `0.013982`
- 5d: sample `80`, hit `0.4875`, avg `-0.002957`, median `-0.000371`, mae `0.017548`
- 10d: sample `80`, hit `0.45`, avg `-0.001027`, median `-0.003263`, mae `0.019876`
- 20d: sample `80`, hit `0.725`, avg `0.010917`, median `0.013877`, mae `0.030635`
- 60d: sample `80`, hit `0.5625`, avg `0.016763`, median `0.029831`, mae `0.063776`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.001052`, median `0.001558`, mae `0.015835`
- 5d: sample `60`, hit `0.45`, avg `-0.003113`, median `-0.001324`, mae `0.019707`
- 10d: sample `60`, hit `0.5`, avg `0.001792`, median `0.000242`, mae `0.020927`
- 20d: sample `60`, hit `0.8`, avg `0.017502`, median `0.021759`, mae `0.031184`
- 60d: sample `60`, hit `0.6333`, avg `0.028911`, median `0.046132`, mae `0.066611`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `80`
- 3d: sample `80`, hit `0.4875`, avg `-0.001906`, median `-0.000722`, mae `0.013982`
- 5d: sample `80`, hit `0.4875`, avg `-0.002957`, median `-0.000371`, mae `0.017548`
- 10d: sample `80`, hit `0.45`, avg `-0.001027`, median `-0.003263`, mae `0.019876`
- 20d: sample `80`, hit `0.725`, avg `0.010917`, median `0.013877`, mae `0.030635`
- 60d: sample `80`, hit `0.5625`, avg `0.016763`, median `0.029831`, mae `0.063776`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.001052`, median `0.001558`, mae `0.015835`
- 5d: sample `60`, hit `0.45`, avg `-0.003113`, median `-0.001324`, mae `0.019707`
- 10d: sample `60`, hit `0.5`, avg `0.001792`, median `0.000242`, mae `0.020927`
- 20d: sample `60`, hit `0.8`, avg `0.017502`, median `0.021759`, mae `0.031184`
- 60d: sample `60`, hit `0.6333`, avg `0.028911`, median `0.046132`, mae `0.066611`

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
- 3d: sample `20`, hit `0.35`, avg `-0.004469`, median `-0.002654`, mae `0.008423`
- 5d: sample `20`, hit `0.6`, avg `-0.002489`, median `0.001303`, mae `0.01107`
- 10d: sample `20`, hit `0.3`, avg `-0.009484`, median `-0.010413`, mae `0.016723`
- 20d: sample `20`, hit `0.5`, avg `-0.00884`, median `0.001555`, mae `0.028986`
- 60d: sample `20`, hit `0.35`, avg `-0.019681`, median `-0.020815`, mae `0.055269`

### mixed_internal_resonance
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `-0.001052`, median `0.001558`, mae `0.015835`
- 5d: sample `60`, hit `0.45`, avg `-0.003113`, median `-0.001324`, mae `0.019707`
- 10d: sample `60`, hit `0.5`, avg `0.001792`, median `0.000242`, mae `0.020927`
- 20d: sample `60`, hit `0.8`, avg `0.017502`, median `0.021759`, mae `0.031184`
- 60d: sample `60`, hit `0.6333`, avg `0.028911`, median `0.046132`, mae `0.066611`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.004469`, median `-0.002654`, mae `0.008423`
- 5d: sample `20`, hit `0.6`, avg `-0.002489`, median `0.001303`, mae `0.01107`
- 10d: sample `20`, hit `0.3`, avg `-0.009484`, median `-0.010413`, mae `0.016723`
- 20d: sample `20`, hit `0.5`, avg `-0.00884`, median `0.001555`, mae `0.028986`
- 60d: sample `20`, hit `0.35`, avg `-0.019681`, median `-0.020815`, mae `0.055269`

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
