# High Confidence Edge Report

Generated at: `2026-07-16T14:26:35.303716+00:00`

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
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `80`
- 3d: sample `80`, hit `0.5`, avg `-0.002924`, median `0.000201`, mae `0.014568`
- 5d: sample `80`, hit `0.55`, avg `-0.001635`, median `0.001303`, mae `0.01598`
- 10d: sample `80`, hit `0.4375`, avg `-0.003197`, median `-0.007011`, mae `0.020891`
- 20d: sample `80`, hit `0.6`, avg `0.004251`, median `0.004241`, mae `0.02976`
- 60d: sample `80`, hit `0.5625`, avg `0.006164`, median `0.010234`, mae `0.06699`

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
- 3d: sample `8`, hit `0.5`, avg `-0.00328`, median `0.006632`, mae `0.015252`
- 5d: sample `8`, hit `0.5`, avg `-0.000619`, median `0.003476`, mae `0.017721`
- 10d: sample `8`, hit `0.75`, avg `0.020756`, median `0.045189`, mae `0.034072`
- 20d: sample `8`, hit `1.0`, avg `0.034681`, median `0.054665`, mae `0.034681`
- 60d: sample `8`, hit `0.5`, avg `0.041882`, median `0.0765`, mae `0.074607`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.000694`, median `0.000744`, mae `0.00643`
- 5d: sample `8`, hit `0.5`, avg `0.004802`, median `0.006133`, mae `0.01015`
- 10d: sample `8`, hit `0.5`, avg `-0.010007`, median `0.000242`, mae `0.021672`
- 20d: sample `8`, hit `0.625`, avg `0.00685`, median `0.007748`, mae `0.03216`
- 60d: sample `8`, hit `0.625`, avg `0.025265`, median `0.096756`, mae `0.093598`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.000694, 'median_return': 0.000744, 'mean_absolute_return': 0.00643, 'max_adverse_excursion': -0.01345, 'max_favorable_excursion': 0.01687}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.004802, 'median_return': 0.006133, 'mean_absolute_return': 0.01015, 'max_adverse_excursion': -0.013784, 'max_favorable_excursion': 0.022754}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.010007, 'median_return': 0.000242, 'mean_absolute_return': 0.021672, 'max_adverse_excursion': -0.039512, 'max_favorable_excursion': 0.023905}, '20d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.00685, 'median_return': 0.007748, 'mean_absolute_return': 0.03216, 'max_adverse_excursion': -0.047612, 'max_favorable_excursion': 0.070755}, '60d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.025265, 'median_return': 0.096756, 'mean_absolute_return': 0.093598, 'max_adverse_excursion': -0.10388, 'max_favorable_excursion': 0.116132}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5, 'avg_return': -0.003326, 'median_return': 0.000201, 'mean_absolute_return': 0.015472, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': -0.00235, 'median_return': 0.001303, 'mean_absolute_return': 0.016628, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 72, 'hit_rate': 0.4306, 'avg_return': -0.00244, 'median_return': -0.007011, 'mean_absolute_return': 0.020804, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.003962, 'median_return': 0.003675, 'mean_absolute_return': 0.029493, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.004041, 'median_return': 0.009227, 'mean_absolute_return': 0.064033, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19082}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.55}, '5d': {'sample_size': 80, 'hit_rate': 0.55}, '10d': {'sample_size': 80, 'hit_rate': 0.6875}, '20d': {'sample_size': 80, 'hit_rate': 0.5}, '60d': {'sample_size': 80, 'hit_rate': 0.5125}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.45, 'primary_minus_secondary': 0.1, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.6875, 'secondary_hit_rate': 0.3125, 'primary_minus_secondary': 0.375, 'both_hit': 0, 'both_miss': 0}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.0, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.025, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.001219, 'median_return': 0.004667, 'mean_absolute_return': 0.012868, 'max_adverse_excursion': -0.057907, 'max_favorable_excursion': 0.037512}, '5d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.004215, 'median_return': 0.006133, 'mean_absolute_return': 0.015374, 'max_adverse_excursion': -0.053416, 'max_favorable_excursion': 0.046426}, '10d': {'sample_size': 40, 'hit_rate': 0.525, 'avg_return': 0.001973, 'median_return': 0.001455, 'mean_absolute_return': 0.02405, 'max_adverse_excursion': -0.047759, 'max_favorable_excursion': 0.058931}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.009564, 'median_return': 0.007366, 'mean_absolute_return': 0.032153, 'max_adverse_excursion': -0.098604, 'max_favorable_excursion': 0.076981}, '60d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.018082, 'median_return': 0.029066, 'mean_absolute_return': 0.074898, 'max_adverse_excursion': -0.210697, 'max_favorable_excursion': 0.19082}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.4, 'avg_return': -0.007066, 'median_return': -0.007923, 'mean_absolute_return': 0.016268, 'max_adverse_excursion': -0.038668, 'max_favorable_excursion': 0.037139}, '5d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.007484, 'median_return': 0.000415, 'mean_absolute_return': 0.016586, 'max_adverse_excursion': -0.061703, 'max_favorable_excursion': 0.025923}, '10d': {'sample_size': 40, 'hit_rate': 0.35, 'avg_return': -0.008366, 'median_return': -0.009882, 'mean_absolute_return': 0.017732, 'max_adverse_excursion': -0.06171, 'max_favorable_excursion': 0.027926}, '20d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': -0.001063, 'median_return': 0.003675, 'mean_absolute_return': 0.027366, 'max_adverse_excursion': -0.118842, 'max_favorable_excursion': 0.062955}, '60d': {'sample_size': 40, 'hit_rate': 0.5, 'avg_return': -0.005754, 'median_return': 8.1e-05, 'mean_absolute_return': 0.059082, 'max_adverse_excursion': -0.146695, 'max_favorable_excursion': 0.121826}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.6`, avg `0.001219`, median `0.004667`, mae `0.012868`
- 5d: sample `40`, hit `0.6`, avg `0.004215`, median `0.006133`, mae `0.015374`
- 10d: sample `40`, hit `0.525`, avg `0.001973`, median `0.001455`, mae `0.02405`
- 20d: sample `40`, hit `0.625`, avg `0.009564`, median `0.007366`, mae `0.032153`
- 60d: sample `40`, hit `0.625`, avg `0.018082`, median `0.029066`, mae `0.074898`

### breadth_conflicted_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.003871`, median `-0.001658`, mae `0.016103`
- 5d: sample `60`, hit `0.5667`, avg `-0.002696`, median `0.001303`, mae `0.016878`
- 10d: sample `60`, hit `0.4833`, avg `-0.000446`, median `-0.0004`, mae `0.020467`
- 20d: sample `60`, hit `0.6167`, avg `0.005673`, median `0.004241`, mae `0.026689`
- 60d: sample `60`, hit `0.55`, avg `0.008903`, median `0.007258`, mae `0.061024`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002518`, median `0.007619`, mae `0.015772`
- 5d: sample `20`, hit `0.7`, avg `0.006879`, median `0.008593`, mae `0.017461`
- 10d: sample `20`, hit `0.75`, avg `0.015394`, median `0.018412`, mae `0.025936`
- 20d: sample `20`, hit `0.7`, avg `0.019147`, median `0.007676`, mae `0.025335`
- 60d: sample `20`, hit `0.65`, avg `0.038217`, median `0.044771`, mae `0.064909`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002518`, median `0.007619`, mae `0.015772`
- 5d: sample `20`, hit `0.7`, avg `0.006879`, median `0.008593`, mae `0.017461`
- 10d: sample `20`, hit `0.75`, avg `0.015394`, median `0.018412`, mae `0.025936`
- 20d: sample `20`, hit `0.7`, avg `0.019147`, median `0.007676`, mae `0.025335`
- 60d: sample `20`, hit `0.65`, avg `0.038217`, median `0.044771`, mae `0.064909`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002518`, median `0.007619`, mae `0.015772`
- 5d: sample `20`, hit `0.7`, avg `0.006879`, median `0.008593`, mae `0.017461`
- 10d: sample `20`, hit `0.75`, avg `0.015394`, median `0.018412`, mae `0.025936`
- 20d: sample `20`, hit `0.7`, avg `0.019147`, median `0.007676`, mae `0.025335`
- 60d: sample `20`, hit `0.65`, avg `0.038217`, median `0.044771`, mae `0.064909`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.5`, avg `-0.002879`, median `0.003785`, mae `0.017796`
- 5d: sample `40`, hit `0.55`, avg `-0.0015`, median `0.003005`, mae `0.017725`
- 10d: sample `40`, hit `0.525`, avg `0.003039`, median `0.001607`, mae `0.022908`
- 20d: sample `40`, hit `0.675`, avg `0.009661`, median `0.007676`, mae `0.030724`
- 60d: sample `40`, hit `0.6`, avg `0.020872`, median `0.037425`, mae `0.067752`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002518`, median `0.007619`, mae `0.015772`
- 5d: sample `20`, hit `0.7`, avg `0.006879`, median `0.008593`, mae `0.017461`
- 10d: sample `20`, hit `0.75`, avg `0.015394`, median `0.018412`, mae `0.025936`
- 20d: sample `20`, hit `0.7`, avg `0.019147`, median `0.007676`, mae `0.025335`
- 60d: sample `20`, hit `0.65`, avg `0.038217`, median `0.044771`, mae `0.064909`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.002518`, median `0.007619`, mae `0.015772`
- 5d: sample `20`, hit `0.7`, avg `0.006879`, median `0.008593`, mae `0.017461`
- 10d: sample `20`, hit `0.75`, avg `0.015394`, median `0.018412`, mae `0.025936`
- 20d: sample `20`, hit `0.7`, avg `0.019147`, median `0.007676`, mae `0.025335`
- 60d: sample `20`, hit `0.65`, avg `0.038217`, median `0.044771`, mae `0.064909`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.007066`, median `-0.007923`, mae `0.016268`
- 5d: sample `40`, hit `0.5`, avg `-0.007484`, median `0.000415`, mae `0.016586`
- 10d: sample `40`, hit `0.35`, avg `-0.008366`, median `-0.009882`, mae `0.017732`
- 20d: sample `40`, hit `0.575`, avg `-0.001063`, median `0.003675`, mae `0.027366`
- 60d: sample `40`, hit `0.5`, avg `-0.005754`, median `8.1e-05`, mae `0.059082`

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
- 3d: sample `20`, hit `0.6`, avg `-8.1e-05`, median `0.001999`, mae `0.009964`
- 5d: sample `20`, hit `0.5`, avg `0.001551`, median `0.006133`, mae `0.013287`
- 10d: sample `20`, hit `0.3`, avg `-0.011448`, median `-0.013321`, mae `0.022163`
- 20d: sample `20`, hit `0.55`, avg `-1.8e-05`, median `0.005003`, mae `0.038972`
- 60d: sample `20`, hit `0.6`, avg `-0.002054`, median `0.019812`, mae `0.084887`

### surface_only_strength
- sample_size: `40`
- 3d: sample `40`, hit `0.4`, avg `-0.007066`, median `-0.007923`, mae `0.016268`
- 5d: sample `40`, hit `0.5`, avg `-0.007484`, median `0.000415`, mae `0.016586`
- 10d: sample `40`, hit `0.35`, avg `-0.008366`, median `-0.009882`, mae `0.017732`
- 20d: sample `40`, hit `0.575`, avg `-0.001063`, median `0.003675`, mae `0.027366`
- 60d: sample `40`, hit `0.5`, avg `-0.005754`, median `8.1e-05`, mae `0.059082`

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
