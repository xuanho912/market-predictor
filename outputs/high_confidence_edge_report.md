# High Confidence Edge Report

Generated at: `2026-07-12T13:59:01.822418+00:00`

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
- 3d: sample `80`, hit `0.525`, avg `-0.000956`, median `0.001448`, mae `0.011965`
- 5d: sample `80`, hit `0.55`, avg `-0.000938`, median `0.003197`, mae `0.01519`
- 10d: sample `80`, hit `0.5125`, avg `-0.002566`, median `0.002362`, mae `0.020314`
- 20d: sample `80`, hit `0.6625`, avg `-0.002328`, median `0.009812`, mae `0.034126`
- 60d: sample `80`, hit `0.5125`, avg `0.003881`, median `0.010234`, mae `0.062642`

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
- 3d: sample `8`, hit `0.625`, avg `-0.002449`, median `0.009229`, mae `0.016473`
- 5d: sample `8`, hit `0.375`, avg `-0.004006`, median `-0.004989`, mae `0.017767`
- 10d: sample `8`, hit `0.5`, avg `0.001119`, median `0.019233`, mae `0.023093`
- 20d: sample `8`, hit `0.875`, avg `0.026927`, median `0.029166`, mae `0.028823`
- 60d: sample `8`, hit `0.625`, avg `0.042692`, median `0.087104`, mae `0.065002`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.002449`, median `0.009229`, mae `0.016473`
- 5d: sample `8`, hit `0.375`, avg `-0.004006`, median `-0.004989`, mae `0.017767`
- 10d: sample `8`, hit `0.5`, avg `0.001119`, median `0.019233`, mae `0.023093`
- 20d: sample `8`, hit `0.875`, avg `0.026927`, median `0.029166`, mae `0.028823`
- 60d: sample `8`, hit `0.625`, avg `0.042692`, median `0.087104`, mae `0.065002`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.525, 'avg_return': -0.000956, 'median_return': 0.001448, 'mean_absolute_return': 0.011965, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 80, 'hit_rate': 0.55, 'avg_return': -0.000938, 'median_return': 0.003197, 'mean_absolute_return': 0.01519, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.002566, 'median_return': 0.002362, 'mean_absolute_return': 0.020314, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.045189}, '20d': {'sample_size': 80, 'hit_rate': 0.6625, 'avg_return': -0.002328, 'median_return': 0.009812, 'mean_absolute_return': 0.034126, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070768}, '60d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': 0.003881, 'median_return': 0.010234, 'mean_absolute_return': 0.062642, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.190256}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.002449, 'median_return': 0.009229, 'mean_absolute_return': 0.016473, 'max_adverse_excursion': -0.033125, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.004006, 'median_return': -0.004989, 'mean_absolute_return': 0.017767, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.001119, 'median_return': 0.019233, 'mean_absolute_return': 0.023093, 'max_adverse_excursion': -0.030486, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.026927, 'median_return': 0.029166, 'mean_absolute_return': 0.028823, 'max_adverse_excursion': -0.007581, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.042692, 'median_return': 0.087104, 'mean_absolute_return': 0.065002, 'max_adverse_excursion': -0.038302, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.00079, 'median_return': 0.000324, 'mean_absolute_return': 0.011465, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': -0.000597, 'median_return': 0.003714, 'mean_absolute_return': 0.014903, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': -0.002976, 'median_return': 0.002362, 'mean_absolute_return': 0.020005, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.045189}, '20d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': -0.005578, 'median_return': 0.007748, 'mean_absolute_return': 0.034716, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070768}, '60d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.000432, 'median_return': 0.008034, 'mean_absolute_return': 0.06238, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.190256}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.5125}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.025, 'both_hit': 33, 'both_miss': 27}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': 0.0, 'both_hit': 34, 'both_miss': 26}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 32, 'both_miss': 28}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6375, 'primary_minus_secondary': 0.025, 'both_hit': 42, 'both_miss': 18}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': -0.025, 'both_hit': 32, 'both_miss': 28}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.000953, 'median_return': 0.003026, 'mean_absolute_return': 0.011726, 'max_adverse_excursion': -0.037634, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.000866, 'median_return': 0.003197, 'mean_absolute_return': 0.015031, 'max_adverse_excursion': -0.042983, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.002466, 'median_return': 0.004067, 'mean_absolute_return': 0.021228, 'max_adverse_excursion': -0.057921, 'max_favorable_excursion': 0.045189}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': -0.007246, 'median_return': 0.007366, 'mean_absolute_return': 0.037592, 'max_adverse_excursion': -0.150542, 'max_favorable_excursion': 0.070768}, '60d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.004561, 'median_return': 0.010234, 'mean_absolute_return': 0.061194, 'max_adverse_excursion': -0.128011, 'max_favorable_excursion': 0.190256}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': -0.002866, 'median_return': 0.001448, 'mean_absolute_return': 0.012205, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.002743, 'median_return': 0.003714, 'mean_absolute_return': 0.015349, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.031236}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.002666, 'median_return': 0.002362, 'mean_absolute_return': 0.0194, 'max_adverse_excursion': -0.063198, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 40, 'hit_rate': 0.7, 'avg_return': 0.00259, 'median_return': 0.012958, 'mean_absolute_return': 0.030661, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.0032, 'median_return': 0.012092, 'mean_absolute_return': 0.06409, 'max_adverse_excursion': -0.141126, 'max_favorable_excursion': 0.121826}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.00267`, median `0.000145`, mae `0.012289`
- 5d: sample `60`, hit `0.55`, avg `-0.002793`, median `0.003005`, mae `0.015749`
- 10d: sample `60`, hit `0.4833`, avg `-0.004175`, median `-0.000214`, mae `0.022212`
- 20d: sample `60`, hit `0.65`, avg `-0.004136`, median `0.007988`, mae `0.036157`
- 60d: sample `60`, hit `0.4833`, avg `0.001164`, median `-0.004982`, mae `0.064025`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002278`, median `-0.002441`, mae `0.012456`
- 5d: sample `20`, hit `0.5`, avg `-0.002894`, median `0.001259`, mae `0.01655`
- 10d: sample `20`, hit `0.45`, avg `-0.007194`, median `-0.010743`, mae `0.027835`
- 20d: sample `20`, hit `0.55`, avg `-0.017588`, median `0.002759`, mae `0.047149`
- 60d: sample `20`, hit `0.45`, avg `-0.002908`, median `-0.005997`, mae `0.063894`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.00267`, median `0.000145`, mae `0.012289`
- 5d: sample `60`, hit `0.55`, avg `-0.002793`, median `0.003005`, mae `0.015749`
- 10d: sample `60`, hit `0.4833`, avg `-0.004175`, median `-0.000214`, mae `0.022212`
- 20d: sample `60`, hit `0.65`, avg `-0.004136`, median `0.007988`, mae `0.036157`
- 60d: sample `60`, hit `0.4833`, avg `0.001164`, median `-0.004982`, mae `0.064025`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002278`, median `-0.002441`, mae `0.012456`
- 5d: sample `20`, hit `0.5`, avg `-0.002894`, median `0.001259`, mae `0.01655`
- 10d: sample `20`, hit `0.45`, avg `-0.007194`, median `-0.010743`, mae `0.027835`
- 20d: sample `20`, hit `0.55`, avg `-0.017588`, median `0.002759`, mae `0.047149`
- 60d: sample `20`, hit `0.45`, avg `-0.002908`, median `-0.005997`, mae `0.063894`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.007619`, median `0.001448`, mae `0.016436`
- 5d: sample `20`, hit `0.45`, avg `-0.009489`, median `-0.002525`, mae `0.017598`
- 10d: sample `20`, hit `0.3`, avg `-0.008356`, median `-0.011432`, mae `0.021354`
- 20d: sample `20`, hit `0.65`, avg `0.001616`, median `0.020068`, mae `0.035743`
- 60d: sample `20`, hit `0.55`, avg `0.011506`, median `0.029831`, mae `0.064908`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.00267`, median `0.000145`, mae `0.012289`
- 5d: sample `60`, hit `0.55`, avg `-0.002793`, median `0.003005`, mae `0.015749`
- 10d: sample `60`, hit `0.4833`, avg `-0.004175`, median `-0.000214`, mae `0.022212`
- 20d: sample `60`, hit `0.65`, avg `-0.004136`, median `0.007988`, mae `0.036157`
- 60d: sample `60`, hit `0.4833`, avg `0.001164`, median `-0.004982`, mae `0.064025`

### bounce_without_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.004184`, median `0.004569`, mae `0.010996`
- 5d: sample `20`, hit `0.55`, avg `0.004626`, median `0.00596`, mae `0.013512`
- 10d: sample `20`, hit `0.6`, avg `0.002262`, median `0.005616`, mae `0.014621`
- 20d: sample `20`, hit `0.7`, avg `0.003096`, median `0.01011`, mae `0.028035`
- 60d: sample `20`, hit `0.6`, avg `0.012031`, median `0.029945`, mae `0.058493`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.007619`, median `0.001448`, mae `0.016436`
- 5d: sample `20`, hit `0.45`, avg `-0.009489`, median `-0.002525`, mae `0.017598`
- 10d: sample `20`, hit `0.3`, avg `-0.008356`, median `-0.011432`, mae `0.021354`
- 20d: sample `20`, hit `0.65`, avg `0.001616`, median `0.020068`, mae `0.035743`
- 60d: sample `20`, hit `0.55`, avg `0.011506`, median `0.029831`, mae `0.064908`

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
- 3d: sample `20`, hit `0.55`, avg `0.001887`, median `0.004004`, mae `0.007975`
- 5d: sample `20`, hit `0.7`, avg `0.004004`, median `0.007324`, mae `0.013099`
- 10d: sample `20`, hit `0.7`, avg `0.003024`, median `0.009675`, mae `0.017447`
- 20d: sample `20`, hit `0.75`, avg `0.003564`, median `0.012682`, mae `0.025579`
- 60d: sample `20`, hit `0.45`, avg `-0.005106`, median `-0.01711`, mae `0.063272`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.007619`, median `0.001448`, mae `0.016436`
- 5d: sample `20`, hit `0.45`, avg `-0.009489`, median `-0.002525`, mae `0.017598`
- 10d: sample `20`, hit `0.3`, avg `-0.008356`, median `-0.011432`, mae `0.021354`
- 20d: sample `20`, hit `0.65`, avg `0.001616`, median `0.020068`, mae `0.035743`
- 60d: sample `20`, hit `0.55`, avg `0.011506`, median `0.029831`, mae `0.064908`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002278`, median `-0.002441`, mae `0.012456`
- 5d: sample `20`, hit `0.5`, avg `-0.002894`, median `0.001259`, mae `0.01655`
- 10d: sample `20`, hit `0.45`, avg `-0.007194`, median `-0.010743`, mae `0.027835`
- 20d: sample `20`, hit `0.55`, avg `-0.017588`, median `0.002759`, mae `0.047149`
- 60d: sample `20`, hit `0.45`, avg `-0.002908`, median `-0.005997`, mae `0.063894`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001887`, median `0.004004`, mae `0.007975`
- 5d: sample `20`, hit `0.7`, avg `0.004004`, median `0.007324`, mae `0.013099`
- 10d: sample `20`, hit `0.7`, avg `0.003024`, median `0.009675`, mae `0.017447`
- 20d: sample `20`, hit `0.75`, avg `0.003564`, median `0.012682`, mae `0.025579`
- 60d: sample `20`, hit `0.45`, avg `-0.005106`, median `-0.01711`, mae `0.063272`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.002278`, median `-0.002441`, mae `0.012456`
- 5d: sample `20`, hit `0.5`, avg `-0.002894`, median `0.001259`, mae `0.01655`
- 10d: sample `20`, hit `0.45`, avg `-0.007194`, median `-0.010743`, mae `0.027835`
- 20d: sample `20`, hit `0.55`, avg `-0.017588`, median `0.002759`, mae `0.047149`
- 60d: sample `20`, hit `0.45`, avg `-0.002908`, median `-0.005997`, mae `0.063894`

## Flow / Positioning Proxy Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Flow / positioning proxy attribution is tracked, but forward-only samples are still below the minimum gate.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.000956`, median `0.001448`, mae `0.011965`
- 5d: sample `80`, hit `0.55`, avg `-0.000938`, median `0.003197`, mae `0.01519`
- 10d: sample `80`, hit `0.5125`, avg `-0.002566`, median `0.002362`, mae `0.020314`
- 20d: sample `80`, hit `0.6625`, avg `-0.002328`, median `0.009812`, mae `0.034126`
- 60d: sample `80`, hit `0.5125`, avg `0.003881`, median `0.010234`, mae `0.062642`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `80`
- 3d: sample `80`, hit `0.525`, avg `-0.000956`, median `0.001448`, mae `0.011965`
- 5d: sample `80`, hit `0.55`, avg `-0.000938`, median `0.003197`, mae `0.01519`
- 10d: sample `80`, hit `0.5125`, avg `-0.002566`, median `0.002362`, mae `0.020314`
- 20d: sample `80`, hit `0.6625`, avg `-0.002328`, median `0.009812`, mae `0.034126`
- 60d: sample `80`, hit `0.5125`, avg `0.003881`, median `0.010234`, mae `0.062642`

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
