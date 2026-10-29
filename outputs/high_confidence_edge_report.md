# High Confidence Edge Report

Generated at: `2026-10-29T10:26:36.141883+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `144`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `historical_proxy_supports_higher_confidence_but_forward_validation_required`

## Forward Sample Gates

- 3d: completed `144`, gate `stronger_evidence`
- 5d: completed `144`, gate `stronger_evidence`
- 10d: completed `144`, gate `stronger_evidence`
- 20d: completed `144`, gate `stronger_evidence`
- 60d: completed `144`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004511`, median `0.004886`, mae `0.013748`
- 5d: sample `60`, hit `0.6167`, avg `0.007134`, median `0.00971`, mae `0.019618`
- 10d: sample `60`, hit `0.7833`, avg `0.015998`, median `0.019702`, mae `0.026679`
- 20d: sample `60`, hit `0.75`, avg `0.02093`, median `0.028626`, mae `0.036157`
- 60d: sample `60`, hit `0.7167`, avg `0.031908`, median `0.055822`, mae `0.067153`

### MODERATE_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### WEAK_EDGE
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001275`, median `0.003865`, mae `0.016905`
- 5d: sample `20`, hit `0.45`, avg `-0.001891`, median `-0.00459`, mae `0.021909`
- 10d: sample `20`, hit `0.55`, avg `-6.9e-05`, median `0.004865`, mae `0.02724`
- 20d: sample `20`, hit `0.6`, avg `0.010388`, median `0.002548`, mae `0.0327`
- 60d: sample `20`, hit `0.75`, avg `0.044542`, median `0.055515`, mae `0.0798`

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
- 3d: sample `8`, hit `0.625`, avg `0.003864`, median `0.004243`, mae `0.015101`
- 5d: sample `8`, hit `0.5`, avg `0.008008`, median `0.013109`, mae `0.020881`
- 10d: sample `8`, hit `0.75`, avg `0.019334`, median `0.023979`, mae `0.02779`
- 20d: sample `8`, hit `0.875`, avg `0.033152`, median `0.031196`, mae `0.035534`
- 60d: sample `8`, hit `0.875`, avg `0.061844`, median `0.073586`, mae `0.066877`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.625`, avg `0.003864`, median `0.004243`, mae `0.015101`
- 5d: sample `8`, hit `0.5`, avg `0.008008`, median `0.013109`, mae `0.020881`
- 10d: sample `8`, hit `0.75`, avg `0.019334`, median `0.023979`, mae `0.02779`
- 20d: sample `8`, hit `0.875`, avg `0.033152`, median `0.031196`, mae `0.035534`
- 60d: sample `8`, hit `0.875`, avg `0.061844`, median `0.073586`, mae `0.066877`

### confidence validation
- `{'strong_edge': {'sample_size': 60, 'by_horizon': {'3d': {'sample_size': 60, 'hit_rate': 0.6333, 'avg_return': 0.004511, 'median_return': 0.004886, 'mean_absolute_return': 0.013748, 'max_adverse_excursion': -0.028651, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 60, 'hit_rate': 0.6167, 'avg_return': 0.007134, 'median_return': 0.00971, 'mean_absolute_return': 0.019618, 'max_adverse_excursion': -0.036194, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 60, 'hit_rate': 0.7833, 'avg_return': 0.015998, 'median_return': 0.019702, 'mean_absolute_return': 0.026679, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 60, 'hit_rate': 0.75, 'avg_return': 0.02093, 'median_return': 0.028626, 'mean_absolute_return': 0.036157, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 60, 'hit_rate': 0.7167, 'avg_return': 0.031908, 'median_return': 0.055822, 'mean_absolute_return': 0.067153, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.139935}}}, 'moderate_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.625, 'avg_return': 0.003864, 'median_return': 0.004243, 'mean_absolute_return': 0.015101, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.008008, 'median_return': 0.013109, 'mean_absolute_return': 0.020881, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.75, 'avg_return': 0.019334, 'median_return': 0.023979, 'mean_absolute_return': 0.02779, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.054167}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.033152, 'median_return': 0.031196, 'mean_absolute_return': 0.035534, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.061844, 'median_return': 0.073586, 'mean_absolute_return': 0.066877, 'max_adverse_excursion': -0.02013, 'max_favorable_excursion': 0.101208}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.6111, 'avg_return': 0.003684, 'median_return': 0.004886, 'mean_absolute_return': 0.014474, 'max_adverse_excursion': -0.028651, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 72, 'hit_rate': 0.5833, 'avg_return': 0.00453, 'median_return': 0.00774, 'mean_absolute_return': 0.020114, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 72, 'hit_rate': 0.7222, 'avg_return': 0.011164, 'median_return': 0.010559, 'mean_absolute_return': 0.026712, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 72, 'hit_rate': 0.6944, 'avg_return': 0.016644, 'median_return': 0.018293, 'mean_absolute_return': 0.035266, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.032091, 'median_return': 0.05455, 'mean_absolute_return': 0.070697, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.188184}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.5875}, '5d': {'sample_size': 80, 'hit_rate': 0.6}, '10d': {'sample_size': 80, 'hit_rate': 0.7}, '20d': {'sample_size': 80, 'hit_rate': 0.6625}, '60d': {'sample_size': 80, 'hit_rate': 0.6}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.5875, 'secondary_hit_rate': 0.6125, 'primary_minus_secondary': -0.025, 'both_hit': 38, 'both_miss': 22}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.575, 'primary_minus_secondary': 0.025, 'both_hit': 37, 'both_miss': 23}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.7, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.025, 'both_hit': 47, 'both_miss': 13}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.6625, 'secondary_hit_rate': 0.7125, 'primary_minus_secondary': -0.05, 'both_hit': 45, 'both_miss': 15}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.6, 'secondary_hit_rate': 0.725, 'primary_minus_secondary': -0.125, 'both_hit': 43, 'both_miss': 17}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.002195, 'median_return': 0.004886, 'mean_absolute_return': 0.015515, 'max_adverse_excursion': -0.028651, 'max_favorable_excursion': 0.039385}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.004414, 'median_return': 0.009561, 'mean_absolute_return': 0.02172, 'max_adverse_excursion': -0.037279, 'max_favorable_excursion': 0.049428}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.0117, 'median_return': 0.010559, 'mean_absolute_return': 0.029155, 'max_adverse_excursion': -0.070586, 'max_favorable_excursion': 0.070075}, '20d': {'sample_size': 40, 'hit_rate': 0.625, 'avg_return': 0.012281, 'median_return': 0.018082, 'mean_absolute_return': 0.040688, 'max_adverse_excursion': -0.209364, 'max_favorable_excursion': 0.086431}, '60d': {'sample_size': 40, 'hit_rate': 0.775, 'avg_return': 0.037063, 'median_return': 0.056005, 'mean_absolute_return': 0.081975, 'max_adverse_excursion': -0.231866, 'max_favorable_excursion': 0.188184}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.005209, 'median_return': 0.004569, 'mean_absolute_return': 0.013559, 'max_adverse_excursion': -0.028191, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 40, 'hit_rate': 0.575, 'avg_return': 0.005342, 'median_return': 0.007324, 'mean_absolute_return': 0.018662, 'max_adverse_excursion': -0.033198, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.012262, 'median_return': 0.012964, 'mean_absolute_return': 0.024484, 'max_adverse_excursion': -0.062902, 'max_favorable_excursion': 0.060273}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.024308, 'median_return': 0.028264, 'mean_absolute_return': 0.029897, 'max_adverse_excursion': -0.030715, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.675, 'avg_return': 0.033069, 'median_return': 0.049084, 'mean_absolute_return': 0.058655, 'max_adverse_excursion': -0.077263, 'max_favorable_excursion': 0.105571}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004511`, median `0.004886`, mae `0.013748`
- 5d: sample `60`, hit `0.6167`, avg `0.007134`, median `0.00971`, mae `0.019618`
- 10d: sample `60`, hit `0.7833`, avg `0.015998`, median `0.019702`, mae `0.026679`
- 20d: sample `60`, hit `0.75`, avg `0.02093`, median `0.028626`, mae `0.036157`
- 60d: sample `60`, hit `0.7167`, avg `0.031908`, median `0.055822`, mae `0.067153`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001275`, median `0.003865`, mae `0.016905`
- 5d: sample `20`, hit `0.45`, avg `-0.001891`, median `-0.00459`, mae `0.021909`
- 10d: sample `20`, hit `0.55`, avg `-6.9e-05`, median `0.004865`, mae `0.02724`
- 20d: sample `20`, hit `0.6`, avg `0.010388`, median `0.002548`, mae `0.0327`
- 60d: sample `20`, hit `0.75`, avg `0.044542`, median `0.055515`, mae `0.0798`

### breadth_confirmed_bounce_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004511`, median `0.004886`, mae `0.013748`
- 5d: sample `60`, hit `0.6167`, avg `0.007134`, median `0.00971`, mae `0.019618`
- 10d: sample `60`, hit `0.7833`, avg `0.015998`, median `0.019702`, mae `0.026679`
- 20d: sample `60`, hit `0.75`, avg `0.02093`, median `0.028626`, mae `0.036157`
- 60d: sample `60`, hit `0.7167`, avg `0.031908`, median `0.055822`, mae `0.067153`

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
- 3d: sample `60`, hit `0.6333`, avg `0.004511`, median `0.004886`, mae `0.013748`
- 5d: sample `60`, hit `0.6167`, avg `0.007134`, median `0.00971`, mae `0.019618`
- 10d: sample `60`, hit `0.7833`, avg `0.015998`, median `0.019702`, mae `0.026679`
- 20d: sample `60`, hit `0.75`, avg `0.02093`, median `0.028626`, mae `0.036157`
- 60d: sample `60`, hit `0.7167`, avg `0.031908`, median `0.055822`, mae `0.067153`

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
- 3d: sample `20`, hit `0.55`, avg `0.001275`, median `0.003865`, mae `0.016905`
- 5d: sample `20`, hit `0.45`, avg `-0.001891`, median `-0.00459`, mae `0.021909`
- 10d: sample `20`, hit `0.55`, avg `-6.9e-05`, median `0.004865`, mae `0.02724`
- 20d: sample `20`, hit `0.6`, avg `0.010388`, median `0.002548`, mae `0.0327`
- 60d: sample `20`, hit `0.75`, avg `0.044542`, median `0.055515`, mae `0.0798`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.005001`, median `0.004243`, mae `0.017881`
- 5d: sample `20`, hit `0.5`, avg `0.004708`, median `0.00971`, mae `0.021918`
- 10d: sample `20`, hit `0.7`, avg `0.016815`, median `0.020918`, mae `0.026566`
- 20d: sample `20`, hit `0.85`, avg `0.032039`, median `0.028791`, mae `0.036557`
- 60d: sample `20`, hit `0.8`, avg `0.053609`, median `0.073778`, mae `0.068753`

### mixed_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.675`, avg `0.004266`, median `0.005785`, mae `0.011681`
- 5d: sample `40`, hit `0.675`, avg `0.008348`, median `0.010187`, mae `0.018468`
- 10d: sample `40`, hit `0.825`, avg `0.015589`, median `0.019702`, mae `0.026736`
- 20d: sample `40`, hit `0.7`, avg `0.015376`, median `0.025541`, mae `0.035957`
- 60d: sample `40`, hit `0.675`, avg `0.021057`, median `0.044733`, mae `0.066354`

### surface_only_strength
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001275`, median `0.003865`, mae `0.016905`
- 5d: sample `20`, hit `0.45`, avg `-0.001891`, median `-0.00459`, mae `0.021909`
- 10d: sample `20`, hit `0.55`, avg `-6.9e-05`, median `0.004865`, mae `0.02724`
- 20d: sample `20`, hit `0.6`, avg `0.010388`, median `0.002548`, mae `0.0327`
- 60d: sample `20`, hit `0.75`, avg `0.044542`, median `0.055515`, mae `0.0798`

### bounce_with_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.005001`, median `0.004243`, mae `0.017881`
- 5d: sample `20`, hit `0.5`, avg `0.004708`, median `0.00971`, mae `0.021918`
- 10d: sample `20`, hit `0.7`, avg `0.016815`, median `0.020918`, mae `0.026566`
- 20d: sample `20`, hit `0.85`, avg `0.032039`, median `0.028791`, mae `0.036557`
- 60d: sample `20`, hit `0.8`, avg `0.053609`, median `0.073778`, mae `0.068753`

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
- sample_size: `40`
- 3d: sample `40`, hit `0.575`, avg `0.002195`, median `0.004886`, mae `0.015515`
- 5d: sample `40`, hit `0.575`, avg `0.004414`, median `0.009561`, mae `0.02172`
- 10d: sample `40`, hit `0.725`, avg `0.0117`, median `0.010559`, mae `0.029155`
- 20d: sample `40`, hit `0.625`, avg `0.012281`, median `0.018082`, mae `0.040688`
- 60d: sample `40`, hit `0.775`, avg `0.037063`, median `0.056005`, mae `0.081975`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.6125`, avg `0.003702`, median `0.004569`, mae `0.014537`
- 5d: sample `80`, hit `0.575`, avg `0.004878`, median `0.00774`, mae `0.020191`
- 10d: sample `80`, hit `0.725`, avg `0.011981`, median `0.012215`, mae `0.026819`
- 20d: sample `80`, hit `0.7125`, avg `0.018295`, median `0.025541`, mae `0.035293`
- 60d: sample `80`, hit `0.725`, avg `0.035066`, median `0.055515`, mae `0.070315`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.6`, avg `0.003115`, median `0.005785`, mae `0.014125`
- 5d: sample `20`, hit `0.7`, avg `0.010719`, median `0.017768`, mae `0.021531`
- 10d: sample `20`, hit `0.9`, avg `0.023469`, median `0.021778`, mae `0.03107`
- 20d: sample `20`, hit `0.65`, avg `0.014175`, median `0.042224`, mae `0.048676`
- 60d: sample `20`, hit `0.8`, avg `0.029584`, median `0.064194`, mae `0.08415`

### bounce_with_flow_conflict
- sample_size: `60`
- 3d: sample `60`, hit `0.6333`, avg `0.004511`, median `0.004886`, mae `0.013748`
- 5d: sample `60`, hit `0.6167`, avg `0.007134`, median `0.00971`, mae `0.019618`
- 10d: sample `60`, hit `0.7833`, avg `0.015998`, median `0.019702`, mae `0.026679`
- 20d: sample `60`, hit `0.75`, avg `0.02093`, median `0.028626`, mae `0.036157`
- 60d: sample `60`, hit `0.7167`, avg `0.031908`, median `0.055822`, mae `0.067153`

### risk_path_with_flow_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.55`, avg `0.001275`, median `0.003865`, mae `0.016905`
- 5d: sample `20`, hit `0.45`, avg `-0.001891`, median `-0.00459`, mae `0.021909`
- 10d: sample `20`, hit `0.55`, avg `-6.9e-05`, median `0.004865`, mae `0.02724`
- 20d: sample `20`, hit `0.6`, avg `0.010388`, median `0.002548`, mae `0.0327`
- 60d: sample `20`, hit `0.75`, avg `0.044542`, median `0.055515`, mae `0.0798`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
