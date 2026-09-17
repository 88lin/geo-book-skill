---
name: geo-playbook
description: |
  中文 AI 搜索优化（GEO，生成式引擎优化）实战方法论，蒸馏自《从 SEO 到 GEO：AI 时代的搜索优化实战手册》（JingHao-Leon，2026-08-05 六引擎实测），并补充 GEO Wiki 与 GeoLook CN-GEO 大样本数据。覆盖豆包、DeepSeek、腾讯元宝、通义千问、文心一言、Kimi 六家国产引擎。
  何时使用：内容该发哪个平台／主攻哪个 AI 引擎；为什么 AI 不引用我的文章、稿子怎么改才被引用；列 GEO 选题清单与优先级；一稿多发怎么改写；怎么监测 AI 有没有引用我、引用带来多少生意；实测某引擎引不引用、值不值得投；被问"智商税／割韭菜／靠谱吗"怎么应对；门店在地图/点评搜不到；抖音视频怎么被搜到；FAQ 页、精选摘要、FAQPage schema 还要不要做；官网事实页与结构化数据基建；robots.txt 要不要屏蔽 GPTBot、llms.txt 要不要做、网站被 AI 抓不到怎么排查。
  何时不使用：传统 SEO 关键词排名与竞价投放；海外引擎（Google AI Overviews／Perplexity／ChatGPT Search）的优化实操；地理信息 GIS（此处 GEO 指生成式引擎优化）；刷量刷评、伪造评价等灰产。
  所有引擎信源数字为 2026-08-05 单日快照或第三方数据集口径，按方向性使用并定期复核。
license: MIT
metadata:
  cangjie.generated-by: cangjie-tools v2.5.0
  cangjie.variant: single
  cangjie.bundle-id: bundle.geo-book
  cangjie.capability-count: 13
  cangjie.entrypoint-count: 1
---
# 从 SEO 到 GEO：AI 时代的搜索优化实战手册 — 全书能力入口

## 不适用（命中即说明超出范围，不要硬套）

- 海外引擎（Google AI Overviews、Perplexity、ChatGPT Search）的优化实操——本包只含其机制层对照数据
- AI 回答的广告投放与竞价采买（截至 2026 年初国内六家均无此产品）
- 刷量、伪造评价、批量账号自问自答等灰产操作（原书明确红线）
- 各 AI 引擎算法逆向与内部机制猜测

## 核心原则（常驻速览，概览类问题读到这里即可回答）

1. 七分渠道三分内容：先按引擎生态绑定选对渠道，再打磨内容形态
2. 内容写给 AI 拆件：结论前置 40-60 字、对比表 5+ 维度、价格带日期、数字可验证
3. query 三维分级（决策阶段×引用性×竞争度），先做 easy_win，放弃纯定义类
4. 先测引用再投入：引用率是投入决策的第一道筛子
5. 一鱼多吃是改写不是复制粘贴；不高频抓取、不铺低质稿、不造假
6. 排名/引用是仪表盘不是目标，长期资产是经得起机器核查的事实

## 能力路由（先读本表，按意图加载 1 张能力卡）

能力卡路径统一为 `references/capabilities/<名>.md`，下表只写名。

| 用户意图 | 先读 | 补读 |
|---|---|---|
| 决定内容发哪些平台渠道；选择主攻的 AI 引擎；查询某引擎引用什么信源；评估某渠道在 GEO 中的地位 | geo-channel-map | geo-test-protocol、one-fish-multi-platform、citable-content-spec、geo-query-research |
| 判断一道题属于哪类黄金问题；为具体 query 设计内容骨架；解释为什么内容没被 AI 引用 | golden-question-formulas | citable-content-spec、negative-semantic-occupy、geo-channel-map |
| 检查稿件是否容易被 AI 引用；改写内容提高被引概率；制定内容生产规范 | citable-content-spec | golden-question-formulas、one-fish-multi-platform、geo-monitoring-iteration |
| 为 GEO 项目列选题清单；给 query 排优先级；判断哪些问题不值得做 | geo-query-research | geo-test-protocol、golden-question-formulas、geo-channel-map |
| 把一份内容改造成多平台版本；排多平台分发计划；判断各平台版本该怎么改 | one-fish-multi-platform | citable-content-spec、geo-channel-map、geo-monitoring-iteration |
| 追踪品牌在 AI 回答中的引用情况；决定监测结果出来后做什么；选择监测工具或决定是否自建；算"引用带来多少生意" | geo-monitoring-iteration | geo-test-protocol、citable-content-spec、one-fish-multi-platform |
| 实测或复现某引擎的引用行为；判断某 query 在某引擎上值不值得投入；设计引用采样方案并规避风控 | geo-test-protocol | geo-channel-map、geo-monitoring-iteration、geo-query-research |
| 应对 AI 回答中的负面口碑；处理智商税/骗局类 query 的占位；排负面 query 优先级 | negative-semantic-occupy | golden-question-formulas、geo-channel-map、geo-query-research |
| 解决地图搜不到/点评排名低；新店开业线上信息搭建；本地口碑与评价运营 | lso-local-playbook | geo-channel-map、golden-question-formulas |
| 让视频被抖音搜索收录；让 AI 引擎引用自己的视频；规划视频与图文的形态分工 | vso-video-optimization | geo-channel-map、geo-query-research、one-fish-multi-platform |
| 优化网页被精选摘要/答案卡片引用；制作 FAQ 页与 schema 标记；判断 FAQPage 还值不值得做 | aeo-answer-optimization | citable-content-spec、brand-data-infrastructure、one-fish-multi-platform、ai-crawler-access |
| 制定品牌 AI 时代基建路线图；建设官网事实页与结构化数据；准备 Agent 时代的产品信息接口 | brand-data-infrastructure | aeo-answer-optimization、geo-monitoring-iteration、negative-semantic-occupy、ai-crawler-access |
| 决定 robots.txt 对 AI 爬虫的放行策略；判断要不要部署 llms.txt；排查网站内容抓不到的问题 | ai-crawler-access | brand-data-infrastructure、aeo-answer-optimization、geo-monitoring-iteration |

**非能力类查询**：

- 从零跑一个 GEO 项目、"第一步做什么"、多卡串联的完整流程 → `references/workflow.md`
- 书名/作者/章节/整书概览、数据边界 → `references/overview.md`
- 术语解释 → `references/glossary.md`
- 决策规则与关键数字速查（不需要原文依据时） → `references/cheatsheet.md`
- 完整意图与关键词索引（本表未覆盖的意图先查这里） → `references/capability-index.md`

## 随包资源（需要交付物时按需读取，不预先加载）

`resources/` 下是可直接填写的模板，索引见 `resources/README.md`：

- **JSON-LD 结构化数据模板（国内口径）**：`schema-organization` / `schema-software-saas` / `schema-product-ecommerce` / `schema-local-business` / `schema-article-author` / `schema-website-searchaction` / `schema-faqpage` / `schema-howto` / `schema-breadcrumb`。配 brand-data-infrastructure、aeo-answer-optimization、lso-local-playbook 使用。
- **爬虫与索引文件模板**：`resources/robots-ai-crawlers.txt`（按训练/检索/用户触发三类放行）、`resources/llms.txt.template`。配 ai-crawler-access 使用。
- **产出物表格模板**（`resources/templates/`）：渠道分工表、query 分级表、稿件体检表、分发对照表、实测记录表、双周迭代表、NAP 对照表。对应各卡 E 段承诺的输出格式。

## 加载规则

- 每次任务先读本文件，再按路由表加载 **1** 张能力卡；任务明确跨域时最多加载 2 张；需要串联全流程时读 `references/workflow.md` 再按它指示逐卡加载。
- 概览/书名类问题不加载能力卡，用「核心原则」与 `references/overview.md` 回答。
- 路由表与 `references/capability-index.md` 都无法命中的意图，明确告知超出本书范围，不要硬套。

## 回答纪律（违反即答错）

1. **不凭常识即兴**：每条 GEO 建议都要能追到卡内依据；卡里没有的，说"本包未覆盖"，不用通用 SEO 常识填空。
2. **数据口径**：引擎信源数字是 2026-08-05 单日快照（原书）或第三方数据集口径（GEO Wiki CC BY 4.0 / GeoLook CN-GEO v2.0.1 / geo-seo-claude）；一律按"方向性"使用，禁止把 "9/12" 转写成"引用率 75%"式精确报告；引用第三方数字时标来源与口径，不同口径不横比。
3. **先测后投**：用户问"这个题/这个引擎值不值得做"时，先给小样本实测方案（独立新对话、逐字提问、二值引用口径、5 次起），不纸面拍板。
4. **缺输入先问**：能力卡标注"缺 X 先询问"的（目标 query 原话、决策人画像、品牌立场、语料来源、robots.txt 现状等），停下来问，不猜值、不代填产品参数与价格。
5. **风控红线**：自动化提问必须分钟级间隔 + 每日上限（约 30 次连续提问会触发 DeepSeek 风控）；用户要求高频批量跑时拒绝并给限速方案。
6. **拒绝项**：刷好评/刷量、编造数据、伪造评价、批量账号自问自答、伪装中立洗地——明确拒绝并给合规替代，说明"铺出来的东西经不起查，上榜就是上榜示众"。
7. **不承诺**：GEO 提高的是被引用概率，不是保证；不承诺任何引擎一定引用某个页面，不承诺 ROI。

## 边界与判停

- 目标行业的"决策人-引擎"映射无法从已验证行业（广告电商、教育）推出时，先建议小样本实测再定渠道，不硬套
- 需要精确百分比结论（如引用率 75% vs 83%）时，声明 n=1 局限并建议多次采样，不提供虚假精度
- 涉及海外引擎时，只提供本包已有的机制层对照数据，并说明"两套市场两套打法，结果不可互推"
- 用户要求刷好评、编造数据、伪装中立洗地时，拒绝执行并说明"上榜示众"风险
