# 品牌数据基建三层

> 能力单元 brand-data-infrastructure ｜ 来源：《从 SEO 到 GEO》第 11 章（未来：品牌数据基建、三类读者行动清单）、第 1 章

## R — 原文

> "现在客人连点评都不看了，直接在外卖平台上下单——这时候你嗓门再大也没用，平台系统里没录的菜，等于不存在。"（ch11，推演章）
>
> "官方事实页，就是挂在摊位上的那张执照——写清楚产品参数、价格（带日期）、服务范围、联系方式，保持全平台口径一致。"（ch11）

出处：ch11 第三节、第五节（章内自我标注为推演，第三层有实测支撑）。候选来源：f26, f27, p81, p82, p83, p13。

## I — 解释

AI 时代品牌基建的三层模型（餐馆比喻：从门口吆喝→点评照片→平台后台字段）：

1. **结构化数据**：给机器看的身份证——用 Schema.org 标清"我是谁、卖什么、多少钱、怎么联系"，机器不用猜；机器读不懂就直接跳过你（技术 SEO 四件功课是它的前置，p13）。
2. **API 化内容**：让内容能被程序调用而不只是被人阅读——价格表、库存、课程安排、服务范围，凡会被问到的都应有机器可查的出口（"谁的接口在，谁就是默认选项"）。⚠️ 本层是推演，Agent 接口标准未定。
3. **官方事实页**：产品参数、价格（带日期）、服务范围、联系方式，全平台口径一致。实测支撑：引用覆盖率仅 50.4%，能被引即稀缺；Kimi 官网引用覆盖率 67.6% 六家最高之一；晓多官方博客进豆包/元宝/DeepSeek 三家引用；文心 12 题全引连长尾小号都在被引——官方口径缺位的地方，自然有别人的嘴替你填上。

按角色的节奏（三类读者行动清单）：**品牌方**——本周盘点官网事实页；三个月内核心产品信息结构化、全渠道口径对齐；持续监测出现率与口径、负面词条占位。**内容创作者**——每篇结论前置+带日期真实数字+5 维对比表；渠道按实测优先级铺；长期只吃真实数据和真实经验。**工具服务商**——监测控频或接现成数据源；产品机会从"监测可见度"升级到"建设可调性"。

**补充定位校正（GeoLook CN-GEO 数据集 v2.0.1，MIT）**：品牌官网类信源只占国内 AI 引用全库的 **1.37%**——官方事实页的价值在"**事实源**"（让 AI 描述你时口径正确、不出事实错误），不在"引用源"（引用大头在内容平台与榜单站）。建事实页的目标是口径一致与可被抓取，不是指望官网本身带来大量引用。

**补充二（来自 geo-seo-claude，MIT，github.com/zubair-trabzada/geo-seo-claude）——6 个可直接填的 JSON-LD 模板**随本技能分发（resources/ 目录）：organization（组织实体主干）、software-saas（SaaS 产品）、product-ecommerce（电商商品）、local-business（本地商户）、article-author（文章与作者，E-E-A-T 信号）、website-searchaction（站内搜索）。部署顺序：先建实体主干（Organization），再声明页面类型，最后才考虑答案形态类标记（FAQ/HowTo）；标记必须与服务端输出的可见内容一致——**解析器会丢弃不合规标记，而实时抓取型模型会把整个块当页面文字读**，两类读者对错误标记的处理恰好相反。

**补充三（改编自 GEO Wiki《面向 AI 的 Schema.org》，CC BY 4.0；GeoLook 事实卡实践）——标记的正确预期与优先级：**

- **标记 ≠ 引用**：Schema 标记不是排名信号也不是引用信号——它作用于检索前的页面解析与实体识别，不参与由可引用性与 E-E-A-T 决定的采信环节。"为 FAQ 加标记并不会让其中的答案更容易被引用"，答案是否被用取决于可见正文的写法。
- **两类读者对错误标记的处理相反**（searchVIU 2025）：依赖搜索索引的 AI（Google AI Overviews、Bing Copilot）会解析标记；实时抓取页面的对话引擎（ChatGPT、Perplexity）只把 JSON-LD 当普通正文读。
- **sameAs 是最高优先级属性**：优先给 Organization/Person 正确设置 sameAs（Wikipedia、Wikidata、官网、社媒主页），它决定知识图谱里"你是谁"的消歧；类型优先级 Organization/Person > Article/WebSite/BreadcrumbList > FAQPage/HowTo（最后两者只是声明解析器本可识别的结构，Google 的 HowTo 富结果也已移除）。
- **事实卡实践**（GeoLook）：把品牌事实（成立时间、价格、客户、资质）维护成一张带来源、核验日期、证据等级（A 官方已证实 / B 第三方可佐证 / C 内部待授权 / D 需补证 / E 禁止使用）的事实卡，作为 llms.txt、JSON-LD、内容稿的唯一口径来源；每条事实标证据等级，查不到标"待确认"，绝不用常识填充。

**补充四（geo-seo-claude + GEO Wiki，MIT / CC BY 4.0，2026-09-14 穷尽审查）——结构化数据的审计细则与打分：**

- **四级台阶审计法**：覆盖（原始 HTML 含 JSON-LD，非 JS 注入——AI 爬虫不执行 JS，JS 注入的 schema 会被整体漏掉）→ 有效（语法 + @context）→ 一致（@id 唯一、页面内引用可解析、无重复实体、有稳定 Organization/Person 节点）→ 属实（标记标题 vs 可见标题、作者可见、日期合理；抽查最多 10 个 sameAs）。**无效或不一致的标记比不加更糟**：实时抓取型 AI 把 JSON-LD 当正文读，受控观察发现 ChatGPT/Perplexity 甚至照搬无效或虚构标记中的值。
- **生成五规则**：@graph 合并多类型；@id 交叉引用；ISO 8601 日期；绝对 URL；放 head 由服务端输出（非 JS 注入）。speakable 用 cssSelector 圈候选段（如 .article-summary / .key-takeaway）；knowsAbout 列 3+ 主题。
- **十分项评分表**（结构化维度 0-100）：Organization 20 / Article 15 / Person 15 / sameAs 15（含 Wikipedia 在内的 5+ 平台才满分）/ Speakable 10 / Breadcrumb 5 / SearchAction 5 / 无废弃类型 5 / JSON-LD 格式 5 / 通过验证 5。
- **废弃/受限类型**：FAQPage 富结果 2023-08 起仅限政府/医疗站、HowTo 富结果 2023-09 彻底移除、SpecialAnnouncement 弃用——但**准确且维护成本低的 FAQPage 标记仍值得保留**（AI 平台解析 FAQ 结构做问答抽取，受益不依赖富结果）；过时或与页面冲突才更新/删除。
- **品牌权威综合分**（海外生态，两套口径并存勿混用）：点数版 Wikipedia 30/垂评 25/Reddit 20/YouTube 15/LinkedIn 10；权重版 = YouTube×0.25 + Reddit×0.25 + Wikipedia×0.20 + LinkedIn×0.15 + 其他×0.15。档位判据示例：YouTube 90-100 = 1 万订阅 + 20+ 第三方视频提及；Reddit 90-100 = 自有 subreddit 5K+ 成员。情感四分：正面/中性/负面（抱怨类表述）/混合。**平台补强速赢**：做对比/"替代品"视频（比较类查询会被 AI 引用）；勿自编自家 Wikipedia 词条（利益冲突，先攒声望、先做全 Wikidata）；Reddit 真实参与勿马甲（被识破反噬极大）；近 6 个月的提及远胜 3 年前的。

## A1 — 书中案例

- **官方阵地的实测表现（作者亲历，ch11 引用 ch6/ch7 数据）**：小鹅通官方 SEM 页被 DeepSeek 引用、抖音电商学习中心（school.jinritemai.com）在千川类问题上被豆包和 DeepSeek 反复引用（DeepSeek 采样中 9 次）——"官方事实页 + 结构化内容"今天的形态，就是 Agent 时代"可被调用的事实接口"的雏形（后半句为作者推演）。

## A2 — 未来触发

- 品牌方问"GEO 之外还有什么长期该建的 / 官网要怎么改才能被 AI 用上"。
- 用户问"Agent 能直接下单的时候品牌要准备什么"。
- 制定季度/年度基建路线图。
- 语言信号：事实页、结构化数据、Schema、API 化、数据基建、Agent 时代、口径对齐 / fact page, structured data, brand data infrastructure, agent-ready。
- 与相邻能力区分：本卡是长期底座与路线图；单页怎么写归 aeo-answer-optimization；内容生产归 citable-content-spec；本卡第 1 层执行细节可参考技术 SEO 功课（p13，见 overview 参考区）。

## E — 执行步骤

输入契约：品牌官网现状（有无事实页/schema）；核心产品清单；渠道口径现状。产品事实缺失时先索取，不代填参数。

1. **本周动作（层 3 起步）**：盘点官网有无一页事实页——产品参数、价格（带更新日期）、对比维度、常见质疑的官方回应；没有就建，写给人看也写给机器看。完成标准：事实页含全部核心产品与带日期价格。
2. **三个月动作（层 1）**：核心产品信息 Schema.org 结构化（Product/Organization/FAQ 等类型）；全渠道（官网/公众号/百家号/电商页）口径对齐。完成标准：任两渠道的价格与参数逐字一致。
3. **层 2（推演，按需）**：识别"最常被问到的动态信息"（价格、库存、排期），评估是否有机器可查出口（公开价格页/API/开放文档）；标注本层收益属推演，投入与业务阶段匹配。
4. **持续动作**：监测品牌在各引擎回答中的出现率与口径（转 geo-monitoring-iteration）；负面语义词条主动占位（转 negative-semantic-occupy）。
5. **输出**：带时间窗的基建清单（本周/三月/持续三档，每档有完成标准）。

## B — 边界

- 第 11 章是推演章：层 1/2 的"Agent 时代收益"没有实测依据，Agent 接口标准未定；层 3（事实页）有实测支撑。执行层 1/2 的动作（结构化标记、机器可查出口）本身有独立价值（SEO/AEO 基本功），不必依赖推演成立。
- "官方口径缺位会被别人填上"是实测观察（文心连长尾小号都引），不是威胁预言。
- 本卡不解决转化归因——被引用与生意结果的因果链全书未验证。
- 全渠道口径对齐不等于全渠道同稿：分发仍需按平台改写（one-fish-multi-platform 纪律）。

## 相关能力

下游 geo-monitoring-iteration、negative-semantic-occupy（持续档动作）；aeo-answer-optimization（层 3 单页技术）；citable-content-spec（口径一致的稿件规格）。

## 配套资源

路径相对于本文件；脚本需先检查运行条件，不因附带而自动执行。

- [resources/schema-organization.json](../../resources/schema-organization.json)
- [resources/schema-software-saas.json](../../resources/schema-software-saas.json)
- [resources/schema-product-ecommerce.json](../../resources/schema-product-ecommerce.json)
- [resources/schema-local-business.json](../../resources/schema-local-business.json)
- [resources/schema-article-author.json](../../resources/schema-article-author.json)
- [resources/schema-website-searchaction.json](../../resources/schema-website-searchaction.json)
