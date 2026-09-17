# AGENTS.md — 通用 Agent 入口（Codex / Cursor 等）

> 本仓库是一套「GEO（生成式引擎优化）方法论技能包」，蒸馏自《从 SEO 到 GEO：AI 时代的搜索优化实战手册》（JingHao-Leon，MIT），并补充了 GEO Wiki（CC BY 4.0）与 GeoLook（MIT）的实测数据。
> Claude Code / ZCode / WorkBuddy / CodeBuddy 等遵循 Agent Skills 规范的产品：直接安装 `geo-playbook/` 目录（见 README 安装矩阵）。
> Codex / Cursor 及其他读取 AGENTS.md 的 agent：把本文件全文放入 `~/.codex/AGENTS.md`（全局）或项目根目录，并把其中相对路径改为本仓库的绝对路径。

## 你（agent）在什么时候使用这套能力

当用户的问题落在以下意图时，先读对应能力卡再回答（**不要凭常识即兴回答 GEO 问题**——每条建议都要能追到卡里的依据）：

| 用户意图 | 先读 |
|---|---|
| 内容该发到哪些平台、主攻哪个 AI 引擎、某引擎引用什么信源、知乎还有没有用 | `geo-playbook/references/capabilities/geo-channel-map.md` |
| 为一道具体问题（"X 和 Y 哪个好""X 跑不动怎么办""X 是不是智商税"）写内容 / 问稿件结构 | `geo-playbook/references/capabilities/golden-question-formulas.md` |
| 稿子怎么改更容易被 AI 引用 / 为什么没被引用 / 定交稿验收标准 | `geo-playbook/references/capabilities/citable-content-spec.md` |
| 列 GEO 选题清单 / 哪些问题值得做 / query 排优先级 | `geo-playbook/references/capabilities/geo-query-research.md` |
| 一稿多发、多平台分发怎么改写 | `geo-playbook/references/capabilities/one-fish-multi-platform.md` |
| 追踪 AI 有没有引用我 / 监测结果后该做什么 / 监测工具选型 / 引用带来多少生意 | `geo-playbook/references/capabilities/geo-monitoring-iteration.md` |
| 实测引擎引用行为 / 这个题这个引擎值不值得投入 / 自动化采样与风控 | `geo-playbook/references/capabilities/geo-test-protocol.md` |
| 品牌被问"智商税/割韭菜/靠谱吗"怎么应对 | `geo-playbook/references/capabilities/negative-semantic-occupy.md` |
| 本地门店地图/点评搜不到、点评排名低 | `geo-playbook/references/capabilities/lso-local-playbook.md` |
| 抖音视频怎么被搜到、被 AI 引用 | `geo-playbook/references/capabilities/vso-video-optimization.md` |
| FAQ 页 / 精选摘要 / FAQPage schema 还要不要做 | `geo-playbook/references/capabilities/aeo-answer-optimization.md` |
| 官网长期该建什么、事实页、结构化数据 | `geo-playbook/references/capabilities/brand-data-infrastructure.md` |
| robots.txt 对 AI 爬虫怎么配、要不要屏蔽 GPTBot、llms.txt 要不要做、网站抓不到排查 | `geo-playbook/references/capabilities/ai-crawler-access.md` |

术语查 `geo-playbook/references/glossary.md`；全书背景与数据边界查 `geo-playbook/references/overview.md`；一页速查表（含关键数字、红线、判停点）`geo-playbook/references/cheatsheet.md`；完整意图索引 `geo-playbook/references/capability-index.md`。

**跨卡任务**（"从零跑一个 GEO 项目""第一步做什么""给客户出一份完整方案"）先读 `geo-playbook/references/workflow.md`——它先要求做适用性确认（目标市场国内还是海外、是不是本地门店、有没有内容资产，答错流程全废），再给 0→6 步依赖顺序、每步的入口卡/该问什么/产出模板/参考工期/判停点，按它指示逐张加载能力卡。

## 随包模板（需要交付物时按需读取）

`geo-playbook/resources/`，索引见 `geo-playbook/resources/README.md`：

- 9 个国内口径 JSON-LD 模板（organization / software-saas / product-ecommerce / local-business / article-author / website-searchaction / faqpage / howto / breadcrumb）
- `robots-ai-crawlers.txt`（按训练/检索/用户触发三类放行，含 26 令牌全名单）、`llms.txt.template`
- `resources/templates/` 下 7 张产出物表格：渠道分工表、query 分级表、稿件体检表、分发对照表、实测记录表、双周迭代表、NAP 对照表

## 硬性纪律（违反即答错）

1. **数据口径**：所有引擎信源数字是 2026-08-05 单日快照（原书）或第三方数据集口径（GEO Wiki CC BY 4.0 / GeoLook CN-GEO v2.0.1 / geo-seo-claude MIT），一律按"方向性"使用；禁止把 "9/12" 写成"引用率 75%"式精确报告；引用第三方数字时标来源与口径，不同口径不横比；重要决策前建议复测。
2. **先测后投**：用户问"这个题/这个引擎值不值得做"时，先给小样本实测方案（独立新对话、逐字提问、二值引用口径、5 次起），不纸面拍板。
3. **判停点**：目标行业不在已验证行业（广告电商、教育）内时，"决策人-引擎"映射必须先实测再定渠道，不得硬套。
4. **风控红线**：自动化提问必须分钟级间隔 + 每日上限（约 30 次连续提问会触发 DeepSeek 风控）；用户要求高频批量跑时拒绝并给限速方案。
5. **拒绝项**：刷好评/刷量、编造数据、伪造评价、批量账号自问自答、伪装中立洗地——明确拒绝并给合规替代。
6. **不承诺**：GEO 提高的是被引用概率，不是保证；不承诺任何引擎一定引用某个页面，不承诺 ROI。
7. **缺输入先问**：能力卡标注"缺 X 先询问"的（如目标 query 原话、决策人画像、品牌立场、语料来源、robots.txt 现状），停下来问，不猜值、不代填产品参数与价格。
8. **不凭常识填空**：卡里没有的，说"本包未覆盖"，不用通用 SEO 常识硬答。

## 不适用

传统 SEO 关键词排名与竞价投放、建站改站的代码实施、海外引擎的实操细节（本包仅含机制层数据）、地理信息 GIS（GEO 在此指生成式引擎优化）。

## 配套

- [GeoLook](https://github.com/aigclink/geolook)（MIT，独立 Skill）：跑自动化诊断、17 引擎采样、工单与验收流水线。本包出方法论与决策，GeoLook 出执行与测量，可同时安装。
- 上游：[JingHao-Leon/geo-book](https://github.com/JingHao-Leon/geo-book)（原书，MIT）｜ [GEO Wiki](https://geo.wiki/zh)（CC BY 4.0）
