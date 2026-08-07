# High Confidence Edge Report

Generated at: `2026-08-07T23:44:47.330530+00:00`

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
- 3d: sample `80`, hit `0.625`, avg `0.003576`, median `0.005642`, mae `0.013447`
- 5d: sample `80`, hit `0.6875`, avg `0.005924`, median `0.006133`, mae `0.016057`
- 10d: sample `80`, hit `0.5875`, avg `0.005937`, median `0.00903`, mae `0.023384`
- 20d: sample `80`, hit `0.675`, avg `0.010016`, median `0.014007`, mae `0.039374`
- 60d: sample `80`, hit `0.575`, avg `0.022271`, median `0.032982`, mae `0.069781`

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
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.625, 'avg_return': 0.003576, 'median_return': 0.005642, 'mean_absolute_return': 0.013447, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 80, 'hit_rate': 0.6875, 'avg_return': 0.005924, 'median_return': 0.006133, 'mean_absolute_return': 0.016057, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 80, 'hit_rate': 0.5875, 'avg_return': 0.005937, 'median_return': 0.00903, 'mean_absolute_return': 0.023384, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.010016, 'median_return': 0.014007, 'mean_absolute_return': 0.039374, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 80, 'hit_rate': 0.575, 'avg_return': 0.022271, 'median_return': 0.032982, 'mean_absolute_return': 0.069781, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.192595}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.003813, 'median_return': 0.001448, 'mean_absolute_return': 0.013805, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.022579}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.000899, 'median_return': 0.004014, 'mean_absolute_return': 0.010054, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.017206}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.002265, 'median_return': 0.011426, 'mean_absolute_return': 0.018665, 'max_adverse_excursion': -0.023505, 'max_favorable_excursion': 0.025531}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.009259, 'median_return': 0.020068, 'mean_absolute_return': 0.026767, 'max_adverse_excursion': -0.047316, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': -0.012738, 'median_return': -0.03081, 'mean_absolute_return': 0.04907, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.087104}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6389, 'avg_return': 0.004397, 'median_return': 0.006565, 'mean_absolute_return': 0.013407, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.006482, 'median_return': 0.007324, 'mean_absolute_return': 0.016724, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.006344, 'median_return': 0.00903, 'mean_absolute_return': 0.023909, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.010101, 'median_return': 0.014007, 'mean_absolute_return': 0.040775, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.02616, 'median_return': 0.045044, 'mean_absolute_return': 0.072082, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.6375}, '10d': {'sample_size': 80, 'hit_rate': 0.5375}, '20d': {'sample_size': 80, 'hit_rate': 0.6}, '60d': {'sample_size': 80, 'hit_rate': 0.5}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.125, 'both_hit': 35, 'both_miss': 25}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6375, 'secondary_hit_rate': 0.6875, 'primary_minus_secondary': -0.05, 'both_hit': 43, 'both_miss': 17}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.05, 'both_hit': 35, 'both_miss': 25}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.675, 'primary_minus_secondary': -0.075, 'both_hit': 41, 'both_miss': 19}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.075, 'both_hit': 33, 'both_miss': 27}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 20, 'non_close_call_sample_size': 60, 'close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.008277, 'median_return': 0.010849, 'mean_absolute_return': 0.015572, 'max_adverse_excursion': -0.027337, 'max_favorable_excursion': 0.043088}, '5d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.005087, 'median_return': 0.010281, 'mean_absolute_return': 0.021714, 'max_adverse_excursion': -0.046804, 'max_favorable_excursion': 0.061826}, '10d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.010077, 'median_return': 0.01246, 'mean_absolute_return': 0.030764, 'max_adverse_excursion': -0.081709, 'max_favorable_excursion': 0.086422}, '20d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.017854, 'median_return': 0.015261, 'mean_absolute_return': 0.052868, 'max_adverse_excursion': -0.142028, 'max_favorable_excursion': 0.163909}, '60d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.042947, 'median_return': 0.061844, 'mean_absolute_return': 0.082147, 'max_adverse_excursion': -0.122187, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.002009, 'median_return': 0.003538, 'mean_absolute_return': 0.012739, 'max_adverse_excursion': -0.051543, 'max_favorable_excursion': 0.030142}, '5d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.006203, 'median_return': 0.006133, 'mean_absolute_return': 0.014171, 'max_adverse_excursion': -0.048844, 'max_favorable_excursion': 0.045153}, '10d': {'sample_size': 60, 'hit_rate': 0.5833, 'avg_return': 0.004556, 'median_return': 0.007467, 'mean_absolute_return': 0.020925, 'max_adverse_excursion': -0.135097, 'max_favorable_excursion': 0.061466}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.007404, 'median_return': 0.014007, 'mean_absolute_return': 0.034876, 'max_adverse_excursion': -0.208363, 'max_favorable_excursion': 0.101086}, '60d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.015378, 'median_return': 0.032982, 'mean_absolute_return': 0.065659, 'max_adverse_excursion': -0.224179, 'max_favorable_excursion': 0.147541}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002009`, median `0.003538`, mae `0.012739`
- 5d: sample `60`, hit `0.7167`, avg `0.006203`, median `0.006133`, mae `0.014171`
- 10d: sample `60`, hit `0.5833`, avg `0.004556`, median `0.007467`, mae `0.020925`
- 20d: sample `60`, hit `0.6833`, avg `0.007404`, median `0.014007`, mae `0.034876`
- 60d: sample `60`, hit `0.55`, avg `0.015378`, median `0.032982`, mae `0.065659`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008277`, median `0.010849`, mae `0.015572`
- 5d: sample `20`, hit `0.6`, avg `0.005087`, median `0.010281`, mae `0.021714`
- 10d: sample `20`, hit `0.6`, avg `0.010077`, median `0.01246`, mae `0.030764`
- 20d: sample `20`, hit `0.65`, avg `0.017854`, median `0.015261`, mae `0.052868`
- 60d: sample `20`, hit `0.65`, avg `0.042947`, median `0.061844`, mae `0.082147`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002009`, median `0.003538`, mae `0.012739`
- 5d: sample `60`, hit `0.7167`, avg `0.006203`, median `0.006133`, mae `0.014171`
- 10d: sample `60`, hit `0.5833`, avg `0.004556`, median `0.007467`, mae `0.020925`
- 20d: sample `60`, hit `0.6833`, avg `0.007404`, median `0.014007`, mae `0.034876`
- 60d: sample `60`, hit `0.55`, avg `0.015378`, median `0.032982`, mae `0.065659`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002009`, median `0.003538`, mae `0.012739`
- 5d: sample `60`, hit `0.7167`, avg `0.006203`, median `0.006133`, mae `0.014171`
- 10d: sample `60`, hit `0.5833`, avg `0.004556`, median `0.007467`, mae `0.020925`
- 20d: sample `60`, hit `0.6833`, avg `0.007404`, median `0.014007`, mae `0.034876`
- 60d: sample `60`, hit `0.55`, avg `0.015378`, median `0.032982`, mae `0.065659`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008277`, median `0.010849`, mae `0.015572`
- 5d: sample `20`, hit `0.6`, avg `0.005087`, median `0.010281`, mae `0.021714`
- 10d: sample `20`, hit `0.6`, avg `0.010077`, median `0.01246`, mae `0.030764`
- 20d: sample `20`, hit `0.65`, avg `0.017854`, median `0.015261`, mae `0.052868`
- 60d: sample `20`, hit `0.65`, avg `0.042947`, median `0.061844`, mae `0.082147`

## Internal Resonance Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Internal-resonance attribution is being tracked, but forward-only samples are still below the minimum gate.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002412`, median `0.000145`, mae `0.008236`
- 5d: sample `20`, hit `0.8`, avg `0.004463`, median `0.005084`, mae `0.010418`
- 10d: sample `20`, hit `0.55`, avg `0.003036`, median `0.007467`, mae `0.01485`
- 20d: sample `20`, hit `0.65`, avg `0.004702`, median `0.012291`, mae `0.021499`
- 60d: sample `20`, hit `0.35`, avg `-0.005679`, median `-0.01711`, mae `0.049585`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.000331`, median `0.006714`, mae `0.016252`
- 5d: sample `20`, hit `0.65`, avg `0.007083`, median `0.005319`, mae `0.014809`
- 10d: sample `20`, hit `0.6`, avg `0.007944`, median `0.011426`, mae `0.021907`
- 20d: sample `20`, hit `0.75`, avg `0.018501`, median `0.024743`, mae `0.038384`
- 60d: sample `20`, hit `0.5`, avg `0.013948`, median `0.012092`, mae `0.061389`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.75`, avg `0.008277`, median `0.010849`, mae `0.015572`
- 5d: sample `20`, hit `0.6`, avg `0.005087`, median `0.010281`, mae `0.021714`
- 10d: sample `20`, hit `0.6`, avg `0.010077`, median `0.01246`, mae `0.030764`
- 20d: sample `20`, hit `0.65`, avg `0.017854`, median `0.015261`, mae `0.052868`
- 60d: sample `20`, hit `0.65`, avg `0.042947`, median `0.061844`, mae `0.082147`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002412`, median `0.000145`, mae `0.008236`
- 5d: sample `20`, hit `0.8`, avg `0.004463`, median `0.005084`, mae `0.010418`
- 10d: sample `20`, hit `0.55`, avg `0.003036`, median `0.007467`, mae `0.01485`
- 20d: sample `20`, hit `0.65`, avg `0.004702`, median `0.012291`, mae `0.021499`
- 60d: sample `20`, hit `0.35`, avg `-0.005679`, median `-0.01711`, mae `0.049585`

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
- sample_size: `80`
- 3d: sample `80`, hit `0.625`, avg `0.003576`, median `0.005642`, mae `0.013447`
- 5d: sample `80`, hit `0.6875`, avg `0.005924`, median `0.006133`, mae `0.016057`
- 10d: sample `80`, hit `0.5875`, avg `0.005937`, median `0.00903`, mae `0.023384`
- 20d: sample `80`, hit `0.675`, avg `0.010016`, median `0.014007`, mae `0.039374`
- 60d: sample `80`, hit `0.575`, avg `0.022271`, median `0.032982`, mae `0.069781`

### flow_conflicted_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5833`, avg `0.002009`, median `0.003538`, mae `0.012739`
- 5d: sample `60`, hit `0.7167`, avg `0.006203`, median `0.006133`, mae `0.014171`
- 10d: sample `60`, hit `0.5833`, avg `0.004556`, median `0.007467`, mae `0.020925`
- 20d: sample `60`, hit `0.6833`, avg `0.007404`, median `0.014007`, mae `0.034876`
- 60d: sample `60`, hit `0.55`, avg `0.015378`, median `0.032982`, mae `0.065659`

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
