# High Confidence Edge Report

Generated at: `2026-09-09T16:42:19.807928+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `4`
Forward validation notice: `当前高置信度还没有被前向样本验证，不应当视为稳定预测能力。`
Conclusion: `forward_validation_insufficient_keep_confidence_capped`

## Forward Sample Gates

- 3d: completed `4`, gate `insufficient`
- 5d: completed `4`, gate `insufficient`
- 10d: completed `4`, gate `insufficient`
- 20d: completed `4`, gate `insufficient`
- 60d: completed `4`, gate `insufficient`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.575`, avg `0.002164`, median `0.002067`, mae `0.013242`
- 5d: sample `80`, hit `0.6`, avg `0.002586`, median `0.00175`, mae `0.016041`
- 10d: sample `80`, hit `0.4`, avg `0.001062`, median `-0.007117`, mae `0.024723`
- 20d: sample `80`, hit `0.625`, avg `0.010701`, median `0.020226`, mae `0.038746`
- 60d: sample `80`, hit `0.725`, avg `0.040486`, median `0.059948`, mae `0.076125`

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
- 3d: sample `8`, hit `0.625`, avg `-0.000535`, median `0.00234`, mae `0.013471`
- 5d: sample `8`, hit `0.5`, avg `-0.005484`, median `0.000208`, mae `0.01003`
- 10d: sample `8`, hit `0.375`, avg `0.000352`, median `-0.001222`, mae `0.015751`
- 20d: sample `8`, hit `0.875`, avg `0.019425`, median `0.029166`, mae `0.027737`
- 60d: sample `8`, hit `0.875`, avg `0.048845`, median `0.059495`, mae `0.062721`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `-0.000535`, median `0.00234`, mae `0.013471`
- 5d: sample `8`, hit `0.5`, avg `-0.005484`, median `0.000208`, mae `0.01003`
- 10d: sample `8`, hit `0.375`, avg `0.000352`, median `-0.001222`, mae `0.015751`
- 20d: sample `8`, hit `0.875`, avg `0.019425`, median `0.029166`, mae `0.027737`
- 60d: sample `8`, hit `0.875`, avg `0.048845`, median `0.059495`, mae `0.062721`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': -0.000535, 'median_return': 0.00234, 'mean_absolute_return': 0.013471, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.023707}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.005484, 'median_return': 0.000208, 'mean_absolute_return': 0.01003, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.011143}, '10d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.000352, 'median_return': -0.001222, 'mean_absolute_return': 0.015751, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.035895}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.019425, 'median_return': 0.029166, 'mean_absolute_return': 0.027737, 'max_adverse_excursion': -0.033249, 'max_favorable_excursion': 0.055822}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.048845, 'median_return': 0.059495, 'mean_absolute_return': 0.062721, 'max_adverse_excursion': -0.055503, 'max_favorable_excursion': 0.120808}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.002464, 'median_return': 0.002067, 'mean_absolute_return': 0.013216, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003482, 'median_return': 0.004473, 'mean_absolute_return': 0.016709, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 72, 'hit_rate': 0.4028, 'avg_return': 0.001141, 'median_return': -0.007491, 'mean_absolute_return': 0.02572, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.009732, 'median_return': 0.020226, 'mean_absolute_return': 0.039969, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.039557, 'median_return': 0.061042, 'mean_absolute_return': 0.077614, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.192595}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.425}, '5d': {'sample_size': 80, 'hit_rate': 0.4}, '10d': {'sample_size': 80, 'hit_rate': 0.6}, '20d': {'sample_size': 80, 'hit_rate': 0.375}, '60d': {'sample_size': 80, 'hit_rate': 0.275}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.425, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.15, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.2, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.4, 'primary_minus_secondary': 0.2, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.375, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.25, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.275, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.45, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.001454, 'median_return': 0.001558, 'mean_absolute_return': 0.01321, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.000163, 'median_return': 0.000873, 'mean_absolute_return': 0.016478, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.051659}, '10d': {'sample_size': 60, 'hit_rate': 0.4, 'avg_return': 0.002858, 'median_return': -0.007011, 'mean_absolute_return': 0.024612, 'max_adverse_excursion': -0.049389, 'max_favorable_excursion': 0.080879}, '20d': {'sample_size': 60, 'hit_rate': 0.6833, 'avg_return': 0.015433, 'median_return': 0.025442, 'mean_absolute_return': 0.038867, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.147965}, '60d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.045986, 'median_return': 0.061042, 'mean_absolute_return': 0.075312, 'max_adverse_excursion': -0.099158, 'max_favorable_excursion': 0.192595}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.004294, 'median_return': 0.005296, 'mean_absolute_return': 0.013337, 'max_adverse_excursion': -0.022578, 'max_favorable_excursion': 0.035961}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.009855, 'median_return': 0.011391, 'mean_absolute_return': 0.014733, 'max_adverse_excursion': -0.01226, 'max_favorable_excursion': 0.035465}, '10d': {'sample_size': 20, 'hit_rate': 0.4, 'avg_return': -0.004326, 'median_return': -0.011522, 'mean_absolute_return': 0.025054, 'max_adverse_excursion': -0.068262, 'max_favorable_excursion': 0.059577}, '20d': {'sample_size': 20, 'hit_rate': 0.45, 'avg_return': -0.003494, 'median_return': -0.005788, 'mean_absolute_return': 0.038383, 'max_adverse_excursion': -0.131405, 'max_favorable_excursion': 0.062064}, '60d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.023985, 'median_return': 0.039842, 'mean_absolute_return': 0.078565, 'max_adverse_excursion': -0.236029, 'max_favorable_excursion': 0.117141}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.000663`, median `-0.001428`, mae `0.008173`
- 5d: sample `20`, hit `0.6`, avg `-0.00226`, median `0.000873`, mae `0.009963`
- 10d: sample `20`, hit `0.3`, avg `-0.008149`, median `-0.01051`, mae `0.020632`
- 20d: sample `20`, hit `0.45`, avg `-0.008985`, median `-0.001203`, mae `0.035937`
- 60d: sample `20`, hit `0.55`, avg `0.019717`, median `0.057625`, mae `0.060001`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003107`, median `0.005296`, mae `0.014931`
- 5d: sample `60`, hit `0.6`, avg `0.004201`, median `0.00609`, mae `0.018068`
- 10d: sample `60`, hit `0.4333`, avg `0.004132`, median `-0.00367`, mae `0.026087`
- 20d: sample `60`, hit `0.6833`, avg `0.017263`, median `0.029029`, mae `0.039682`
- 60d: sample `60`, hit `0.7833`, avg `0.047408`, median `0.065295`, mae `0.0815`

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
- 3d: sample `20`, hit `0.75`, avg `0.00896`, median `0.010664`, mae `0.0178`
- 5d: sample `20`, hit `0.65`, avg `0.011765`, median `0.012316`, mae `0.02406`
- 10d: sample `20`, hit `0.6`, avg `0.021005`, median `0.020588`, mae `0.035109`
- 20d: sample `20`, hit `0.9`, avg `0.041845`, median `0.041967`, mae `0.044404`
- 60d: sample `20`, hit `0.85`, avg `0.080777`, median `0.084994`, mae `0.088712`

### bounce_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003107`, median `0.005296`, mae `0.014931`
- 5d: sample `60`, hit `0.6`, avg `0.004201`, median `0.00609`, mae `0.018068`
- 10d: sample `60`, hit `0.4333`, avg `0.004132`, median `-0.00367`, mae `0.026087`
- 20d: sample `60`, hit `0.6833`, avg `0.017263`, median `0.029029`, mae `0.039682`
- 60d: sample `60`, hit `0.7833`, avg `0.047408`, median `0.065295`, mae `0.0815`

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
- 3d: sample `80`, hit `0.575`, avg `0.002164`, median `0.002067`, mae `0.013242`
- 5d: sample `80`, hit `0.6`, avg `0.002586`, median `0.00175`, mae `0.016041`
- 10d: sample `80`, hit `0.4`, avg `0.001062`, median `-0.007117`, mae `0.024723`
- 20d: sample `80`, hit `0.625`, avg `0.010701`, median `0.020226`, mae `0.038746`
- 60d: sample `80`, hit `0.725`, avg `0.040486`, median `0.059948`, mae `0.076125`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

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
