"use client";

import { useMemo, useState } from "react";
import type { HistoricalAnalogCase, PredictionDashboard, SimulatedSymbolPaths } from "../lib/api";

const SYMBOL_ORDER = ["SPY", "QQQ", "IWM", "DIA"];

const stateText: Record<string, string> = {
  oversold_bounce: "超跌反弹",
  risk_off: "风险偏弱",
  sideways: "震荡观望",
  recovery: "修复中",
  panic: "恐慌",
  no_edge: "暂无优势",
};

const supportText: Record<string, string> = {
  supportive: "偏支持",
  weak_or_conflicting: "偏冲突",
  neutral: "中性",
};

function pct(value: number | null | undefined, digits = 0) {
  if (value == null || Number.isNaN(value)) {
    return "暂无";
  }
  return `${(value * 100).toFixed(digits)}%`;
}

function price(value: number | null | undefined) {
  if (value == null || Number.isNaN(value)) {
    return "暂无";
  }
  return value.toLocaleString("zh-CN", { maximumFractionDigits: 2 });
}

function signedPct(value: number | null | undefined, digits = 1) {
  if (value == null || Number.isNaN(value)) {
    return "暂无";
  }
  const formatted = `${(value * 100).toFixed(digits)}%`;
  return value > 0 ? `+${formatted}` : formatted;
}

function stateCn(value: string | undefined) {
  return stateText[value ?? ""] ?? value ?? "未知";
}

function supportCn(value: string | undefined) {
  return supportText[value ?? ""] ?? value ?? "中性";
}

function strongestScenario(symbolData: SimulatedSymbolPaths | undefined) {
  if (!symbolData) {
    return "暂无";
  }
  const cards = [...symbolData.scenario_cards].sort((left, right) => right.probability_weight - left.probability_weight);
  return cards[0]?.name_cn ?? "暂无";
}

function plainSummary(symbolData: SimulatedSymbolPaths | undefined) {
  if (!symbolData) {
    return "当前没有可用数据。";
  }
  const state = stateCn(symbolData.market_state);
  const support = supportCn(symbolData.historical_support);
  const scenario = strongestScenario(symbolData);
  if (symbolData.live_signal) {
    return `${symbolData.symbol} 当前有反弹候选信号，状态偏“${state}”。大白话：系统认为短中期有反抽机会，最强情景是“${scenario}”，历史相似情景${support}。这不是必涨，只是前向观察。`;
  }
  return `${symbolData.symbol} 当前没有 Alpha v1 实时信号，状态偏“${state}”。大白话：系统暂时没有看到足够强的反弹优势，最强情景是“${scenario}”，继续观察。`;
}

function svgPath(values: Array<number | null>, minY: number, maxY: number, width: number, height: number, pad: number) {
  const step = (width - pad * 2) / Math.max(values.length - 1, 1);
  const scaleY = (value: number) => height - pad - ((value - minY) / Math.max(maxY - minY, 1)) * (height - pad * 2);
  let path = "";
  values.forEach((value, index) => {
    if (value == null) {
      return;
    }
    const x = pad + index * step;
    const y = scaleY(value);
    path += path ? ` L ${x.toFixed(2)} ${y.toFixed(2)}` : `M ${x.toFixed(2)} ${y.toFixed(2)}`;
  });
  return path;
}

function xForIndex(index: number, total: number, width: number, pad: number) {
  const step = (width - pad * 2) / Math.max(total - 1, 1);
  return pad + index * step;
}

function PredictionChart({ data }: { data: SimulatedSymbolPaths }) {
  const width = 760;
  const height = 320;
  const pad = 36;
  const paths = data.paths;
  const allValues = [
    ...paths.historical_price,
    ...paths.expected_path,
    ...paths.bounce_path,
    ...paths.bearish_path,
    ...paths.analog_average_path,
    ...paths.confidence_band_upper,
    ...paths.confidence_band_lower,
  ].filter((value): value is number => typeof value === "number" && Number.isFinite(value));
  const minY = Math.min(...allValues) * 0.985;
  const maxY = Math.max(...allValues) * 1.015;
  const splitX = xForIndex(paths.split_index, paths.dates.length, width, pad);
  const horizonIndexes = [3, 5, 10, 20, 60].map((days) => ({
    days,
    index: Math.min(paths.split_index + days, paths.dates.length - 1),
  }));

  return (
    <section className="mt-5 rounded-lg border border-line bg-panel p-4">
      <div className="flex items-start justify-between gap-3">
        <div>
          <p className="text-xs uppercase text-muted">未来模拟走势图</p>
          <h2 className="mt-1 text-base font-semibold">过去走势 + 概率情景路径</h2>
        </div>
        <p className="text-right text-xs text-muted">分界线右侧为模拟路径</p>
      </div>
      <div className="mt-3 overflow-x-auto">
        <svg viewBox={`0 0 ${width} ${height}`} className="h-80 min-w-[720px] w-full">
          <rect x="0" y="0" width={width} height={height} rx="8" fill="#ffffff" />
          {[0.2, 0.4, 0.6, 0.8].map((ratio) => (
            <line key={ratio} x1={pad} x2={width - pad} y1={pad + (height - pad * 2) * ratio} y2={pad + (height - pad * 2) * ratio} stroke="#e5ece9" />
          ))}
          <line x1={splitX} x2={splitX} y1={pad} y2={height - pad} stroke="#14211f" strokeDasharray="4 4" />
          {horizonIndexes.map(({ days, index }) => {
            const x = xForIndex(index, paths.dates.length, width, pad);
            return (
              <g key={days}>
                <line x1={x} x2={x} y1={pad} y2={height - pad} stroke="#d6dedb" strokeDasharray="3 6" />
                <text x={x} y={height - 12} textAnchor="middle" fontSize="11" fill="#62706b">{days}日</text>
              </g>
            );
          })}
          <path d={svgPath(paths.confidence_band_upper, minY, maxY, width, height, pad)} fill="none" stroke="#94a3b8" strokeWidth="1.2" strokeDasharray="5 5" />
          <path d={svgPath(paths.confidence_band_lower, minY, maxY, width, height, pad)} fill="none" stroke="#94a3b8" strokeWidth="1.2" strokeDasharray="5 5" />
          <path d={svgPath(paths.historical_price, minY, maxY, width, height, pad)} fill="none" stroke="#14211f" strokeWidth="2.4" />
          <path d={svgPath(paths.expected_path, minY, maxY, width, height, pad)} fill="none" stroke="#2563eb" strokeWidth="2.3" />
          <path d={svgPath(paths.bounce_path, minY, maxY, width, height, pad)} fill="none" stroke="#0f9f7a" strokeWidth="2" />
          <path d={svgPath(paths.bearish_path, minY, maxY, width, height, pad)} fill="none" stroke="#dc4a4a" strokeWidth="2" />
          <path d={svgPath(paths.analog_average_path, minY, maxY, width, height, pad)} fill="none" stroke="#f59e0b" strokeWidth="2" />
          <text x={pad} y={22} fontSize="12" fill="#62706b">历史价格</text>
          <text x={splitX + 10} y={22} fontSize="12" fill="#62706b">模拟未来</text>
        </svg>
      </div>
      <div className="mt-3 grid grid-cols-2 gap-2 text-xs text-muted sm:grid-cols-5">
        <span>黑线：历史价格</span>
        <span className="text-blue-700">蓝线：基准情景</span>
        <span className="text-teal">绿线：反弹情景</span>
        <span className="text-rose">红线：失败反弹</span>
        <span className="text-amber">黄线：历史均值</span>
      </div>
      <p className="mt-3 text-xs text-muted">
        模拟路径是基于当前信号和历史相似情景生成的概率情景，不是保证会发生的预测。
      </p>
    </section>
  );
}

function MarketCard({
  symbol,
  selected,
  data,
  onSelect,
}: {
  symbol: string;
  selected: boolean;
  data: SimulatedSymbolPaths;
  onSelect: () => void;
}) {
  return (
    <button
      type="button"
      onClick={onSelect}
      className={`rounded-lg border p-3 text-left transition ${selected ? "border-teal bg-panel shadow-sm" : "border-line bg-white"}`}
    >
      <div className="flex items-center justify-between gap-2">
        <div className="flex items-center gap-2">
          <span className="flex h-10 w-10 items-center justify-center rounded-full bg-ink text-sm font-semibold text-white">{symbol}</span>
          <div>
            <p className="font-semibold">{symbol}</p>
            <p className="text-xs text-muted">{data.name}</p>
          </div>
        </div>
        <span className={data.live_signal ? "text-xs font-semibold text-teal" : "text-xs text-muted"}>{data.live_signal ? "有信号" : "无信号"}</span>
      </div>
      <div className="mt-3 grid grid-cols-2 gap-2 text-xs">
        <div>
          <p className="text-muted">收盘价</p>
          <p className="mt-1 font-medium">{price(data.current_price)}</p>
        </div>
        <div>
          <p className="text-muted">状态</p>
          <p className="mt-1 font-medium">{stateCn(data.market_state)}</p>
        </div>
        <div>
          <p className="text-muted">反弹概率</p>
          <p className="mt-1 font-medium">{pct(data.bounce_probability)}</p>
        </div>
        <div>
          <p className="text-muted">历史支持</p>
          <p className="mt-1 font-medium">{supportCn(data.historical_support)}</p>
        </div>
      </div>
    </button>
  );
}

export function MarketDashboard({ dashboard }: { dashboard: PredictionDashboard }) {
  const availableSymbols = SYMBOL_ORDER.filter((symbol) => dashboard.simulated_paths.symbols[symbol]);
  const defaultSymbol = availableSymbols.includes(dashboard.overview.strongest_symbol)
    ? dashboard.overview.strongest_symbol
    : availableSymbols[0] ?? "SPY";
  const [selectedSymbol, setSelectedSymbol] = useState(defaultSymbol);
  const selected = dashboard.simulated_paths.symbols[selectedSymbol];
  const analog = dashboard.analogs[selectedSymbol];
  const topAnalogs = (analog?.top_similar_cases ?? []).slice(0, 5);
  const strongest = useMemo(() => {
    return availableSymbols
      .map((symbol) => dashboard.simulated_paths.symbols[symbol])
      .sort((left, right) => right.bounce_probability - left.bounce_probability)[0];
  }, [availableSymbols, dashboard.simulated_paths.symbols]);

  if (!selected) {
    return (
      <main className="mx-auto min-h-screen w-full max-w-5xl px-4 py-5">
        <h1 className="text-2xl font-semibold">市场预测终端</h1>
        <p className="mt-3 text-muted">暂无可用数据。请先运行 GitHub Actions 的 Forward Alpha v1 Observation。</p>
      </main>
    );
  }

  return (
    <main className="mx-auto min-h-screen w-full max-w-6xl px-4 py-5">
      <header className="border-b border-line pb-5">
        <p className="text-xs uppercase text-muted">Market Prediction Dashboard</p>
        <div className="mt-2 flex flex-col gap-3 sm:flex-row sm:items-end sm:justify-between">
          <div>
            <h1 className="text-4xl font-semibold tracking-normal text-ink">市场预测终端</h1>
            <p className="mt-2 text-sm text-muted">最近更新：{dashboard.as_of ?? "暂无"}。打开网页即可查看，不需要提问。</p>
          </div>
          <div className="rounded-lg border border-line bg-panel px-3 py-2 text-sm">
            <p className="text-xs uppercase text-muted">当前最强信号</p>
            <p className="mt-1 font-semibold">{strongest ? `${strongest.symbol} / ${stateCn(strongest.market_state)}` : "暂无"}</p>
          </div>
        </div>
      </header>

      <section className="mt-5">
        <div className="mb-3 flex items-center justify-between gap-3">
          <h2 className="text-base font-semibold">大盘概览</h2>
          <p className="text-xs text-muted">点击卡片切换下方预测</p>
        </div>
        <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 lg:grid-cols-4">
          {availableSymbols.map((symbol) => (
            <MarketCard
              key={symbol}
              symbol={symbol}
              selected={selectedSymbol === symbol}
              data={dashboard.simulated_paths.symbols[symbol]}
              onSelect={() => setSelectedSymbol(symbol)}
            />
          ))}
        </div>
      </section>

      <PredictionChart data={selected} />

      <section className="mt-5 rounded-lg border border-teal bg-panel p-4">
        <p className="text-xs uppercase text-muted">当前预测判断</p>
        <h2 className="mt-1 text-lg font-semibold">{plainSummary(selected)}</h2>
        <div className="mt-4 grid grid-cols-2 gap-3 text-sm sm:grid-cols-3">
          <div>
            <p className="text-xs uppercase text-muted">当前状态</p>
            <p className="mt-1 font-medium">{stateCn(selected.market_state)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">最强情景</p>
            <p className="mt-1 font-medium">{strongestScenario(selected)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">置信度</p>
            <p className="mt-1 font-medium">{supportCn(selected.historical_support)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">反弹概率</p>
            <p className="mt-1 font-medium">{pct(selected.bounce_probability)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">下跌延续风险</p>
            <p className="mt-1 font-medium">{pct(selected.downside_continuation_probability)}</p>
          </div>
          <div>
            <p className="text-xs uppercase text-muted">趋势反转概率</p>
            <p className="mt-1 font-medium">{pct(selected.trend_reversal_probability)}</p>
          </div>
        </div>
      </section>

      <section className="mt-5 grid grid-cols-1 gap-3 md:grid-cols-4">
        {selected.scenario_cards.map((card) => (
          <article key={card.name} className="rounded-lg border border-line bg-panel p-4">
            <p className="text-xs uppercase text-muted">{card.name_cn}</p>
            <p className={card.return_20d >= 0 ? "mt-2 text-2xl font-semibold text-teal" : "mt-2 text-2xl font-semibold text-rose"}>
              {signedPct(card.return_20d)}
            </p>
            <p className="mt-1 text-xs text-muted">20日情景收益</p>
            <p className="mt-3 text-sm">{card.summary_cn}</p>
            <p className="mt-3 text-xs text-muted">情景权重：{pct(card.probability_weight)}</p>
          </article>
        ))}
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <div className="flex items-start justify-between gap-3">
          <div>
            <p className="text-xs uppercase text-muted">历史相似情景</p>
            <h2 className="mt-1 text-base font-semibold">{selected.symbol} 最相似历史日期</h2>
          </div>
          <p className="text-sm font-semibold text-amber">{supportCn(selected.historical_support)}</p>
        </div>
        <div className="mt-3 space-y-2">
          {topAnalogs.map((day: HistoricalAnalogCase) => (
            <div key={day.date} className="grid grid-cols-4 gap-2 border-b border-line pb-2 text-sm last:border-b-0 last:pb-0">
              <span className="font-medium">{day.date}</span>
              <span className="text-muted">相似 {pct(day.similarity_score)}</span>
              <span className={day.forward_return_20d != null && day.forward_return_20d >= 0 ? "text-teal" : "text-rose"}>
                20日 {signedPct(day.forward_return_20d)}
              </span>
              <span className="text-muted">最差 {signedPct(day.max_adverse_excursion)}</span>
            </div>
          ))}
        </div>
      </section>

      <section className="mt-5 rounded-lg border border-line bg-panel p-4">
        <p className="text-xs uppercase text-muted">预测失效条件</p>
        <h2 className="mt-1 text-base font-semibold">出现这些情况，当前情景要重新评估</h2>
        <div className="mt-3 grid grid-cols-1 gap-2 sm:grid-cols-2">
          {selected.risk_invalidation_conditions.map((condition) => (
            <div key={condition} className="rounded border border-line bg-white px-3 py-2 text-sm">
              {condition}
            </div>
          ))}
        </div>
        <p className="mt-3 text-xs text-muted">
          当前状态：{selected.live_signal ? "observation，有信号但只做前向观察" : "no signal，等待下一次观察"}。Alpha v1 仍然是研究候选，不是实盘交易信号。
        </p>
      </section>
    </main>
  );
}
