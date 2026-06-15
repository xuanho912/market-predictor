# Multi-Source Confluence Principle

本项目提高预测质量的核心不是寻找某一个神奇指标，而是判断多个独立市场维度是否共振。

单独任何一个指标都不够。真正有价值的是：

```text
价格 + 成交量 + 宽度 + 信用 + 波动率/期权 + 资金流 + 新闻事件 + 历史相似
```

## 为什么必须做多源共振

市场上涨可能只是少数大票拉指数，也可能是全市场修复。

VIX 回落可能是恐慌释放，也可能只是短线波动卖压下降。

新闻利好可能真的改变路径，也可能已经被定价，或者市场不认可。

历史相似样本可能支持反抽，但如果当前信用、宽度、波动率和价格结构不配合，就不能给强结论。

所以系统必须问：

- 价格是否确认？
- 成交量是否确认？
- 市场宽度是否确认？
- 信用是否稳定？
- 波动率和期权结构是否修复？
- flow / positioning proxy 是否支持 risk-on？
- 新闻事件是否被价格反应确认？
- 历史相似情景是否支持当前路径？

## Evidence Groups

### Price

价格结构回答：指数是否收复关键位、突破近期高点、跌破近期低点、站上均线、接近主路径确认价或失效价。

### Volume

成交量回答：上涨是否有量、下跌是否放量、是否出现恐慌量、是否存在反弹无量或承接不足。

### Breadth

宽度回答：市场内部是否共振。指数上涨但多数成分股不跟，不能算高质量修复。

### Credit

信用回答：风险资产反弹时，HYG/LQD、HY OAS、IG/BAA proxy 是否稳定。如果信用继续恶化，反抽质量下降。

### Volatility / Options

波动率和期权结构回答：VIX、VVIX、SKEW、VIX term structure 是否显示恐慌释放，还是尾部风险仍在。

### Flow / Positioning

资金流/仓位 proxy 回答：risk-on / risk-off rotation 是否支持当前路径。proxy 必须明确标注，不能当成真实 fund flow。

### News / Events

新闻事件回答：是否出现宏观、政策、地缘、油价、信用或流动性事件，并且市场价格是否确认该事件方向。

### Historical Analogs

历史相似回答：类似环境下后续 3d / 5d / 10d / 20d / 60d 的条件分布如何。历史相似不是证明，只是参考和解释。

## Confluence Rules

强判断必须满足多个独立来源同向。

如果只有单一来源支持：

- 不允许输出强结论。
- 不允许标记为 confirmed alpha。
- 不允许提高为 high precision。
- 只能作为 supporting evidence 或 shadow evidence。

如果多个来源冲突：

- 降低 confidence。
- 标记 `mixed`、`close_call` 或 `NO_EDGE`。
- 显示 conflicting evidence。
- 给出路径切换条件。

如果数据缺失：

- 显示 `missing`、`proxy_only`、`stale_data` 或 `data_source_failed`。
- 不允许用 0% 或假数据占位。
- 不允许因为缺失数据而强行给高置信度。

## Strong Forecast Gate

要输出强预测优势，至少需要：

- data completeness 足够高。
- signal confirmation 足够高。
- confluence score 足够高。
- price / volume 没有明显冲突。
- breadth 与主路径不冲突。
- credit 没有明显恶化。
- volatility / options 不支持风险扩散。
- flow proxy 不明显 risk-off。
- news/event 没有强 risk-off 冲突，或者已被价格确认为可控。
- historical analog 不明显冲突。
- forward validation 状态必须透明。

## Dashboard Requirement

第一屏必须直接显示：

- 今日是否有 forecast edge。
- 主路径、第二路径、风险路径。
- 强预警状态。
- 多源共振评分。
- 支持证据。
- 冲突证据。
- 关键确认价、失效价、风险路径接管价。
- 当前是否已经通过前向验证。

## Validation Requirement

多源共振本身也必须被验证。

Forecast Accuracy Ledger 和 historical replay / forward validation 必须回答：

- 高 confluence 样本是否比低 confluence 样本更准？
- confluence 支持主路径时，primary scenario 是否更常命中？
- confluence 冲突时，failed bounce / risk scenario 是否更常发生？
- 哪个 evidence group 真正提高了预测质量？

如果没有足够 forward samples，状态必须保持：

```text
not_yet_validated
```

多源共振是预测质量核心，但不是已验证 alpha 的替代品。
