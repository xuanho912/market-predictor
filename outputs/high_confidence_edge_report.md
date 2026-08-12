# High Confidence Edge Report

Generated at: `2026-08-12T03:32:02.615045+00:00`

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
- 3d: sample `40`, hit `0.625`, avg `0.002244`, median `0.006565`, mae `0.014675`
- 5d: sample `40`, hit `0.625`, avg `0.003682`, median `0.005327`, mae `0.016136`
- 10d: sample `40`, hit `0.575`, avg `0.003652`, median `0.005616`, mae `0.023891`
- 20d: sample `40`, hit `0.675`, avg `0.005491`, median `0.01666`, mae `0.041067`
- 60d: sample `40`, hit `0.625`, avg `0.023899`, median `0.052998`, mae `0.070842`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.002359`, median `0.004004`, mae `0.014158`
- 5d: sample `40`, hit `0.725`, avg `0.003644`, median `0.004606`, mae `0.017987`
- 10d: sample `40`, hit `0.5`, avg `0.007377`, median `0.001935`, mae `0.026614`
- 20d: sample `40`, hit `0.65`, avg `0.016927`, median `0.011728`, mae `0.036305`
- 60d: sample `40`, hit `0.5`, avg `0.024167`, median `0.018072`, mae `0.071357`

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
- 3d: sample `8`, hit `0.5`, avg `-0.003813`, median `0.001448`, mae `0.013805`
- 5d: sample `8`, hit `0.75`, avg `0.000899`, median `0.004014`, mae `0.010054`
- 10d: sample `8`, hit `0.5`, avg `0.002265`, median `0.011426`, mae `0.018665`
- 20d: sample `8`, hit `0.625`, avg `0.009259`, median `0.020068`, mae `0.026767`
- 60d: sample `8`, hit `0.375`, avg `-0.012738`, median `-0.03081`, mae `0.04907`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.003813`, median `0.001448`, mae `0.013805`
- 5d: sample `8`, hit `0.75`, avg `0.000899`, median `0.004014`, mae `0.010054`
- 10d: sample `8`, hit `0.5`, avg `0.002265`, median `0.011426`, mae `0.018665`
- 20d: sample `8`, hit `0.625`, avg `0.009259`, median `0.020068`, mae `0.026767`
- 60d: sample `8`, hit `0.375`, avg `-0.012738`, median `-0.03081`, mae `0.04907`

### confidence validation
- `{'strong_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.002244, 'median_return': 0.006565, 'mean_absolute_return': 0.014675, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.003682, 'median_return': 0.005327, 'mean_absolute_return': 0.016136, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.003652, 'median_return': 0.005616, 'mean_absolute_return': 0.023891, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.005491, 'median_return': 0.01666, 'mean_absolute_return': 0.041067, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.023899, 'median_return': 0.052998, 'mean_absolute_return': 0.070842, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.147541}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.002359, 'median_return': 0.004004, 'mean_absolute_return': 0.014158, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.003644, 'median_return': 0.004606, 'mean_absolute_return': 0.017987, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.007377, 'median_return': 0.001935, 'mean_absolute_return': 0.026614, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.016927, 'median_return': 0.011728, 'mean_absolute_return': 0.036305, 'max_adverse_excursion': -0.080875, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': 0.024167, 'median_return': 0.018072, 'mean_absolute_return': 0.071357, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003813, 'median_return': 0.001448, 'mean_absolute_return': 0.013805, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.000899, 'median_return': 0.004014, 'mean_absolute_return': 0.010054, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002265, 'median_return': 0.011426, 'mean_absolute_return': 0.018665, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009259, 'median_return': 0.020068, 'mean_absolute_return': 0.026767, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012738, 'median_return': -0.03081, 'mean_absolute_return': 0.04907, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.002981, 'median_return': 0.004569, 'mean_absolute_return': 0.014484, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.00397, 'median_return': 0.005327, 'mean_absolute_return': 0.01784, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5417, 'avg_return': 0.005876, 'median_return': 0.003491, 'mean_absolute_return': 0.025984, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6667, 'avg_return': 0.011426, 'median_return': 0.012291, 'mean_absolute_return': 0.04001, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.028119, 'median_return': 0.045044, 'mean_absolute_return': 0.073547, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.625}, '5d': {'sample_size': 80, 'hit_rate': 0.675}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': 0.0, 'both_hit': 50, 'both_miss': 30}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.675, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': 0.0, 'both_hit': 54, 'both_miss': 26}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.0, 'both_hit': 43, 'both_miss': 37}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.6625, 'primary_minus_secondary': 0.0, 'both_hit': 53, 'both_miss': 27}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5625, 'primary_minus_secondary': 0.0, 'both_hit': 45, 'both_miss': 35}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.007899, 'median_return': 0.012091, 'mean_absolute_return': 0.020706, 'max_adverse_excursion': -0.052683, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.00437, 'median_return': 0.010908, 'mean_absolute_return': 0.027099, 'max_adverse_excursion': -0.059118, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.016412, 'median_return': 0.011168, 'mean_absolute_return': 0.038, 'max_adverse_excursion': -0.086627, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.035622, 'median_return': 0.029029, 'mean_absolute_return': 0.050656, 'max_adverse_excursion': -0.080875, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.064751, 'median_return': 0.079128, 'mean_absolute_return': 0.095012, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.000436, 'median_return': 0.001448, 'mean_absolute_return': 0.01232, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.025806}, '5d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.003428, 'median_return': 0.004606, 'mean_absolute_return': 0.013716, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.034246}, '10d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.001882, 'median_return': 0.003491, 'mean_absolute_return': 0.021003, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.003072, 'median_return': 0.011728, 'mean_absolute_return': 0.034696, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.5167, 'avg_return': 0.01046, 'median_return': 0.018072, 'mean_absolute_return': 0.063129, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.147541}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002913`, median `0.000145`, mae `0.012102`
- 5d: sample `40`, hit `0.675`, avg `0.00193`, median `0.003005`, mae `0.01225`
- 10d: sample `40`, hit `0.5`, avg `0.001012`, median `0.001517`, mae `0.018029`
- 20d: sample `40`, hit `0.625`, avg `0.00494`, median `0.011728`, mae `0.029507`
- 60d: sample `40`, hit `0.4`, avg `0.000607`, median `-0.01711`, mae `0.052916`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.007899`, median `0.012091`, mae `0.020706`
- 5d: sample `20`, hit `0.65`, avg `0.00437`, median `0.010908`, mae `0.027099`
- 10d: sample `20`, hit `0.55`, avg `0.016412`, median `0.011168`, mae `0.038`
- 20d: sample `20`, hit `0.75`, avg `0.035622`, median `0.029029`, mae `0.050656`
- 60d: sample `20`, hit `0.7`, avg `0.064751`, median `0.079128`, mae `0.095012`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002913`, median `0.000145`, mae `0.012102`
- 5d: sample `40`, hit `0.675`, avg `0.00193`, median `0.003005`, mae `0.01225`
- 10d: sample `40`, hit `0.5`, avg `0.001012`, median `0.001517`, mae `0.018029`
- 20d: sample `40`, hit `0.625`, avg `0.00494`, median `0.011728`, mae `0.029507`
- 60d: sample `40`, hit `0.4`, avg `0.000607`, median `-0.01711`, mae `0.052916`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.8`, avg `0.007899`, median `0.012091`, mae `0.020706`
- 5d: sample `20`, hit `0.65`, avg `0.00437`, median `0.010908`, mae `0.027099`
- 10d: sample `20`, hit `0.55`, avg `0.016412`, median `0.011168`, mae `0.038`
- 20d: sample `20`, hit `0.75`, avg `0.035622`, median `0.029029`, mae `0.050656`
- 60d: sample `20`, hit `0.7`, avg `0.064751`, median `0.079128`, mae `0.095012`

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
- 3d: sample `40`, hit `0.5`, avg `-0.002913`, median `0.000145`, mae `0.012102`
- 5d: sample `40`, hit `0.675`, avg `0.00193`, median `0.003005`, mae `0.01225`
- 10d: sample `40`, hit `0.5`, avg `0.001012`, median `0.001517`, mae `0.018029`
- 20d: sample `40`, hit `0.625`, avg `0.00494`, median `0.011728`, mae `0.029507`
- 60d: sample `40`, hit `0.4`, avg `0.000607`, median `-0.01711`, mae `0.052916`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.75`, avg `0.007516`, median `0.011125`, mae `0.016731`
- 5d: sample `40`, hit `0.675`, avg `0.005396`, median `0.010281`, mae `0.021872`
- 10d: sample `40`, hit `0.575`, avg `0.010017`, median `0.005616`, mae `0.032475`
- 20d: sample `40`, hit `0.7`, avg `0.017479`, median `0.015261`, mae `0.047865`
- 60d: sample `40`, hit `0.725`, avg `0.047459`, median `0.064104`, mae `0.089283`

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
- 3d: sample `20`, hit `0.45`, avg `-0.00318`, median `-0.001166`, mae `0.00761`
- 5d: sample `20`, hit `0.8`, avg `0.002919`, median `0.003714`, mae `0.008874`
- 10d: sample `20`, hit `0.45`, avg `-0.001657`, median `-0.001676`, mae `0.015228`
- 20d: sample `20`, hit `0.55`, avg `-0.001768`, median `0.007988`, mae `0.021954`
- 60d: sample `20`, hit `0.3`, avg `-0.016418`, median `-0.018455`, mae `0.047702`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `-0.002646`, median `0.003785`, mae `0.016593`
- 5d: sample `20`, hit `0.55`, avg `0.00094`, median `0.003005`, mae `0.015627`
- 10d: sample `20`, hit `0.55`, avg `0.003681`, median `0.010691`, mae `0.020831`
- 20d: sample `20`, hit `0.7`, avg `0.011647`, median `0.022652`, mae `0.03706`
- 60d: sample `20`, hit `0.5`, avg `0.017631`, median `0.012092`, mae `0.05813`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.00318`, median `-0.001166`, mae `0.00761`
- 5d: sample `20`, hit `0.8`, avg `0.002919`, median `0.003714`, mae `0.008874`
- 10d: sample `20`, hit `0.45`, avg `-0.001657`, median `-0.001676`, mae `0.015228`
- 20d: sample `20`, hit `0.55`, avg `-0.001768`, median `0.007988`, mae `0.021954`
- 60d: sample `20`, hit `0.3`, avg `-0.016418`, median `-0.018455`, mae `0.047702`

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
