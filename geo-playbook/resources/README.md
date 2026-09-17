# resources/ — 随包模板索引

按需读取，不预先加载。所有模板都是**填空件**，不是可直接上线的成品——填之前先读对应能力卡。

## JSON-LD 结构化数据模板（国内口径）

| 文件 | 用途 | 对应能力卡 |
|---|---|---|
| `schema-organization.json` | 组织实体主干。**先建它**——`sameAs` 决定知识图谱里"你是谁"的消歧，是最高优先级属性 | brand-data-infrastructure |
| `schema-software-saas.json` | SaaS / 软件产品，含三档定价 AggregateOffer | brand-data-infrastructure |
| `schema-product-ecommerce.json` | 电商商品，含运费与七天无理由退货政策 | brand-data-infrastructure |
| `schema-local-business.json` | 本地商户。`sameAs` 正好填高德/百度地图/点评/美团的商户页链接 | lso-local-playbook |
| `schema-article-author.json` | 文章与作者（E-E-A-T 信号），含 speakable | citable-content-spec、aeo-answer-optimization |
| `schema-website-searchaction.json` | 站内搜索 | brand-data-infrastructure |
| `schema-faqpage.json` | FAQ 页 | aeo-answer-optimization |
| `schema-howto.json` | 操作指南 / 症状型步骤页 | golden-question-formulas、aeo-answer-optimization |
| `schema-breadcrumb.json` | 面包屑导航 | brand-data-infrastructure |

**部署顺序**：先建实体主干（Organization）→ 再声明页面类型（Article / WebSite / BreadcrumbList）→ 最后才考虑答案形态类标记（FAQPage / HowTo）。

**五条生成规则**：`@graph` 合并多类型；`@id` 交叉引用；ISO 8601 日期；绝对 URL；**放 head 由服务端输出（非 JS 注入）**——AI 爬虫不执行 JS，JS 注入的 schema 会被整体漏掉。

**正确预期**：标记 ≠ 引用。它作用于检索前的页面解析与实体识别，不参与采信。加 FAQPage 标记不会让答案更容易被引用——答案是否被用取决于可见正文的写法。

**红线**：标记必须与服务端输出的**可见内容一致**。两类读者对错误标记的处理恰好相反——依赖搜索索引的 AI 会解析并丢弃不合规标记，而实时抓取型对话引擎会把整个 JSON-LD 块当页面文字读（受控观察发现 ChatGPT / Perplexity 会照搬无效或虚构标记中的值）。**无效或不一致的标记比不加更糟。**

**评分与评价字段专项警告**：`aggregateRating` / `review` 的占位符刻意写成 `X.X`、`X`、`XXX` 这类**不可能通过校验**的形式，就是为了逼出一个决定——**有真实平台数据就填真数据，没有就把整块删掉**。绝不能留着一个看起来合理的分数（如 4.8）上线：那既是伪造评价（本技能明确拒绝的红线），也踩了"数字可验证"这条硬指标，而且实时抓取型引擎会把它当正文读走。`review` 块里的评价原文同理，只能用真实买家评价，不得编造或批量生成。

**海外站点**：模板已本地化为国内口径（`addressCountry: CN`、`+86` 电话、`CNY`、`zh-CN`，`sameAs` 指向知乎/微博/百度百科/企查查/高德/点评等）。打海外市场时对应替换为目标国家的国别码、货币、语言与平台（LinkedIn / Crunchbase / G2 / Yelp / Wikipedia），并注意国内外是两套打法，结论不可互推。

模板由 `scripts/gen_schema_templates.py` 生成——改模板请改脚本再重跑，保证九份口径一致。

## 爬虫与索引文件模板

| 文件 | 用途 | 对应能力卡 |
|---|---|---|
| `robots-ai-crawlers.txt` | robots.txt 按训练/检索/用户触发三类放行，含 26 个令牌全名单与 RFC 9309 specificity 陷阱说明 | ai-crawler-access |
| `llms.txt.template` | llms.txt 筛选索引，含硬格式要求、收录三档与误用清单 | ai-crawler-access |

两份都不是"抄了就完事"：robots.txt 是声明不是强制，部署后必须换真实 AI 爬虫 UA 实测 + 查 X-Robots-Tag 响应头 + 查 SPA 空壳。llms.txt 只押"向前兼容"，不押当下引用。

## 产出物表格模板（`templates/`）

| 文件 | 产出自 |
|---|---|
| `templates/channel-matrix.md` | geo-channel-map 第 5 步 — 引擎 × 渠道 × 形态分工表 + 信源四层计划 |
| `templates/query-grading.md` | geo-query-research 第 6 步 — query 三维分级清单 |
| `templates/citable-content-checklist.md` | citable-content-spec 第 1/5 步 — 稿件体检表（四硬指标 + 七信号 + 段落评分 + E-E-A-T） |
| `templates/distribution-matrix.md` | one-fish-multi-platform 第 4 步 — 分发对照表 + 原料清单 + 逐版规格核对 |
| `templates/geo-test-log.md` | geo-test-protocol 第 6 步 — 实测记录表 + 证据等级 + 使用声明 |
| `templates/monitoring-log.md` | geo-monitoring-iteration 第 6 步 — 双周迭代记录 + 归因三段 + 报告七陷阱 |
| `templates/nap-table.md` | lso-local-playbook 第 6 步 — 全平台 NAP 对照表 + 五步执行进度 |

跑完整流程时按 [references/workflow.md](../references/workflow.md) 的顺序逐张填。
