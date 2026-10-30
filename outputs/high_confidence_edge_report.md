# High Confidence Edge Report

Generated at: `2026-10-30T18:09:39.507993+00:00`

Status: `historical_proxy_and_forward_pending`
Sample size: `80`
Forward completed sample size: `152`
Forward validation notice: `Forward samples have started to mature, but alpha status remains research-only until stability is proven.`
Conclusion: `not_enough_strong_edge_samples`

## Forward Sample Gates

- 3d: completed `152`, gate `stronger_evidence`
- 5d: completed `152`, gate `stronger_evidence`
- 10d: completed `152`, gate `stronger_evidence`
- 20d: completed `152`, gate `stronger_evidence`
- 60d: completed `152`, gate `stronger_evidence`

## By Edge Status

### STRONG_EDGE
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### MODERATE_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

### WEAK_EDGE
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.002992`, median `-0.004006`, mae `0.021799`
- 5d: sample `40`, hit `0.65`, avg `0.003579`, median `0.012471`, mae `0.029534`
- 10d: sample `40`, hit `0.725`, avg `0.014265`, median `0.0211`, mae `0.039436`
- 20d: sample `40`, hit `0.65`, avg `0.020164`, median `0.035101`, mae `0.052533`
- 60d: sample `40`, hit `0.725`, avg `0.02961`, median `0.030649`, mae `0.052082`

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
- 3d: sample `8`, hit `0.375`, avg `-0.001501`, median `-0.003228`, mae `0.014558`
- 5d: sample `8`, hit `0.5`, avg `0.003122`, median `0.006571`, mae `0.016965`
- 10d: sample `8`, hit `0.5`, avg `0.002094`, median `0.006878`, mae `0.032627`
- 20d: sample `8`, hit `0.625`, avg `0.019394`, median `0.028589`, mae `0.033465`
- 60d: sample `8`, hit `0.75`, avg `0.029337`, median `0.043989`, mae `0.047533`

### confidence_score top 10%
- sample_size: `8`
- 3d: sample `8`, hit `0.5`, avg `0.007121`, median `0.004243`, mae `0.016131`
- 5d: sample `8`, hit `0.5`, avg `0.010503`, median `0.013109`, mae `0.018765`
- 10d: sample `8`, hit `0.5`, avg `0.017916`, median `0.023979`, mae `0.029367`
- 20d: sample `8`, hit `0.875`, avg `0.036171`, median `0.031658`, mae `0.038552`
- 60d: sample `8`, hit `1.0`, avg `0.078997`, median `0.074055`, mae `0.078997`

### confidence validation
- `{'strong_edge': {'sample_size': 0, 'by_horizon': {'3d': {'sample_size': 0}, '5d': {'sample_size': 0}, '10d': {'sample_size': 0}, '20d': {'sample_size': 0}, '60d': {'sample_size': 0}}}, 'moderate_edge': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.001613, 'median_return': -0.000756, 'mean_absolute_return': 0.016806, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.004751, 'median_return': -0.003328, 'mean_absolute_return': 0.018234, 'max_adverse_excursion': -0.03028, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.013506, 'median_return': 0.017689, 'mean_absolute_return': 0.027833, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.030718, 'median_return': 0.031196, 'mean_absolute_return': 0.039927, 'max_adverse_excursion': -0.045992, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.060215, 'median_return': 0.072365, 'mean_absolute_return': 0.067554, 'max_adverse_excursion': -0.056528, 'max_favorable_excursion': 0.135454}}}, 'confidence_top_10': {'sample_size': 8, 'by_horizon': {'3d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.007121, 'median_return': 0.004243, 'mean_absolute_return': 0.016131, 'max_adverse_excursion': -0.026999, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.010503, 'median_return': 0.013109, 'mean_absolute_return': 0.018765, 'max_adverse_excursion': -0.016952, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 8, 'hit_rate': 0.5, 'avg_return': 0.017916, 'median_return': 0.023979, 'mean_absolute_return': 0.029367, 'max_adverse_excursion': -0.021975, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 8, 'hit_rate': 0.875, 'avg_return': 0.036171, 'median_return': 0.031658, 'mean_absolute_return': 0.038552, 'max_adverse_excursion': -0.009524, 'max_favorable_excursion': 0.074271}, '60d': {'sample_size': 8, 'hit_rate': 1.0, 'avg_return': 0.078997, 'median_return': 0.074055, 'mean_absolute_return': 0.078997, 'max_adverse_excursion': 0.054522, 'max_favorable_excursion': 0.105209}}}, 'ordinary_confidence': {'sample_size': 72, 'by_horizon': {'3d': {'sample_size': 72, 'hit_rate': 0.4444, 'avg_return': -0.001557, 'median_return': -0.004006, 'mean_absolute_return': 0.019655, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 72, 'hit_rate': 0.5694, 'avg_return': 0.003461, 'median_return': 0.007479, 'mean_absolute_return': 0.024452, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 72, 'hit_rate': 0.6806, 'avg_return': 0.013438, 'median_return': 0.020244, 'mean_absolute_return': 0.034109, 'max_adverse_excursion': -0.124781, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 72, 'hit_rate': 0.7083, 'avg_return': 0.024249, 'median_return': 0.034842, 'mean_absolute_return': 0.047083, 'max_adverse_excursion': -0.133308, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 72, 'hit_rate': 0.7778, 'avg_return': 0.041125, 'median_return': 0.05488, 'mean_absolute_return': 0.057687, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.140054}}}, 'validation_question': 'Does high confidence beat ordinary confidence in hit rate, average return, and lower mean absolute error?', 'status': 'forward_validation_required'}`

## Scenario Checks

- primary_scenario_hit_rate: `{'3d': {'sample_size': 80, 'hit_rate': 0.525}, '5d': {'sample_size': 80, 'hit_rate': 0.4125}, '10d': {'sample_size': 80, 'hit_rate': 0.4375}, '20d': {'sample_size': 80, 'hit_rate': 0.575}, '60d': {'sample_size': 80, 'hit_rate': 0.575}}`
- primary_vs_secondary: `{'status': 'forward_ready', 'by_horizon': {'3d': {'sample_size': 80, 'primary_hit_rate': 0.525, 'secondary_hit_rate': 0.475, 'primary_minus_secondary': 0.05, 'both_hit': 0, 'both_miss': 0}, '5d': {'sample_size': 80, 'primary_hit_rate': 0.4125, 'secondary_hit_rate': 0.5875, 'primary_minus_secondary': -0.175, 'both_hit': 0, 'both_miss': 0}, '10d': {'sample_size': 80, 'primary_hit_rate': 0.4375, 'secondary_hit_rate': 0.55, 'primary_minus_secondary': -0.1125, 'both_hit': 0, 'both_miss': 1}, '20d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}, '60d': {'sample_size': 80, 'primary_hit_rate': 0.575, 'secondary_hit_rate': 0.425, 'primary_minus_secondary': 0.15, 'both_hit': 0, 'both_miss': 0}}, 'note': 'Forward sample gate has opened, but alpha status still requires stable performance over time.'}`
- close_call_samples: `{'close_call_sample_size': 40, 'non_close_call_sample_size': 40, 'close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.001613, 'median_return': -0.000756, 'mean_absolute_return': 0.016806, 'max_adverse_excursion': -0.03272, 'max_favorable_excursion': 0.032246}, '5d': {'sample_size': 40, 'hit_rate': 0.475, 'avg_return': 0.004751, 'median_return': -0.003328, 'mean_absolute_return': 0.018234, 'max_adverse_excursion': -0.03028, 'max_favorable_excursion': 0.03939}, '10d': {'sample_size': 40, 'hit_rate': 0.6, 'avg_return': 0.013506, 'median_return': 0.017689, 'mean_absolute_return': 0.027833, 'max_adverse_excursion': -0.057482, 'max_favorable_excursion': 0.060007}, '20d': {'sample_size': 40, 'hit_rate': 0.8, 'avg_return': 0.030718, 'median_return': 0.031196, 'mean_absolute_return': 0.039927, 'max_adverse_excursion': -0.045992, 'max_favorable_excursion': 0.07846}, '60d': {'sample_size': 40, 'hit_rate': 0.875, 'avg_return': 0.060215, 'median_return': 0.072365, 'mean_absolute_return': 0.067554, 'max_adverse_excursion': -0.056528, 'max_favorable_excursion': 0.135454}}}, 'non_close_call_metrics': {'sample_size': 40, 'by_horizon': {'3d': {'sample_size': 40, 'hit_rate': 0.425, 'avg_return': -0.002992, 'median_return': -0.004006, 'mean_absolute_return': 0.021799, 'max_adverse_excursion': -0.083956, 'max_favorable_excursion': 0.044028}, '5d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.003579, 'median_return': 0.012471, 'mean_absolute_return': 0.029534, 'max_adverse_excursion': -0.177985, 'max_favorable_excursion': 0.076593}, '10d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.014265, 'median_return': 0.0211, 'mean_absolute_return': 0.039436, 'max_adverse_excursion': -0.124781, 'max_favorable_excursion': 0.090323}, '20d': {'sample_size': 40, 'hit_rate': 0.65, 'avg_return': 0.020164, 'median_return': 0.035101, 'mean_absolute_return': 0.052533, 'max_adverse_excursion': -0.133308, 'max_favorable_excursion': 0.112509}, '60d': {'sample_size': 40, 'hit_rate': 0.725, 'avg_return': 0.02961, 'median_return': 0.030649, 'mean_absolute_return': 0.052082, 'max_adverse_excursion': -0.106402, 'max_favorable_excursion': 0.140054}}}, 'note': 'close_call rows are tracked separately because path probabilities differ by less than eight percentage points.'}`

## Breadth Forward Validation

- status: `forward_ready`
- evidence_note: `Forward-only sample gate has opened; compare breadth-supported buckets against conflicted buckets before raising confidence.`

### breadth_confirmed_signals
- sample_size: `60`
- 3d: sample `60`, hit `0.45`, avg `-0.000404`, median `-0.001811`, mae `0.017404`
- 5d: sample `60`, hit `0.55`, avg `0.001895`, median `0.009101`, mae `0.022528`
- 10d: sample `60`, hit `0.6333`, avg `0.009919`, median `0.016016`, mae `0.031522`
- 20d: sample `60`, hit `0.7`, avg `0.019417`, median `0.028626`, mae `0.043378`
- 60d: sample `60`, hit `0.7667`, avg `0.039779`, median `0.05488`, mae `0.05833`

### breadth_conflicted_signals
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001546`, median `-0.004006`, mae `0.024997`
- 5d: sample `20`, hit `0.6`, avg `0.010975`, median `0.004752`, mae `0.02795`
- 10d: sample `20`, hit `0.75`, avg `0.025784`, median `0.033298`, mae `0.039972`
- 20d: sample `20`, hit `0.8`, avg `0.043512`, median `0.053953`, mae `0.054786`
- 60d: sample `20`, hit `0.9`, avg `0.060312`, median `0.069634`, mae `0.064281`

### breadth_confirmed_bounce_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

### breadth_conflicted_bounce_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### breadth_confirmed_reversal_signals
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

### breadth_conflicted_reversal_signals
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

### bounce_without_breadth_support
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### trend_reversal_with_breadth_support
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

### failed_bounce_risk_with_breadth_conflict
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001546`, median `-0.004006`, mae `0.024997`
- 5d: sample `20`, hit `0.6`, avg `0.010975`, median `0.004752`, mae `0.02795`
- 10d: sample `20`, hit `0.75`, avg `0.025784`, median `0.033298`, mae `0.039972`
- 20d: sample `20`, hit `0.8`, avg `0.043512`, median `0.053953`, mae `0.054786`
- 60d: sample `20`, hit `0.9`, avg `0.060312`, median `0.069634`, mae `0.064281`

## Internal Resonance Forward Validation

- status: `forward_ready`
- evidence_note: `Forward sample gate has opened; compare aligned internals against surface-only cases before raising confidence.`

### aligned_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

### mixed_internal_resonance
- sample_size: `20`
- 3d: sample `20`, hit `0.4`, avg `-0.004437`, median `-0.002446`, mae `0.018601`
- 5d: sample `20`, hit `0.7`, avg `-0.003818`, median `0.012641`, mae `0.031117`
- 10d: sample `20`, hit `0.7`, avg `0.002746`, median `0.016016`, mae `0.038899`
- 20d: sample `20`, hit `0.5`, avg `-0.003185`, median `0.002869`, mae `0.05028`
- 60d: sample `20`, hit `0.55`, avg `-0.001093`, median `0.005281`, mae `0.039882`

### surface_only_strength
- sample_size: `0`
- 3d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 5d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 10d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 20d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`
- 60d: sample `0`, hit `None`, avg `None`, median `None`, mae `None`

### bounce_with_internal_resonance
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

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
- sample_size: `60`
- 3d: sample `60`, hit `0.4333`, avg `-0.002332`, median `-0.004006`, mae `0.019748`
- 5d: sample `60`, hit `0.6`, avg `0.003379`, median `0.009101`, mae `0.02599`
- 10d: sample `60`, hit `0.6667`, avg `0.012575`, median `0.019956`, mae `0.035324`
- 20d: sample `60`, hit `0.6833`, avg `0.022433`, median `0.034842`, mae `0.04789`
- 60d: sample `60`, hit `0.75`, avg `0.033784`, median `0.043979`, mae `0.05332`

### flow_conflicted_signals
- sample_size: `80`
- 3d: sample `80`, hit `0.45`, avg `-0.000689`, median `-0.002446`, mae `0.019302`
- 5d: sample `80`, hit `0.5625`, avg `0.004165`, median `0.007479`, mae `0.023884`
- 10d: sample `80`, hit `0.6625`, avg `0.013886`, median `0.020244`, mae `0.033634`
- 20d: sample `80`, hit `0.725`, avg `0.025441`, median `0.031658`, mae `0.04623`
- 60d: sample `80`, hit `0.8`, avg `0.044912`, median `0.059406`, mae `0.059818`

### bounce_with_flow_support
- sample_size: `20`
- 3d: sample `20`, hit `0.45`, avg `-0.001014`, median `-0.003228`, mae `0.015645`
- 5d: sample `20`, hit `0.5`, avg `0.00298`, median `0.006571`, mae `0.018904`
- 10d: sample `20`, hit `0.55`, avg `0.009193`, median `0.014227`, mae `0.027099`
- 20d: sample `20`, hit `0.75`, avg `0.026971`, median `0.030239`, mae `0.038604`
- 60d: sample `20`, hit `0.8`, avg `0.042134`, median `0.052632`, mae `0.055796`

### bounce_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.475`, avg `0.001613`, median `-0.000756`, mae `0.016806`
- 5d: sample `40`, hit `0.475`, avg `0.004751`, median `-0.003328`, mae `0.018234`
- 10d: sample `40`, hit `0.6`, avg `0.013506`, median `0.017689`, mae `0.027833`
- 20d: sample `40`, hit `0.8`, avg `0.030718`, median `0.031196`, mae `0.039927`
- 60d: sample `40`, hit `0.875`, avg `0.060215`, median `0.072365`, mae `0.067554`

### risk_path_with_flow_conflict
- sample_size: `40`
- 3d: sample `40`, hit `0.425`, avg `-0.002992`, median `-0.004006`, mae `0.021799`
- 5d: sample `40`, hit `0.65`, avg `0.003579`, median `0.012471`, mae `0.029534`
- 10d: sample `40`, hit `0.725`, avg `0.014265`, median `0.0211`, mae `0.039436`
- 20d: sample `40`, hit `0.65`, avg `0.020164`, median `0.035101`, mae `0.052533`
- 60d: sample `40`, hit `0.725`, avg `0.02961`, median `0.030649`, mae `0.052082`

- This report is not proof of alpha; it is a proxy check until forward-only samples mature.
- If strong/high-confirmation buckets do not beat weak/no-edge buckets, model confidence must remain capped.
- Forward completed samples are required before STRONG_EDGE or high-confidence buckets can be treated as validated.
- Breadth buckets remain not_enough_forward_samples until enough forward-only observations complete.
- Flow buckets are proxy-only until true fund-flow / positioning feeds are connected and forward validation matures.
