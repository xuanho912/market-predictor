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
    return "暂无";
  }
  return signedPct(value);
}

function optionalPct(value: number | null | undefined) {
  if (value == null) {
    return "暂无";
  }
  return `${(value * 100).toFixed(1)}%`;
}

const statusText: Record<string, string> = {
  "NO ALPHA": "暂无 Alpha",
  "RESEARCH ALPHA CANDIDATE": "研究候选，尚未确认",
  "FORWARD-VALIDATED ALPHA CANDIDATE": "已通过前向验证的候选",
};

const regimeText: Record<string, string> = {
  bull: "牛市",
  bear: "熊市",
  crisis: "危机",
  high_volatility: "高波动",
  low_volatility: "低波动",
  sideways: "震荡",
  unknown: "未知",
  bull_trend: "牛市趋势",
  bear_trend: "熊市趋势",
  liquidity_crunch: "流动性紧张",
  credit_stress: "信用压力",
  crisis_mode: "危机模式",
};

const riskSourceText: Record<string, string> = {
  credit_spreads: "信用利差",
  breadth_deterioration: "市场宽度恶化",
  positioning_crowding: "仓位拥挤",
  valuation_overheat: "估值过热",
  momentum_extension: "动量过热",
  rates_up: "利率上行",
  dollar_strength: "美元走强",
  earnings_downgrades: "盈利下修",
  news_event_risk: "新闻事件风险",
  funding_market_stress: "融资压力",
  bank_stress: "银行压力",
};

function cnRegime(value: string | undefined) {
  if (!value) {
    return "未知";
  }
  return regimeText[value] ?? value.replaceAll("_", " ");
}

function cnAlphaStatus(value: string) {
  return statusText[value] ?? value;
}

function cnSupport(value: string | undefined) {
  if (value === "supportive") {
    return "偏支持";
  }
  return "不够一致";
}

function cnBool(value: boolean) {
  return value ? "有" : "没有";
}

function cnRiskSource(value: string) {
  return riskSourceText[value] ?? value.replaceAll("_", " ");
}

function cnAnalogPhrase(value: string) {
  return value
    .replace("same regime:", "市场状态相同：")
    .replace("bounce_probability above frozen alpha_v1 threshold", "反弹概率高于 Alpha v1 固定阈值")
    .replace("VIX elevated", "VIX 处在偏高位置")
    .replace("price oversold by RSI", "RSI 显示价格偏超卖")
    .replace("meaningful recent drawdown", "近期有明显回撤")
    .replace("credit proxy not showing severe spread stress", "信用代理指标没有显示严重压力")
    .replace("closest match is multi-factor, not a single obvious feature", "相似性来自多项指标，不是单一指标")
    .replace("current credit proxy differs materially", "当前信用代理指标差异较大")
    .replace("current dollar behavior differs", "当前美元走势差异较大")
    .replace("current VIX level differs", "当前 VIX 水平差异较大")
    .replace("regime differs:", "市场状态不同：")
    .replace("current", "当前")
    .replace("historical", "历史")
    .replace("vs", "对比")
    .replace("no large first-order difference across selected analog features", "选定相似指标没有特别大的第一层差异");
}

function plainPredictionSummary(
  alpha: Awaited<ReturnType<typeof getAlphaV1Status>>,
  analogs: Awaited<ReturnType<typeof getAlphaV1Analogs>>,
  strongestSymbol: string,
  strongestBounce: number | null,
  realDataFailed: boolean,
) {
  if (realDataFailed) {
    return "今天真实数据源没有正常更新，所以系统不允许生成实时信号。大白话：先别看信号，等下一次真实数据更新。";
  }
  if (alpha.live_signal) {
    const support = analogs.interpretation.historical_support === "supportive" ? "历史相似情景也偏支持" : "但历史相似情景并不完全一致";
    const strongest = strongestBounce == null ? "" : `目前最强的是 ${strongestSymbol}，反弹概率约 ${pct(strongestBounce)}。`;
    return `现在 Alpha v1 已触发。大白话：系统认为这里有短中期反弹机会，${strongest}${support}。但这不是“必涨”，也不是实盘买入指令，只是继续做 3/5/10/20/60 日前向验证。`;
  }
  return "现在 Alpha v1 没有触发。大白话：系统暂时没有看到足够强的反弹候选信号，当前动作就是等待下一次每日观察。";
}

export default async function Home() {
  const prediction = await getLatestPrediction("SPY");
  const alpha = await getAlphaV1Status();
  const analogs = await getAlphaV1Analogs("SPY");
  const alphaSymbols = ["SPY", "QQQ", "IWM", "DIA"];
  const realDataFailed = alpha.data_source_status === "failed" || alpha.data_source_status === "synthetic_fallback_no_signal";
  const alphaNextAction = realDataFailed
    ? "真实数据失败，不生成信号"
    : alpha.live_signal
      ? "只做前向观察，暂不进入模拟交易"
      : "等待下一次每日观察";
  const hasBackendPrediction = prediction.model_version !== "frontend-fallback";
  const bounceEntries = Object.entries(alpha.latest_bounce_probability_by_symbol).filter((entry): entry is [string, number] => entry[1] != null);
  const strongest = bounceEntries.sort((left, right) => right[1] - left[1])[0];
  const strongestSymbol = strongest?.[0] ?? "SPY";
  const strongestBounce = strongest?.[1] ?? null;
  const summary = plainPredictionSummary(alpha, analogs, strongestSymbol, strongestBounce, realDataFailed);

  return (
    <main className="mx-auto min-h-screen w-full max-w-3xl px-4 py-5">
      <section className="border-b border-line pb-5">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">市场预测观察</p>
            <h1 className="mt-2 text-4xl font-semibold tracking-normal text-ink">{alpha.live_signal ? "有反弹信号" : "暂无强信号"}</h1>
            <p className="mt-1 text-sm text-muted">Alpha v1 反弹候选</p>
          </div>
          <div className="rounded-lg border border-line bg-panel px-3 py-2 text-right">
            <p className="text-xs uppercase text-muted">状态</p>
            <p className="mt-1 text-sm font-semibold text-amber">{cnAlphaStatus(alpha.status)}</p>
          </div>
        </div>
        <p className="mt-3 text-xs text-muted">最近检查日期：{alpha.latest_checked_date ?? "暂无"}</p>
      </section>

      <section className="mt-5 rounded-lg border border-teal bg-panel p-4">
        <p className="text-xs uppercase text-muted">大白话预测总结</p>
        <p className="mt-2 text-lg font-semibold leading-7 text-ink">{summary}</p>
        <p className="mt-3 text-xs text-muted">注意：这是研究候选信号的概率观察，不是确定性判断，也不是交易建议。</p>
      </section>

      <section className="mt-5 grid grid-cols-3 gap-2">
        <ProbabilityCard name="回调风险" value={hasBackendPrediction ? prediction.pullback_risk_score : 0} tone="amber" />
        <ProbabilityCard name="危机风险" value={hasBackendPrediction ? prediction.crisis_risk_score : 0} tone="rose" />
        <ProbabilityCard name="反弹质量" value={hasBackendPrediction ? prediction.bounce_quality_score : (strongestBounce ?? 0) * 100} tone="teal" />
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">Alpha v1</p>
            <h2 className="mt-1 text-base font-semibold">反弹概率前 10% 候选</h2>
          </div>
          <div className="text-right">
            <p className="text-xs uppercase text-muted">实时信号</p>
            <p className={alpha.live_signal ? "mt-1 text-sm font-semibold text-teal" : "mt-1 text-sm font-semibold text-muted"}>
              {cnBool(alpha.live_signal)}
            </p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-2 gap-2 text-sm">
          <div>
            <p className="text-xs uppercase text-muted">候选状态</p>
            <p className="mt-1 font-medium">{cnAlphaStatus(alpha.status)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">固定阈值</p>
            <p className="mt-1 font-medium">{alpha.threshold.toFixed(8)}</p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-2 gap-2 text-sm">
          {alphaSymbols.map((symbol) => {
            const value = alpha.latest_bounce_probability_by_symbol[symbol];
            const distance = alpha.distance_to_threshold_by_symbol[symbol];
            return (
              <div key={symbol} className="rounded border border-line px-3 py-2">
                <p className="text-xs uppercase text-muted">{symbol} 反弹概率</p>
                <p className="mt-1 font-semibold">{value == null ? "暂无" : pct(value)}</p>
                <p className="mt-1 text-xs text-muted">距阈值：{distance == null ? "暂无" : signedPct(-distance)}</p>
              </div>
            );
          })}
        </div>
        <div className="mt-3 text-sm">
          <p className="text-xs uppercase text-muted">下一步</p>
          <p className="mt-1 font-medium">{alphaNextAction}</p>
          {alpha.signal_blocked_reason ? <p className="mt-1 text-xs text-muted">{alpha.signal_blocked_reason}</p> : null}
        </div>
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">历史相似情景</p>
            <h2 className="mt-1 text-base font-semibold">当前市场像哪些历史日期</h2>
          </div>
          <div className="text-right">
            <p className="text-xs uppercase text-muted">支持度</p>
            <p className={analogs.interpretation.historical_support === "supportive" ? "mt-1 text-sm font-semibold text-teal" : "mt-1 text-sm font-semibold text-amber"}>
              {cnSupport(analogs.interpretation.historical_support)}
            </p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-3 gap-2 text-sm">
          <div className="rounded border border-line px-3 py-2">
            <p className="text-xs uppercase text-muted">5日平均</p>
            <p className="mt-1 font-semibold">{optionalSignedPct(analogs.historical_distribution.avg_return_5d)}</p>
          </div>
          <div className="rounded border border-line px-3 py-2">
            <p className="text-xs uppercase text-muted">20日平均</p>
            <p className="mt-1 font-semibold">{optionalSignedPct(analogs.historical_distribution.avg_return_20d)}</p>
          </div>
          <div className="rounded border border-line px-3 py-2">
            <p className="text-xs uppercase text-muted">60日平均</p>
            <p className="mt-1 font-semibold">{optionalSignedPct(analogs.historical_distribution.avg_return_60d)}</p>
          </div>
        </div>
        <div className="mt-3 grid grid-cols-3 gap-2 text-sm">
          <div>
            <p className="text-xs uppercase text-muted">样本数</p>
            <p className="mt-1 font-medium">{analogs.sample_count}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">5日胜率</p>
            <p className="mt-1 font-medium">{optionalPct(analogs.historical_distribution.hit_rate_5d)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">最差路径</p>
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
              <span className="text-muted">{cnRegime(day.regime)}</span>
            </div>
          ))}
        </div>
        <div className="mt-3 text-xs text-muted">
          <p>历史相似情景只用于解释和辅助观察，不能证明 Alpha 一定有效。</p>
          {analogs.low_sample_warning ? <p className="mt-1">样本偏少：只能参考，不能下结论。</p> : null}
        </div>
        {analogs.top_similar_cases[0] ? (
          <div className="mt-3 grid grid-cols-1 gap-3 text-sm">
            <div>
              <p className="text-xs uppercase text-muted">共同点</p>
              <p className="mt-1">{analogs.top_similar_cases[0].key_shared_features.map(cnAnalogPhrase).join("；")}</p>
            </div>
            <div>
              <p className="text-xs uppercase text-muted">差异点</p>
              <p className="mt-1">{analogs.top_similar_cases[0].key_differences.map(cnAnalogPhrase).join("；")}</p>
            </div>
          </div>
        ) : null}
      </section>

      {hasBackendPrediction ? (
        <section className="mt-5 overflow-hidden rounded-lg border border-line bg-panel">
          <div className="grid grid-cols-7 border-b border-line px-3 py-2 text-xs uppercase text-muted">
            <span>周期</span>
            <span>上涨</span>
            <span>下跌</span>
            <span>震荡</span>
            <span>预期</span>
            <span>风险</span>
            <span>置信</span>
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
      ) : null}

      {hasBackendPrediction ? (
        <section className="mt-5 grid grid-cols-2 gap-2">
          <ProbabilityCard name="反弹概率" value={prediction.bounce_probability * 100} tone="teal" />
          <ProbabilityCard name="假反弹风险" value={prediction.dead_cat_bounce_risk * 100} tone="rose" />
          <ProbabilityCard name="下跌延续" value={prediction.downside_continuation_probability * 100} tone="amber" />
          <ProbabilityCard name="趋势反转" value={prediction.trend_reversal_probability * 100} tone="teal" />
        </section>
      ) : null}

      {hasBackendPrediction ? (
        <section className="mt-5 rounded-lg border border-line bg-panel p-4">
          <h2 className="text-base font-semibold">主要原因</h2>
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
      ) : null}

      {hasBackendPrediction ? (
        <section className="mt-5 rounded-lg border border-line bg-panel p-4">
          <h2 className="text-base font-semibold">风险来源</h2>
          <div className="mt-3 space-y-2">
            {prediction.risk_source_breakdown.slice(0, 6).map((source) => (
              <div key={source.source}>
                <div className="mb-1 flex justify-between text-sm">
                  <span>{cnRiskSource(source.source)}</span>
                  <span>{Math.round(source.score)}%</span>
                </div>
                <div className="h-2 overflow-hidden rounded-full bg-slate-200">
                  <div className="h-full bg-amber" style={{ width: `${Math.min(source.score, 100)}%` }} />
                </div>
              </div>
            ))}
          </div>
        </section>
      ) : null}

      {hasBackendPrediction ? (
        <section className="mt-5 rounded-lg border border-line bg-panel p-4">
          <h2 className="text-base font-semibold">相似日期</h2>
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
      ) : null}
    </main>
  );
}
