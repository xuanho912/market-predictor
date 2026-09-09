# High Confidence Edge Report

Generated at: `2026-09-09T06:02:42.597174+00:00`

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
- sample_size: `20`
- 3d: sample `20`, hit `0.65`, avg `0.001226`, median `0.004487`, mae `0.014237`
- 5d: sample `20`, hit `0.7`, avg `0.00951`, median `0.011391`, mae `0.019419`
- 10d: sample `20`, hit `0.55`, avg `0.005267`, median `0.004883`, mae `0.0271`
- 20d: sample `20`, hit `0.6`, avg `0.009542`, median `0.007572`, mae `0.035049`
- 60d: sample `20`, hit `0.85`, avg `0.034481`, median `0.039842`, mae `0.069657`

### WEAK_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.4667`, avg `-0.001011`, median `-0.001641`, mae `0.013432`
- 5d: sample `60`, hit `0.5167`, avg `-0.002301`, median `0.000415`, mae `0.016683`
- 10d: sample `60`, hit `0.3667`, avg `7.2e-05`, median `-0.007491`, mae `0.022884`
- 20d: sample `60`, hit `0.7`, avg `0.011708`, median `0.02086`, mae `0.036714`
- 60d: sample `60`, hit `0.7167`, avg `0.04339`, median `0.059948`, mae `0.072634`

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
- 3d: sample `8`, hit `0.5`, avg `-0.002268`, median `0.000616`, mae `0.012909`
- 5d: sample `8`, hit `0.75`, avg `0.010126`, median `0.01181`, mae `0.015281`
- 10d: sample `8`, hit `0.375`, avg `-0.001276`, median `-0.011522`, mae `0.030449`
- 20d: sample `8`, hit `0.625`, avg `0.005107`, median `0.007572`, mae `0.039905`
- 60d: sample `8`, hit `0.875`, avg `0.044291`, median `0.085054`, mae `0.080767`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.004996`, median `0.001558`, mae `0.009462`
- 5d: sample `8`, hit `0.25`, avg `-0.008407`, median `-0.012956`, mae `0.015361`
- 10d: sample `8`, hit `0.625`, avg `0.006152`, median `0.019233`, mae `0.019493`
- 20d: sample `8`, hit `0.875`, avg `0.016559`, median `0.029166`, mae `0.024871`
- 60d: sample `8`, hit `0.75`, avg `0.0436`, median `0.059495`, mae `0.062508`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.65, 'avg_return': 0.001226, 'median_return': 0.004487, 'mean_absolute_return': 0.014237, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.026658}, '5d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.00951, 'median_return': 0.011391, 'mean_absolute_return': 0.019419, 'max_adverse_excursion': -0.04784, 'max_favorable_excursion': 0.043092}, '10d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.005267, 'median_return': 0.004883, 'mean_absolute_return': 0.0271, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.059577}, '20d': {'sample_size': 20, 'hit_rate': 0.6, 'avg_return': 0.009542, 'median_return': 0.007572, 'mean_absolute_return': 0.035049, 'max_adverse_excursion': -0.090764, 'max_favorable_excursion': 0.062064}, '60d': {'sample_size': 20, 'hit_rate': 0.85, 'avg_return': 0.034481, 'median_return': 0.039842, 'mean_absolute_return': 0.069657, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.117141}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.004996, 'median_return': 0.001558, 'mean_absolute_return': 0.009462, 'max_adverse_excursion': -0.030499, 'max_favorable_excursion': 0.01018}, '5d': {'sample_size': 8, 'hit_rate': 0.25, 'avg_return': -0.008407, 'median_return': -0.012956, 'mean_absolute_return': 0.015361, 'max_adverse_excursion': -0.031628, 'max_favorable_excursion': 0.023986}, '10d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.006152, 'median_return': 0.019233, 'mean_absolute_return': 0.019493, 'max_adverse_excursion': -0.020281, 'max_favorable_excursion': 0.03085}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.016559, 'median_return': 0.029166, 'mean_absolute_return': 0.024871, 'max_adverse_excursion': -0.033249, 'max_favorable_excursion': 0.033999}, '60d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.0436, 'median_return': 0.059495, 'mean_absolute_return': 0.062508, 'max_adverse_excursion': -0.055503, 'max_favorable_excursion': 0.101282}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5139, 'avg_return': 5.3e-05, 'median_return': 0.000616, 'mean_absolute_return': 0.014097, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 72, 'hit_rate': 0.5972, 'avg_return': 0.001658, 'median_return': 0.002786, 'mean_absolute_return': 0.01759, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 72, 'hit_rate': 0.3889, 'avg_return': 0.00084, 'median_return': -0.007117, 'mean_absolute_return': 0.024431, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.010567, 'median_return': 0.015261, 'mean_absolute_return': 0.037567, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 72, 'hit_rate': 0.75, 'avg_return': 0.040892, 'median_return': 0.058598, 'mean_absolute_return': 0.072933, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.4875}, '5d': {'sample_size': 80, 'hit_rate': 0.5625}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.5}, '60d': {'sample_size': 80, 'hit_rate': 0.55}}`
- primary_vs_secondary: `{'status': 'forward_pending', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.4875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.1, 'both_hit': 13, 'both_miss': 7}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.5375, 'primary_minus_secondary': 0.025, 'both_hit': 14, 'both_miss': 6}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.15, 'both_hit': 11, 'both_miss': 9}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.05, 'both_hit': 12, 'both_miss': 8}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.55, 'secondary_hit_rate': 0.625, 'primary_minus_secondary': -0.075, 'both_hit': 17, 'both_miss': 3}}, 'note': 'Forward samples are still below the minimum gate; primary-vs-secondary remains a historical analog proxy.'}`
- close_call_samples: `{'close_call_sample_size': 80, 'non_close_call_sample_size': 0, 'close_call_metrics': {'sample_size': 80, 'by_horizon': {'3d': {'sample_size': 80, 'hit_rate': 0.5125, 'avg_return': -0.000452, 'median_return': 0.000616, 'mean_absolute_return': 0.013634, 'max_adverse_excursion': -0.052474, 'max_favorable_excursion': 0.037156}, '5d': {'sample_size': 80, 'hit_rate': 0.5625, 'avg_return': 0.000652, 'median_return': 0.001303, 'mean_absolute_return': 0.017367, 'max_adverse_excursion': -0.053538, 'max_favorable_excursion': 0.049624}, '10d': {'sample_size': 80, 'hit_rate': 0.4125, 'avg_return': 0.001371, 'median_return': -0.007011, 'mean_absolute_return': 0.023938, 'max_adverse_excursion': -0.05316, 'max_favorable_excursion': 0.080289}, '20d': {'sample_size': 80, 'hit_rate': 0.675, 'avg_return': 0.011166, 'median_return': 0.020068, 'mean_absolute_return': 0.036298, 'max_adverse_excursion': -0.095492, 'max_favorable_excursion': 0.138891}, '60d': {'sample_size': 80, 'hit_rate': 0.75, 'avg_return': 0.041163, 'median_return': 0.058598, 'mean_absolute_return': 0.07189, 'max_adverse_excursion': -0.145907, 'max_favorable_excursion': 0.19145}}}, 'non_close_call_metrics': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `not_enough_forward_samples`
- evidence_note: `Forward-only breadth attribution is still below the minimum sample gate; these buckets are tracked but not proof.`

### breadth_confirmed_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003443`, median `-0.003594`, mae `0.007894`
- 5d: sample `20`, hit `0.5`, avg `-0.003933`, median `0.000688`, mae `0.010268`
- 10d: sample `20`, hit `0.25`, avg `-0.009551`, median `-0.012383`, mae `0.020848`
- 20d: sample `20`, hit `0.45`, avg `-0.015866`, median `-0.003522`, mae `0.038993`
- 60d: sample `20`, hit `0.5`, avg `0.011287`, median `0.032982`, mae `0.062327`

### breadth_conflicted_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000205`, median `0.002329`, mae `0.016201`
- 5d: sample `40`, hit `0.525`, avg `-0.001485`, median `0.000415`, mae `0.01989`
- 10d: sample `40`, hit `0.425`, avg `0.004884`, median `-0.00367`, mae `0.023901`
- 20d: sample `40`, hit `0.825`, avg `0.025495`, median `0.029166`, mae `0.035574`
- 60d: sample `40`, hit `0.825`, avg `0.059442`, median `0.067551`, mae `0.077788`

### breadth_confirmed_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003443`, median `-0.003594`, mae `0.007894`
- 5d: sample `20`, hit `0.5`, avg `-0.003933`, median `0.000688`, mae `0.010268`
- 10d: sample `20`, hit `0.25`, avg `-0.009551`, median `-0.012383`, mae `0.020848`
- 20d: sample `20`, hit `0.45`, avg `-0.015866`, median `-0.003522`, mae `0.038993`
- 60d: sample `20`, hit `0.5`, avg `0.011287`, median `0.032982`, mae `0.062327`

### breadth_conflicted_bounce_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `-0.002001`, median `0.001558`, mae `0.012742`
- 5d: sample `20`, hit `0.55`, avg `-0.004314`, median `0.000415`, mae `0.013555`
- 10d: sample `20`, hit `0.4`, avg `0.001189`, median `-0.001222`, mae `0.017584`
- 20d: sample `20`, hit `0.8`, avg `0.020325`, median `0.031196`, mae `0.037143`
- 60d: sample `20`, hit `0.75`, avg `0.04366`, median `0.065295`, mae `0.074018`

### breadth_confirmed_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_conflicted_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.525`, avg `0.000205`, median `0.002329`, mae `0.016201`
- 5d: sample `40`, hit `0.525`, avg `-0.001485`, median `0.000415`, mae `0.01989`
- 10d: sample `40`, hit `0.425`, avg `0.004884`, median `-0.00367`, mae `0.023901`
- 20d: sample `40`, hit `0.825`, avg `0.025495`, median `0.029166`, mae `0.035574`
- 60d: sample `40`, hit `0.825`, avg `0.059442`, median `0.067551`, mae `0.077788`

### bounce_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.35`, avg `-0.003443`, median `-0.003594`, mae `0.007894`
- 5d: sample `20`, hit `0.5`, avg `-0.003933`, median `0.000688`, mae `0.010268`
- 10d: sample `20`, hit `0.25`, avg `-0.009551`, median `-0.012383`, mae `0.020848`
- 20d: sample `20`, hit `0.45`, avg `-0.015866`, median `-0.003522`, mae `0.038993`
- 60d: sample `20`, hit `0.5`, avg `0.011287`, median `0.032982`, mae `0.062327`

### bounce_without_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `-0.000387`, median `0.001824`, mae `0.013489`
- 5d: sample `40`, hit `0.625`, avg `0.002598`, median `0.004491`, mae `0.016487`
- 10d: sample `40`, hit `0.475`, avg `0.003228`, median `-0.0004`, mae `0.022342`
- 20d: sample `40`, hit `0.7`, avg `0.014933`, median `0.029166`, mae `0.036096`
- 60d: sample `40`, hit `0.8`, avg `0.03907`, median `0.058598`, mae `0.071838`

### trend_reversal_with_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.002411`, median `0.008973`, mae `0.019661`
- 5d: sample `20`, hit `0.5`, avg `0.001344`, median `0.007909`, mae `0.026226`
- 10d: sample `20`, hit `0.45`, avg `0.008578`, median `-0.00367`, mae `0.030218`
- 20d: sample `20`, hit `0.85`, avg `0.030665`, median `0.025442`, mae `0.034006`
- 60d: sample `20`, hit `0.9`, avg `0.075224`, median `0.079128`, mae `0.081558`

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
- 3d: sample `80`, hit `0.5125`, avg `-0.000452`, median `0.000616`, mae `0.013634`
- 5d: sample `80`, hit `0.5625`, avg `0.000652`, median `0.001303`, mae `0.017367`
- 10d: sample `80`, hit `0.4125`, avg `0.001371`, median `-0.007011`, mae `0.023938`
- 20d: sample `80`, hit `0.675`, avg `0.011166`, median `0.020068`, mae `0.036298`
- 60d: sample `80`, hit `0.75`, avg `0.041163`, median `0.058598`, mae `0.07189`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `60`
- 3d: sample `60`, hit `0.5`, avg `-0.001406`, median `0.000603`, mae `0.011624`
- 5d: sample `60`, hit `0.5833`, avg `0.000421`, median `0.001303`, mae `0.014414`
- 10d: sample `60`, hit `0.4`, avg `-0.001032`, median `-0.007011`, mae `0.021844`
- 20d: sample `60`, hit `0.6167`, avg `0.004667`, median `0.013877`, mae `0.037061`
- 60d: sample `60`, hit `0.7`, avg `0.029809`, median `0.046132`, mae `0.068668`

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
