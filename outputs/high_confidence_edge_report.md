# High Confidence Edge Report

Generated at: `2026-11-11T07:48:03.305844+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `180`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `180`, gate `stronger_evidence`
- 5d: completed `180`, gate `stronger_evidence`
- 10d: completed `180`, gate `stronger_evidence`
- 20d: completed `180`, gate `stronger_evidence`
- 60d: completed `180`, gate `stronger_evidence`

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
- 3d: sample `60`, hit `0.5333`, avg `0.001162`, median `0.002171`, mae `0.016575`
- 5d: sample `60`, hit `0.5`, avg `0.002148`, median `0.002812`, mae `0.019621`
- 10d: sample `60`, hit `0.65`, avg `0.011377`, median `0.012964`, mae `0.027899`
- 20d: sample `60`, hit `0.7333`, avg `0.020572`, median `0.02604`, mae `0.035301`
- 60d: sample `60`, hit `0.8167`, avg `0.044117`, median `0.056005`, mae `0.064668`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.005067`, median `0.009501`, mae `0.01975`
- 5d: sample `20`, hit `0.75`, avg `0.014461`, median `0.007257`, mae `0.021688`
- 10d: sample `20`, hit `0.7`, avg `0.013376`, median `0.033298`, mae `0.044879`
- 20d: sample `20`, hit `0.75`, avg `0.023544`, median `0.040208`, mae `0.046475`
- 60d: sample `20`, hit `0.95`, avg `0.074653`, median `0.07271`, mae `0.076152`

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
- 3d: sample `8`, hit `0.75`, avg `0.008091`, median `0.018908`, mae `0.020005`
- 5d: sample `8`, hit `0.875`, avg `0.021151`, median `0.032932`, mae `0.028859`
- 10d: sample `8`, hit `1.0`, avg `0.04168`, median `0.050779`, mae `0.04168`
- 20d: sample `8`, hit `1.0`, avg `0.056508`, median `0.056907`, mae `0.056508`
- 60d: sample `8`, hit `1.0`, avg `0.071794`, median `0.066636`, mae `0.071794`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `-0.001563`, median `0.001558`, mae `0.017854`
- 5d: sample `8`, hit `0.375`, avg `0.000921`, median `-0.007346`, mae `0.015631`
- 10d: sample `8`, hit `0.75`, avg `0.014659`, median `0.020918`, mae `0.023115`
- 20d: sample `8`, hit `0.75`, avg `0.021069`, median `0.028264`, mae `0.030353`
- 60d: sample `8`, hit `1.0`, avg `0.067681`, median `0.072891`, mae `0.067681`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.5333, 'avg_return': 0.001162, 'median_return': 0.002171, 'mean_absolute_return': 0.016575, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.033969}, '5d': {'sample_size': 60, 'hit_rate': 0.5, 'avg_return': 0.002148, 'median_return': 0.002812, 'mean_absolute_return': 0.019621, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.65, 'avg_return': 0.011377, 'median_return': 0.012964, 'mean_absolute_return': 0.027899, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.7333, 'avg_return': 0.020572, 'median_return': 0.02604, 'mean_absolute_return': 0.035301, 'max_adverse_excursion': -0.069108, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 60, 'hit_rate': 0.8167, 'avg_return': 0.044117, 'median_return': 0.056005, 'mean_absolute_return': 0.064668, 'max_adverse_excursion': -0.118502, 'max_favorable_excursion': 0.135457}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': -0.001563, 'median_return': 0.001558, 'mean_absolute_return': 0.017854, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.031732}, '5d': {'sample_size': 8, 'hit_rate': 0.375, 'avg_return': 0.000921, 'median_return': -0.007346, 'mean_absolute_return': 0.015631, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.014659, 'median_return': 0.020918, 'mean_absolute_return': 0.023115, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.050979}, '20d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.021069, 'median_return': 0.028264, 'mean_absolute_return': 0.030353, 'max_adverse_excursion': -0.027614, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.067681, 'median_return': 0.072891, 'mean_absolute_return': 0.067681, 'max_adverse_excursion': 0.029831, 'max_favorable_excursion': 0.095045}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.5556, 'avg_return': 0.00255, 'median_return': 0.002574, 'mean_absolute_return': 0.017315, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.005705, 'median_return': 0.005676, 'mean_absolute_return': 0.020638, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.05994}, '10d': {'sample_size': 72, 'hit_rate': 0.6528, 'avg_return': 0.011568, 'median_return': 0.01749, 'mean_absolute_return': 0.033147, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.7361, 'avg_return': 0.021343, 'median_return': 0.027893, 'mean_absolute_return': 0.038955, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.096879}, '60d': {'sample_size': 72, 'hit_rate': 0.8333, 'avg_return': 0.049981, 'median_return': 0.065766, 'mean_absolute_return': 0.067523, 'max_adverse_excursion': -0.118502, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5}, '5d': {'sample_size': 80, 'hit_rate': 0.4375}, '10d': {'sample_size': 80, 'hit_rate': 0.5625}, '20d': {'sample_size': 80, 'hit_rate': 0.6125}, '60d': {'sample_size': 80, 'hit_rate': 0.625}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5, 'secondary_hit_rate': 0.525, 'primary_minus_secondary': -0.025, 'both_hit': 11, 'both_miss': 9}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.15, 'both_hit': 11, 'both_miss': 9}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.5625, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': -0.0125, 'both_hit': 16, 'both_miss': 5}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6125, 'secondary_hit_rate': 0.4875, 'primary_minus_secondary': 0.125, 'both_hit': 14, 'both_miss': 6}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.625, 'secondary_hit_rate': 0.5, 'primary_minus_secondary': 0.125, 'both_hit': 15, 'both_miss': 5}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 60, 'non_close_call_sample_size': 20, 'close_call_metrics': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.55, 'avg_return': 0.002957, 'median_return': 0.002484, 'mean_absolute_return': 0.017235, 'max_adverse_excursion': -0.033574, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 60, 'hit_rate': 0.5667, 'avg_return': 0.005446, 'median_return': 0.004752, 'mean_absolute_return': 0.019027, 'max_adverse_excursion': -0.042713, 'max_favorable_excursion': 0.05994}, '10d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.009188, 'median_return': 0.014227, 'mean_absolute_return': 0.0319, 'max_adverse_excursion': -0.120976, 'max_favorable_excursion': 0.065696}, '20d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.019757, 'median_return': 0.027893, 'mean_absolute_return': 0.037954, 'max_adverse_excursion': -0.099264, 'max_favorable_excursion': 0.096879}, '60d': {'sample_size': 60, 'hit_rate': 0.8833, 'avg_return': 0.05587, 'median_return': 0.068113, 'mean_absolute_return': 0.067051, 'max_adverse_excursion': -0.072844, 'max_favorable_excursion': 0.140054}}}, 'non_close_call_metrics': {'sample_size': 20, 'by_horizon': {'3d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': -0.000317, 'median_return': 0.004886, 'mean_absolute_return': 0.017772, 'max_adverse_excursion': -0.049442, 'max_favorable_excursion': 0.033003}, '5d': {'sample_size': 20, 'hit_rate': 0.55, 'avg_return': 0.004568, 'median_return': 0.006832, 'mean_absolute_return': 0.02347, 'max_adverse_excursion': -0.04049, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 20, 'hit_rate': 0.8, 'avg_return': 0.019944, 'median_return': 0.021778, 'mean_absolute_return': 0.032876, 'max_adverse_excursion': -0.058968, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 20, 'hit_rate': 0.7, 'avg_return': 0.025991, 'median_return': 0.031303, 'mean_absolute_return': 0.038516, 'max_adverse_excursion': -0.060735, 'max_favorable_excursion': 0.088538}, '60d': {'sample_size': 20, 'hit_rate': 0.75, 'avg_return': 0.039396, 'median_return': 0.056005, 'mean_absolute_return': 0.069002, 'max_adverse_excursion': -0.118502, 'max_favorable_excursion': 0.135457}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.001162`, median `0.002171`, mae `0.016575`
- 5d: sample `60`, hit `0.5`, avg `0.002148`, median `0.002812`, mae `0.019621`
- 10d: sample `60`, hit `0.65`, avg `0.011377`, median `0.012964`, mae `0.027899`
- 20d: sample `60`, hit `0.7333`, avg `0.020572`, median `0.02604`, mae `0.035301`
- 60d: sample `60`, hit `0.8167`, avg `0.044117`, median `0.056005`, mae `0.064668`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.005067`, median `0.009501`, mae `0.01975`
- 5d: sample `20`, hit `0.75`, avg `0.014461`, median `0.007257`, mae `0.021688`
- 10d: sample `20`, hit `0.7`, avg `0.013376`, median `0.033298`, mae `0.044879`
- 20d: sample `20`, hit `0.75`, avg `0.023544`, median `0.040208`, mae `0.046475`
- 60d: sample `20`, hit `0.95`, avg `0.074653`, median `0.07271`, mae `0.076152`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.001162`, median `0.002171`, mae `0.016575`
- 5d: sample `60`, hit `0.5`, avg `0.002148`, median `0.002812`, mae `0.019621`
- 10d: sample `60`, hit `0.65`, avg `0.011377`, median `0.012964`, mae `0.027899`
- 20d: sample `60`, hit `0.7333`, avg `0.020572`, median `0.02604`, mae `0.035301`
- 60d: sample `60`, hit `0.8167`, avg `0.044117`, median `0.056005`, mae `0.064668`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001476`, median `0.002574`, mae `0.018147`
- 5d: sample `40`, hit `0.475`, avg `0.002056`, median `-0.00109`, mae `0.020732`
- 10d: sample `40`, hit `0.7`, avg `0.015274`, median `0.01749`, mae `0.029268`
- 20d: sample `40`, hit `0.725`, avg `0.022665`, median `0.027343`, mae `0.036877`
- 60d: sample `40`, hit `0.8`, avg `0.045006`, median `0.064194`, mae `0.069367`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.001162`, median `0.002171`, mae `0.016575`
- 5d: sample `60`, hit `0.5`, avg `0.002148`, median `0.002812`, mae `0.019621`
- 10d: sample `60`, hit `0.65`, avg `0.011377`, median `0.012964`, mae `0.027899`
- 20d: sample `60`, hit `0.7333`, avg `0.020572`, median `0.02604`, mae `0.035301`
- 60d: sample `60`, hit `0.8167`, avg `0.044117`, median `0.056005`, mae `0.064668`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001476`, median `0.002574`, mae `0.018147`
- 5d: sample `40`, hit `0.475`, avg `0.002056`, median `-0.00109`, mae `0.020732`
- 10d: sample `40`, hit `0.7`, avg `0.015274`, median `0.01749`, mae `0.029268`
- 20d: sample `40`, hit `0.725`, avg `0.022665`, median `0.027343`, mae `0.036877`
- 60d: sample `40`, hit `0.8`, avg `0.045006`, median `0.064194`, mae `0.069367`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.005067`, median `0.009501`, mae `0.01975`
- 5d: sample `20`, hit `0.75`, avg `0.014461`, median `0.007257`, mae `0.021688`
- 10d: sample `20`, hit `0.7`, avg `0.013376`, median `0.033298`, mae `0.044879`
- 20d: sample `20`, hit `0.75`, avg `0.023544`, median `0.040208`, mae `0.046475`
- 60d: sample `20`, hit `0.95`, avg `0.074653`, median `0.07271`, mae `0.076152`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.55`, avg `0.001476`, median `0.002574`, mae `0.018147`
- 5d: sample `40`, hit `0.475`, avg `0.002056`, median `-0.00109`, mae `0.020732`
- 10d: sample `40`, hit `0.7`, avg `0.015274`, median `0.01749`, mae `0.029268`
- 20d: sample `40`, hit `0.725`, avg `0.022665`, median `0.027343`, mae `0.036877`
- 60d: sample `40`, hit `0.8`, avg `0.045006`, median `0.064194`, mae `0.069367`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000536`, median `0.002171`, mae `0.013432`
- 5d: sample `20`, hit `0.55`, avg `0.002332`, median `0.006571`, mae `0.017398`
- 10d: sample `20`, hit `0.55`, avg `0.003583`, median `0.009031`, mae `0.025161`
- 20d: sample `20`, hit `0.75`, avg `0.016386`, median `0.02604`, mae `0.03215`
- 60d: sample `20`, hit `0.85`, avg `0.042339`, median `0.052632`, mae `0.055271`

### bounce_with_internal_resonance
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_surface_only
- sample_size: `20`
- 3d: sample `20`, hit `0.5`, avg `0.000536`, median `0.002171`, mae `0.013432`
- 5d: sample `20`, hit `0.55`, avg `0.002332`, median `0.006571`, mae `0.017398`
- 10d: sample `20`, hit `0.55`, avg `0.003583`, median `0.009031`, mae `0.025161`
- 20d: sample `20`, hit `0.75`, avg `0.016386`, median `0.02604`, mae `0.03215`
- 60d: sample `20`, hit `0.85`, avg `0.042339`, median `0.052632`, mae `0.055271`

## Flow / Positioning Proxy Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare flow-confirmed and flow-conflicted buckets before raising confidence.`

### flow_confirmed_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.002138`, median `0.002484`, mae `0.017369`
- 5d: sample `80`, hit `0.5625`, avg `0.005226`, median `0.004752`, mae `0.020138`
- 10d: sample `80`, hit `0.6625`, avg `0.011877`, median `0.01749`, mae `0.032144`
- 20d: sample `80`, hit `0.7375`, avg `0.021315`, median `0.027893`, mae `0.038095`
- 60d: sample `80`, hit `0.85`, avg `0.051751`, median `0.066455`, mae `0.067539`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.55`, avg `0.002138`, median `0.002484`, mae `0.017369`
- 5d: sample `80`, hit `0.5625`, avg `0.005226`, median `0.004752`, mae `0.020138`
- 10d: sample `80`, hit `0.6625`, avg `0.011877`, median `0.01749`, mae `0.032144`
- 20d: sample `80`, hit `0.7375`, avg `0.021315`, median `0.027893`, mae `0.038095`
- 60d: sample `80`, hit `0.85`, avg `0.051751`, median `0.066455`, mae `0.067539`

### bounce_with_flow_support
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.001162`, median `0.002171`, mae `0.016575`
- 5d: sample `60`, hit `0.5`, avg `0.002148`, median `0.002812`, mae `0.019621`
- 10d: sample `60`, hit `0.65`, avg `0.011377`, median `0.012964`, mae `0.027899`
- 20d: sample `60`, hit `0.7333`, avg `0.020572`, median `0.02604`, mae `0.035301`
- 60d: sample `60`, hit `0.8167`, avg `0.044117`, median `0.056005`, mae `0.064668`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.5333`, avg `0.001162`, median `0.002171`, mae `0.016575`
- 5d: sample `60`, hit `0.5`, avg `0.002148`, median `0.002812`, mae `0.019621`
- 10d: sample `60`, hit `0.65`, avg `0.011377`, median `0.012964`, mae `0.027899`
- 20d: sample `60`, hit `0.7333`, avg `0.020572`, median `0.02604`, mae `0.035301`
- 60d: sample `60`, hit `0.8167`, avg `0.044117`, median `0.056005`, mae `0.064668`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.005067`, median `0.009501`, mae `0.01975`
- 5d: sample `20`, hit `0.75`, avg `0.014461`, median `0.007257`, mae `0.021688`
- 10d: sample `20`, hit `0.7`, avg `0.013376`, median `0.033298`, mae `0.044879`
- 20d: sample `20`, hit `0.75`, avg `0.023544`, median `0.040208`, mae `0.046475`
- 60d: sample `20`, hit `0.95`, avg `0.074653`, median `0.07271`, mae `0.076152`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
