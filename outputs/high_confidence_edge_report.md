# High Confidence Edge Report

Generated at: `2026-11-05T03:28:51.792129+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `164`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `164`, gate `stronger_evidence`
- 5d: completed `164`, gate `stronger_evidence`
- 10d: completed `164`, gate `stronger_evidence`
- 20d: completed `164`, gate `stronger_evidence`
- 60d: completed `164`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.6167`, avg `0.003135`, median `0.006372`, mae `0.015377`
- 5d: sample `60`, hit `0.6167`, avg `0.008235`, median `0.011065`, mae `0.020419`
- 10d: sample `60`, hit `0.7`, avg `0.015829`, median `0.02025`, mae `0.031021`
- 20d: sample `60`, hit `0.75`, avg `0.024612`, median `0.030239`, mae `0.040229`
- 60d: sample `60`, hit `0.7167`, avg `0.038485`, median `0.054522`, mae `0.062115`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.004511`, median `0.000543`, mae `0.021448`
- 5d: sample `20`, hit `0.55`, avg `0.008093`, median `0.004752`, mae `0.026674`
- 10d: sample `20`, hit `0.8`, avg `0.033389`, median `0.033298`, mae `0.037348`
- 20d: sample `20`, hit `0.95`, avg `0.05737`, median `0.057896`, mae `0.065004`
- 60d: sample `20`, hit `0.85`, avg `0.064645`, median `0.068113`, mae `0.068614`

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
- 3d: sample `8`, hit `0.625`, avg `0.005346`, median `0.013154`, mae `0.012917`
- 5d: sample `8`, hit `0.625`, avg `0.006265`, median `0.006712`, mae `0.016662`
- 10d: sample `8`, hit `0.625`, avg `0.011401`, median `0.030403`, mae `0.033108`
- 20d: sample `8`, hit `0.75`, avg `0.016085`, median `0.028859`, mae `0.039018`
- 60d: sample `8`, hit `0.75`, avg `0.032459`, median `0.052632`, mae `0.058848`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.875`, avg `0.017581`, median `0.02433`, mae `0.018034`
- 5d: sample `8`, hit `0.75`, avg `0.016446`, median `0.025502`, mae `0.023942`
- 10d: sample `8`, hit `0.875`, avg `0.029618`, median `0.050979`, mae `0.042346`
- 20d: sample `8`, hit `0.875`, avg `0.035665`, median `0.065204`, mae `0.052942`
- 60d: sample `8`, hit `0.875`, avg `0.062042`, median `0.073586`, mae `0.067075`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.003135, 'median_return': 0.006372, 'mean_absolute_return': 0.015377, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.033003}, '5d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.008235, 'median_return': 0.011065, 'mean_absolute_return': 0.020419, 'max_adverse_excursion': -0.04049, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.7, 'avg_return': 0.015829, 'median_return': 0.02025, 'mean_absolute_return': 0.031021, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.024612, 'median_return': 0.030239, 'mean_absolute_return': 0.040229, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.038485, 'median_return': 0.054522, 'mean_absolute_return': 0.062115, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.136877}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.017581, 'median_return': 0.02433, 'mean_absolute_return': 0.018034, 'max_adverse_excursion': -0.001811, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.016446, 'median_return': 0.025502, 'mean_absolute_return': 0.023942, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.029618, 'median_return': 0.050979, 'mean_absolute_return': 0.042346, 'max_adverse_excursion': -0.050912, 'max_favorable_excursion': 0.060273}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.035665, 'median_return': 0.065204, 'mean_absolute_return': 0.052942, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.062042, 'median_return': 0.073586, 'mean_absolute_return': 0.067075, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.105209}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.001912, 'median_return': 0.004699, 'mean_absolute_return': 0.016769, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.007283, 'median_return': 0.007257, 'mean_absolute_return': 0.021765, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.019175, 'median_return': 0.021778, 'mean_absolute_return': 0.03152, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7917, 'avg_return': 0.032484, 'median_return': 0.041918, 'mean_absolute_return': 0.045698, 'max_adverse_excursion': -0.076338, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.043134, 'median_return': 0.057111, 'mean_absolute_return': 0.063369, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.575}, '10d': {'sample_size': 80, 'hit_rate': 0.575}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.5625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': 0.0, 'both_hit': 37, 'both_miss': 23}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.6, 'primary_minus_secondary': -0.025, 'both_hit': 37, 'both_miss': 23}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.15, 'both_hit': 42, 'both_miss': 18}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.8, 'primary_minus_secondary': -0.225, 'both_hit': 45, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.75, 'primary_minus_secondary': -0.1875, 'both_hit': 43, 'both_miss': 18}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.003247, 'median_return': 0.007176, 'mean_absolute_return': 0.019519, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.011285, 'median_return': 0.012136, 'mean_absolute_return': 0.025583, 'max_adverse_excursion': -0.045128, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.028635, 'median_return': 0.032111, 'mean_absolute_return': 0.034884, 'max_adverse_excursion': -0.037736, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 40, 'hit_rate': 0.825, 'avg_return': 0.040093, 'median_return': 0.053017, 'mean_absolute_return': 0.054738, 'max_adverse_excursion': -0.076338, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.05718, 'median_return': 0.066455, 'mean_absolute_return': 0.066461, 'max_adverse_excursion': -0.090957, 'max_favorable_excursion': 0.140054}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.003712, 'median_return': 0.006228, 'mean_absolute_return': 0.014271, 'max_adverse_excursion': -0.028191, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 40, 'hit_rate': 0.55, 'avg_return': 0.005113, 'median_return': 0.006571, 'mean_absolute_return': 0.018383, 'max_adverse_excursion': -0.033198, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.011803, 'median_return': 0.018086, 'mean_absolute_return': 0.030322, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.060273}, '20d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.025511, 'median_return': 0.028859, 'mean_absolute_return': 0.038107, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.03287, 'median_return': 0.052632, 'mean_absolute_return': 0.061018, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.10846}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003135`, median `0.006372`, mae `0.015377`
- 5d: sample `60`, hit `0.6167`, avg `0.008235`, median `0.011065`, mae `0.020419`
- 10d: sample `60`, hit `0.7`, avg `0.015829`, median `0.02025`, mae `0.031021`
- 20d: sample `60`, hit `0.75`, avg `0.024612`, median `0.030239`, mae `0.040229`
- 60d: sample `60`, hit `0.7167`, avg `0.038485`, median `0.054522`, mae `0.062115`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.004511`, median `0.000543`, mae `0.021448`
- 5d: sample `20`, hit `0.55`, avg `0.008093`, median `0.004752`, mae `0.026674`
- 10d: sample `20`, hit `0.8`, avg `0.033389`, median `0.033298`, mae `0.037348`
- 20d: sample `20`, hit `0.95`, avg `0.05737`, median `0.057896`, mae `0.065004`
- 60d: sample `20`, hit `0.85`, avg `0.064645`, median `0.068113`, mae `0.068614`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003135`, median `0.006372`, mae `0.015377`
- 5d: sample `60`, hit `0.6167`, avg `0.008235`, median `0.011065`, mae `0.020419`
- 10d: sample `60`, hit `0.7`, avg `0.015829`, median `0.02025`, mae `0.031021`
- 20d: sample `60`, hit `0.75`, avg `0.024612`, median `0.030239`, mae `0.040229`
- 60d: sample `60`, hit `0.7167`, avg `0.038485`, median `0.054522`, mae `0.062115`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001982`, median `0.009101`, mae `0.017589`
- 5d: sample `20`, hit `0.75`, avg `0.014477`, median `0.020876`, mae `0.024492`
- 10d: sample `20`, hit `0.8`, avg `0.023881`, median `0.025759`, mae `0.032419`
- 20d: sample `20`, hit `0.7`, avg `0.022815`, median `0.043233`, mae `0.044472`
- 60d: sample `20`, hit `0.7`, avg `0.049714`, median `0.064194`, mae `0.064307`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003135`, median `0.006372`, mae `0.015377`
- 5d: sample `60`, hit `0.6167`, avg `0.008235`, median `0.011065`, mae `0.020419`
- 10d: sample `60`, hit `0.7`, avg `0.015829`, median `0.02025`, mae `0.031021`
- 20d: sample `60`, hit `0.75`, avg `0.024612`, median `0.030239`, mae `0.040229`
- 60d: sample `60`, hit `0.7167`, avg `0.038485`, median `0.054522`, mae `0.062115`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001982`, median `0.009101`, mae `0.017589`
- 5d: sample `20`, hit `0.75`, avg `0.014477`, median `0.020876`, mae `0.024492`
- 10d: sample `20`, hit `0.8`, avg `0.023881`, median `0.025759`, mae `0.032419`
- 20d: sample `20`, hit `0.7`, avg `0.022815`, median `0.043233`, mae `0.044472`
- 60d: sample `20`, hit `0.7`, avg `0.049714`, median `0.064194`, mae `0.064307`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.004511`, median `0.000543`, mae `0.021448`
- 5d: sample `20`, hit `0.55`, avg `0.008093`, median `0.004752`, mae `0.026674`
- 10d: sample `20`, hit `0.8`, avg `0.033389`, median `0.033298`, mae `0.037348`
- 20d: sample `20`, hit `0.95`, avg `0.05737`, median `0.057896`, mae `0.065004`
- 60d: sample `20`, hit `0.85`, avg `0.064645`, median `0.068113`, mae `0.068614`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.003712`, median `0.006228`, mae `0.014271`
- 5d: sample `40`, hit `0.55`, avg `0.005113`, median `0.006571`, mae `0.018383`
- 10d: sample `40`, hit `0.65`, avg `0.011803`, median `0.018086`, mae `0.030322`
- 20d: sample `40`, hit `0.775`, avg `0.025511`, median `0.028859`, mae `0.038107`
- 60d: sample `40`, hit `0.725`, avg `0.03287`, median `0.052632`, mae `0.061018`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.001982`, median `0.009101`, mae `0.017589`
- 5d: sample `20`, hit `0.75`, avg `0.014477`, median `0.020876`, mae `0.024492`
- 10d: sample `20`, hit `0.8`, avg `0.023881`, median `0.025759`, mae `0.032419`
- 20d: sample `20`, hit `0.7`, avg `0.022815`, median `0.043233`, mae `0.044472`
- 60d: sample `20`, hit `0.7`, avg `0.049714`, median `0.064194`, mae `0.064307`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.625`, avg `0.003712`, median `0.006228`, mae `0.014271`
- 5d: sample `40`, hit `0.55`, avg `0.005113`, median `0.006571`, mae `0.018383`
- 10d: sample `40`, hit `0.65`, avg `0.011803`, median `0.018086`, mae `0.030322`
- 20d: sample `40`, hit `0.775`, avg `0.025511`, median `0.028859`, mae `0.038107`
- 60d: sample `40`, hit `0.725`, avg `0.03287`, median `0.052632`, mae `0.061018`

### bounce_surface_only
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.003479`, median `0.006228`, mae `0.016895`
- 5d: sample `80`, hit `0.6`, avg `0.008199`, median `0.007479`, mae `0.021983`
- 10d: sample `80`, hit `0.725`, avg `0.020219`, median `0.023889`, mae `0.032603`
- 20d: sample `80`, hit `0.8`, avg `0.032802`, median `0.041918`, mae `0.046422`
- 60d: sample `80`, hit `0.75`, avg `0.045025`, median `0.057501`, mae `0.06374`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.5875`, avg `0.003479`, median `0.006228`, mae `0.016895`
- 5d: sample `80`, hit `0.6`, avg `0.008199`, median `0.007479`, mae `0.021983`
- 10d: sample `80`, hit `0.725`, avg `0.020219`, median `0.023889`, mae `0.032603`
- 20d: sample `80`, hit `0.8`, avg `0.032802`, median `0.041918`, mae `0.046422`
- 60d: sample `80`, hit `0.75`, avg `0.045025`, median `0.057501`, mae `0.06374`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003135`, median `0.006372`, mae `0.015377`
- 5d: sample `60`, hit `0.6167`, avg `0.008235`, median `0.011065`, mae `0.020419`
- 10d: sample `60`, hit `0.7`, avg `0.015829`, median `0.02025`, mae `0.031021`
- 20d: sample `60`, hit `0.75`, avg `0.024612`, median `0.030239`, mae `0.040229`
- 60d: sample `60`, hit `0.7167`, avg `0.038485`, median `0.054522`, mae `0.062115`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6167`, avg `0.003135`, median `0.006372`, mae `0.015377`
- 5d: sample `60`, hit `0.6167`, avg `0.008235`, median `0.011065`, mae `0.020419`
- 10d: sample `60`, hit `0.7`, avg `0.015829`, median `0.02025`, mae `0.031021`
- 20d: sample `60`, hit `0.75`, avg `0.024612`, median `0.030239`, mae `0.040229`
- 60d: sample `60`, hit `0.7167`, avg `0.038485`, median `0.054522`, mae `0.062115`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.004511`, median `0.000543`, mae `0.021448`
- 5d: sample `20`, hit `0.55`, avg `0.008093`, median `0.004752`, mae `0.026674`
- 10d: sample `20`, hit `0.8`, avg `0.033389`, median `0.033298`, mae `0.037348`
- 20d: sample `20`, hit `0.95`, avg `0.05737`, median `0.057896`, mae `0.065004`
- 60d: sample `20`, hit `0.85`, avg `0.064645`, median `0.068113`, mae `0.068614`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
