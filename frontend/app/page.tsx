import { ProbabilityCard } from "../components/probability-card";
import { getAlphaV1Analogs, getAlphaV1Status, getLatestPrediction } from "../lib/api";

export const dynamic = "force-static";

function pct(value: number) {
  return `${Math.round(value * 100)}%`;
}

function signedPct(value: number) {
  const formatted = `${(value * 100).toFixed(1)}%`;
  return value > 0 ? `+${formatted}` : formatted;
}

function optionalSignedPct(value: number | null | undefined) {
  if (value == null) {
    return "n/a";
  }
  return signedPct(value);
}

function optionalPct(value: number | null | undefined) {
  if (value == null) {
    return "n/a";
  }
  return `${(value * 100).toFixed(1)}%`;
}

export default async function Home() {
  const prediction = await getLatestPrediction("SPY");
  const alpha = await getAlphaV1Status();
  const analogs = await getAlphaV1Analogs("SPY");
  const primary = prediction.horizons.find((forecast) => forecast.horizon === "20d") ?? prediction.horizons[0];
  const alphaSymbols = ["SPY", "QQQ", "IWM", "DIA"];
  const realDataFailed = alpha.data_source_status === "failed" || alpha.data_source_status === "synthetic_fallback_no_signal";
  const alphaNextAction = realDataFailed
    ? "No live signal because real data source failed"
    : alpha.live_signal
      ? "forward-only observation, not paper trading yet"
      : "wait";

  return (
    <main className="mx-auto min-h-screen w-full max-w-3xl px-4 py-5">
      <section className="border-b border-line pb-5">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">{prediction.symbol}</p>
            <h1 className="mt-2 text-5xl font-semibold tracking-normal text-ink">{pct(primary.down_probability)}</h1>
            <p className="mt-1 text-sm text-muted">20d down probability</p>
          </div>
          <div className="rounded-lg border border-line bg-panel px-3 py-2 text-right">
            <p className="text-xs uppercase text-muted">Regime</p>
            <p className="mt-1 text-sm font-semibold uppercase text-amber">{prediction.market_regime.replaceAll("_", " ")}</p>
          </div>
        </div>
        <p className="mt-3 text-xs text-muted">{new Date(prediction.forecast_timestamp).toLocaleString()}</p>
      </section>

      <section className="mt-5 grid grid-cols-3 gap-2">
        <ProbabilityCard name="Pullback" value={prediction.pullback_risk_score} tone="amber" />
        <ProbabilityCard name="Crisis" value={prediction.crisis_risk_score} tone="rose" />
        <ProbabilityCard name="Bounce" value={prediction.bounce_quality_score} tone="teal" />
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">Alpha v1</p>
            <h2 className="mt-1 text-base font-semibold">{alpha.signal_name}</h2>
          </div>
          <div className="text-right">
            <p className="text-xs uppercase text-muted">Live signal</p>
            <p className={alpha.live_signal ? "mt-1 text-sm font-semibold text-teal" : "mt-1 text-sm font-semibold text-muted"}>
              {alpha.live_signal ? "Yes" : "No"}
            </p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-2 gap-2 text-sm">
          <div>
            <p className="text-xs uppercase text-muted">Status</p>
            <p className="mt-1 font-medium">{alpha.status}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">Threshold</p>
            <p className="mt-1 font-medium">{alpha.threshold.toFixed(8)}</p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-2 gap-2 text-sm">
          {alphaSymbols.map((symbol) => {
            const value = alpha.latest_bounce_probability_by_symbol[symbol];
            return (
              <div key={symbol} className="rounded border border-line px-3 py-2">
                <p className="text-xs uppercase text-muted">{symbol} bounce probability</p>
                <p className="mt-1 font-semibold">{value == null ? "n/a" : pct(value)}</p>
              </div>
            );
          })}
        </div>
        <div className="mt-3 text-sm">
          <p className="text-xs uppercase text-muted">Next action</p>
          <p className="mt-1 font-medium">{alphaNextAction}</p>
          {alpha.signal_blocked_reason ? <p className="mt-1 text-xs text-muted">{alpha.signal_blocked_reason}</p> : null}
        </div>
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">Historical Analogs</p>
            <h2 className="mt-1 text-base font-semibold">Alpha v1 context</h2>
          </div>
          <div className="text-right">
            <p className="text-xs uppercase text-muted">Support</p>
            <p className={analogs.interpretation.historical_support === "supportive" ? "mt-1 text-sm font-semibold text-teal" : "mt-1 text-sm font-semibold text-amber"}>
              {analogs.interpretation.historical_support.replaceAll("_", " ")}
            </p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-3 gap-2 text-sm">
          <div className="rounded border border-line px-3 py-2">
            <p className="text-xs uppercase text-muted">5d avg</p>
            <p className="mt-1 font-semibold">{optionalSignedPct(analogs.historical_distribution.avg_return_5d)}</p>
          </div>
          <div className="rounded border border-line px-3 py-2">
            <p className="text-xs uppercase text-muted">20d avg</p>
            <p className="mt-1 font-semibold">{optionalSignedPct(analogs.historical_distribution.avg_return_20d)}</p>
          </div>
          <div className="rounded border border-line px-3 py-2">
            <p className="text-xs uppercase text-muted">60d avg</p>
            <p className="mt-1 font-semibold">{optionalSignedPct(analogs.historical_distribution.avg_return_60d)}</p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-3 gap-2 text-sm">
          <div>
            <p className="text-xs uppercase text-muted">Samples</p>
            <p className="mt-1 font-medium">{analogs.sample_count}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">5d hit rate</p>
            <p className="mt-1 font-medium">{optionalPct(analogs.historical_distribution.hit_rate_5d)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">Worst path</p>
            <p className="mt-1 font-medium">{optionalSignedPct(analogs.historical_distribution.worst_path_max_adverse_excursion)}</p>
          </div>
        </div>
        <div className="mt-3 space-y-2">
          {analogs.top_similar_cases.slice(0, 5).map((day) => (
            <div key={day.date} className="grid grid-cols-4 gap-2 border-b border-line pb-2 text-sm last:border-b-0 last:pb-0">
              <span className="font-medium">{day.date}</span>
              <span className="text-muted">{optionalPct(day.similarity_score)}</span>
              <span className={day.forward_return_20d != null && day.forward_return_20d >= 0 ? "text-teal" : "text-rose"}>
                {optionalSignedPct(day.forward_return_20d)}
              </span>
              <span className="text-muted">{day.regime.replaceAll("_", " ")}</span>
            </div>
          ))}
        </div>
        <div className="mt-3 text-xs text-muted">
          <p>{analogs.interpretation.confidence_note}</p>
          {analogs.low_sample_warning ? <p className="mt-1">Low sample warning: use this only as context.</p> : null}
          <p className="mt-1">Historical analogs are not proof of alpha.</p>
        </div>
        {analogs.top_similar_cases[0] ? (
          <div className="mt-3 grid grid-cols-1 gap-3 text-sm">
            <div>
              <p className="text-xs uppercase text-muted">Shared</p>
              <p className="mt-1">{analogs.top_similar_cases[0].key_shared_features.join("; ")}</p>
            </div>
            <div>
              <p className="text-xs uppercase text-muted">Different</p>
              <p className="mt-1">{analogs.top_similar_cases[0].key_differences.join("; ")}</p>
            </div>
          </div>
        ) : null}
      </section>

      <section className="mt-5 overflow-hidden rounded-lg border border-line bg-panel">
        <div className="grid grid-cols-7 border-b border-line px-3 py-2 text-xs uppercase text-muted">
          <span>H</span>
          <span>Up</span>
          <span>Down</span>
          <span>Side</span>
          <span>Exp</span>
          <span>Risk</span>
          <span>Conf</span>
        </div>
        {prediction.horizons.map((forecast) => (
          <div key={forecast.horizon} className="grid grid-cols-7 border-b border-line px-3 py-3 text-sm last:border-b-0">
            <span className="font-semibold">{forecast.horizon}</span>
            <span className="text-teal">{pct(forecast.up_probability)}</span>
            <span className="text-rose">{pct(forecast.down_probability)}</span>
            <span>{pct(forecast.sideways_probability)}</span>
            <span>{signedPct(forecast.expected_return)}</span>
            <span>{signedPct(forecast.max_downside_p50)}</span>
            <span>{pct(forecast.confidence)}</span>
          </div>
        ))}
      </section>

      <section className="mt-5 grid grid-cols-2 gap-2">
        <ProbabilityCard name="Bounce prob" value={prediction.bounce_probability * 100} tone="teal" />
        <ProbabilityCard name="Dead cat" value={prediction.dead_cat_bounce_risk * 100} tone="rose" />
        <ProbabilityCard name="Continuation" value={prediction.downside_continuation_probability * 100} tone="amber" />
        <ProbabilityCard name="Reversal" value={prediction.trend_reversal_probability * 100} tone="teal" />
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <h2 className="text-base font-semibold">Top Reasons</h2>
        <div className="mt-3 space-y-3">
          {prediction.top_reasons.map((reason) => (
            <div key={reason.title} className="border-b border-line pb-3 last:border-b-0 last:pb-0">
              <div className="flex items-center justify-between gap-3">
                <p className="font-medium">{reason.title}</p>
                <span className="text-xs uppercase text-muted">{reason.direction}</span>
              </div>
              <p className="mt-1 text-sm text-muted">{reason.evidence}</p>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <h2 className="text-base font-semibold">Risk Sources</h2>
        <div className="mt-3 space-y-2">
          {prediction.risk_source_breakdown.slice(0, 6).map((source) => (
            <div key={source.source}>
              <div className="mb-1 flex justify-between text-sm">
                <span>{source.source.replaceAll("_", " ")}</span>
                <span>{Math.round(source.score)}%</span>
              </div>
              <div className="h-2 overflow-hidden rounded-full bg-slate-200">
                <div className="h-full bg-amber" style={{ width: `${Math.min(source.score, 100)}%` }} />
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <h2 className="text-base font-semibold">Similar Days</h2>
        <div className="mt-3 space-y-2">
          {prediction.historical_similar_days.map((day) => (
            <div key={day.date} className="flex items-center justify-between gap-3 text-sm">
              <span>{day.date}</span>
              <span className="text-muted">{pct(day.similarity)}</span>
              <span className={day.forward_20d_return >= 0 ? "text-teal" : "text-rose"}>{signedPct(day.forward_20d_return)}</span>
            </div>
          ))}
        </div>
      </section>
    </main>
  );
}
